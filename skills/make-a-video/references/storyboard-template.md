# Storyboard Template — Beat-by-Beat

Used by `/make-a-video` Gate 5. Generates `<project-folder>/STORYBOARD.md` — the build blueprint.

## Header

```markdown
# STORYBOARD — <project-slug>

**Total duration:** <duration>s · <fps>fps · <width>×<height>
**Style profile:** see `assets/style-profile.md`
**Script / brief:** see `BRIEF.md`

## Act structure

- **Act 1 (0 → ≈20%):** hook — grab attention in the first 1–2 seconds
- **Act 2 (≈20% → ≈75%):** body — one idea per beat, 1–2 second scenes
- **Act 3 (≈75% → end):** payoff + outro with 4–6 second hold

## Timing table

| # | Start | Dur | Scene file | Concept |
|---|-------|-----|------------|---------|
| 0 | 0.0 | <total> | `ambient-bg.html` | Persistent background |
| 1 | 0.0 | 1.5 | `01-opener.html` | Hook |
| 2 | 1.5 | 1.2 | `02-...` | ... |
| N | ... | 4.5 | `N-cta-outro.html` | CTA hold |
```

---

## Per-beat format (one block per beat)

```markdown
## Beat N — <TITLE> (<start>s–<end>s, <duration>s) — <one-sentence concept>

**Visual elements:**
- <element 1> — position, size, animation, timing
- <element 2> — ...

**Motion language:** <1–2 sentences: what kind of motion carries this beat?>

**Eases used:**
- Entry: `<ease>` (e.g. `power3.out`)
- Hold: `<ease>` (or `none` for linear)
- Exit: `<ease>`

**Exit transition:** <how this beat hands off — whip streak · morph · blur crossfade · color recolor · hard cut aligned to streak peak>

**Audio:** <VO line if any · SFX · music layer notes>
```

---

## Worked example — 15-second product promo

```markdown
# STORYBOARD — acme-promo-15s

**Total duration:** 15s · 30fps · 1920×1080
**Style profile:** see `assets/style-profile.md`

## Act structure

- Act 1 (0–3s): hook — "Why is this still so hard?"
- Act 2 (3–11s): body — three benefits in kinetic type + product shot
- Act 3 (11–15s): CTA — logo + URL, 4s hold

## Timing table

| # | Start | Dur | Scene file | Concept |
|---|-------|-----|------------|---------|
| 0 | 0.0 | 15.0 | `ambient-bg.html` | Perspective-grid background |
| 1 | 0.0 | 1.5 | `01-hook.html` | "Why is this still so hard?" kinetic type |
| 2 | 1.4 | 0.4 | `02-whip.html` | Light-streak whip transition |
| 3 | 1.5 | 2.0 | `03-benefit-fast.html` | "Fast" + comet streak |
| 4 | 3.5 | 2.0 | `04-benefit-simple.html` | "Simple" + object morph |
| 5 | 5.5 | 2.0 | `05-benefit-reliable.html` | "Reliable" + flowchart |
| 6 | 7.5 | 2.5 | `06-product-shot.html` | App showcase block |
| 7 | 10.0 | 1.0 | `07-logo-crystallize.html` | Logo crystallizes |
| 8 | 11.0 | 4.0 | `08-cta-outro.html` | Wordmark + URL hold |

## Beat 1 — Hook (0.0–1.5s, 1.5s) — "Why is this still so hard?"

**Visual elements:**
- Perspective grid floor (ambient, already on)
- Five words, chrome gradient, Inter 96px, centered
- Hero word "hard?" scales 1× → 8× camera-dolly-through at 1.0–1.5s

**Motion language:** kinetic typography, per-word stagger, final word dolly-through

**Eases used:**
- Entry per word: `power3.out`, duration 0.5s, stagger 0.08s
- Each word fade-out: `power2.in`, duration 0.4s, overlaps next by 0.15s
- "Hard?" dolly: `power2.in`, duration 1.0s, scale 1 → 8, opacity 1 → 0

**Exit transition:** light-streak whip (Beat 2) fires at t=1.4s, crosses the grid, hard cut on the streak peak at t=1.6s

**Audio:** VO "Why is this still so hard?" (TTS `am_adam`) · ambient pad `data-volume="0.15"`

## Beat 2 — Whip (1.4–1.8s, 0.4s) — Motion-blur transition

**Visual elements:**
- Single horizontal streak: `linear-gradient(90deg, transparent, #fff, transparent)`, 40% width, 8px tall, blur 6px
- Hides the cut between Beat 1 and Beat 3

**Motion language:** speed line, no content

**Eases used:**
- `xPercent: -100` → `xPercent: 250`, duration 0.4s, `power3.in`

**Exit transition:** N/A (is itself the transition)

**Audio:** whoosh SFX at 0.2 volume

## Beat 3 — Fast (1.5–3.5s, 2.0s) — "Fast" benefit

... (and so on)
```

---

## Rules the storyboard enforces

1. **Every beat ≤ 2 seconds** unless it's the hero moment or outro.
2. **Every transition has a name and a duration** — no "and then we cut to the next scene" hand-waving.
3. **Every beat names its eases** (at least entry + exit). Don't let every beat default to `power2.out`.
4. **The outro holds 4–6 seconds.** No exceptions.
5. **At least one visual callback** appears in Act 2 or Act 3 — an element that echoes something set up earlier (MOTION_PHILOSOPHY §0 Law 6).
6. **Rule of threes** where possible — 3 benefits · 3 product surfaces · 3 icons. The reference Infinite spot uses it everywhere.
7. **Ambient background composition** always present on `data-track-index="0"` for the full duration.

---

## After writing

Show the storyboard + timing table to the user. They will often:
- Cut a beat ("I don't need 'Reliable,' combine it with 'Simple'")
- Shift an emphasis ("the hook should be longer so it lands")
- Ask for different transition feel ("this should feel more cinematic, less energetic")

Iterate. Don't build until they approve.
