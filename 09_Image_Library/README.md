# 09 Image Library

Single source of truth for **worksheet artwork**. Every PAS worksheet pulls its pictures
from here instead of drawing them on the fly. This is the "image bible": generate once,
reuse forever.

## Why this exists

Code-drawn icons look rough and inconsistent. Generating a fresh image every time a
worksheet is made is slow and expensive. Instead we:

1. Define **one fixed style** (`style-bible.md`) so every picture looks like it belongs to the same set.
2. List **every vocabulary word that needs a picture** (`vocab-image-list.md`).
3. Generate **2–3 variants per word**, once, in both **black-and-white** and **color**.
4. Save them here with a strict naming convention.
5. Worksheets reference the files — no regeneration.

## Cost logic (why this is cheaper)

| Step | When it costs | How often you pay |
|---|---|---|
| Generate a word's images | Image generation (the expensive part) | **Once per word**, then never again |
| Build a worksheet | Layout only — pulls existing PNGs | Almost free in tokens |
| Scene/grammar illustration (e.g. "3 birds in a tree") | Image generation | Once per **unique scene**; common scenes are pre-generated and cached (see `scene-prompts.md`) |

Net effect: the heavy cost is paid up front, one time, and amortized across every future worksheet.

## Folder structure

```text
09_Image_Library/
  README.md            <- this file
  style-bible.md       <- the fixed style standard + prompt templates + naming rules
  vocab-image-list.md  <- master list of every word needing a picture (EOW1 complete)
  scene-prompts.md     <- templates for grammar/counting scene illustrations
  words/
    <word>/
      <word>-v1-color.png
      <word>-v1-bw.png
      <word>-v2-color.png
      <word>-v2-bw.png
      prompt.txt        <- exact prompt used (for reproducibility / regeneration)
  scenes/
    <scene-id>/
      <scene-id>-color.png
      <scene-id>-bw.png
      prompt.txt
```

Word-keyed (not unit-keyed) on purpose: a word generated once is reused across **any**
unit or level that uses it.

## Workflow

1. Open `vocab-image-list.md`, pick the words with status `TODO`.
2. For each, build the prompt from `style-bible.md` (template + the word's "subject + poses").
3. Generate in your image tool (GPT/DALL·E, Canva, etc.) — color first, then the b/w version.
4. Save into `words/<word>/` with the exact naming above; paste the prompt into `prompt.txt`.
5. Mark the word `DONE` in `vocab-image-list.md`.
6. When a worksheet is generated, the layout step pulls these files; output is produced in both b/w and color.

## Status

- EOW1 (Units 1–8): vocabulary fully listed here. Images: **not yet generated**.
- EOW2–4: vocabulary not yet extracted from teacher manuals; add once those unit pages exist.
