// render_vocab.js — Vocabulary activity renderers for the PAS worksheet generator.
// Assumes global helpers: cardOpen, disp, imgsrc, shuffle
// Assumes global CSS variables: --navy --ink --grey --bg --pink --blue --green --orange --purple
//   tints: --pinkt --bluet --greent --purplet --oranget
//   extras: --gold --red --lblue --frame
// Assumes existing CSS classes: .n .wl .wordbox .ws .tile .card .tab .instr .line .lrow

// ─── A) New CSS classes (v- namespace) ───────────────────────────────────────
const CSS_VOCAB = `
/* v- vocab renderer classes — safe to inject once into <head><style> */

/* Write the Word */
.v-write-row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 14px 0 16px;
}
.v-write-row img {
  width: 74px;
  height: 74px;
  object-fit: contain;
  flex-shrink: 0;
}
.v-write-row .wl { height: 26px; min-width: 240px; }

/* Sound Chunks */
.v-sound-row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 13px 0 15px;
  flex-wrap: wrap;
}
.v-sound-row img {
  width: 64px;
  height: 64px;
  object-fit: contain;
  flex-shrink: 0;
}
.v-sound-row .wl { height: 24px; min-width: 160px; }
.v-sound-tiles {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  align-items: center;
}
/* .tile is already styled globally with orange border; override colour per card via inline style */
.v-tile-chunk {
  border: 1.4px solid;
  background: #fff;
  border-radius: 7px;
  padding: 3px 9px;
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 14px;
}

/* Label the Picture — 2-column picture grid */
/* Note: this activity uses per-word icons arranged in a grid as an approximation
   of a labelled scene (the app has no single composite scene image). */
.v-label-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 26px 36px;
  margin-bottom: 12px;
}
.v-label-cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}
.v-label-cell img {
  width: 104px;
  height: 104px;
  object-fit: contain;
}
.v-label-wl {
  width: 180px;
  border-bottom: 1.8px solid var(--lblue);
  height: 22px;
}

/* Categorize — two-column layout */
.v-word-bank {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin-bottom: 14px;
}
.v-bank-chip {
  border: 1.4px solid;
  background: #fff;
  border-radius: 8px;
  padding: 4px 11px;
  font-family: Poppins, sans-serif;
  font-weight: 600;
  font-size: 13px;
}
.v-cat-cols {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}
.v-cat-col {
  border: 1.4px solid;
  border-radius: 12px;
  overflow: hidden;
}
.v-cat-head {
  padding: 6px 12px;
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 13px;
  color: #fff;
}
.v-cat-hint {
  font-family: Poppins, sans-serif;
  font-size: 11px;
  opacity: 0.88;
  margin-left: 6px;
  font-weight: 400;
}
.v-cat-body {
  padding: 8px 12px 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

/* Hidden Word */
.v-hidden-row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 0 14px;
}
.v-hidden-row img {
  width: 62px;
  height: 62px;
  object-fit: contain;
  flex-shrink: 0;
}
.v-hunt-str {
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 17px;
  letter-spacing: 4px;
  color: var(--navy);
}
`;

// ─── Phonics chunker ─────────────────────────────────────────────────────────
// Splits a (slug-display) word into phonics sound chunks.
//
// Design notes (matching approved examples from the spec):
//   count     -> c · ou · nt         vowel grapheme chunk, then coda cluster as own chunk
//   drawing   -> dr · aw · ing       onset blend, vowel grapheme, -ing suffix
//   gluing    -> gl · u · ing        onset blend, single vowel, -ing
//   cutting   -> c · u · tt · ing    vowel, doubled consonant as own chunk, -ing
//   counting  -> c · ou · nt · ing
//   coloring  -> c · o · l · or · ing   'or' treated as vowel-r digraph
//   talking   -> t · al · k · ing    'al' treated as vowel-l digraph
//
// Algorithm (left-to-right token scan after peeling -ing):
//   1. Strip hyphens, lowercase.
//   2. Peel -ing suffix if word is long enough.
//   3. Scan base left-to-right, greedily matching in priority order:
//      P1. Onset blends (2-char consonant sequences before a vowel).
//      P2. Vowel digraphs: or, al, ar, er, ir, ur (vowel-r/l), then
//          ou, ow, aw, oo, ee, ea, oa, ai, ay, ie, igh (3-char last).
//      P3. Single vowels: a e i o u.
//      P4. Doubled consonant clusters: tt, ll, ss, ff, nn, rr, dd, gg, bb, pp, mm, zz.
//      P5. Coda clusters after a vowel (nt, nd, nk, st, mp, ng, lk, sk, sp).
//      P6. Single consonant (fallback).
//   4. Append -ing chunk if peeled.
//   5. Guarantee ≥2 chunks; if only 1, return word as-is.
function phonicsChunk(word) {
  const core = word.replace(/-/g, "").toLowerCase();

  // Step 2: peel -ing suffix (guard: base must be ≥2 chars so we don't eat whole word)
  let base = core;
  let ingSuffix = "";
  if (core.length > 4 && core.endsWith("ing")) {
    base = core.slice(0, core.length - 3);
    ingSuffix = "ing";
  }

  // Token lists — order within each group: longest first
  const BLENDS    = ["shr","thr","spl","spr","str","bl","br","cl","cr","dr","fl","fr","gl","gr","ph","pl","pr","sc","sk","sl","sm","sn","sp","st","sw","tr","wh","sh","ch","th","ck","qu"];
  const VOWEL_DIG = ["igh","or","al","ar","er","ir","ur","ou","ow","aw","oo","ee","ea","oa","ai","ay","ie"];
  const SINGLE_V  = ["a","e","i","o","u"];
  const DOUBLED   = ["tt","ll","ss","ff","nn","rr","dd","gg","bb","pp","mm","zz"];
  const CODAS     = ["nk","nt","nd","st","mp","ng","lk","sk","sp","ct","ft"];

  function isVowelChar(ch) { return "aeiou".includes(ch); }

  const chunks = [];
  let i = 0;
  let lastWasVowel = false;

  while (i < base.length) {
    const rest = base.slice(i);

    // P1: onset blend — only when last token was NOT a vowel (we're in consonant position)
    if (!lastWasVowel) {
      const bl = BLENDS.find(b => rest.startsWith(b) && rest.length > b.length && isVowelChar(rest[b.length]));
      if (bl) { chunks.push(bl); i += bl.length; lastWasVowel = false; continue; }
    }

    // P2: vowel digraph / vowel-r/l
    const vd = VOWEL_DIG.find(g => rest.startsWith(g));
    if (vd) {
      chunks.push(vd);
      i += vd.length;
      lastWasVowel = true;
      // P5: immediately after a vowel digraph, grab a coda cluster as its own chunk
      //     only if it ends the base (or is followed by another vowel — next syllable onset)
      const afterVd = base.slice(i);
      if (afterVd.length > 0) {
        const coda = CODAS.find(c => afterVd.startsWith(c));
        if (coda) {
          const afterCoda = base.slice(i + coda.length);
          // attach as own chunk (per spec: c·ou·nt not c·ount)
          chunks.push(coda);
          i += coda.length;
          lastWasVowel = false;
        }
      }
      continue;
    }

    // P3: single vowel
    const sv = SINGLE_V.find(v => rest.startsWith(v));
    if (sv) {
      chunks.push(sv);
      i += sv.length;
      lastWasVowel = true;
      // P5: coda cluster after single vowel (e.g. u·tt, u·mp)
      const afterSv = base.slice(i);
      if (afterSv.length > 0) {
        // P4 check first: doubled consonant (tt, ll …)
        const dbl = DOUBLED.find(d => afterSv.startsWith(d));
        if (dbl) {
          // Only grab doubled if what follows is end-of-base or another vowel (next syllable)
          const afterDbl = base.slice(i + dbl.length);
          if (afterDbl.length === 0 || isVowelChar(afterDbl[0])) {
            chunks.push(dbl);
            i += dbl.length;
            lastWasVowel = false;
            continue;
          }
        }
        const coda = CODAS.find(c => afterSv.startsWith(c));
        if (coda) {
          const afterCoda = base.slice(i + coda.length);
          if (afterCoda.length === 0 || isVowelChar(afterCoda[0])) {
            chunks.push(coda);
            i += coda.length;
            lastWasVowel = false;
          }
        }
      }
      continue;
    }

    // P4: doubled consonant (not after vowel path — rare but guard it)
    const dbl = DOUBLED.find(d => rest.startsWith(d));
    if (dbl) { chunks.push(dbl); i += dbl.length; lastWasVowel = false; continue; }

    // P6: single consonant fallback
    chunks.push(base[i]);
    i += 1;
    lastWasVowel = false;
  }

  if (ingSuffix) chunks.push(ingSuffix);

  const result = chunks.filter(Boolean);
  if (result.length < 2) return [core];
  return result;
}

// ─── 1. renderWrite ───────────────────────────────────────────────────────────
// "Write the Word" — picture + handwriting line, Word Box at bottom.
function renderWrite(words, color) {
  const c = `var(--${color})`;
  let h = cardOpen(color, "A", "Write the Word",
    "Look at the picture. Write the word. Use the Word Box.", "v-write");
  words.forEach((w, i) => {
    h += `<div class="v-write-row">` +
      `<span class="n" style="background:${c}">${i + 1}</span>` +
      `<img src="${imgsrc(w)}" alt="${disp(w)}">` +
      `<span class="wl"></span>` +
      `</div>`;
  });
  // Word Box
  h += `<div class="wordbox" style="border-color:${c}">` +
    `<b style="color:${c}">Word Box</b>` +
    `<span class="ws">${words.map(disp).join("　")}</span>` +
    `</div>`;
  h += `</div>`;
  return h;
}

// ─── 2. renderSound ───────────────────────────────────────────────────────────
// "Sound Chunks" — shuffled phonics-chunk tiles per word, handwriting line, Word Box.
function renderSound(words, color) {
  const c = `var(--${color})`;
  let h = cardOpen(color, "B", "Sound Chunks",
    "Put the sound chunks in order. Write the word.", "v-sound");
  words.forEach((w, i) => {
    const chunks = phonicsChunk(w);
    const shuffled = shuffle(chunks, i * 17 + 3);
    const tiles = shuffled
      .map(ch => `<span class="v-tile-chunk" style="border-color:${c};color:${c}">${ch}</span>`)
      .join("");
    h += `<div class="v-sound-row">` +
      `<span class="n" style="background:${c}">${i + 1}</span>` +
      `<img src="${imgsrc(w)}" alt="${disp(w)}">` +
      `<div class="v-sound-tiles">${tiles}</div>` +
      `<span class="wl"></span>` +
      `</div>`;
  });
  h += `<div class="wordbox" style="border-color:${c}">` +
    `<b style="color:${c}">Word Box</b>` +
    `<span class="ws">${words.map(disp).join("　")}</span>` +
    `</div>`;
  h += `</div>`;
  return h;
}

// ─── 3. renderLabel ───────────────────────────────────────────────────────────
// "Label the Picture" — 2-column grid, each cell: big picture + writing line.
// Note: uses per-word icons arranged in a grid, approximating a labelled scene,
// because the image library provides individual word images, not composite scenes.
function renderLabel(words, color) {
  const c = `var(--${color})`;
  let h = cardOpen(color, "C", "Label the Picture",
    "Write the correct word for each picture.", "v-label");
  h += `<div class="v-label-grid">`;
  words.forEach(w => {
    h += `<div class="v-label-cell">` +
      `<img src="${imgsrc(w)}" alt="">` +
      `<div class="v-label-wl"></div>` +
      `</div>`;
  });
  h += `</div>`;
  // Word Box
  h += `<div class="wordbox" style="border-color:${c}">` +
    `<b style="color:${c}">Word Box</b>` +
    `<span class="ws">${words.map(disp).join("　")}</span>` +
    `</div>`;
  h += `</div>`;
  return h;
}

// ─── 4. renderCategorize ─────────────────────────────────────────────────────
// "Categorize" — word bank row + 2 blank sorted columns.
// opts.categories = [{title, hint}, {title, hint}]  (optional)
function renderCategorize(words, color, opts) {
  const c = `var(--${color})`;
  const cats = (opts && opts.categories && opts.categories.length >= 2)
    ? opts.categories
    : [{ title: "Group 1", hint: "" }, { title: "Group 2", hint: "" }];

  let h = cardOpen(color, "D", "Categorize",
    "Read the words. Write each word in the correct group.", "v-cat");

  // Word bank
  h += `<div class="v-word-bank">`;
  words.forEach(w => {
    h += `<span class="v-bank-chip" style="border-color:${c};color:${c}">${disp(w)}</span>`;
  });
  h += `</div>`;

  // Two category columns with blank lines for the student to fill
  const linesEach = Math.max(4, Math.ceil(words.length / 2) + 1);
  h += `<div class="v-cat-cols">`;
  cats.slice(0, 2).forEach(cat => {
    const hint = cat.hint ? `<span class="v-cat-hint">(${cat.hint})</span>` : "";
    h += `<div class="v-cat-col" style="border-color:${c}">` +
      `<div class="v-cat-head" style="background:${c}">${cat.title}${hint}</div>` +
      `<div class="v-cat-body">`;
    for (let i = 0; i < linesEach; i++) {
      h += `<div class="wl"></div>`;
    }
    h += `</div></div>`;
  });
  h += `</div>`;
  h += `</div>`;
  return h;
}

// ─── 5. renderHidden ─────────────────────────────────────────────────────────
// "Hidden Word" — each row: picture + letter string with the word embedded.
function renderHidden(words, color) {
  const c = `var(--${color})`;
  // Filler letters — avoid letters that would double-spell the hidden word accidentally
  const FILLER = "abcdefghijklmnoprstuvwxyz";
  let h = cardOpen(color, "E", "Hidden Word",
    "Find and circle the hidden word in each row.", "v-hidden");
  words.forEach((w, i) => {
    const core = disp(w).replace(/ /g, "").toLowerCase();
    // Choose a random insertion point (seeded so it's stable)
    const seed = i * 31 + core.length;
    const prefixLen = (seed % 3) + 1;          // 1–3 filler letters before
    const suffixLen = ((seed * 7) % 3) + 1;    // 1–3 filler letters after
    // Build filler avoiding the first/last letter of core (reduce accidental matches)
    function fillerChar(pos) {
      const idx = (seed * (pos + 1) * 13) % FILLER.length;
      let ch = FILLER[idx];
      // Simple avoid: skip if same as first char of core
      if (ch === core[0] || ch === core[core.length - 1]) {
        ch = FILLER[(idx + 5) % FILLER.length];
      }
      return ch;
    }
    let prefix = "";
    for (let k = 0; k < prefixLen; k++) prefix += fillerChar(k);
    let suffix = "";
    for (let k = 0; k < suffixLen; k++) suffix += fillerChar(k + prefixLen + core.length);

    const row = prefix + core + suffix;
    h += `<div class="v-hidden-row">` +
      `<span class="n" style="background:${c}">${i + 1}</span>` +
      `<img src="${imgsrc(w)}" alt="${disp(w)}">` +
      `<span class="v-hunt-str">${row}</span>` +
      `</div>`;
  });
  h += `</div>`;
  return h;
}

// ─── C) Node.js smoke test ───────────────────────────────────────────────────
/* node self-test removed for browser use; SAMPLE_* and renderers above are the exports. */
