# Composition Scaffold — Scoped Styles + IIFE GSAP Pattern

Used by `/make-a-video` Gate 6. Every sub-composition follows this pattern.

## Why this pattern

- **Scoped styles** (`[data-composition-id="..."] { ... }`) prevent CSS bleed between compositions and from catalog blocks.
- **IIFE** keeps GSAP variables out of the global namespace — multiple sub-compositions won't collide.
- **Anchor tween** (`tl.to({}, { duration: SLOT_DURATION }, 0)`) guarantees `timeline.duration() ≥ data-duration`, preventing the black-frame flash HyperFrames emits when a timeline ends short. MOTION_PHILOSOPHY Law 11.

---

## Boilerplate — one sub-composition file

```html
<div data-composition-id="scene-01-hook" data-start="0" data-duration="1.5">
  <!-- Scoped styles — every selector under the [data-composition-id] -->
  <style>
    [data-composition-id="scene-01-hook"] {
      position: absolute;
      inset: 0;
      display: grid;
      place-items: center;
    }
    [data-composition-id="scene-01-hook"] .word {
      font-family: 'Inter', sans-serif;
      font-weight: 700;
      font-size: 96px;
      background: linear-gradient(180deg, #fff 0%, #999 100%);
      -webkit-background-clip: text;
      color: transparent;
    }
  </style>

  <!-- DOM — timed elements get class="clip" + data-start/duration/track -->
  <span class="word w1 clip" data-start="0.0" data-duration="0.8" data-track-index="2">Why</span>
  <span class="word w2 clip" data-start="0.2" data-duration="0.8" data-track-index="2">is</span>
  <span class="word w3 clip" data-start="0.4" data-duration="0.8" data-track-index="2">this</span>
  <span class="word w4 clip" data-start="0.6" data-duration="0.8" data-track-index="2">still</span>
  <span class="word w5 clip" data-start="0.8" data-duration="0.7" data-track-index="2">hard?</span>

  <!-- IIFE + anchor tween -->
  <script>
    (function(){
      const SLOT_DURATION = 1.5;
      const tl = gsap.timeline({ paused: true });

      // Per-word reveal stagger
      tl.from('[data-composition-id="scene-01-hook"] .w1',
        { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0);
      tl.from('[data-composition-id="scene-01-hook"] .w2',
        { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0.2);
      tl.from('[data-composition-id="scene-01-hook"] .w3',
        { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0.4);
      tl.from('[data-composition-id="scene-01-hook"] .w4',
        { y: 30, opacity: 0, scale: 0.9, duration: 0.5, ease: 'power3.out' }, 0.6);
      tl.fromTo('[data-composition-id="scene-01-hook"] .w5',
        { y: 30, opacity: 0, scale: 0.9 },
        { y: 0, opacity: 1, scale: 1, duration: 0.3, ease: 'power3.out' }, 0.8);
      // Dolly-through on the hero word
      tl.to('[data-composition-id="scene-01-hook"] .w5',
        { scale: 8, opacity: 0, duration: 0.4, ease: 'power2.in' }, 1.1);

      // ANCHOR — keeps timeline.duration() >= SLOT_DURATION. Non-negotiable.
      tl.to({}, { duration: SLOT_DURATION }, 0);

      // Register — key MUST exactly match data-composition-id
      window.__timelines['scene-01-hook'] = tl;
    })();
  </script>
</div>
```

---

## Hard rules the scaffold enforces

1. **Root composition `<div>` in `index.html`** has `id`, `data-composition-id`, `data-start="0"`, `data-width`, `data-height`. Sub-composition roots have `data-composition-id`, `data-start`, `data-duration` — no width/height.
2. **Every timed visible element** has `class="clip"`, `data-start`, `data-duration`, `data-track-index`. **Exceptions:** `<video>` and `<audio>` do NOT get `class="clip"` — it breaks them.
3. **CSS is scoped.** No top-level rules inside a sub-composition file. Every selector lives under `[data-composition-id="..."]`.
4. **Timeline registered** on `window.__timelines['<id>']` with key exactly matching `data-composition-id`.
5. **Anchor tween** at the end of every timeline: `tl.to({}, { duration: SLOT_DURATION }, 0)`.
6. **Never** `masterTL.add(child)` — HyperFrames auto-links sub-composition timelines to the parent.
7. **Never** call `.play()` / `.pause()` / set `.currentTime` on media. The framework owns playback.
8. **Never animate** `width` · `height` · `top` · `left` directly on a `<video>` — browsers freeze frames. Wrap in a `<div>` and animate the wrapper.
9. **Same-track clips never overlap** (same `data-track-index`). Use separate track indices for overlapping elements.

---

## Ambient background pattern

One persistent composition, bottom layer, full video duration.

In `index.html`:
```html
<template
  data-composition-src="compositions/ambient-bg.html"
  data-start="0"
  data-duration="<total-seconds>"
  data-track-index="0"></template>
```

`compositions/ambient-bg.html` is its own sub-composition: grid + vignette + grain + slow drifts (breathing vignette, parallax grid). Uses the same scaffold pattern — scoped styles, IIFE, anchor tween.

---

## Caption pattern (body-level siblings)

Captions go OUTSIDE the master composition `<div>` in `index.html`, each with `data-track-index ≥ 20`:

```html
<div class="cap clip"
     data-start="0.5" data-duration="1.8" data-track-index="30">
  Why is this still so hard?
</div>
<div class="cap clip"
     data-start="2.4" data-duration="2.2" data-track-index="31">
  Ship faster with ACME.
</div>

<style>
  .cap {
    position: absolute;
    bottom: 72px;
    left: 50%;
    transform: translateX(-50%);
    padding: 12px 22px;
    border-radius: 14px;
    background: rgba(10, 8, 5, 0.55);
    backdrop-filter: blur(8px);
    font: 500 28px/1.3 Inter, sans-serif;
    color: #fff;
  }
</style>
```

Central control, zero coupling to scene timelines. MOTION_PHILOSOPHY §3.13.

---

## Time-reference aliasing

A clip's `data-start` can reference another clip by id:

```html
<span id="intro" data-start="0" data-duration="2">...</span>
<span data-start="intro + 1.5" data-duration="2">...</span>
<span data-start="intro - 0.3" data-duration="2">...</span>
```

Useful for small offsets around a named beat without hard-coding seconds.

---

## Diagnostic — every timeline fills its slot

Before shipping, open Studio devtools and run:

```js
const p = document.querySelector('hyperframes-player');
const iw = p.shadowRoot.querySelector('iframe').contentWindow;
Object.fromEntries(Object.entries(iw.__timelines).map(([k, v]) =>
  [k, +v.duration().toFixed(4)]));
```

Compare every value against the corresponding `data-duration`. Any gap where `timeline.duration() < data-duration` is a black-frame risk. Fix by adjusting the anchor tween's duration.

---

## Time-snapping

Tween end-times should snap to multiples of `1 / fps`:
- 30fps: 0.0333, 0.0667, 0.1, 0.1333, 0.1667, 0.2, …
- 60fps: 0.0167, 0.0333, 0.05, 0.0667, …

Steep-tail easings (`expo.in`, `power4.in`) visibly alias at sub-frame boundaries. MOTION_PHILOSOPHY §4.

---

## Determinism

Never use `Math.random()` or `Date.now()` inside render logic. Use seeded hashes:

```js
// Deterministic pseudo-random per index
const noise = i => 80 + 220 * Math.abs(Math.sin(i * 0.7 + 0.3) * Math.cos(i * 1.3 + 0.7));
```

Renders must be identical frame-to-frame across runs.
