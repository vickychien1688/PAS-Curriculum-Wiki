---
name: worksheet-generator
description: Generate PAS Summer Camp student handbooks (cover, learning passport, daily worksheets). Use when creating worksheets, covers, or learning passports for any Summer Camp project. Covers prompt crafting, visual style consistency, page structure, and quality checks.
---

# Worksheet Generator

Generate high-quality, visually consistent student handbooks for PAS Summer Camp projects. A complete handbook includes a Cover, a Learning Passport, and 4 worksheet pages per day.

## Workflow

1. Study the lesson plan and extract vocabulary, grammar, phonics, and story content
2. Define visual style and recurring characters for the project
3. Generate the Cover page
4. Generate the Learning Passport page
5. Generate daily worksheets (4 pages/day)
6. Review all outputs against the quality checklist

## Visual Style Rules

Every project has a unique visual theme (e.g., "Warm Watercolor Storybook", "Neon Forest"). These rules apply universally:

| Rule | Detail |
|------|--------|
| Character Consistency | Same recurring characters on ALL pages of a project |
| Thematic Border | Project-specific border on every page (e.g., autumn leaves, neon vines) |
| Aspect Ratio | ALL images use `3:4` |
| Quality | ALWAYS use `quality: "high"` for text legibility |
| Reference Chaining | After the first successful page, use it as `references` for all subsequent pages |
| Text Case | Normal sentence case; NEVER all caps except for single-word titles |
| Font Size | Minimum 12pt equivalent; children must read easily |
| Style Diversity | Each project MUST have a different visual theme from previous projects |

## Page Structures

### Cover (`worksheets_cover.png`)

Required elements:
- Project title on a prominent sign (e.g., "My Handmade Toy")
- "2026 Summer English Camp" banner
- PAS Logo (yellow smiling hand) + "Our Reading Space 愉閱空間 語感英文"
- Student info on ONE line: `Name: _____________ Class: _____________`
- Day 1–4 decorative icons at the bottom

Prohibited: Do NOT include project numbers (e.g., "Project 2").

### Learning Passport (`worksheets_passport.png`)

Layout: A4 divided into 4 quadrants (2x2 grid), one per day.

Each quadrant contains:
- Day label on a colored ribbon
- Summary of Phonics rules, key words, and grammar for that day
- A "Stamp Here" collection area (dotted circle or box)

### Daily Worksheets (4 Pages per Day)

| Page | Title | Content |
|------|-------|---------|
| P1 | Our Story Chant | Story text + illustrations + "My Turn!" fill-in + Word Bank |
| P2 | Phonics Power (Rule A) | One phonics rule, 4 words + illustrations (2x2), Listen & Circle |
| P3 | Phonics Power (Rule B) | Second phonics rule, same structure as P2 |
| P4 | Explorer / Sentence Builder | Vocabulary matching, grammar fill-in, sentence writing |

### Critical Rules for Phonics Pages

- ONE phonics rule per page. Never mix multiple new rules on a single page.
- Exercise answers MUST be completely randomized. Never group same sounds together.
- Example (gl-/pl-/sl-): Q1: sl-(slip), Q2: gl-(glad), Q3: pl-(plan), Q4: sl-(slim), Q5: gl-(glow), Q6: pl-(plug).

## Prompt Crafting

For detailed prompt templates, see [references/prompt_templates.md](references/prompt_templates.md).

Key principles:
- Provide EXACT text to render (never let the AI invent text)
- Describe layout explicitly: sections, grid arrangements, banner colors
- Always include the visual theme description at the start of the prompt
- Always mention "clear, legible, large font text" and "no gibberish"
- Include character placement instructions (e.g., "bear in top-right corner")

## File Naming & GitHub Structure

```
02_Summer_Camp/
└── Project_N_[Name]/
    ├── worksheets_cover.png
    ├── worksheets_passport.png
    ├── Day_One/
    │   └── worksheets/
    │       ├── day1_page1_story.png
    │       ├── day1_page2_phonics.png
    │       ├── day1_page3_phonics.png
    │       └── day1_page4_sentences.png
    ├── Day_Two/
    │   └── worksheets/
    │       └── ...
    ├── Day_Three/
    │   └── worksheets/
    │       └── ...
    └── Day_Four/
        └── worksheets/
            └── ...
```

Commit message format: `Add [Project Name] worksheets (cover + passport + N days)`

## Quality Checklist

Before delivery, verify:
- [ ] All images use `3:4` aspect ratio
- [ ] Cover has Name/Class on ONE line, includes PAS Logo, no project number
- [ ] Passport has 4 quadrants with correct day summaries and stamp areas
- [ ] Each phonics page focuses on ONE rule only
- [ ] Phonics answers are randomly scrambled (no patterns)
- [ ] Visual style (borders, characters, colors) is identical across all pages
- [ ] All rendered text is legible and free of AI gibberish
- [ ] No unnecessary labels (e.g., "Label 3", "Project 2")
- [ ] Content matches PAS Curriculum Wiki (vocabulary, grammar, phonics)
- [ ] Files pushed to GitHub with correct naming convention
