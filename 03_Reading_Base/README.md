# Reading Base

Status: Canva master source identified; exported PDF story maps partially available.

Reading Base lives in Canva. Local PDF exports are useful for extraction, but Canva should be treated as the editable source of truth.

## Editing Standards

Reading Base writing and structure vary by level. Read the [level-specific editing standards](editing-standards-by-level.md) before planning or revising a story.

Do not assume that every level uses the same story count, page count, language density, humor, or activity format. Confirm the approved plan for the selected level and unit first.

When a unit uses the four-story structure, follow this alignment:

| Story | Required alignment |
|---|---|
| Story 1 | Vocabulary 1 + Grammar 1 |
| Story 2 | Vocabulary 2 + Grammar 2 |
| Story 3 | The unit's Reading section |
| Story 4 | The unit's Value section |

### Shared Story Content Principles

Each story must:

- be interesting and engaging enough to motivate children to learn; or
- be an age-appropriate adaptation inspired by a classic work.

Whichever approach is used, the story must stay inside the selected EOW level and unit. Do not introduce vocabulary, grammar, reading content, or values outside the mapped scope. If required source content is missing, mark it as `DATA NEEDED` instead of inventing it.

### Editing Checklist

Before finalizing a Reading Base unit, confirm that:

- the story count and page format match the selected level's approved plan;
- each story or chapter has a documented source alignment;
- a four-story unit follows the required alignment order;
- each story is engaging for children or clearly based on an age-appropriate classic adaptation;
- all language and content remain within the selected level and unit;
- the story follows the level-specific standards for language, tone, structure, and activity design.

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
story_count_for_unit:
story_title:
approval_status:
approved_version:
pages:
word_count:
point_of_view:
genre:
tone:
source_alignment:
target_vocabulary:
target_grammar:
spiral_review_language:
reading_focus:
value_focus:
classic_adaptation_source:
story_hook:
central_problem:
resolution:
activity_type:
worksheet_opportunities:
important_revision_decisions:
notes:
```

## Why This Matters

Worksheet generation should eventually be able to target a specific story and page range.

Example future request:

```text
Generate a worksheet for EOW1 Unit 3, Reading Base Story 2, pages 1-4.
```

Until a Canva reader design is opened, exported, or mapped, worksheet generation should use EOW and Grammar Box only and mark reading details as `DATA NEEDED`.
