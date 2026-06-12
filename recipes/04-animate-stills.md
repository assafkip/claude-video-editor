# Recipe 4 - Animate stills (the deterministic motion path)

Turn a folder of still keyframes into a finished, narrated video with camera
language and atmosphere — no generative video model, no external service, no
per-second cost. This is the Ken Burns technique, driven by a manifest:
HyperFrames renders the motion, your stills carry the look.

**Requires Node >= 22** for the HyperFrames CLI (`node --version` first).

## When to use this one

- You have stills (AI-generated, screenshots, photos, scans, HTML renders)
  and narration, and you want a documentary-style explainer.
- You want renders that are identical every run and work offline.
- A generative image-to-video service just died mid-production and you still
  have a deadline (see `docs/rca/rca-generate-footage-animation-2026-06-11.md`
  for the day this recipe was born).

## The method

1. **Voice first.** Narration with `tts_v3.py`, then
   `npx hyperframes transcribe narration.mp3`. Sentence boundaries from the
   transcript become your scene windows. Never build visuals first.

2. **Stills from anywhere.** One PNG per scene, named `kf-NN.png` (or any
   path you list in the manifest). Verify magic bytes — some tools serve
   JPEGs with .png names (`file kf-01.png`).

3. **Write the manifest** (`manifest.json`):

   ```json
   {
     "size": [1080, 1080],
     "fps": 30,
     "scenes": [
       {"n": 1, "image": "assets/stills/s1.png", "window": [0.0, 6.0],
        "move": "push-in", "atmosphere": "mist"}
     ],
     "captions": [
       {"text": "Phrase-level caption.", "at": [0.6, 5.4]}
     ]
   }
   ```

   - `move`: `push-in` | `pull-back` | `drift-left` | `drift-right` |
     `rise` | `hold`. Linear over the full window — documentary register,
     no easing tricks.
   - `atmosphere` (optional): `mist` | `rain` | `light` | `none`. One
     overlay per scene; the global vignette unifies mixed-source stills.
   - Windows must tile (gaps <= 0.2s, no overlaps). Scene `n` is 1-based
     and ordered.

4. **Build, check, render.**

   ```bash
   python3 ../../skills/generate-footage/scripts/build_scenes.py manifest.json
   npx hyperframes lint && npx hyperframes validate
   npx hyperframes render     # output lands in renders/
   ```

   `build_scenes.py` owns the scene layers and timeline between marker
   comments in `index.html`; your styles and extra layers outside the
   markers survive rebuilds. Scenes fade in over each other in z-order;
   a hidden sentinel pins total duration to the last window's end.

5. **Add the narration track.** HyperFrames renders picture; mux audio with
   ffmpeg:

   ```bash
   ffmpeg -i renders/<output>.mp4 -i narration.mp3 -c:v copy -c:a aac -shortest final.mp4
   ```

6. **Prove it moves.** A broken timeline renders a slideshow of one frame.
   The gate:

   ```bash
   python3 ../../skills/generate-footage/scripts/motion_check.py final.mp4 --t1 1.0 --t2 5.0 --min-diff 3
   ```

   Pick t1/t2 inside ONE scene window. Run it on your lowest-motion scene.

7. **Audio + frame QA.** `ffmpeg -af volumedetect` (documentary speech mean
   sits near -26 dB); `npx hyperframes snapshot .` for the contact sheet —
   check text overflow, style drift, dead frames before publishing.

## The gotchas

- **Low-detail stills hide motion.** A slow push-in on a smooth gradient can
  measure near-zero pixel diff even though it renders correctly. If
  motion_check fails on a real render, check the still's detail level before
  blaming the timeline (and prefer textured artwork for slow moves).
- **Vendor your fonts** if your caption styling uses custom type — CDN font
  fetches fail in the sandboxed renderer and fall back silently.
- **Camera overflow is intentional** — the `cam` wrapper carries
  `data-layout-allow-overflow` because zooms push content off-canvas.
- **Never `repeat: -1`** in anything you add outside the markers; infinite
  loops break the capture engine.
- The template ships a 2-scene, 12s fixture (`templates/animate-stills/`)
  with deterministic test stills. Render it once after install to verify
  your toolchain end-to-end.
