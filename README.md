# PAS Curriculum Wiki

This wiki is the source of truth for PAS curriculum generation.

Use it before asking GPT or Codex to create lesson plans, brainstorm course ideas, or generate worksheets.

## Current Scope

- Detailed unit scope: EOW1
- Indexed source folders: EOW1-4
- EOW official sources: Google Drive and local exported PDFs
- Reading Base master source: Canva
- Grammar Box master source: Canva
- Preferred PAS worksheet style source: Dropbox, supported by Canva layout examples

## Core Rule

All generated materials must stay inside the selected level and unit.

If vocabulary, grammar, reading content, or worksheet patterns are not present in this wiki, the generator should mark the field as `DATA NEEDED` instead of inventing content.

## Source Navigation

Start at [00_Admin/source-navigation.md](00_Admin/source-navigation.md) to find where any content lives:

- Google Drive: official EOW textbooks, teacher manuals, worksheets, answer keys, audio.
- Canva: editable masters for Reading Base and Grammar Box.
- Dropbox: preferred PAS worksheet style examples.

## Folder Map

```text
00_Admin/
  Source files and extraction notes.

01_EOW/
  Official EOW scope, sequence, vocabulary, grammar, reading, and values.

02_Grammar_Box/
  Canva Grammar Box source index and local extracted grammar mappings.

03_Reading_Base/
  Canva Reading Base source index and exported reader mappings.

04_Worksheet_Pattern_Bank/
  Reusable worksheet activity patterns.

05_Prompt_Library/
  Prompts for GPT/Codex workflows.

06_Generator_Specs/
  Structured specs for future automation.

07_Style_Sources/
  Canva, Dropbox, and Drive style references. Use for layout, activity pacing, and worksheet tone.

08_Pilot_Runs/
  Archived generation runs: draft, audit report, and final PDF per run.
```

## Automation

The generation chain (Wiki → Prompt → Draft → Scope Audit → PDF) is defined in [06_Generator_Specs/automation-pipeline.md](06_Generator_Specs/automation-pipeline.md). First validated run: `08_Pilot_Runs/2026-06-12-eow1-u1/`.

## Recommended Workflow

1. Choose level and unit.
2. Read the EOW unit page.
3. Read matching Grammar Box source. Canva is the master source.
4. Read matching Reading Base entry. Canva is the master source.
5. Choose patterns from the Worksheet Pattern Bank.
6. Check Style Sources if the output should match PAS worksheet style.
7. Generate lesson plan or worksheet.
8. Run the EOW scope audit prompt before finalizing.
