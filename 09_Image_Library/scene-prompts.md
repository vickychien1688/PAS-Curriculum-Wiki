# Scene & Grammar Illustration Prompts

For questions that need a **scene**, not a single object — e.g. "How many birds are in
the tree?" or "Where is the cat?". These are tied to the question, so they can't always
be reused. To keep cost down: **pre-generate the common, predictable scenes once and
cache them** in `scenes/`. Only truly one-off scenes get generated per worksheet.

## Style

Same look as the icon set (`style-bible.md` §1–2): flat vector, thick black outline,
white background, no text or numbers in the image, both `color` and `bw`. The difference:
a scene may contain **more than one object** and a simple setting.

## Scene prompt template

```
Flat vector worksheet illustration: {scene description}.
Show exactly {count} clearly separate, countable {object}s.
Simple flat style with thick black outline matching a child worksheet icon set,
pure white background, {MODE_SPEC}, no text, no numbers, no labels.
Square composition.
```

- `{MODE_SPEC}` color → `flat cheerful limited color palette`
- `{MODE_SPEC}` bw → `pure black and white line art, white fill, no grey`

Keep **counts unambiguous**: objects clearly separated, not overlapping, easy to count.

## High-value scenes to pre-generate (cache once)

These recur across units and grammar points. Generate the whole batch once into `scenes/`.

### Counting (How many...?) — grammar: How many / numbers

For each target object, generate counts **1 through 6** (Level 1 range):

```
scenes/count-<object>-<n>/   e.g. scenes/count-bird-3/
```
Template fill: `{scene description}` = `{n} {object}s grouped together`, `{count}` = n.
Priority objects (from high-use units): bird, apple, book, pencil, star, flower, ball, fish, cookie, chair.

### Position (Where is...?) — grammar: Where + in / on

Generate the common in/on relationships:

```
scenes/pos-<object>-<in|on>-<place>/   e.g. scenes/pos-bird-on-tree/
```
Starter set for EOW1 U2:
- bird **on** tree · bird **in** bush
- flower **in** bush · flower **on** rock
- star **in** sky · cloud **in** sky
- butterfly **on** flower · sun **in** sky

### Comparison (Compare/contrast, adjectives) — grammar: big/small, tall/short

```
scenes/compare-<adj>/   e.g. scenes/compare-tall-short/
```
- tall tree + short tree · big ball + small ball · old person + young person · long hair + short hair

## One-off scenes

If a question needs a scene not in the cache, build it from the template, save it under
`scenes/<descriptive-id>/`, and add a line here so it's reused next time. The cache only
grows; you never regenerate an existing scene.

## Worksheet wiring

When a worksheet question references a scene, the layout step looks for the matching
`scenes/<id>/<id>-<mode>.png`. If missing, it is flagged `IMAGE NEEDED` (same spirit as
the wiki's `DATA NEEDED` rule) rather than invented.
