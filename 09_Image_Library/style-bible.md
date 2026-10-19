# Style Bible — PAS Worksheet Image Standard

The fixed rules every generated picture must follow. Do not change these per image;
consistency is the whole point. If a rule must change, change it **here** and regenerate.

## 1. Universal style (applies to every word icon)

- **Cute, hand-drawn children's storybook illustration** (kawaii). Warm and friendly, like a
  **watercolour / colored-pencil picture book — NOT flat vector, NOT a hard sticker icon.**
- Soft, rounded, chunky shapes. **Only animals and people get a face** (tiny dot eyes, small smile,
  soft rosy cheeks where natural). **Plants, food, the sun/moon, weather, and all objects have NO face** —
  do not anthropomorphise them; keep them simple, soft, and rounded.
- **One** subject, centered, no background scene. Background = clean white (a faint paper texture is fine).
- **Soft hand-drawn outline** (pencil / ink feel), gentle and slightly uneven — not a crisp vector line, not harsh thick black.
- Soft hand-drawn colouring: light watercolour / colored-pencil shading and a little texture. No flat vector fills, no harsh gradients, no 3D.
- Square 1:1 frame; subject fills ~80%, with even margin.
- **No text, letters, numbers, or labels** anywhere in the image.
- Front view or gentle 3/4 view at eye level. Keep perspective consistent.

## 2. Two color modes (generate BOTH for every image)

| Mode | Spec | Use |
|---|---|---|
| `color` | Soft **pastel** watercolour / colored-pencil palette (a few gentle colours, hand-drawn shading). | Screen, color printing, display copies. |
| `bw` | Hand-drawn pencil / ink line art, soft light-grey pencil shading allowed. | Everyday photocopying. |

The two modes must be the **same drawing** — only the colouring changes. Easiest path:
generate `color`, then produce `bw` as the pencil-line version of the same art.

## 3. Variants (2–3 per word)

Each word gets 2–3 variants so worksheets can vary without looking copy-pasted.
**Variants change pose/angle/example only — never the style.**

Examples:
- `bird`: v1 perched side view · v2 flying · v3 facing front.
- `cow`: v1 standing side view · v2 grazing head-down · v3 front view.
- `chair`: v1 3/4 view · v2 side view.

## 4. Naming convention (strict)

```
words/<word>/<word>-v<N>-<mode>.png
```
- `<word>` lowercase, spaces → hyphens (`teddy bear` → `teddy-bear`).
- `<N>` = variant number (1, 2, 3).
- `<mode>` = `color` or `bw`.
- Also save `words/<word>/prompt.txt` with the exact prompt(s) used.

Examples: `words/bird/bird-v1-color.png`, `words/bird/bird-v1-bw.png`, `words/teddy-bear/teddy-bear-v2-bw.png`.

## 5. Master prompt template

Fill the `{...}` slots from `vocab-image-list.md`. Keep everything else verbatim.

```
Cute hand-drawn children's storybook illustration of a single {word} ({variant_pose}),
soft warm watercolour / colored-pencil style (NOT flat vector, NOT a hard sticker icon),
rounded chunky shapes, simple friendly look
(tiny dot eyes and soft rosy cheeks ONLY if it is an animal or person; no face on plants, food, sun/moon, or objects),
soft hand-drawn outline, gentle hand-drawn shading and a little paper texture,
centered on a clean white background, {MODE_SPEC},
no harsh gradients, no 3D, no text or numbers,
square composition, subject fills about 80% of the frame.
Consistent picture-book icon set for ages 6 to 8.
```

- `{MODE_SPEC}` for color → `soft pastel watercolour palette of a few gentle colours`
- `{MODE_SPEC}` for bw → `hand-drawn pencil line art with soft light-grey pencil shading, white background`

## 6. Special categories (not plain objects)

| Category | Words (examples) | How to illustrate |
|---|---|---|
| People | mother, father, sister, grandfather… | Simple friendly figure, head-to-knee, neutral clothing. Vary age/hair to read the role. |
| Adjectives (pairs) | big/small, tall/short, old/young, long/short | Draw a **contrast pair** in one square (e.g. a tall tree next to a short tree). Use the same base object for both. |
| Actions (verbs) | run, jump, walk, cooking, eating, sleeping… | One figure clearly doing the action, side view, motion readable. |
| Colors | brown, pink | Not an icon — a labeled-free **color swatch** (rounded square of that flat color). For `bw`, skip; handle in layout. |
| Settings | sky, river, living room, kitchen… | Simple emblematic scene, still single-subject and flat. |

## 7. Quality gate before saving

- Reads correctly at small size (worksheets shrink icons to ~30–40 px).
- Matches the rest of the set (outline weight, margin, simplicity).
- No stray text, watermark, or background.
- Both `color` and `bw` saved, plus `prompt.txt`.
