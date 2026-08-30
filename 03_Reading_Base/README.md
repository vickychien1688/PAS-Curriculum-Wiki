# Reading Base

Status: Canva master source identified; exported PDF story maps partially available.

Reading Base lives in Canva. Local PDF exports are useful for extraction, but Canva should be treated as the editable source of truth.

## Editing Standard

Each Reading Base unit contains four stories. Design and edit the stories in the following order:

| Story | Required alignment |
|---|---|
| Story 1 | Vocabulary 1 + Grammar 1 |
| Story 2 | Vocabulary 2 + Grammar 2 |
| Story 3 | The unit's Reading section |
| Story 4 | The unit's Value section |

### Story Content Principles

Each story must:

- be interesting and engaging enough to motivate children to learn; or
- be an age-appropriate adaptation inspired by a classic work.

Whichever approach is used, the story must stay inside the selected EOW level and unit. Do not introduce vocabulary, grammar, reading content, or values outside the mapped scope. If required source content is missing, mark it as `DATA NEEDED` instead of inventing it.

### Editing Checklist

Before finalizing a Reading Base unit, confirm that:

- all four stories follow the required alignment order;
- Story 1 uses Vocabulary 1 and Grammar 1;
- Story 2 uses Vocabulary 2 and Grammar 2;
- Story 3 supports the unit's Reading section;
- Story 4 communicates the unit's Value focus;
- each story is engaging for children or clearly based on an age-appropriate classic adaptation; and
- all language and content remain within the selected level and unit.

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
story_number:
story_title:
pages:
source_alignment:
target_vocabulary:
target_grammar:
reading_skill:
value_focus:
classic_adaptation_source:
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
