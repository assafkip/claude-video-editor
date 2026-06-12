# Changelog

## 0.3.0 — 2026-06-11

The deterministic-motion release. A hosted image-to-video actor died
mid-production and took the pipeline's animation step with it; this release
removes that class of failure from the plugin.

### Added
- **animate-stills recipe** (`recipes/04-animate-stills.md`): manifest-driven
  HyperFrames composition — camera language (push-in, pull-back, drifts,
  rise, hold) and GSAP atmosphere (mist, rain, light, vignette) over still
  keyframes. Deterministic, offline, zero marginal cost. Template with a
  renderable 2-scene fixture at `templates/animate-stills/`.
- `skills/generate-footage/scripts/build_scenes.py` — generates scene layers
  and timeline from `manifest.json`; marker-owned regions survive hand edits.
- `skills/generate-footage/scripts/motion_check.py` — pixel-diff gate proving
  a render actually moves (median of sampled frame pairs).
- `skills/generate-footage/scripts/check_skill_md.py` — structure gate
  keeping hosted-service mentions inside explicitly optional sections.
- **RCA** for the 2026-06-11 animation failure:
  `docs/rca/rca-generate-footage-animation-2026-06-11.md`.

### Changed
- `generate-footage` is now **stills from anywhere**: keyframes are PNGs from
  any source (AI image tools, screenshots, photos, HyperFrames-rendered
  HTML). The motion step is the deterministic animate-stills recipe.
- README requirements: ElevenLabs is the only key; Node requirement corrected
  to >= 22 for the HyperFrames CLI.

### Removed
- Hosted image-to-video actor as the animation path (see RCA). Generative
  image-to-video lives in a separate BYO-key companion repo
  (claude-video-generator); the editor never depends on it.

## 0.2.0 — 2026-06-11

- Public release prep: MIT + Commons Clause license, demo GIF, explicit
  requirements; recipes and worked examples (formerly the Launch Video Kit)
  merged in free; funnel links removed.
