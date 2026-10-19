# Automation Pipeline

End-to-end chain: Curriculum Wiki → Prompt → Generation → Scope Audit → PDF.

This is the operating plan for producing any PAS lesson plan or worksheet with AI. Validated with a pilot run on EOW1 Unit 1 (see `08_Pilot_Runs/`).

## Pipeline Stages

| # | Stage | Input | Output | Gate |
|---|---|---|---|---|
| 1 | Select target | Level, unit, worksheet types, student level | Generation request (YAML per `worksheet-generator-spec.md`) | Unit page must exist in `01_EOW/`; otherwise stop with `DATA NEEDED`. |
| 2 | Wiki reads | Request | Planning YAML (`selected_unit`, `target_vocabulary`, `target_grammar`, `reading_source`, `selected_patterns`, `missing_data`) | All four required reads done: EOW unit page, Grammar Box mapping, Reading Base entry, Pattern Bank. |
| 3 | Draft generation | Planning YAML + Prompt Library template + Dropbox style guide | Worksheet/lesson plan in Markdown | Only wiki vocabulary and grammar; unknown fields marked `DATA NEEDED`. |
| 4 | Scope audit | Draft + `05_Prompt_Library/scope-audit.md` | PASS / NEEDS REVISION report | NEEDS REVISION loops back to stage 3. Max 2 loops, then escalate to human. |
| 5 | Render | Audited Markdown | PDF (A4, print-first, Dropbox style) | Filename follows `EOW{level} U{unit}-{seq} {tag}.pdf`. |
| 6 | Archive | PDF + draft + audit report | `08_Pilot_Runs/{date}-{target}/` in this repo | Human review before printing or distribution. |

## Execution Modes

1. Manual with any chat AI: paste the prompt from `05_Prompt_Library/`, attach or let it read the wiki pages from stage 2.
2. Cowork/Claude session: point the session at this repo and say e.g. `EOW1 Unit 3, vocabulary + grammar worksheet`. The session follows this pipeline file.
3. Future script: see `worksheet-generator-spec.md` "Future Automation". Not built yet.

## Hard Rules (apply in every mode)

- The wiki is the only allowed content source. No invented vocabulary, grammar, or story details.
- Canva is the master for Reading Base / Grammar Box text. Image-based PDFs require manual verification before student-facing copy.
- Every output lists its pattern IDs (`WS-XXX`) and source wiki pages.
- Every output ends with the unit Value line where layout allows.
- Answer keys are generated with every worksheet.

## Roadmap

| Priority | Item | Blocked by |
|---|---|---|
| 1 | Pilot EOW1 U1 worksheet chain | Done. See `08_Pilot_Runs/`. |
| 2 | Repeat for EOW1 U2-U8 | Nothing; same chain. |
| 3 | EOW2-4 unit scope extraction (teacher manuals in Google Drive) | Manual extraction or Drive connector session. |
| 4 | Reading Base story-level extraction from Canva | Opening each Canva design and exporting text. |
| 5 | Generator script (md → PDF, batch mode) | Stable worksheet template from pilots 1-2. |
