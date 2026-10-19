# Scope Audit: EOW1 U1-01 My Classroom

Prompt: `05_Prompt_Library/scope-audit.md`
Level: EOW1 / Unit: 1
Draft: `worksheet.md` → `EOW1 U1-01 My Classroom.pdf`

## Result: PASS

| Check | Result | Notes |
|---|---|---|
| 1. Vocabulary inside EOW1 U1 | PASS | Used: clock, computer, pencil, pen, book, chair, desk. All from Vocabulary 1/2. Unused U1 words (crayon, map, paper, eraser, picture) available for U1-02. |
| 2. Grammar inside U1 / Grammar Box 1-2 | PASS | Yes/No with `it's` (Part B, D), What / How many (Part C, D). Singular/plural counting aligns with Grammar Box U1-2 noun pages. |
| 3. Reading Base supported | PASS | Part D mirrors Story 1 `What is it?` (reader pages 1-6) per `03_Reading_Base/eow1-unit-01.md`. |
| 4. Patterns in Pattern Bank | PASS | WS-001, WS-002, WS-003, WS-006. Matching item count 6 (within 6-10 Level 1 constraint). |
| 5. Difficulty appropriate for Level 1 | PASS | Recognition, matching, counting, controlled frames; word bank provided for Part C. |

## Notes

- Number words `two/three/four/five` appear as required output of the `How many` grammar target; they are not unit vocabulary but are unavoidable for this pattern.
- Icons are generated line drawings; replace with PAS art in Canva if printing for students.
- Value line `Work hard in school.` present on all pages.

## Chain Verification

Wiki read → planning YAML → draft → audit → PDF all completed inside this repo. The pipeline in `06_Generator_Specs/automation-pipeline.md` is confirmed workable for EOW1 U2-U8 replication.

## Design Pass (v3 — approved direction)

Final output `EOW1 U1 My Classroom.pdf`, 3 pages, matches the user-approved reference layout (GPT-rendered sample, 2026-06-12):

- White page, NAME/DATE header, centered black-circle-badge title.
- Black numbered item badges, dotted section dividers, dotted write-on lines.
- Section A Match (6 items), B Circle 2x2 grid, C How many + word bank box, D What is it.
- Page 3 answer key + teacher notes.
- Icons: realistic flat classroom objects, code-drawn in `icons2.py` (no external images; resolution-independent).

Reproduce with: `python3 generator.py` (needs reportlab + pdf2image for preview; fonts: Poppins).
