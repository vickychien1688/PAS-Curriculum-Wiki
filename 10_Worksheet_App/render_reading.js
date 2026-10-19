/**
 * render_reading.js — Reading & extension renderers for the PAS Worksheet Generator
 * Designed to work alongside index.html; all globals (cardOpen, disp, imgsrc, shuffle) are
 * provided by the host page. For Node self-test they are stubbed below.
 *
 * =============================================================================
 * SCHEMA
 * =============================================================================
 *
 * renderReadingComp(data, color)
 *   data = {
 *     title   : string,                      // story name only, no "Reading:" prefix
 *     passage : string,                      // multi-sentence prose
 *     image   : string,                      // slug (used with imgsrc) OR a bare URL/path
 *     tf      : [{ text: string, answer: boolean }],   // ~5 items
 *     mc      : [{ text: string, options: string[], answer: number }]  // ~5 items; answer = 0-based index
 *   }
 *
 * renderWritingLab(data, color)
 *   data = {
 *     emotions : string[],    // word chips for Emotion Bank
 *     thoughts : string[],    // prompt phrases for Thought Bank
 *     stems    : string[],    // sentence starter stems
 *     lines    : number       // blank handwriting lines in "Build Your Paragraph"
 *   }
 *
 * renderListenCircle(data, color)
 *   data = {
 *     items: [
 *       { pics: ["slug1","slug2",...], answer: number }   // picture-based
 *       | { words: string[], answer: number }             // word-based
 *     ]
 *   }
 *
 * renderLookAnswer(data, color)
 *   data = {
 *     items: [{ image: string, question: string }]
 *   }
 *
 * =============================================================================
 */

/* ─── New CSS (namespaced r-) ────────────────────────────────────────────── */
const CSS_READING = `
/* ── Reading Comprehension ─────────────────────────────────────── */
.r-title-area {
  text-align: center;
  margin: 10px 8px 14px;
}
.r-title-area h2 {
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 22px;
  color: var(--navy);
  margin: 0 0 2px;
  line-height: 1.2;
}
.r-title-accent {
  display: inline-block;
  width: 60px;
  height: 3px;
  border-radius: 2px;
  background: currentColor;
}

.r-passage {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  background: #fff;
  border-radius: 14px;
  border: 1.5px solid var(--frame, #d8e0ea);
  padding: 16px 18px;
  margin: 0 8px 16px;
}
.r-pass-text {
  flex: 1;
  font-size: 14px;
  line-height: 2;
  color: var(--ink);
}
.r-pass-img {
  width: 200px;
  min-width: 160px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}
.r-pass-img img {
  width: 100%;
  max-width: 200px;
  height: 180px;
  object-fit: contain;
  border-radius: 10px;
  background: var(--bg);
}
.r-pass-img figcaption {
  font-size: 10px;
  color: var(--grey);
  text-align: center;
}

/* ── True / False ─────────────────────────────────────────────── */
.r-tf-row {
  display: flex;
  align-items: baseline;
  gap: 10px;
  padding: 9px 0;
  border-bottom: 1px solid #edf0f5;
}
.r-tf-row:last-child { border-bottom: none; }
.r-tf-text {
  flex: 1;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--ink);
}
.r-tf-opts {
  display: flex;
  gap: 10px;
  flex-shrink: 0;
}
.r-circle-btn {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  border: 1.8px solid;
  display: grid;
  place-items: center;
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 12px;
  background: #fff;
}

/* ── Multiple Choice ──────────────────────────────────────────── */
.r-mc-row {
  padding: 10px 0;
  border-bottom: 1px solid #edf0f5;
}
.r-mc-row:last-child { border-bottom: none; }
.r-mc-q {
  display: flex;
  align-items: baseline;
  gap: 8px;
  font-size: 13.5px;
  line-height: 1.5;
  color: var(--ink);
  margin-bottom: 6px;
}
.r-mc-options {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-left: 30px;
}
.r-mc-opt {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-family: Poppins, sans-serif;
}
.r-mc-letter {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 1.6px solid;
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 11px;
  background: #fff;
  flex-shrink: 0;
}

/* ── Writing Lab ─────────────────────────────────────────────── */
.r-wlab-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 14px;
}
.r-bank {
  border-radius: 12px;
  border: 1.4px solid;
  background: #fff;
  padding: 10px 14px 12px;
}
.r-bank-title {
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 12px;
  margin-bottom: 8px;
  letter-spacing: .3px;
}
.r-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.r-chip {
  border: 1.4px solid;
  border-radius: 20px;
  padding: 3px 11px;
  font-family: Poppins, sans-serif;
  font-weight: 600;
  font-size: 12.5px;
  background: #fff;
}
.r-thought-list {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.r-thought-item {
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--ink);
  padding-left: 10px;
  position: relative;
}
.r-thought-item::before {
  content: "✦";
  position: absolute;
  left: -2px;
  font-size: 9px;
  top: 3px;
}
.r-stem-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  padding: 8px 0;
  border-bottom: 1px dashed #e0e4ed;
}
.r-stem-row:last-child { border-bottom: none; }
.r-stem-label {
  font-family: Poppins, sans-serif;
  font-weight: 600;
  font-size: 13px;
  white-space: nowrap;
  flex-shrink: 0;
}
.r-stem-line {
  flex: 1;
  border-bottom: 1.6px solid var(--lblue);
  height: 14px;
  min-width: 80px;
}
.r-para-lines {
  margin-top: 6px;
}
.r-para-line {
  border-bottom: 1.6px solid var(--lblue);
  height: 32px;
  margin-bottom: 6px;
}

/* ── Listen and Circle ───────────────────────────────────────── */
.r-lc-row {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 10px 0;
  border-bottom: 1px solid #edf0f5;
}
.r-lc-row:last-child { border-bottom: none; }
.r-speaker {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--bg);
  border: 1.6px solid;
}
.r-lc-options {
  display: flex;
  align-items: center;
  gap: 20px;
  flex: 1;
  flex-wrap: wrap;
}
.r-lc-pic-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
}
.r-lc-pic-wrap img {
  width: 72px;
  height: 72px;
  object-fit: contain;
  border: 1.6px solid transparent;
  border-radius: 10px;
  background: var(--bg);
}
.r-lc-word-opt {
  border: 1.8px solid;
  border-radius: 10px;
  padding: 7px 18px;
  font-family: Poppins, sans-serif;
  font-weight: 700;
  font-size: 14px;
  background: #fff;
}

/* ── Look and Answer ─────────────────────────────────────────── */
.r-la-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 12px 0;
  border-bottom: 1px solid #edf0f5;
}
.r-la-item:last-child { border-bottom: none; }
.r-la-img {
  width: 110px;
  height: 100px;
  object-fit: contain;
  border-radius: 10px;
  background: var(--bg);
  flex-shrink: 0;
  border: 1.5px solid #e6e9f0;
}
.r-la-right {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding-top: 4px;
}
.r-la-q {
  font-size: 13.5px;
  font-family: Poppins, sans-serif;
  font-weight: 600;
  color: var(--ink);
  margin-bottom: 14px;
  line-height: 1.4;
}
.r-la-line {
  border-bottom: 1.6px solid var(--lblue);
  height: 14px;
}
`;

/* ─── Helpers ────────────────────────────────────────────────────────────── */
/** Resolve image src: if looks like a URL/path keep as-is, else use imgsrc(slug). */
function _imgSrc(ref) {
  if (!ref) return "";
  if (ref.startsWith("http") || ref.startsWith("/") || ref.startsWith("../") || ref.includes(".")) {
    return ref;
  }
  return imgsrc(ref);
}

const _LETTERS = ["a", "b", "c", "d", "e"];

/* ─── A) renderReadingComp ───────────────────────────────────────────────── */
/**
 * Outputs:
 *  (a) title heading area (full-width, above cards)
 *  (b) passage box (text left, image right)
 *  (c) card: Part A — True or False
 *  (d) card: Part B — Multiple Choice
 */
function renderReadingComp(data, color) {
  const c = `var(--${color})`;
  const ct = `var(--${color}t)`;

  // (a) Title heading
  let h = `<div class="r-title-area">`;
  h += `<h2 style="color:${c}">${data.title}</h2>`;
  h += `<span class="r-title-accent" style="color:${c}"></span>`;
  h += `</div>`;

  // (b) Passage box
  h += `<div class="r-passage">`;
  h += `<div class="r-pass-text">${data.passage}</div>`;
  if (data.image) {
    h += `<figure class="r-pass-img" style="margin:0">`;
    h += `<img src="${_imgSrc(data.image)}" alt="${data.title}">`;
    h += `</figure>`;
  }
  h += `</div>`;

  // (c) True / False card
  if (data.tf && data.tf.length) {
    h += cardOpen(color, "A", "True or False", "Read each sentence. Circle T for True or F for False.", "r-tf-section");
    data.tf.forEach((item, i) => {
      h += `<div class="r-tf-row">`;
      h += `<span class="n" style="background:${c};color:#fff;border-radius:50%;width:22px;height:22px;display:inline-grid;place-items:center;font-family:Poppins;font-weight:700;font-size:12px;flex-shrink:0">${i + 1}</span>`;
      h += `<span class="r-tf-text">${item.text}</span>`;
      h += `<span class="r-tf-opts">`;
      h += `<span class="r-circle-btn" style="border-color:${c};color:${c}">T</span>`;
      h += `<span class="r-circle-btn" style="border-color:var(--grey);color:var(--grey)">F</span>`;
      h += `</span>`;
      h += `</div>`;
    });
    h += `</div>`;
  }

  // (d) Multiple Choice card
  if (data.mc && data.mc.length) {
    h += cardOpen(color, "B", "Multiple Choice", "Read each question. Circle the best answer.", "r-mc-section");
    data.mc.forEach((item, i) => {
      h += `<div class="r-mc-row">`;
      h += `<div class="r-mc-q">`;
      h += `<span class="n" style="background:${c};color:#fff;border-radius:50%;width:22px;height:22px;display:inline-grid;place-items:center;font-family:Poppins;font-weight:700;font-size:12px;flex-shrink:0">${i + 1}</span>`;
      h += `<span>${item.text}</span>`;
      h += `</div>`;
      h += `<div class="r-mc-options">`;
      (item.options || []).forEach((opt, oi) => {
        h += `<div class="r-mc-opt">`;
        h += `<span class="r-mc-letter" style="border-color:${c};color:${c}">${_LETTERS[oi]}</span>`;
        h += `<span>${opt}</span>`;
        h += `</div>`;
      });
      h += `</div>`;
      h += `</div>`;
    });
    h += `</div>`;
  }

  return h;
}

/* ─── B) renderWritingLab ────────────────────────────────────────────────── */
function renderWritingLab(data, color) {
  const c = `var(--${color})`;
  const ct = `var(--${color}t)`;

  let h = cardOpen(color, "C", "Writing Lab", "Use the banks below to build your own paragraph.", "r-wlab");

  // Top row: Emotion Bank + Thought Bank
  h += `<div class="r-wlab-grid">`;

  // Emotion Bank
  h += `<div class="r-bank" style="border-color:${c};background:${ct}">`;
  h += `<div class="r-bank-title" style="color:${c}">Emotion Bank</div>`;
  h += `<div class="r-chips">`;
  (data.emotions || []).forEach(e => {
    h += `<span class="r-chip" style="border-color:${c};color:${c}">${e}</span>`;
  });
  h += `</div></div>`;

  // Thought Bank
  h += `<div class="r-bank" style="border-color:var(--navy);background:#f5f6fb">`;
  h += `<div class="r-bank-title" style="color:var(--navy)">Thought Bank</div>`;
  h += `<div class="r-thought-list">`;
  (data.thoughts || []).forEach(t => {
    h += `<div class="r-thought-item">${t}</div>`;
  });
  h += `</div></div>`;

  h += `</div>`; // close grid

  // Sentence Builder
  h += `<div class="r-bank" style="border-color:${c};margin-bottom:12px">`;
  h += `<div class="r-bank-title" style="color:${c}">Sentence Builder</div>`;
  (data.stems || []).forEach(stem => {
    h += `<div class="r-stem-row">`;
    h += `<span class="r-stem-label" style="color:var(--navy)">${stem}</span>`;
    h += `<span class="r-stem-line"></span>`;
    h += `</div>`;
  });
  h += `</div>`;

  // Build Your Paragraph
  h += `<div class="r-bank" style="border-color:var(--grey)">`;
  h += `<div class="r-bank-title" style="color:var(--grey)">Build Your Paragraph</div>`;
  h += `<div class="r-para-lines">`;
  const lineCount = data.lines || 6;
  for (let i = 0; i < lineCount; i++) {
    h += `<div class="r-para-line"></div>`;
  }
  h += `</div></div>`;

  h += `</div>`;
  return h;
}

/* ─── C) renderListenCircle ──────────────────────────────────────────────── */
function renderListenCircle(data, color) {
  const c = `var(--${color})`;

  // Speaker SVG icon
  const speakerSVG = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>`;

  let h = cardOpen(color, "D", "Listen and Circle", "Listen to your teacher. Circle the correct answer.", "r-lc-section");

  (data.items || []).forEach((item, i) => {
    h += `<div class="r-lc-row">`;
    h += `<span class="n" style="background:${c};color:#fff;border-radius:50%;width:22px;height:22px;display:inline-grid;place-items:center;font-family:Poppins;font-weight:700;font-size:12px;flex-shrink:0">${i + 1}</span>`;
    h += `<span class="r-speaker" style="border-color:${c};color:${c}">${speakerSVG}</span>`;
    h += `<div class="r-lc-options">`;

    if (item.pics && item.pics.length) {
      // Picture-based
      item.pics.forEach((slug, pi) => {
        h += `<div class="r-lc-pic-wrap">`;
        h += `<img src="${_imgSrc(slug)}" alt="${disp(slug)}" style="border-color:${pi === item.answer ? c : 'transparent'}">`;
        h += `<span style="font-family:Poppins;font-size:11px;color:var(--grey)">${disp(slug)}</span>`;
        h += `</div>`;
      });
    } else if (item.words && item.words.length) {
      // Word-based
      item.words.forEach((w, wi) => {
        h += `<span class="r-lc-word-opt" style="border-color:${wi === item.answer ? c : 'var(--grey)'};color:${wi === item.answer ? c : 'var(--ink)'}">`;
        h += `${w}`;
        h += `</span>`;
      });
    }

    h += `</div>`; // r-lc-options
    h += `</div>`; // r-lc-row
  });

  h += `</div>`;
  return h;
}

/* ─── D) renderLookAnswer ────────────────────────────────────────────────── */
function renderLookAnswer(data, color) {
  const c = `var(--${color})`;

  let h = cardOpen(color, "E", "Look and Answer", "Look at the picture. Write a complete sentence.", "r-la-section");

  (data.items || []).forEach((item, i) => {
    h += `<div class="r-la-item">`;
    h += `<img class="r-la-img" src="${_imgSrc(item.image)}" alt="${item.question}">`;
    h += `<div class="r-la-right">`;
    h += `<div class="r-la-q">`;
    h += `<span class="n" style="background:${c};color:#fff;border-radius:50%;width:22px;height:22px;display:inline-grid;place-items:center;font-family:Poppins;font-weight:700;font-size:12px;margin-right:8px">${i + 1}</span>`;
    h += `${item.question}`;
    h += `</div>`;
    h += `<div class="r-la-line"></div>`;
    h += `</div>`;
    h += `</div>`;
  });

  h += `</div>`;
  return h;
}

/* ─── SAMPLE DATA ────────────────────────────────────────────────────────── */
const SAMPLE_READING = {

  readingComp: {
    title: "Paper Art",
    passage: "Sam loves paper art. He folds paper into many shapes. He makes birds, boats, and frogs. First, he picks a color. Then he folds it step by step. Paper art is fun for everyone!",
    image: "book",
    tf: [
      { text: "Sam likes paper art.", answer: true },
      { text: "Sam makes paper cars.", answer: false },
      { text: "Sam picks a color first.", answer: true },
      { text: "Paper art is only for boys.", answer: false },
      { text: "Sam folds paper step by step.", answer: true }
    ],
    mc: [
      {
        text: "What does Sam love?",
        options: ["Paper art", "Music", "Sports"],
        answer: 0
      },
      {
        text: "What does Sam make first?",
        options: ["A boat", "A bird", "He picks a color"],
        answer: 2
      },
      {
        text: "Which shape does Sam NOT make?",
        options: ["A frog", "A car", "A boat"],
        answer: 1
      },
      {
        text: "How does Sam fold the paper?",
        options: ["Quickly and randomly", "Step by step", "All at once"],
        answer: 1
      },
      {
        text: "Who can enjoy paper art?",
        options: ["Only boys", "Only girls", "Everyone"],
        answer: 2
      }
    ]
  },

  writingLab: {
    emotions: ["happy", "excited", "proud", "nervous", "surprised", "calm"],
    thoughts: [
      "I think … because …",
      "It makes me feel … when …",
      "I want to … someday.",
      "My favorite part is …"
    ],
    stems: [
      "I feel _____ when I",
      "One day I hope to",
      "My best memory is"
    ],
    lines: 7
  },

  listenCircle: {
    items: [
      { pics: ["cat", "dog", "bird"], answer: 0 },
      { words: ["happy", "angry", "tired"], answer: 2 },
      { pics: ["apple", "banana", "chicken"], answer: 1 }
    ]
  },

  lookAnswer: {
    items: [
      { image: "cat", question: "Where is the cat?" },
      { image: "book", question: "What color is the book?" },
      { image: "apple", question: "How many apples are there?" }
    ]
  }
};

/* ─── Node self-test ─────────────────────────────────────────────────────── */
/* node self-test removed for browser use; SAMPLE_* and renderers above are the exports. */
