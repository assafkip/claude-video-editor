# Style Intake — How to Interview Without Imposing a Brand

Used by `/make-a-video` Gate 3. The goal: extract the user's visual identity (or fall back cleanly when they don't have one) without ever picking a brand *for* them.

## The decision tree

```
Does the user have a style guide, brand doc, or explicit palette?
├── Yes → Extract values → Use exactly what they supplied
├── Partial (some answers, not all) → Fill gaps with MOTION_PHILOSOPHY defaults, flag the gaps in BRIEF.md
└── No → Offer MOTION_PHILOSOPHY defaults AND ask for reference videos as a fallback
```

## MOTION_PHILOSOPHY defaults (the fallback, only when user declines to supply a style)

### Palette

| Role | Value |
|---|---|
| Background | `#000` (pure black) or `#0a0a0a` (near-black) |
| Chrome text gradient | `linear-gradient(180deg, #ffffff 0%, #999999 60%, #cccccc 100%)` with `-webkit-background-clip: text; color: transparent;` |
| Grid lines | `rgba(255, 255, 255, 0.05)` |
| Vignette | `radial-gradient(ellipse at center, transparent 30%, black 100%)` |
| Accent | ONE hex picked for symbolic meaning — ask the user "what's the ONE emotion of this video?" and map it |

Keep accent discipline tight. MOTION_PHILOSOPHY §0 Law 7: ≤5 symbolic colors across the whole video, each with a named meaning.

### Fonts

- **Headlines / kinetic type:** Inter (Google Fonts), weight 700
- **Mono (code, numbers, terminal):** JetBrains Mono, weight 500
- Load via `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=JetBrains+Mono:wght@500&display=swap">`

Variations allowed: Space Grotesk or Geist for a tech feel, Instrument Serif for editorial, Bebas Neue for impact. **One display family plus one mono.** Two sans-serifs in the same piece almost always looks wrong.

### Textures (always on, even with custom palette)

- Perspective grid floor (low-opacity lines)
- Vignette layer on top
- Film grain: `npx hyperframes add grain-overlay` installed as a component
- Crosshair `+` markers at grid intersections (optional but recommended)

---

## When the user supplies hex codes

1. **Ask for at least three roles:**
   - Background
   - Primary text / main accent
   - Secondary accent (the "emotion" color)
   - (Optional: surface · border · warn)

2. **Enforce the ≤5 symbolic colors rule.** If they give you 8 colors, ask which three carry narrative work and which five are decorative — drop the decorative.

3. **Assign meaning to each color.** One sentence per color, e.g. "cyan = action, orange = warning, white = brand voice." Save the mapping in the project's `style-profile.md`.

4. **Check contrast.** If accent hex on background hex is below 4.5:1 for text-sized elements, flag it to the user. Text on a dark background often needs a `text-shadow` halo to read well — MOTION_PHILOSOPHY §2.2 covers the recipe.

## When the user supplies fonts

1. Resolve Google Fonts names → `<link>` tags. If a font is custom, capture the file path and plan a `@font-face` declaration.
2. Confirm weights: default to Regular (400) + Bold (700) + one display weight if specified.
3. Pair rule: one display / headline family + one mono. Avoid stacking two sans-serifs.

## When the user supplies a logo

1. Ask for: file path · clearspace preference · any known glow/effect spec
2. In `style-profile.md` record: path · dimensions · CSS filter recipe (e.g. `drop-shadow(0 0 40px rgba(accent, 0.6))` if they want a glow)
3. Never recolor or stretch the logo in compositions.

## When the user supplies reference videos

1. Watch / read the references. If URLs, fetch them.
2. Extract:
   - Dominant palette (2–4 hex codes)
   - Type feel (serif · sans · mono · display)
   - Pacing (kinetic · balanced · relaxed)
   - Primary motion vocabulary (whip-pans · morphs · fades · glitches · 3D reveals)
3. Propose a derived palette + font pair + pacing. **Confirm with the user** before building.

---

## `<project-folder>/assets/style-profile.md` — what it contains

```markdown
# Style Profile — <project-slug>

## Palette
- bg: #...              (role: background)
- text: #...            (role: primary text)
- accent: #...          (role: <named meaning>)
- warn: #...            (optional, role: ...)
- surface: #...         (optional)

## Fonts
- Display: <Family Name> (weight(s), loaded from Google Fonts or file path)
- Mono: <Family Name> (weight, loaded from ...)

## Logo
- Path: assets/<logo-file>
- Clearspace: <e.g. half a logo-height on all sides>
- CSS filter (if any): filter: drop-shadow(0 0 40px rgba(..., 0.6));

## Source of profile
- [ ] Provided by user (style guide / brand doc)
- [ ] Derived from reference videos (confirmed by user)
- [ ] MOTION_PHILOSOPHY defaults (user declined to supply)

## Meanings (≤5 colors)
- <color> = <meaning>
- ...
```

Every composition in Gate 6 pulls from this file. It's the project's single source of truth.

---

## The discipline that applies regardless of palette

Even when the user chooses a fully custom palette, keep these MOTION_PHILOSOPHY principles. They're aesthetic-agnostic:

- 1–2 second scenes in the body of the video
- One idea per beat
- ≤5 symbolic colors, each with a named meaning
- Grid / vignette / grain texture on every scene
- Motion-blur transitions (whip-pans, morphs) — never hard cuts
- Hold the outro 4–6 seconds
- At least one visual callback (element that returns later)

Brand changes. Discipline doesn't.
