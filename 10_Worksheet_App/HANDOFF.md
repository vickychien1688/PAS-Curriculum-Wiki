# Worksheet App — Handoff / 交接說明

_Last updated: 2026-06-18 (overnight build)._

## What changed 這次做了什麼

1. **New file `content_eow2.js`** — a real, unit-specific grammar content layer for
   **EOW2 Units 1–8**, authored from your approved Pilot-Run generators
   (`08_Pilot_Runs/2026-06-16-eow2-u#-voc-gram/generator_color.py` + `eow2lib.py`).
   English only. Every `pic` slug was checked against `../09_Image_Library/words/`.
2. **`index.html`** now loads `content_eow2.js` (after the three `render_*.js` files)
   and prefers this real content for EOW2 grammar sections. The grey
   *"Sample content — unit-specific questions coming soon."* note now only appears
   when a section is genuinely using sample data.

The visual house style and all renderers were **not** changed.

---

## What is now REAL (EOW2 grammar) 已是真實題庫

Each unit follows its actual grammar focus. Pick these in the app under
**Grammar 文法** for the matching EOW2 unit:

| Unit | Grammar focus | Real patterns available |
|------|---------------|--------------------------|
| **U1 Animal Friends** | They are + verb-ing; word order | `fillblank`, `circlecorrect`, `scrambledsentences`, `sentencebuilder` |
| **U2 Fun in Class** | We're + verb-ing; Are there…? | `fillblank`, `circlecorrect`, `mc` |
| **U3 Boots & Bathing Suits** | It's + weather; imperatives | `fillblank`, `circlecorrect`, `mc` |
| **U4 Fun in the Sun** | Do you like to…?; Let's… | `scrambledsentences`, `sentencebuilder`, `mc`, `sentencecompletion` |
| **U5 Inside Our House** | prepositions; It's / They're | `fillblank`, `circlecorrect`, `mc` |
| **U6 Day by Day** | telling time; always/never/every day | `fillblank`, `circlecorrect`, `mc` |
| **U7 How Are You?** | looks + adjective; plurals | `mc`, `fillblank`, `circlecorrect` |
| **U8 Awesome Animals** | can / can't; Does … have …? | `truefalse`, `mc`, `circlecorrect` |

Each pattern has ~8 items (a few have fewer where the source did). If you ask for
more questions than exist, the app shows as many as it has.

> Note: any EOW2 grammar pattern **not** in the table above (e.g. `dialoguecompletion`,
> `lookwrite`, `lookanswer` for some units) still falls back to generic sample data
> and will show the grey "Sample content" note. That is expected.

---

## What is still SAMPLE 仍是範例（暫用）

- **Reading 閱讀** and **Value 品格** passages — for ALL levels/units.
  We don't have the textbook "Listen and Read" text, so these use a placeholder
  passage. They are clearly marked with the grey sample note.
- **EOW1, EOW3, EOW4 grammar** — all still sample. Only EOW2 grammar is real.
- **Vocabulary 單字** is word-driven (real) for every level/unit already — it pulls
  the actual unit word list, so it does NOT show a sample note.

---

## How to open the app 如何開啟

Open **`index.html` directly in Chrome** from this folder
(`10_Worksheet_App/`) — e.g. drag the file into a Chrome tab, or
`File ▸ Open File…`.

Do **NOT** open it through a preview pane or a different folder: the artwork is
loaded with the relative path `../09_Image_Library/words/…`, so the page must run
from inside `10_Worksheet_App/` for the pictures to appear.

Then: choose **Level + Unit + 區塊 + 題型 + 題數** → **加入此區段** (can add up to 8) →
**產生學習單** → **列印 / 存 PDF**.

---

## Next content the teacher needs to provide 下一步請老師提供

1. **Textbook "Listen and Read" passages** for each EOW2 unit (U1–U8) — the real
   story text + 4–5 comprehension questions per story. This unlocks real
   **Reading** worksheets (currently sample).
2. **Value (品格) passages** per unit (the short character-education text already
   in your generators, e.g. U1 "Be good to animals", U2 "Be neat").
3. **EOW1 / EOW3 / EOW4 grammar focuses** — once you confirm each unit's target
   structure (the way EOW2 generators already encode it), we can build the same
   real grammar layer (`content_eow1.js`, etc.) for those levels.

When you hand any of these over, we add them the same way `content_eow2.js` was
built — unit by unit, English only, using only that unit's vocabulary.

---

## Verification done 已通過的自動檢查

A jsdom test (`/tmp/test_worksheet.js`) generated **299** worksheet combinations
(every block × pattern for EOW2 U1–8, plus multi-section combines) and confirmed:
no `undefined` in output, **zero Chinese characters** in any worksheet, every
worksheet renders ≥1 page, real EOW2 grammar shows (with no sample note), and the
requested question count is respected. `node -c` passes on all four JS files.
