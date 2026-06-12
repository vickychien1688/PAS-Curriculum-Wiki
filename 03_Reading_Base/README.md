# Reading Base

Status: Canva master source identified; exported PDF story maps partially available.

Reading Base lives in Canva. Local PDF exports are useful for extraction, but Canva should be treated as the editable source of truth.

## Current Index

- [Canva Reading Base Index](canva-index.md)
- [EOW1 Reading Base Index](eow1-index.md)
- [EOW1 Unit 1 Reader](eow1-unit-01.md)
- [EOW1 Unit 2 Reader](eow1-unit-02.md)
- [EOW1 Unit 3 Reader](eow1-unit-03.md)
- [EOW1 Unit 4 Reader](eow1-unit-04.md)
- [EOW1 Unit 5 Reader](eow1-unit-05.md)
- [EOW1 Unit 6 Reader](eow1-unit-06.md)

## What To Add

For each Reading Base story, add:

```yaml
level:
unit:
story_title:
pages:
target_vocabulary:
target_grammar:
reading_skill:
worksheet_opportunities:
notes:
```

## Why This Matters

Worksheet generation should eventually be able to target a specific story and page range.

Example future request:

```text
Generate a worksheet for EOW1 Unit 3, Reading Base Story 2, pages 1-4.
```

Until a Canva reader design is opened, exported, or mapped, worksheet generation should use EOW and Grammar Box only and mark reading details as `DATA NEEDED`.
