# Build Checklist — Preflight + Pre-Delivery

Used by `/make-a-video` Gates 7 and 8. Run before any render and before telling the user "it's done."

---

## Preflight — structural (before PREVIEW GATE 1)

- [ ] Root `<div>` in `index.html` has `id`, `data-composition-id`, `data-start="0"`, `data-width`, `data-height`
- [ ] Every sub-composition `.html` has a root `<div>` with `data-composition-id`, `data-start`, `data-duration`
- [ ] Every timed visible element has `class="clip"`, `data-start`, `data-duration`, `data-track-index`
- [ ] NO `class="clip"` on `<video>` tags
- [ ] `<video>` elements are `muted`; audio lives in sibling `<audio>` elements
- [ ] Same-track clips never overlap (different `data-track-index` for overlapping elements)
- [ ] Every GSAP timeline ends with `tl.to({}, { duration: SLOT_DURATION }, 0)`
- [ ] Every timeline registered on `window.__timelines['<id>']` with key matching `data-composition-id` exactly
- [ ] Captions are body-level siblings in `index.html` (not inside sub-compositions), each with `data-track-index ≥ 20`
- [ ] No `Math.random()`, no `Date.now()`, no render-time `fetch()`
- [ ] Catalog block CSS is scoped under `[data-composition-id="..."]` (no leaked `html, body { ... }`)
- [ ] `npx hyperframes lint` — all errors fixed, warnings triaged

---

## Preflight — aesthetic

- [ ] Palette on-brief — no rogue colors, ≤5 symbolic hues
- [ ] Typography on-brief — only the fonts declared in `assets/style-profile.md`
- [ ] Grid / vignette / grain texture present on every scene (or on the full-composition background)
- [ ] Ambient background composition on `data-track-index="0"` for full duration
- [ ] Every scene transition is a *motion* transition (whip · morph · blur · recolor), not a hard fade
- [ ] Outro holds 4–6 seconds
- [ ] At least one visual callback (element returns later)
- [ ] Scene lengths follow the brief's pacing tier (kinetic 1–2s · balanced 2–3s · relaxed 3–5s)

---

## PREVIEW GATE 1 — Studio

- [ ] `npx hyperframes preview` running (background)
- [ ] User given `http://localhost:3002`
- [ ] If the project has shader blocks, user also given individual composition URLs (`http://localhost:3002/?comp=<id>`)
- [ ] Hot-reload edits show up correctly
- [ ] **Explicit "looks good, render a draft" captured** — silence is not approval

---

## Draft render

- [ ] `npx hyperframes render --quality draft --output renders/<slug>-draft.mp4` completed
- [ ] No render errors or warnings
- [ ] Output file exists and plays in a standard video player

---

## Visual verification (NON-NEGOTIABLE)

- [ ] `mkdir -p renders/frames`
- [ ] Frame extracted at each beat hero moment:
      ```bash
      ffmpeg -y -ss <t> -i renders/<slug>-draft.mp4 -frames:v 1 -q:v 2 renders/frames/t<t>.png
      ```
- [ ] Frame extracted at each transition moment (the mid-streak / mid-morph timestamp)
- [ ] **Every PNG opened via the `Read` tool** — not just listed by filename
- [ ] For each frame confirmed:
  - [ ] No cropped faces
  - [ ] Face-mode correct per scene (full-screen vs. corner as storyboarded)
  - [ ] Text readable, on-palette, not overflowing
  - [ ] Transition lands on the intended word / beat
  - [ ] No blank frames, no black-frame flashes
- [ ] Any regression → fixed → re-rendered → re-verified

---

## PREVIEW GATE 2 — Rendered MP4

- [ ] `npx serve renders -p 8080 -n` running (NOT Python's `http.server` — no Range support breaks scrubbing)
- [ ] User given `http://localhost:8080/<slug>-draft.mp4`
- [ ] Playback scrubs cleanly end-to-end
- [ ] Audio syncs with visuals (voiceover · SFX · music bed)
- [ ] **Explicit sign-off captured**

---

## Final render

- [ ] `npx hyperframes render --quality standard --output renders/<slug>-final.mp4`
- [ ] File exists, size reasonable for duration (roughly 3–10 MB per 10 seconds at 1080p)
- [ ] Final file plays cleanly in a standard player
- [ ] Output path reported to the user

---

## After delivery

- [ ] Update `BRIEF.md` with a `## Delivery` section: final render path, render command used, any post-delivery notes
- [ ] Offer one round of revisions — the user almost always has one
- [ ] If the user wants a different format (e.g. 1:1 crop from 16:9), plan that as a new pass through Gates 1–8 with the original `BRIEF.md` as the starting point

---

## Common fail-modes and how they look

| Symptom in the render | Likely cause | Fix |
|---|---|---|
| Black frame flash at end of a scene | Timeline shorter than `data-duration` | Add / extend the anchor tween in that sub-composition |
| `<video>` freezes on a still frame | Animating `width`/`height` on the video element directly | Wrap in a `<div>` and animate the wrapper |
| Text clipped / cropped | Scoped style missing `overflow: visible` on the container | Add it |
| Catalog block's background covers the whole stage | Block's `html, body { ... }` rule leaked | Scope it under `[data-composition-id="..."]` |
| Transition lands mid-word | `data-start` on the incoming scene is off | Align to the transition's peak frame (usually midway through its duration) |
| Grain flickers / looks random | Using `Math.random()` in the grain script | Replace with a seeded hash |
