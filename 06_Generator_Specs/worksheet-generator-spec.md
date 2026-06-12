# Worksheet Generator Spec

## Goal

Generate PAS worksheets from the Curriculum Wiki without hallucinating vocabulary, grammar, or story details.

## Inputs

```yaml
level: EOW1
unit: 1
reading_base_story: null
page_range: null
worksheet_types:
  - vocabulary
  - grammar
  - reading
student_level: CL1
pages: 1
include_answer_key: true
```

## Required Data Reads

1. `01_EOW/EOW1/unit-XX-*.md`
2. Matching file in `02_Grammar_Box/Level1/`
3. `03_Reading_Base/` entry if requested and available.
4. `04_Worksheet_Pattern_Bank/pattern-bank.md`

## Internal Planning Output

```yaml
selected_unit:
target_vocabulary:
target_grammar:
reading_source:
selected_patterns:
missing_data:
```

## Failure Rules

- If Reading Base story is requested but not mapped, output `DATA NEEDED: Reading Base`.
- If a vocabulary word is not listed in the unit, replace it or flag it.
- If a grammar target is not listed, replace it or flag it.
- If exact printable copy is required from an image-based source, request OCR/manual verification.

## Future Automation

The next implementation step can create a script or small app that:

1. Takes unit and worksheet type as input.
2. Reads the Markdown wiki.
3. Generates worksheet Markdown.
4. Exports to DOCX or PDF.
5. Runs a scope audit before final output.

