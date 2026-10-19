/**
 * render_grammar.js — Grammar activity card renderers for the PAS worksheet generator.
 *
 * ITEM SCHEMAS
 * ─────────────────────────────────────────────────────────────────────────────
 * renderCircleCorrect  item = { text: string,          // sentence with ___ where blank goes
 *                               options: string[],     // exactly 2 choices
 *                               answer: string,        // which option is correct
 *                               pic?: string }         // image slug (optional)
 *
 * renderFillBlank      item = { text: string,          // sentence with ___
 *                               answer: string,        // word to fill
 *                               pic?: string }
 *
 * renderTrueFalse      item = { text: string,          // statement
 *                               answer: boolean,       // true or false
 *                               pic?: string }
 *
 * renderMC             item = { text: string,          // question prompt
 *                               options: string[],     // 2-4 answer choices
 *                               answer: number,        // 0-based index of correct choice
 *                               pic?: string }
 *
 * renderSentenceBuilder  item = { words: string[],     // word tokens (any order, any case)
 *                                 answer: string }     // the correct sentence
 *
 * renderScrambledSentences  item = { words: string[],  // same schema as Sentence Builder
 *                                    answer: string }
 *
 * renderSentenceCompletion  item = { stem: string,     // partial sentence to complete
 *                                    pic?: string }
 *
 * renderDialogueCompletion  item = { lines: [{ who: string,  // speaker label (e.g. "A","B")
 *                                              text: string, // spoken text; empty = blank line
 *                                              answer?: string }] }
 *
 * OPTS (all renderers)
 *   opts.title    — override card label
 *   opts.instr    — override card instruction text
 *   opts.example  — boolean; pre-fill item[0]'s answer in card colour + "(example)" tag
 *   opts.wordBank — string[] shown in a Word Box (used by renderFillBlank)
 * ─────────────────────────────────────────────────────────────────────────────
 */

/* ── A. New CSS (g- namespaced; reuses .n .wl .tile .wordbox .ws) ─────────── */
const CSS_GRAMMAR = `
/* grammar card shared */
.g-rows { list-style:none; margin:6px 0 0; padding:0; }
.g-rows li { display:flex; align-items:center; gap:10px; padding:7px 0; border-bottom:1px dashed #e5e9f0; }
.g-rows li:last-child { border-bottom:none; }

/* small thumbnail next to a row */
.g-pic { width:62px; height:62px; object-fit:contain; flex-shrink:0; }

/* circle-the-answer choices */
.g-choice { font-family:Poppins; font-weight:700; font-size:14px;
             border:1.8px solid; border-radius:20px;
             padding:3px 13px; color:var(--navy); background:#fff;
             display:inline-block; white-space:nowrap; }
.g-choice-wrap { display:inline-flex; gap:8px; align-items:center; flex-wrap:wrap; }

/* T / F boxes */
.g-tf-box { font-family:Poppins; font-weight:700; font-size:13px;
             border:1.8px solid; border-radius:8px;
             width:36px; height:30px; display:grid; place-items:center;
             background:#fff; flex-shrink:0; }

/* MC options */
.g-mc-opts { list-style:none; margin:4px 0 0 32px; padding:0; }
.g-mc-opts li { display:flex; align-items:center; gap:8px; padding:4px 0;
                font-family:Poppins; font-size:13px; color:var(--navy); }
.g-mc-letter { font-weight:700; border:1.8px solid; border-radius:50%;
                width:22px; height:22px; display:grid; place-items:center;
                flex-shrink:0; background:#fff; }

/* tile row for sentence builder */
.g-tiles { display:flex; gap:7px; flex-wrap:wrap; margin:4px 0 8px; }

/* word / word / word scramble string */
.g-slash { font-family:Poppins; font-weight:700; font-size:14px;
           color:var(--navy); letter-spacing:.5px; }

/* stem + long write line */
.g-stem { font-family:Poppins; font-size:14px; color:var(--navy);
           font-weight:600; margin-right:6px; }
.g-stem-row { display:flex; align-items:flex-end; gap:6px; flex-wrap:wrap;
              padding:6px 0; }

/* dialogue */
.g-dlg { margin:6px 0 0; }
.g-dlg-row { display:grid; grid-template-columns:30px 1fr; gap:8px;
              align-items:center; padding:6px 0; }
.g-who { font-family:Poppins; font-weight:700; font-size:14px; }
.g-said { font-family:Poppins; font-size:13px; color:var(--navy); }
.g-dlg-wl { border-bottom:1.6px solid var(--lblue); min-width:160px; flex:1; height:18px; }

/* example label */
.g-ex-label { font-size:10px; color:var(--grey); font-family:Poppins; margin-left:4px; }
.g-ex-ans { font-family:Poppins; font-weight:700; }

/* inline blank */
.g-blank { display:inline-block; border-bottom:1.8px solid var(--lblue);
           min-width:80px; height:17px; vertical-align:bottom; margin:0 3px; }
`;

/* ── helpers ──────────────────────────────────────────────────────────────── */

function _c(color) { return `var(--${color})`; }

// Replace first ___ in text with replacement HTML; return the whole sentence HTML.
function _injectBlank(text, replacement) {
  const parts = text.split("___");
  if (parts.length < 2) return text + " " + replacement;
  return parts[0] + replacement + parts.slice(1).join("___");
}

// Numbered badge reusing house-style .n
function _badge(n, color) {
  return `<span class="n" style="background:${_c(color)};color:#fff;border-radius:50%;width:22px;height:22px;display:grid;place-items:center;font-family:Poppins;font-weight:700;font-size:12px;flex-shrink:0">${n}</span>`;
}

function _picHtml(slug) {
  if (!slug) return "";
  return `<img class="g-pic" src="${imgsrc(slug)}" alt="${disp(slug)}">`;
}

// A single handwriting underline
function _wlLine(minWidth) {
  return `<span class="wl g-blank" style="min-width:${minWidth || 100}px"></span>`;
}

/* ═══════════════════════════════════════════════════════════════════════════
   1. renderCircleCorrect
   ═══════════════════════════════════════════════════════════════════════════ */
function renderCircleCorrect(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Circle the Correct Answer";
  const instr = opts.instr || "Read each sentence. Circle the correct word.";
  let h = cardOpen(color, "A", label, instr, "g-circle-card");
  h += `<ul class="g-rows">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    h += `<li>`;
    h += _badge(i + 1, color);
    if (item.pic) h += _picHtml(item.pic);
    // Build the sentence, inserting choices where ___ is
    const choiceHtml = `<span class="g-choice-wrap">` +
      item.options.map(opt => {
        const isAns = opt === item.answer;
        if (isEx) {
          // pre-fill the correct one highlighted; wrong one greyed
          return isAns
            ? `<span class="g-choice" style="border-color:${c};color:${c}">${opt}</span>`
            : `<span class="g-choice" style="border-color:#ccc;color:#ccc">${opt}</span>`;
        }
        return `<span class="g-choice" style="border-color:${c}">${opt}</span>`;
      }).join("") +
      `</span>`;
    const sentText = _injectBlank(item.text, choiceHtml);
    h += `<span style="font-family:Poppins;font-size:13px;flex:1">${sentText}`;
    if (isEx) h += `<span class="g-ex-label">(example)</span>`;
    h += `</span>`;
    h += `</li>`;
  });
  h += `</ul></div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   2. renderFillBlank
   ═══════════════════════════════════════════════════════════════════════════ */
function renderFillBlank(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Fill in the Blank";
  const instr = opts.instr || "Look at the word box. Write the correct word on the line.";
  let h = cardOpen(color, "B", label, instr, "g-fill-card");
  h += `<ul class="g-rows">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    h += `<li>`;
    h += _badge(i + 1, color);
    if (item.pic) h += _picHtml(item.pic);
    const blankOrAns = isEx
      ? `<span class="g-ex-ans" style="color:${c}">${item.answer}</span>`
      : `<span class="g-blank"></span>`;
    const sentText = _injectBlank(item.text, blankOrAns);
    h += `<span style="font-family:Poppins;font-size:13px;flex:1">${sentText}`;
    if (isEx) h += `<span class="g-ex-label">(example)</span>`;
    h += `</span>`;
    h += `</li>`;
  });
  h += `</ul>`;
  if (opts.wordBank && opts.wordBank.length) {
    h += `<div class="wordbox" style="border-color:${c};margin-top:10px">` +
         `<b style="color:${c}">Word Box</b>` +
         `<span class="ws">${opts.wordBank.join("　　")}</span></div>`;
  }
  h += `</div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   3. renderTrueFalse
   ═══════════════════════════════════════════════════════════════════════════ */
function renderTrueFalse(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "True or False";
  const instr = opts.instr || "Read the sentence. Circle T for True or F for False.";
  let h = cardOpen(color, "C", label, instr, "g-tf-card");
  h += `<ul class="g-rows">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    const tStyle = isEx && item.answer === true  ? `background:${c};color:#fff;border-color:${c}` : `border-color:${c}`;
    const fStyle = isEx && item.answer === false ? `background:${c};color:#fff;border-color:${c}` : `border-color:${c}`;
    h += `<li>`;
    h += _badge(i + 1, color);
    if (item.pic) h += _picHtml(item.pic);
    h += `<span style="font-family:Poppins;font-size:13px;flex:1">${item.text}`;
    if (isEx) h += `<span class="g-ex-label">(example)</span>`;
    h += `</span>`;
    h += `<span class="g-tf-box" style="${tStyle}">T</span>`;
    h += `<span class="g-tf-box" style="${fStyle}">F</span>`;
    h += `</li>`;
  });
  h += `</ul></div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   4. renderMC
   ═══════════════════════════════════════════════════════════════════════════ */
function renderMC(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Multiple Choice";
  const instr = opts.instr || "Read each question. Circle the letter of the best answer.";
  let h = cardOpen(color, "D", label, instr, "g-mc-card");
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    h += `<div style="margin-bottom:10px">`;
    // Question line
    h += `<div style="display:flex;align-items:center;gap:10px">`;
    h += _badge(i + 1, color);
    if (item.pic) h += _picHtml(item.pic);
    h += `<span style="font-family:Poppins;font-size:13px;font-weight:600;color:var(--navy)">${item.text}`;
    if (isEx) h += `<span class="g-ex-label">(example)</span>`;
    h += `</span></div>`;
    // Options — directly under prompt
    h += `<ul class="g-mc-opts">`;
    const letters = ["a", "b", "c", "d"];
    item.options.forEach((opt, j) => {
      const isAns = j === item.answer;
      const lStyle = isEx && isAns
        ? `border-color:${c};background:${c};color:#fff`
        : `border-color:${c};color:${c}`;
      h += `<li><span class="g-mc-letter" style="${lStyle}">${letters[j]}</span>`;
      h += `<span>${opt}</span></li>`;
    });
    h += `</ul></div>`;
  });
  h += `</div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   5. renderSentenceBuilder
   ═══════════════════════════════════════════════════════════════════════════ */
function renderSentenceBuilder(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Sentence Builder";
  const instr = opts.instr || "Put the words in the correct order. Write the sentence on the line.";
  let h = cardOpen(color, "E", label, instr, "g-sb-card");
  h += `<ul class="g-rows" style="list-style:none;padding:0;margin:0">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    // Shuffle word tiles deterministically
    const shuffled = shuffle(item.words, i * 17 + 3);
    h += `<li style="flex-direction:column;align-items:flex-start;padding:8px 0;border-bottom:1px dashed #e5e9f0">`;
    h += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">`;
    h += _badge(i + 1, color);
    // Tiles row
    h += `<div class="g-tiles">`;
    shuffled.forEach(w => {
      h += `<span class="tile" style="border-color:${c};color:${c}">${w}</span>`;
    });
    h += `</div></div>`;
    // Handwriting line (or pre-filled example)
    if (isEx) {
      // Capitalise first char of answer naturally
      const ans = item.answer.charAt(0).toUpperCase() + item.answer.slice(1);
      h += `<div style="padding-left:30px"><span class="g-ex-ans" style="color:${c}">${ans}</span>`;
      h += `<span class="g-ex-label">(example)</span></div>`;
    } else {
      h += `<div style="padding-left:30px;width:100%"><span class="wl" style="display:block;width:calc(100% - 30px);border-bottom:1.6px solid var(--lblue);height:22px"></span></div>`;
    }
    h += `</li>`;
  });
  h += `</ul></div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   6. renderScrambledSentences
   ═══════════════════════════════════════════════════════════════════════════ */
function renderScrambledSentences(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Scrambled Sentences";
  const instr = opts.instr || "Unscramble the words. Write the correct sentence on the line.";
  let h = cardOpen(color, "F", label, instr, "g-ss-card");
  h += `<ul class="g-rows">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    const shuffled = shuffle(item.words, i * 13 + 5);
    const slashStr = shuffled.join(" / ");
    h += `<li style="flex-direction:column;align-items:flex-start;padding:8px 0;border-bottom:1px dashed #e5e9f0">`;
    h += `<div style="display:flex;align-items:center;gap:8px;margin-bottom:6px">`;
    h += _badge(i + 1, color);
    h += `<span class="g-slash">${slashStr}</span>`;
    h += `</div>`;
    if (isEx) {
      const ans = item.answer.charAt(0).toUpperCase() + item.answer.slice(1);
      h += `<div style="padding-left:30px"><span class="g-ex-ans" style="color:${c}">${ans}</span>`;
      h += `<span class="g-ex-label">(example)</span></div>`;
    } else {
      h += `<div style="padding-left:30px;width:100%"><span class="wl" style="display:block;width:calc(100% - 30px);border-bottom:1.6px solid var(--lblue);height:22px"></span></div>`;
    }
    h += `</li>`;
  });
  h += `</ul></div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   7. renderSentenceCompletion
   ═══════════════════════════════════════════════════════════════════════════ */
function renderSentenceCompletion(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Sentence Completion";
  const instr = opts.instr || "Finish the sentence. Write your own ending on the line.";
  let h = cardOpen(color, "G", label, instr, "g-sc-card");
  h += `<ul class="g-rows">`;
  items.forEach((item, i) => {
    const isEx = opts.example && i === 0;
    h += `<li style="flex-direction:column;align-items:flex-start;padding:8px 0;border-bottom:1px dashed #e5e9f0">`;
    h += `<div class="g-stem-row">`;
    h += _badge(i + 1, color);
    if (item.pic) h += _picHtml(item.pic);
    h += `<span class="g-stem">${item.stem}</span>`;
    h += `<span class="g-blank" style="min-width:200px;flex:1"></span>`;
    if (isEx) h += `<span class="g-ex-label">(example)</span>`;
    h += `</div>`;
    h += `</li>`;
  });
  h += `</ul></div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   8. renderDialogueCompletion
   ═══════════════════════════════════════════════════════════════════════════ */
function renderDialogueCompletion(items, color, opts = {}) {
  const c = _c(color);
  const label = opts.title || "Dialogue Completion";
  const instr = opts.instr || "Read the dialogue. Write the missing line on the blank.";
  let h = cardOpen(color, "H", label, instr, "g-dc-card");
  items.forEach((item, dialogueIdx) => {
    const isFirstEx = opts.example && dialogueIdx === 0;
    if (dialogueIdx > 0) h += `<hr style="border:none;border-top:1px dashed #e5e9f0;margin:8px 0">`;
    h += `<div class="g-dlg">`;
    item.lines.forEach((line, li) => {
      const isBlank = !line.text || line.text.trim() === "";
      const isExLine = isFirstEx && isBlank && li === 1; // mark first blank of first dialogue
      h += `<div class="g-dlg-row">`;
      h += `<span class="g-who" style="color:${c}">${line.who}:</span>`;
      if (isBlank) {
        if (isExLine && line.answer) {
          h += `<span class="g-said"><span class="g-ex-ans" style="color:${c}">${line.answer}</span><span class="g-ex-label">(example)</span></span>`;
        } else {
          h += `<span class="g-dlg-wl"></span>`;
        }
      } else {
        h += `<span class="g-said">${line.text}</span>`;
      }
      h += `</div>`;
    });
    h += `</div>`;
  });
  h += `</div>`;
  return h;
}

/* ═══════════════════════════════════════════════════════════════════════════
   C. SAMPLE_GRAMMAR — EOW2 themed sample data
   ═══════════════════════════════════════════════════════════════════════════ */
const SAMPLE_GRAMMAR = {
  circleCorrect: [
    { text: "She ___ happy today.", options: ["is", "are"], answer: "is", pic: "smiling" },
    { text: "They ___ very tired.", options: ["is", "are"], answer: "are", pic: "tired" },
    { text: "I ___ hungry right now.", options: ["am", "is"], answer: "am", pic: "hungry" },
    { text: "He ___ angry at the dog.", options: ["am", "is"], answer: "is", pic: "angry" },
    { text: "We ___ scared of the dark.", options: ["is", "are"], answer: "are", pic: "scared" },
    { text: "The baby ___ crying.", options: ["is", "are"], answer: "is", pic: "crying" },
    { text: "You ___ thirsty.", options: ["am", "are"], answer: "are", pic: "thirsty" },
    { text: "My friends ___ bored.", options: ["is", "are"], answer: "are", pic: "bored" },
    { text: "It ___ a surprise.", options: ["is", "are"], answer: "is", pic: "surprised" },
    { text: "I ___ yawning.", options: ["am", "is"], answer: "am", pic: "yawning" }
  ],
  fillBlank: [
    { text: "I ___ scared of the dark.", answer: "am", pic: "scared" },
    { text: "We ___ so bored at home.", answer: "are", pic: "bored" },
    { text: "She ___ surprised by the gift.", answer: "is", pic: "surprised" },
    { text: "They ___ thirsty after the game.", answer: "are", pic: "thirsty" },
    { text: "He ___ very hungry now.", answer: "is", pic: "hungry" },
    { text: "The dog ___ tired.", answer: "is", pic: "tired" },
    { text: "You ___ angry today.", answer: "are", pic: "angry" },
    { text: "I ___ smiling at you.", answer: "am", pic: "smiling" },
    { text: "We ___ laughing a lot.", answer: "are", pic: "laughing" },
    { text: "She ___ frowning now.", answer: "is", pic: "frowning" }
  ],
  fillBlankWordBank: ["am", "is", "are"],
  trueFalse: [
    { text: "A horse can swim.", answer: true, pic: "horse" },
    { text: "A turtle can fly.", answer: false, pic: "turtle" },
    { text: "A duck can swim.", answer: true, pic: "duck" },
    { text: "A chicken can climb trees.", answer: false, pic: "chicken" },
    { text: "A cat can crawl.", answer: true, pic: "cat" },
    { text: "A cow can fly.", answer: false, pic: "cow" },
    { text: "A goat can climb.", answer: true, pic: "goat" },
    { text: "A sheep can swim.", answer: true, pic: "sheep" },
    { text: "A dog can climb trees.", answer: false, pic: "dog" },
    { text: "A bird can fly.", answer: true, pic: "fly" }
  ],
  mc: [
    { text: "How are you?", options: ["I'm fine, thank you.", "Yes, I am.", "It's a cat."], answer: 0 },
    { text: "What is she doing?", options: ["She is crying.", "She is swimming.", "She is flying."], answer: 0, pic: "crying" },
    { text: "Are they laughing?", options: ["Yes, they are.", "No, I am.", "She is smiling."], answer: 0, pic: "laughing" },
    { text: "What does the dog do?", options: ["It can crawl.", "It can fly.", "It can swim."], answer: 0, pic: "dog" },
    { text: "Why are you yawning?", options: ["I am tired.", "I am a fish.", "Yes, please."], answer: 0, pic: "yawning" },
    { text: "How does he feel?", options: ["He is angry.", "He is a desk.", "It is raining."], answer: 0, pic: "angry" },
    { text: "What do you want?", options: ["I am thirsty.", "I am Monday.", "She is tall."], answer: 0, pic: "thirsty" },
    { text: "Is she happy?", options: ["Yes, she is smiling.", "No, she can fly.", "It is a hat."], answer: 0, pic: "smiling" },
    { text: "Why is the baby crying?", options: ["He is hungry.", "He is green.", "He is a car."], answer: 0, pic: "hungry" },
    { text: "How do they feel?", options: ["They are bored.", "They are clocks.", "They are seven."], answer: 0, pic: "bored" }
  ],
  sentenceBuilder: [
    { words: ["are", "you", "How"], answer: "How are you?" },
    { words: ["I'm", "today", "tired"], answer: "I'm tired today." },
    { words: ["are", "We", "happy"], answer: "We are happy." },
    { words: ["hungry", "I", "am"], answer: "I am hungry." },
    { words: ["is", "She", "scared"], answer: "She is scared." },
    { words: ["are", "They", "bored"], answer: "They are bored." },
    { words: ["thirsty", "am", "I"], answer: "I am thirsty." },
    { words: ["is", "He", "yawning"], answer: "He is yawning." },
    { words: ["smiling", "is", "She"], answer: "She is smiling." },
    { words: ["are", "surprised", "We"], answer: "We are surprised." }
  ],
  scrambledSentences: [
    { words: ["scared", "am", "I"], answer: "I am scared." },
    { words: ["are", "they", "bored"], answer: "They are bored." },
    { words: ["surprised", "is", "she"], answer: "She is surprised." },
    { words: ["angry", "is", "he"], answer: "He is angry." },
    { words: ["hungry", "am", "I"], answer: "I am hungry." },
    { words: ["tired", "are", "we"], answer: "We are tired." },
    { words: ["crying", "is", "baby", "the"], answer: "The baby is crying." },
    { words: ["thirsty", "are", "you"], answer: "You are thirsty." },
    { words: ["laughing", "is", "she"], answer: "She is laughing." },
    { words: ["happy", "am", "I"], answer: "I am happy." }
  ],
  sentenceCompletion: [
    { stem: "My favorite animal is", pic: "cat" },
    { stem: "I am happy when" },
    { stem: "After school, I like to" },
    { stem: "I feel tired when" },
    { stem: "I am scared of" },
    { stem: "My favorite food is" },
    { stem: "On the weekend, I like to" },
    { stem: "I feel excited when" },
    { stem: "My best friend is" },
    { stem: "I am hungry for" }
  ],
  dialogueCompletion: [
    {
      lines: [
        { who: "A", text: "How are you?" },
        { who: "B", text: "", answer: "I'm tired today." },
        { who: "A", text: "Oh no! Get some rest." },
        { who: "B", text: "", answer: "Thank you!" }
      ]
    },
    {
      lines: [
        { who: "A", text: "Are you hungry?" },
        { who: "B", text: "", answer: "Yes, I am very hungry." },
        { who: "A", text: "Let's go eat lunch!" },
        { who: "B", text: "", answer: "Great idea!" }
      ]
    }
  ]
};

/* ═══════════════════════════════════════════════════════════════════════════
   D. Node self-test
   ═══════════════════════════════════════════════════════════════════════════ */
/* node self-test removed for browser use; SAMPLE_* and renderers above are the exports. */
