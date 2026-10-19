# Worksheet Pattern Bank

Use these patterns as reusable activity templates. Do not invent a new pattern unless existing patterns cannot serve the lesson goal.

## Pattern Index

| ID | Type | Best For | Output Format |
|---|---|---|---|
| WS-001 | Matching | Vocabulary recognition | Word-to-picture or word-to-definition pairs. |
| WS-002 | Circle | Grammar choice or vocabulary identification | Students circle the correct word/picture. |
| WS-003 | Fill in the Blank | Grammar form practice | Controlled sentence completion. |
| WS-004 | True / False | Reading comprehension | Short statements based on a text or picture. |
| WS-005 | Multiple Choice | Vocabulary, grammar, reading check | A/B/C choices. |
| WS-006 | Sentence Builder | Grammar production | Word bank plus sentence frame. |
| WS-007 | Picture Description | Speaking/writing bridge | Students describe a picture using target words. |
| WS-008 | Comic Writing | Creative controlled output | Speech bubbles and short lines. |
| WS-009 | Role Play | Speaking practice | Partner prompts with target language. |
| WS-010 | Find Someone Who | Communicative practice | Classroom survey grid. |
| WS-011 | Bingo | Vocabulary recognition and listening | Bingo grid with target unit pictures/words. |
| WS-012 | Mini Book / Reader Companion | Reading extension | Story-page aligned vocabulary and comprehension tasks. |
| WS-013 | Song Worksheet | Chant/song reinforcement | Lyrics gap fill, match, or sequence. |
| WS-014 | Dictionary / Word Bank | Unit reference | Picture dictionary or categorized word list. |
| WS-015 | Spiral Grammar | Review across units | Mixed grammar review with scope guard. |
| WS-016 | Word Scramble | Spelling and vocabulary recall | Scrambled letters + picture hint; students write the word. Use only current unit vocabulary; 4-6 items for Level 1-2. Add a bottom **Word Box** (STW style). |
| WS-017 | Scrambled Sentences | Grammar / sentence-frame production | Words of a sentence given out of order; student rewrites it correctly on handwriting lines. Use unit grammar frames only (e.g. `It's a ___.`, `Is it a ___?`). |
| WS-018 | Word Hunt | Vocabulary recognition (Level 1-2) | Each row: target word + a short letter string containing it once; student circles the word. Simpler than the WS-011 grid search. |
| WS-019 | ABC Order | Alphabetical-order strategy / spelling | Word Box at top; student writes the unit words in alphabetical order on numbered handwriting lines. Matches EOW1 U1 vocab strategy. |
| WS-020 | Write It Twice | Handwriting / spelling | Each word printed once + two primary-ruled (two-line) slots to copy it. Cleaner than faint-trace; good for Level 1 handwriting. |
| WS-021 | Color/Letter Recognition | Letter or category recognition (Pre-K/K) | A field of shapes (e.g. apples) each holding a letter/picture; student colours only the ones that match the target. Adapt for EOW as "colour only the classroom objects" etc. |
| WS-022 | Sentence Completion | Vocabulary in context | Word Box at top; numbered sentences each with a blank handwriting line; student fills each blank with a word from the bank. A sentence-level form of WS-003. |
| WS-023 | Reading Comprehension | Reading + comprehension | A short levelled passage (with picture), then questions: short-answer (handwriting lines) and/or multiple choice (a/b/c). **Requires the actual Reading Base story text** — if not yet extracted from Canva, mark `DATA NEEDED`; do not invent the story. |

See `07_Style_Sources/STW_reference.md` for the Super Teacher Worksheets layout conventions (frame, title tab, handwriting lines, Word Box).

## Pattern Details

### WS-001 Matching

```yaml
activity_id: WS-001
type: matching
difficulty: CL1-CL3
target: vocabulary
good_for:
  - classroom objects
  - family members
  - toys
  - food
constraints:
  - use only current unit vocabulary
  - keep item count between 6 and 10 for Level 1
```

### WS-003 Fill in the Blank

```yaml
activity_id: WS-003
type: fill_in_the_blank
difficulty: CL2-CL4
target: grammar
good_for:
  - am/is/are
  - he/she/they
  - a/an
  - can/can't
constraints:
  - one grammar point per activity
  - include a word bank for Level 1 unless the task is review
```

### WS-006 Sentence Builder

```yaml
activity_id: WS-006
type: sentence_builder
difficulty: CL3-CL5
target: grammar_output
good_for:
  - present progressive
  - there is/there are
  - like/don't like
constraints:
  - sentence frames must match the unit grammar
  - avoid open-ended vocabulary outside the unit
```

## Generator Rule

Every generated worksheet should list the selected pattern IDs at the top of the internal planning output.

## PAS Dropbox Style Notes

Dropbox Level 1 samples suggest the local PAS worksheet style often uses:

- Unit-numbered worksheet packets, e.g. `EOW1 U3-02 how many.pdf`.
- A 4-6 worksheet sequence inside a unit, often moving from vocabulary to grammar to song/review.
- Direct grammar labels in filenames, e.g. `in on under`, `this these`, `Do you`, `Does she`, `does doesnt`.
- Visual-first activities using small pictures, borders, and write-on lines.
- Separate resources for bingo, songs, dictionary, and spiral grammar.

Use official EOW pages for content boundaries, then use Dropbox style sources for layout and activity pacing.

