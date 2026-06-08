# MOTION PHILOSOPHY — The Gold Standard

> Reference deconstruction of the **Infinite — Global Payments** 30s spot
> (`x-XTeSJ-DKx63uB4.mp4`, 1920×1080, 30fps, 900 frames). This is what every
> Hyperframes motion-graphics build should aspire to. Re-read before starting any
> new composition.

---

## 0 · The 11 Laws (memorize)

1. **One idea per beat. Cut fast.** Average scene length in the reference is **~1.5 seconds**. Each visual lands ONE word/concept and moves on. If a scene says two things, split it.
2. **Black is the canvas.** ~90% of every frame is black or near-black. Negative space is the design. Color earns its place by carrying a message.
3. **Light is the brand, not color.** Chrome gradients on type, soft halos, vignettes, light beams. The piece is *lit*, not *colored*. Light reads as premium.
4. **Camera never sleeps.** Even on "still" frames, the grid recedes, the coin rotates, particles drift, the vignette breathes. Static = death.
5. **Motion blur is a feature.** Every transition uses a streak/blur trail — to convey energy AND to mask the cut. Hard cuts feel cheap; whip-streaks feel expensive.
6. **Object metaphors carry meaning.** Red card = old/broken. Teal coin = new/working. The same coin returns 3 times across the piece. Visual continuity = brand.
7. **Palette is symbolic, not decorative.** Each color owns one concept. Don't drop a color in just because it looks nice — assign it a meaning.
8. **Type is a character.** Words SCALE 8×, MORPH, COMPRESS, GLOW. Typography drives ~60% of the storytelling. A text-only beat can be the strongest beat.
9. **Hold the hero shot.** Logo reveal = ~2s of stillness. Outro card = 5+ seconds. Speed earns space for stillness to land. Kinetic chaos → calm = catharsis.
10. **One unifying texture across everything.** The reference uses a faint perspective grid + crosshair (+) registration marks at intersections. Even when invisible, that grid is the spine of the whole piece.
11. **Timelines must fill their slots.** HyperFrames hides a sub-composition the moment `timeline.duration()` is shorter than `data-duration` → black frame flash. Every GSAP timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)` as a no-op duration anchor. Non-negotiable. (Recipe in 3.8; diagnostic in Section 4.)

---

## 1 · The Reference Timeline (30s)

| Time | Beat | What's on screen | Engine |
|------|------|------------------|--------|
| 0.0–0.5 | Empty stage | Black void, perspective grid floor recedes, 4 crosshair `+` markers at center, soft floor wash | Camera holds; grid hints at depth |
| 0.5–1.5 | "Global payments" | Chrome-gradient type appears center, fades subtly | Word reveal #1 |
| 1.5–2.0 | "are a" | Next word ghosts in while previous fades — overlapping reveals | Continuous read |
| 2.0–3.5 | **"a pain"** | Type GROWS to fill 8× — camera dollies through text, grid tilts sideways | Hero kinetic-type moment |
| 3.5–4.0 | **Whip transition** | Glowing white light-saber streak crosses the grid floor at speed | Hides the cut |
| 4.0–5.5 | Red card lands | 3D credit card materializes on grid with motion blur, slight orbit | Object metaphor: problem |
| 5.5–6.5 | **Morph** | Red card transforms into teal/cyan rounded square mid-flight, big light streak | Solution arrives |
| 6.5–7.5 | Coin rises | Teal cylinder coin, vertical light pillar behind, rotates to face camera | Reveals ∞ symbol |
| 7.5–8.5 | "Meet ∞" → logo | Coin shrinks/locks → "∞ Infinite" wordmark crystallizes | Brand reveal |
| 8.5–9.5 | Logo hold | Pure black, subtle chrome shimmer pass | Stillness lands |
| 9.5–10.5 | **"Fast"** | Magenta lightning comet rips left→right, "Fast" in chrome upper-right | Benefit #1 |
| 10.5–11.5 | Network appears | Flowchart of nodes (white outlines), purple energy pulses through edges | Build-up |
| 11.5–12.0 | "Global" | Word lights up, blue energy pulses fill the nodes | Benefit #2 |
| 12.0–13.0 | **Color flip → "Affordable"** | Same flowchart, palette flips to neon orange/yellow with dashed lines, "Affordable" with halo | Benefit #3 (no scene cut!) |
| 13.0–14.5 | "Sign Up In Seconds" | iPhone slides up from below, Account-linking app screen | Product surface #1 |
| 14.5–16.0 | "Send Funds Anywhere" | Different phone screen, transaction list | Product surface #2 |
| 16.0–17.5 | "Built For Businesses" | Laptop showing "Create Transfer" form | Product surface #3 |
| 17.5–19.0 | **Dash** | Iridescent chrome wheel/dial centered, "Dash — Move money globally" panel slides in left (blue gradient) | Product family #1 |
| 19.0–20.5 | **API** | Same wheel rotates, "API — Build your own experience" panel slides in right (purple gradient) | Product family #2 |
| 20.5–22.0 | **SDK** | Wheel rotates again, yellow segment lit, "SDK — Integrate in just a few lines" | Product family #3 |
| 22.0–23.5 | Coin returns | Teal coin spinning in cylinder again — callback | Visual rhyme |
| 23.5–25.0 | "Powered by Stablecoins" | Three coins floating in conical light beam, sparkle particles | Foundation reveal |
| 25.0–30.0 | **CTA hold** | App icon + "Infinite — Instant, global payments" + "GET STARTED — INFINITE.DEV" | 5s of stillness |

**Three-act structure:**
- **Act 1 (0–9.5s):** Problem → metaphor → brand reveal
- **Act 2 (9.5–22s):** Three benefits → three product surfaces → three product names
- **Act 3 (22–30s):** Foundation → CTA → silence

Notice the **rule of threes** everywhere: 3 benefits, 3 surfaces, 3 product names, 3 floating coins.

---

## 2 · The Visual Vocabulary (every technique in the piece)

### 2.1 Backgrounds (in priority order)

| # | Background | Where it lives | How to build in HF |
|---|-----------|----------------|---------------------|
| 1 | **Perspective grid floor** | Opening, brand reveal, outro | `<div>` with `transform: perspective(800px) rotateX(60deg)` + `repeating-linear-gradient(0deg, rgba(255,255,255,.06) 0 1px, transparent 1px 80px)` (×2 axes) + SVG `+` crosshairs as `background-image` at intersections. GSAP animates `background-position-y` for parallax. |
| 2 | **Vignette** | Always | Absolute overlay `<div>` with `background: radial-gradient(ellipse at center, transparent 30%, black 100%)`, `pointer-events: none`. Always on top of bg, below content. |
| 3 | **Pure black stage** | Brand reveal, between major beats | Just `body { background: #000 }`. Used as a "reset" between sections. |
| 4 | **Horizontal speed lines** | Comet/whip moments | `repeating-linear-gradient(0deg, rgba(255,255,255,.04) 0 1px, transparent 1px 60px)` with GSAP scrolling `background-position-x` for motion blur trail |
| 5 | **Iridescent gradient stage** | Wheel scenes (Dash/API/SDK) | Soft conic-gradient or pre-rendered video. Best as `<video muted loop>` for true chromatic shimmer. |
| 6 | **Conical light beam** | Three-coins finale | `<div>` with `background: conic-gradient(from 180deg at 50% 0%, transparent, rgba(0,255,200,.15) 50%, transparent)`, blurred |
| 7 | **Sparkle particles** | All grid scenes | 20–40 absolute-positioned `<div>` `+` shapes at random grid intersections, GSAP `stagger.from('random')` opacity tween, `repeat: -1, yoyo: true` |
| 8 | **Subtle film grain** | Everywhere (super faint) | `npx hyperframes add grain-overlay` |
| 9 | **Liquid-glass card** | Hero product card, player frames, UI panels | 4-stop diagonal gradient `rgba(255,255,255,.075/.025/.010/.055)` + `backdrop-filter: blur(14px) saturate(1.12)` + inner highlight `inset 0 1px 0 rgba(255,255,255,.22)` + thin 1px border. The inner highlight is the iOS-26 "liquid glass" tell. |
| 10 | **Film strip (pure CSS)** | Footage / compositing beats | Single `repeating-linear-gradient(90deg, transparent 0-40px, #0d0d0d 40-44px, transparent 44-60px, rgba(255,255,255,.06) 60-80px, transparent 80-100px)` gives sprockets + perforations in one declaration. Animate via `translateX`. |
| 11 | **Film grain (pure CSS, no PNG)** | Anywhere grain is wanted deterministically | Three radial-gradients at tile sizes 3/5/7px, each a 1px dot at a different position, alphas `.03/.02/.015`. Non-repeating look, fully deterministic, headless-safe. |

### 2.2 Type System

- **Single sans-serif throughout.** Geometric, generous tracking. (Inter, Suisse Int'l, or SF Pro all read correctly.)
- **All headline text uses chrome gradient:** `background: linear-gradient(180deg, #ffffff 0%, #999999 60%, #cccccc 100%); -webkit-background-clip: text; color: transparent;`
- **Halo glow on emphasis words:** `text-shadow: 0 0 20px rgba(255,255,255,0.6), 0 0 40px rgba(255,255,255,0.3)`
- **Word-by-word kinetic reveal** (NOT character-by-character — words land harder):
  ```html
  <span class="clip word" data-start="0.0">Global</span>
  <span class="clip word" data-start="0.4">payments</span>
  <span class="clip word" data-start="0.8">are</span>
  <span class="clip word" data-start="1.0">a</span>
  <span class="clip word" data-start="1.2">pain</span>
  ```
  GSAP: `tl.from('.word', { y: 30, opacity: 0, scale: 0.85, duration: 0.6, ease: 'power3.out', stagger: 0.35 })`
- **Type SCALES dramatically.** Section labels at 48px. Hero kinetic-type at 480px+ (literal screen-filling). Use `font-size: clamp()` and animate via `scale`.
- **No sentence-case for emphasis.** Section words are Title Case ("Sign Up In Seconds", "Built For Businesses").
- **Chrome-gradient sweep (exact recipe).** Use 8-stop gradients with DARK BOOKENDS so the sweep blends into the text's resting dark state — no edge tear:
  ```css
  background: linear-gradient(90deg,
    #14110a 0%, #14110a 15%,
    #5a3215 25%, #c84f1c 40%, #e2b53f 55%, #2a8a7c 70%,
    #14110a 85%, #14110a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-size: 300% 100%;
  background-position: 100% 0;  /* resting dark */
  ```
  Then tween `backgroundPosition` from `100% 0` → `0% 0` over `0.6s` `power2.out` with `stagger: 0.04` across words. Toggle the gradient class on at the exact capture/punch moment via `tl.add(cb)`.
- **Word-reveal carrier pattern.** First word carries the cut's momentum with a 360px slide; subsequent words decay geometrically. Reference roster of slide distances: `360 → 120 → 60 → 25 → 12px`. Carrier uses `expo.out 0.33s`; tail words `power2.out 0.20s`. Anchor to real Whisper word-onset timestamps, and on punchlines lead the VISUAL 0.2s ahead of the audio — it reads as inevitable.
- **Per-beat font discipline.** Every beat uses a DIFFERENT Google-Fonts family; the contrast itself sells "different universes." Reference roster from the HF launch video: Instrument Serif (editorial/hero) · Space Grotesk (tech) · Bebas Neue (impact) · Inter (UI) · EB Garamond italic (footage) · Cormorant Garamond italic (3D) · Azeret Mono (shader/data) · Geist (product) · JetBrains Mono / SF Mono (terminal). Load per-composition from the Google CDN; no custom font files needed.

### 2.3 Color Story (memorize the meanings)

| Color | Hex (approx) | Meaning | Where used |
|-------|------|---------|------------|
| **Black** | `#000` / `#0a0a0a` | Canvas / silence | Always |
| **Chrome white→gray** | gradient `#fff → #999` | Premium / brand voice | All headline type |
| **Red** | `#e10b1f` | Problem / old / broken | Credit card |
| **Teal/cyan** | `#33d4c8` / `#5ee2d9` | Solution / brand / core | Coin, infinity logo |
| **Magenta/purple** | `#a155ff` / `#7e42d8` | Speed / energy / API | Lightning comet, API panel |
| **Blue** | `#3b82f6` / `#5db4ff` | Connection / global | Network energy, "Global" word, Dash panel |
| **Neon orange/yellow** | `#ff9430` / `#ffd84a` | Value / affordability | Recolored flowchart |
| **Iridescent chrome** | conic spectrum | Sophistication / API depth | Wheel UI |

**Discipline:** when adding a new scene, ask "what's the one color carrying this beat?" If you can't name it, you haven't earned it.

### 2.4 Motion Vocabulary (the moves you'll re-use forever)

| Move | What it does | GSAP recipe |
|------|--------------|-------------|
| **Camera dolly through type** | Text grows from 1× to 8×+, opacity fades to 0 at peak — feels like passing through a 3D word | `tl.fromTo(text, { scale: 1, opacity: 1 }, { scale: 8, opacity: 0, duration: 1.5, ease: 'power2.in' })` |
| **Light-streak whip** | Glowing white→transparent gradient bar zips across the frame in 0.3–0.4s, blurred | `gsap.fromTo(streak, { xPercent: -150 }, { xPercent: 250, duration: 0.4, ease: 'power3.in' })` — fire AT the cut, not before |
| **Word ghost reveal** | Word #2 starts entering while word #1 is still leaving (~0.15s overlap) | `stagger: 0.35` with each word's exit at `+= 0.5`, so they overlap by 0.15s |
| **Object morph drift** | Object A scales down + drifts off-axis, Object B scales up from same vector — light streak hides the swap | Two `<div>`s, GSAP `to A: { x: 200, scale: 0.5, opacity: 0 }`, `from B: { x: -200, scale: 0.5, opacity: 0 }`, both 0.5s |
| **Coin spin reveal** | 3D rotateY from 90° (edge-on) to 0° (face), with subtle scale bounce | `tl.from(coin, { rotateY: 90, duration: 0.8, ease: 'back.out(1.4)' })` — needs `transform-style: preserve-3d` on parent |
| **Crystallize → wordmark** | Element shrinks/translates into wordmark position while wordmark fades up | Two timelines aligned: coin scales 1→0.3 + moves to logo position, wordmark fades 0→1, ending at same X/Y |
| **Energy pulse along path** | Glow travels along a network edge to "activate" a node | SVG path with `stroke-dasharray + stroke-dashoffset` animated 1→0; node lights up via `tl.to(node, { boxShadow: '0 0 30px var(--glow)' })` at path end |
| **Color recolor (no cut)** | Same composition, palette shifts via CSS variables | `tl.to(':root', { '--accent': '#ff9430', '--edge': '#ffd84a', duration: 0.6 })` — single tween recolors everything bound to the variables |
| **Slide-up phone reveal** | Device mockup enters from bottom edge with headline above | `tl.from(phone, { y: '100%', duration: 1, ease: 'power3.out' }, 0).from(headline, { y: 30, opacity: 0, duration: 0.6 }, 0.3)` |
| **Wheel + side-panel pattern** | Central UI rotates while text panels slide in from L/R | `tl.to(wheel, { rotation: 120, duration: 1.5 })` then `.from(panel, { x: -100, opacity: 0, duration: 0.6 }, '<0.3')` |
| **Floating cluster drift** | 3+ objects gently bob and drift continuously | `gsap.to(coins, { y: '-=15', duration: 2, repeat: -1, yoyo: true, ease: 'sine.inOut', stagger: { each: 0.4, from: 'random' } })` |
| **Shimmer sweep on hold** | A single chrome glint passes over the logo every few seconds | `npx hyperframes add shimmer-sweep` — set `data-interval` per design |
| **Vignette breath** | Vignette opacity wobbles 0.7→0.9 to keep "still" frames alive | `gsap.to(vignette, { opacity: 0.9, duration: 4, repeat: -1, yoyo: true, ease: 'sine.inOut' })` |
| **Cut-the-curve vertical whip** | Default adjacent-beat transition — exit rides up with blur, entry rises from below with matching blur. Same direction on both sides, velocity matched at the cut. | **Exit (outgoing beat):** `tl.to(wrap, { y: -150, filter: "blur(30px)", duration: 0.33, ease: "power2.in" })`<br>**Entry (incoming beat):** `gsap.set(wrap, { y: 150, filter: "blur(30px)" });` then `tl.to(wrap, { y: 0, filter: "blur(0px)", duration: 1.0, ease: "power2.out" }, 0)` |
| **Faux-cursor click event** | Full 7-tween sequence selling a UI interaction (click, ripple, target overshoot, settle) | 1. Cursor compress — `scale: 0.82, power4.in, 0.07s`<br>2. Target compress — `scale: 0.96, power4.in, 0.07s`<br>3. Ripple — `set(ripple, { scale: 0, opacity: 0.9 })` then `to({ scale: 2.5, opacity: 0, power2.out, 0.2s })`<br>4. Cursor release — `scale: 1, back.out(3), 0.3s`<br>5. Target overshoot — `scale: 1.02, elastic.out(1, 0.4), 0.2s`<br>6. Target settle — `scale: 1, power2.out, 0.2s`<br>**Critical:** SVG cursor's `transform-origin` MUST sit at the click-tip pixel (e.g. `transform-origin: 4.3px 2.6px`). |
| **Card splits (determinism proof)** | Two identical DOM cards stacked; split left/right with mirrored rotation — reads as "same input, identical output, every time" | `tl.to(cardFront, { x: 180, rotation: 3, duration: 0.7, ease: 'power2.out' }, 6.0)` + `tl.to(cardBack, { x: -180, rotation: -3, duration: 0.7, ease: 'power2.out' }, 6.0)` |

### 2.5 Transition Catalog

| Transition | When to use | HF block / approach |
|-----------|-------------|---------------------|
| **Light-streak whip** | Default cut between scenes, especially energy beats | Custom div + GSAP, OR `npx hyperframes add whip-pan` |
| **Cinematic zoom-through** | Going from text into 3D space | `npx hyperframes add cinematic-zoom` |
| **Cross-warp morph** | One object becoming another (red card → teal coin) | `npx hyperframes add cross-warp-morph` |
| **Color recolor (no cut)** | Showing two related ideas on same composition | CSS variables + GSAP tween — no shader needed |
| **Slide-up reveal** | Product mockup intros | Plain GSAP `from y: 100%` |
| **Crossfade with bright pulse** | Brand-reveal landing | Two layered scenes, brightness flash via white overlay tween 0→0.3→0 |
| **Flash-through-white** | Major act break | `npx hyperframes add flash-through-white` |
| **Swirl-vortex** | Product-family rotations (Dash/API/SDK) | `npx hyperframes add swirl-vortex` |
| **Hard cut on action** | When a whip-streak peaks — that's the moment to cut | Just align scene `data-start` with the streak's mid-frame |

### 2.6 Pacing Discipline

- **Default scene length:** 1.0–2.0 seconds. If a scene is longer, it had better be a hero moment or the outro.
- **Reveal cadence:** new visual element every 0.3–0.6s within a scene. No dead air > 1s mid-piece.
- **Word-reveal stagger:** 0.3–0.4s per word for narrative reads, 0.5–0.6s for dramatic single-word emphasis.
- **Whip transition duration:** 0.3–0.4s. Faster feels glitchy; slower loses energy.
- **Hold durations:**
  - Logo crystallization: **1.5–2s**
  - Final CTA card: **4–6s** (the longest single shot in the piece is the outro)
  - Section headlines: **1–1.5s** of read time after fully revealed
- **The breathing rule:** every ~7–8s of kinetic density, give the viewer a 1s "rest" beat (the brand reveal, the coin spin, the outro hold).

### 2.7 Audio Mix Defaults

Every scene with audio sets `data-volume` explicitly. Don't reach for a music track by default — a 0.15 warm pad is almost always the right answer.

| Layer | `data-volume` | Role |
|------|---------------|------|
| Voiceover | `1.0` | Primary, drives timing |
| Underscore (warm ambient pad) | `0.15` | Barely there — sets mood without competing |
| SFX (clicks, twinkles, whooshes) | `0.2` | Tails allowed to bleed into next beat |

**Wire as sibling `<audio>` elements** in the root composition, never mixed inside a `<video>`. Music-free is a valid choice; pad-only is premium; full "music" cue is last resort.

---

## 3 · Building This in HyperFrames — Concrete Recipes

### 3.1 Composition shell

Every scene is a sub-composition. Reference structure:

```
my-promo/
├── index.html                 ← root, wires everything together
├── compositions/
│   ├── 01-intro-type.html     ← "Global payments are a pain"
│   ├── 02-card-to-coin.html   ← red card → teal coin morph
│   ├── 03-brand-reveal.html   ← "Infinite" wordmark
│   ├── 04-fast-network.html   ← Fast / Global / Affordable
│   ├── 05-product-surfaces.html
│   ├── 06-dash-api-sdk.html   ← wheel rotation
│   ├── 07-stablecoins.html
│   └── 08-cta-outro.html
└── assets/
    ├── coin-rotate.mp4         ← pre-rendered 3D coin (the iridescent shimmer)
    ├── wheel-rotate.mp4        ← pre-rendered chrome wheel
    ├── card-3d.png             ← red card render with alpha
    ├── phone-mockup-1.png
    ├── laptop-mockup.png
    └── ambient-music.mp3
```

`index.html` chains them via `<template>` + `data-composition-src`.

### 3.2 The grid background (re-use everywhere)

```html
<div class="stage" data-composition-id="...">
  <!-- Layer 1: perspective grid floor -->
  <div class="grid-floor clip" data-start="0" data-duration="30" data-track-index="0"></div>

  <!-- Layer 2: crosshair markers -->
  <svg class="crosshairs clip" data-start="0" data-duration="30" data-track-index="1">
    <!-- 16 + marks at grid intersections -->
  </svg>

  <!-- Layer 3: vignette (always on top) -->
  <div class="vignette clip" data-start="0" data-duration="30" data-track-index="9"></div>

  <!-- Layer 4: grain overlay -->
  <div class="grain clip" data-start="0" data-duration="30" data-track-index="10"></div>

  <!-- Content layers go in tracks 2-8 -->
</div>

<style>
.grid-floor {
  position: absolute; inset: 0;
  transform: perspective(900px) rotateX(60deg) translateY(20%);
  background:
    repeating-linear-gradient(0deg,  rgba(255,255,255,.05) 0 1px, transparent 1px 80px),
    repeating-linear-gradient(90deg, rgba(255,255,255,.05) 0 1px, transparent 1px 80px);
  background-color: #000;
}
.vignette {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse at center, transparent 30%, #000 95%);
}
.grain { /* installed via `hyperframes add grain-overlay` */ }
</style>
```

### 3.3 Kinetic-type opener

```html
<div class="kinetic-type">
  <span class="word w1" data-start="0.0">Global</span>
  <span class="word w2" data-start="0.4">payments</span>
  <span class="word w3" data-start="1.0">are</span>
  <span class="word w4" data-start="1.2">a</span>
  <span class="word w5" data-start="1.4">pain</span>
</div>

<style>
.word {
  font-family: 'Inter', sans-serif;
  font-weight: 700;
  font-size: 96px;
  background: linear-gradient(180deg, #fff 0%, #999 100%);
  -webkit-background-clip: text;
  color: transparent;
}
.w5 { font-size: 480px; } /* hero scale */
</style>

<script>
const tl = gsap.timeline({ paused: true });
tl.from('.w1', { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0)
  .to('.w1',   { opacity: 0, duration: 0.4 }, 0.5)
  .from('.w2', { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0.4)
  // ... etc
  .fromTo('.w5',
    { scale: 1, opacity: 1 },
    { scale: 8, opacity: 0, duration: 1.0, ease: 'power2.in' },
    1.8
  );
window.__timelines['kinetic-opener'] = tl;
</script>
```

### 3.4 Whip-streak transition between scenes

```html
<div class="whip-streak clip"
     data-start="3.6" data-duration="0.4" data-track-index="8"></div>

<style>
.whip-streak {
  position: absolute; top: 50%; left: 0;
  width: 40%; height: 8px;
  background: linear-gradient(90deg, transparent, #fff, transparent);
  filter: blur(6px);
  transform: translateY(-50%);
}
</style>

<script>
gsap.fromTo('.whip-streak',
  { xPercent: -100, scaleX: 0.5 },
  { xPercent: 250, scaleX: 1.5, duration: 0.4, ease: 'power3.in' }
);
</script>
```

The next scene's `data-start` should land at the streak's peak (~halfway through the streak duration) so the cut is hidden by the brightness.

### 3.5 The Color Recolor Trick (no cut!)

```html
<div class="flowchart" style="--edge: #5db4ff; --node-glow: rgba(91,180,255,.6);">
  <!-- nodes use var(--edge) for borders, var(--node-glow) for box-shadow -->
</div>

<script>
// At t=2.5s, recolor the entire flowchart to neon orange
tl.to('.flowchart', {
  '--edge': '#ffd84a',
  '--node-glow': 'rgba(255,148,48,0.7)',
  duration: 0.6,
  ease: 'power2.inOut'
}, 2.5);
</script>
```

This is one of the highest-value moves in the entire piece. Same DOM, same composition, but the meaning shifts (Global → Affordable). Cheap to build, expensive to look at.

### 3.6 3D objects — pre-render or CSS?

| Effect | Best approach |
|--------|---------------|
| Iridescent chrome wheel | **Pre-render** as MP4 with alpha (or seamless loop). Real-time WebGL is overkill. |
| Spinning coin | **CSS 3D** (`rotateY`) is fine if the texture is flat. Pre-render if you want true reflections. |
| Card with motion blur | **PNG + GSAP transforms**. Add `filter: blur()` keyframe at peak motion. |
| Light beam / sparkles | **CSS gradients + GSAP**. Don't overthink. |

Rule: anything with **iridescent reflections, chromatic shifts, or true 3D refraction** → pre-render. Anything **planar with motion** → CSS + GSAP.

### 3.7 HF Registry Items That Map Directly

```bash
# Install once at the project root, then wire into compositions
npx hyperframes add grain-overlay              # film grain (always on)
npx hyperframes add shimmer-sweep              # logo glints
npx hyperframes add whip-pan                   # scene transitions
npx hyperframes add cinematic-zoom             # text dolly-through
npx hyperframes add cross-warp-morph           # object morphs
npx hyperframes add chromatic-radial-split     # color-flip moments
npx hyperframes add flash-through-white        # act breaks
npx hyperframes add swirl-vortex               # wheel rotations
npx hyperframes add light-leak                 # speed/energy beats
npx hyperframes add app-showcase               # phone/laptop reveals
npx hyperframes add flowchart                  # node networks
npx hyperframes add logo-outro                 # final CTA card
```

Don't write what you can install. The catalog has 38 blocks specifically for this aesthetic.

### 3.8 The timeline-padding rule (framework-critical)

Every sub-composition ends its timeline with a no-op duration anchor:

```js
const tl = gsap.timeline({ paused: true });
// … all your tweens …
tl.to({}, { duration: SLOT_DURATION }, 0);  // anchor: forces timeline.duration() >= SLOT_DURATION
window.__timelines['my-comp'] = tl;
```

Why: HF's `init.ts` sets `visibility: hidden` on the composition the moment `timeline.duration()` falls short of `data-duration` — producing a black frame flash at the beat tail. The anchor tween has zero animation cost but keeps the composition alive for its full slot. Diagnose missing/short timelines with the console snippet in Section 4.

### 3.9 Velocity-matched quadratic easing at beat seams

When an entry tween hands off to a linear hold (or to another tween), derive a custom ease so end-velocity equals the next tween's start-velocity. The eye reads any velocity discontinuity as a stall.

```js
// Scenario: entry goes position 0 → 1 over 0.9s, then holds linearly at velocity −0.123/s for 0.65s.
// Match at the seam: p'(1) = 0.194 (in normalized units).
// Quadratic p(t) = a·t² + b·t with p(0)=0, p(1)=1, p'(1)=0.194 → a = −0.806, b = 1.806.
const entryEase = (t) => -0.806 * t * t + 1.806 * t;

tl.to(card, { z: -50, duration: 0.9, ease: entryEase }, 0);
tl.to(card, { z: -80, duration: 0.65, ease: "none" }, 0.9);
```

**General form** for any entry-to-linear hand-off: given desired end-velocity `v` in normalized units, `p(t) = (1 − v)·t² + v·t − (… just solve for a, b with the three constraints)`. Derive it once per beat pair.

### 3.10 GSAP proxy pattern — Canvas 2D / WebGL inside a timeline

Drive arbitrary procedural rendering (ASCII effects, shaders, particle sims) from a single tween that advances a proxy time value:

```js
const proxy = { time: 0 };
tl.to(proxy, {
  time: DURATION,
  duration: DURATION,
  ease: "none",
  onUpdate: () => renderAtTime(proxy.time)
}, 0);
```

Your `renderAtTime(t)` function does all the work — Canvas 2D dithering, BFS crawls, FBM noise, whatever. Two rules:

1. **Canvas 2D is headless-safe; live WebGL can stall the render.** For shader scenes, ship a Canvas 2D fallback keyed off `renderOptions.headless`.
2. **No `Math.random()` / `Date.now()` inside.** Use seeded PRNGs or harmonic-sin hashes — renders must be deterministic frame-to-frame.

### 3.11 Tall-canvas camera pan

Build the canvas much taller than the viewport; tween `y` through stops to pan:

```css
.eng-viewport { width: 1920px; height: 1080px; overflow: hidden; }
.eng-canvas   { width: 1920px; height: 6000px; position: absolute; top: 0; left: 0; }
```

```js
tl.to(canvas, { y: 0 }, 0);
tl.to(canvas, { y: -1460, duration: 1.2, ease: "power2.inOut" }, 1.8);
tl.to(canvas, { y: -4310, duration: 2.3, ease: "power2.inOut" }, 3.3);
```

One continuous pan for related ideas; discrete pans with small dwells for topic changes. `power2.inOut` is the default; use `none` for constant-velocity "documentary" pans.

### 3.12 `<video>` poster + lastframe bracketing

`<video>` tags flicker on startup and black-frame after their source ends. Bracket every video with static JPG stills at the hand-offs:

```html
<img id="beat-poster"    src="assets/beat4-poster.jpg">
<video id="beat-video"   src="assets/beat4-clip.mp4"
       data-start="7.1" data-duration="8.94" data-track-index="5" muted></video>
<img id="beat-lastframe" src="assets/beat4-lastframe.jpg">
```

```js
// Poster covers beat-start → video-start; hand off at the video's data-start:
tl.set("#beat-poster",    { display: "none" }, 7.1);
// Lastframe covers video-end → beat-end:
tl.set("#beat-lastframe", { opacity: 1 }, 16.04);
```

**Generate posters via ffmpeg:**
```bash
ffmpeg -y -ss 0    -i clip.mp4 -frames:v 1 -q:v 2 poster.jpg
ffmpeg -y -sseof -0.04 -i clip.mp4 -frames:v 1 -q:v 2 lastframe.jpg
```

### 3.13 Captions as body-level siblings

Keep captions OUT of sub-composition timelines. Place them in `index.html` outside the master composition `<div>`, one caption per element, each with a unique `data-track-index ≥ 20`:

```html
<div class="cap clip" data-start="7.29"  data-duration="1.86" data-track-index="30">HyperFrames by HeyGen.</div>
<div class="cap clip" data-start="9.10"  data-duration="3.44" data-track-index="31">Agents can now write HTML and render MP4s.</div>
<div class="cap clip" data-start="12.80" data-duration="2.50" data-track-index="32">Deterministic. Reproducible. Cloneable.</div>

<style>
.cap {
  position: absolute; bottom: 72px; left: 50%; transform: translateX(-50%);
  padding: 12px 22px; border-radius: 14px;
  background: rgba(10, 8, 5, 0.55);
  backdrop-filter: blur(8px);
  font: 500 28px/1.3 Inter, sans-serif;
  color: #fff;
}
</style>
```

Central control, zero coupling to scene timelines.

### 3.14 CSS 3D torus (no Three.js needed)

Two rings of positioned segments using `transform-style: preserve-3d` give a true 3D torus-knot with no WebGL cost:

```js
// Outer ring — 32 segments
for (let i = 0; i < 32; i++) {
  const angle = (i / 32) * Math.PI * 2;
  const rotY = -(angle * 180 / Math.PI) + 90;
  const seg = document.createElement('div');
  seg.className = 'torus-seg';
  seg.style.transform =
    `rotateY(${rotY.toFixed(1)}deg) translateZ(175px) rotateY(90deg)`;
  outerRing.appendChild(seg);
}
// Inner ring — 16 segments offset by half-step, translateZ(125px)
```

```css
.torus-stage { perspective: 900px; transform-style: preserve-3d; }
.torus-form  { transform-style: preserve-3d; backface-visibility: visible; }
.torus-seg   { position: absolute; transform-style: preserve-3d; }
```

Then animate the parent `.torus-form` `rotationY` via GSAP — deterministic, headless-safe, no WebGL stall risk.

### 3.15 Tween-comment convention

Every entry/exit tween's comment explicitly names the matching tween in the adjacent beat. Discoverable seamlessness months later:

```js
// ENTRY — blur de-ramps from 22px to match the outgoing "circle" beat's 22px exit.
// Leftward motion is carried by "Anything" sliding in from x: 360.
gsap.set(wrap, { filter: "blur(22px)" });
tl.to(wrap, { filter: "blur(0px)", duration: 0.33, ease: "power2.out" }, 0);

// EXIT (at local 1.89) — matches the incoming "engine" beat's 150px y + 30px blur entry.
tl.to(wrap, { y: -150, filter: "blur(30px)", duration: 0.33, ease: "power2.in" }, 1.89);
```

**Rule:** if you can't name the matching tween in a comment, you haven't designed the seam.

---

## 4 · Pre-flight Checklist (before claiming any motion piece is "done")

- [ ] **Average scene length ≤ 2s** in mid-section (intro/outro can hold longer)
- [ ] **No dead air > 1s** anywhere except the deliberate hold moments
- [ ] **Every transition uses motion** (whip, morph, slide, recolor — no hard fades)
- [ ] **Color palette ≤ 5 active hues** total in the whole piece, each with a meaning
- [ ] **Every text block uses chrome gradient + halo** — no flat white
- [ ] **Background grid + crosshairs present in ≥ 60% of scenes** (the unifying texture)
- [ ] **Vignette layer on top of every scene** (don't ship a flat-lit composition)
- [ ] **Grain overlay on every scene** (subtle, but there)
- [ ] **One callback minimum** — a visual element that returns later (like the coin reappearing)
- [ ] **Outro holds for 4+ seconds** (silence after the kinetic act)
- [ ] **Visual verification done** — extracted frames, opened them, confirmed: no cropped faces, no text overflow, no scene landing on the wrong word, no broken transitions
- [ ] **Every sub-composition timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)`** — kills black-frame flashes at beat tails (Law #11)
- [ ] **All tween end-times snap to multiples of `1/fps`** — at 30fps: 0.0333, 0.0667, 0.1, 0.1333… Steep-tail easings (`expo.in`, `power4.in`) visibly alias at sub-frame boundaries
- [ ] **Ran the timeline-duration diagnostic** — open Studio preview, run this in the devtools console, and compare every value against the `data-duration` on its host:
  ```js
  const p = document.querySelector('hyperframes-player');
  const iw = p.shadowRoot.querySelector('iframe').contentWindow;
  Object.fromEntries(Object.entries(iw.__timelines).map(([k, v]) =>
    [k, +v.duration().toFixed(4)]));
  ```
  Any gap where `timeline.duration() < data-duration` is a black-frame risk.

### 4.1 GSAP Code Dictionary (exact values used in reference work)

When in doubt, reach for these numbers — they're what the HF launch video and the Infinite spot actually use.

**Easings by purpose:**

| Purpose | Ease | Typical duration |
|---|---|---|
| Word reveal (slide-in) | `expo.out` | 0.20–0.33s |
| Generic element enter | `power2.out` | 0.2–0.5s |
| Generic element exit | `power2.in` | 0.2–0.33s |
| Beat-to-beat whip EXIT | `expo.in` / `power2.in` | 0.2–0.33s |
| Beat-to-beat whip ENTRY | `expo.out` / `power2.out` | 0.5–1.0s |
| Camera pan between stops | `power2.inOut` | 1.2–2.3s |
| Linear hold (after entry) | `"none"` | 0.4–0.65s |
| Bouncy card settle | `back.out(1.2)` – `back.out(1.5)` | 0.3–0.5s |
| Click compress | `power4.in` | 0.07s (70ms) |
| Click release (overshoot) | `back.out(3)` | 0.30s |
| UI overshoot (settle) | `elastic.out(1, 0.3)` – `elastic.out(1, 0.4)` | 0.20s |
| Cursor blink | `steps(1)` yoyo | repeat, 0.4s on / 0.4s off |
| Continuous rotation | `"none"` | full beat |
| Breathe / drift | `sine.inOut` yoyo | 2–4s, `repeat: -1` |

**Stagger values:**

- Chrome-gradient sweep across words: `stagger: 0.04`
- Dot-grid ripple per-column: `0.019`; within-column: `0.004`
- Code-stream lines: `stagger: 0.06`
- Scaffold output lines: `0.08–0.12s` explicit delays (not stagger — lines need individual eases)
- Harmonic bar spikes: `(i % 12) * 0.008`

**Defaults pattern:** don't use `gsap.defaults()` — every tween declares its ease/duration explicitly. Inheritance bugs are harder to diagnose than verbose tweens.

**Timeline skeleton:**

```js
(() => {
  const tl = gsap.timeline({ paused: true });
  // … tweens …
  tl.to({}, { duration: SLOT_DURATION }, 0);  // Law #11 anchor
  window.__timelines['<data-composition-id>'] = tl;
})();
```

Always at the end of the IIFE, key must match `data-composition-id` exactly.

---

## 5 · The "What Would Infinite Do?" Test

Before you ship any motion graphic, ask:

1. **Could I cut this scene in half?** If yes, do it.
2. **Is this color carrying a meaning?** If no, kill it.
3. **Does the camera move during this beat?** If no, add drift.
4. **Where's the motion blur?** If there's none on the transition, add a streak.
5. **Will the viewer see this same visual element again later?** If no, can I make a callback?
6. **Does the type SCALE during its reveal, or just fade in?** Fading in is the lowest-effort move. Scale.
7. **What's the negative space doing?** If 80%+ of the frame isn't black/dark, you're over-designing.
8. **Is this beat ONE idea?** If you can't summarize it in 2 words, you've packed too much in.
9. **What's the unifying texture across all scenes?** If you don't have one, you don't have a piece — you have clips.
10. **Where does the viewer rest?** Identify the breathing moments. If there are none, build them in.

---

## 6 · Anti-patterns (what NOT to do)

- ❌ **Centered, axis-aligned, motionless text fades.** This is the lowest motion-graphics tier. Always add scale, blur, or directional energy.
- ❌ **Hard cuts between scenes.** Every cut needs a transition element bridging it (streak, morph, wipe, shader).
- ❌ **Flat white text on flat black background.** Use chrome gradient and halo glow — costs nothing, looks 10× more expensive.
- ❌ **6+ colors across the piece.** You're decorating, not communicating.
- ❌ **No callbacks.** A visual element that appears once and never returns wastes a setup.
- ❌ **Outro that ends on the last beat.** Always hold the CTA for 4+ seconds.
- ❌ **Scenes that try to say two things.** Split into two scenes.
- ❌ **Static backgrounds.** Every background should have at least one slow-moving element (parallax grid, drifting particles, breathing vignette).
- ❌ **Decorative grain or vignette.** They're not decoration — they're the unifying *texture*. They go on every scene, every time.
- ❌ **Forgetting to render a draft and look at it.** Lint passing ≠ design working. **VIEW THE FRAMES.**
- ❌ **`Math.random()` / `Date.now()` / unseeded PRNGs inside a render loop.** Renders must be deterministic frame-to-frame. Use harmonic hashes instead: `80 + 220 * Math.abs(Math.sin(i*0.7 + 0.3) * Math.cos(i*1.3 + 0.7))` gives "random-looking" reproducible values.
- ❌ **Leaning on `npx hyperframes add <block>` for benchmark pieces.** The official HyperFrames launch video installs ZERO registry blocks — every scene is hand-built. The registry is for production velocity; hand-built scenes are the reference-quality move. Iterate fast with catalog blocks, then decide which ones deserve a bespoke rebuild for the hero moments.

---

## 7 · TL;DR — The Philosophy in One Sentence

> **One idea per beat, lit not colored, kinetic not still, callbacks not novelty, hold the hero, breathe the outro — the grid is always under everything, every timeline fills its slot, every exit snaps to a frame boundary, and every cut hides inside a motion-blurred whip.**
