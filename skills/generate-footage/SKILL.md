---
name: generate-footage
description: Build videos from stills when there is nothing to cut — narration first (ElevenLabs v3 with audio tags), then still keyframes from ANY source (AI image tools, screenshots, photos, HyperFrames-rendered HTML), animated deterministically with the animate-stills recipe (HyperFrames camera moves + GSAP atmosphere). Use when the user wants an explainer, documentary-style video, or any video built from generated or collected visuals instead of recorded footage.
---

# generate-footage

The plugin's other entry point. `video-use` edits footage you HAVE. This skill
builds videos from footage you DON'T have yet: narration plus still keyframes,
composed and animated by HyperFrames, rendered deterministically.

Pipeline (proven in production; see `docs/rca/` for why the motion step is
deterministic):

```
script (with v3 audio tags)
  → eleven_v3 narration            (scripts/tts_v3.py)
  → transcribe                     (npx hyperframes transcribe narration.mp3)
  → lock scene windows to sentence boundaries (word-level timestamps)
  → STILLS FROM ANYWHERE           (one keyframe per scene — see below)
  → animate-stills composition     (recipes/04-animate-stills.md, build_scenes.py)
  → lint → render → motion + audio QA (scripts/motion_check.py, contact sheet)
```

## Order matters: voice FIRST, visuals second

Generate and transcribe the narration BEFORE building any composition or
collecting keyframes. The spoken sentence boundaries are the scene windows.
v3 reads are non-deterministic in pacing — a 120s estimate can come out 100s
or 166s — so visuals built first always get re-timed.

## Voiceover — ElevenLabs v3 with audio tags

`scripts/tts_v3.py` — stdlib-only, no pip deps. Key from `$ELEVENLABS_API_KEY`
or the plugin's `skills/video-use/.env`.

```bash
python3 scripts/tts_v3.py --probe                      # verify eleven_v3 + list voices
python3 scripts/tts_v3.py --voice <id> --stability 0.0 --script SCRIPT.md --out narration.mp3
```

- Audio tags go in the script text: `[excited]`, `[whispers]`, `[softly]`,
  `[dramatic tone]`, `[warmly]`. v3 performs them; v2 ignores them.
- Stability: `0.0` = Creative (max expressiveness), `0.5` = Natural,
  `1.0` = Robust. A "flat" read is fixed by lowering stability and re-tagging
  the script, not by louder words.
- Delivery levers: CAPS on power words, `...` for dramatic pauses, contrast
  (drop to `[whispers]` right before a big line).
- Audition 2-3 voices on the first sentence before committing. The first
  voice is never the pick.
- v3 may paraphrase slightly. Transcribe and READ the result; regenerate if
  a key line drifted.

## Stills from anywhere

A keyframe is just a PNG. The pipeline does not care where it came from.
One still per scene, named `kf-NN.png`, listed in the scene manifest
(`recipes/04-animate-stills.md` documents the schema). Sources that work:

- **AI image tools** — any text-to-image tool you already have (Gemini,
  GPT image, Midjourney, local SD, or a hosted actor — see the optional
  section at the end). Generate from per-scene prompts with one locked
  style suffix.
- **Screenshots and photos** — product UI captures, archive material, scans,
  real photography. The Ken Burns treatment was invented for this.
- **HyperFrames-rendered HTML** — build a styled HTML frame and snapshot it;
  the engine produces its own stills.

Craft rules that hold regardless of source:

- **Lock ONE style** in DESIGN.md and apply it to every frame. Drift across
  frames reads as different shots once there's motion and grading.
- **Verify the file type.** Some tools serve JPEGs with .png names; check
  magic bytes before composing (`file kf-01.png`).
- **QA every frame** (read the image). One off-style frame is a regenerate,
  not a keep. Check for: text artifacts, watermarks, anachronisms, faces in
  close-up (drift risk), wrong palette.
- **No named IP, no real living person's likeness** in generated frames for
  anything posted publicly.

## Animation — deterministic, in-repo

Stills become motion with the **animate-stills recipe**
(`recipes/04-animate-stills.md`): a manifest-driven HyperFrames composition
applying camera language (push-ins, drifts, holds) and GSAP atmosphere
(mist, rain, light shifts, vignette) over each still, scene windows locked
to the transcript. `scripts/build_scenes.py` generates the scene layers from
the manifest; `scripts/motion_check.py` proves real motion via pixel-diff in
the rendered output. Renders identically every run, costs nothing, works
offline.

Requires Node >= 22 for the HyperFrames CLI.

## Captions and assembly

- Captions burned in (muted autoplay on Reddit/X), phrase-level, timed from
  the transcript words.
- White flash (0.28s) at story turns; soft crossfades elsewhere; dark
  vignette grade unifies stills from mixed sources and makes captions read.
- Verify motion in the render: pixel-diff two frames 4s apart inside one
  scene (`scripts/motion_check.py` — mean gray diff > 3 = real motion).
- Audio QA: `ffmpeg -af volumedetect` — documentary speech sits near
  -26 dB mean.

## Optional: hosted generative tools

These are NOT dependencies. They are one way among several to source stills
or clips, and they can disappear without notice — plan accordingly.

- Apify text-to-image actors (e.g. `akash9078/ai-image-generator`,
  ~$0.01/image) worked well for batch keyframe generation. Watch for silent
  failures (`ok:true` with a null URL) and mislabeled file types.
- Hosted image-to-video actors are where this pipeline previously kept its
  motion step. On 2026-06-11 the actor `danitn11/wan22-lightning-image-to-video`
  (2 total users) died upstream mid-production and every run failed
  instantly; the full analysis is in
  `docs/rca/rca-generate-footage-animation-2026-06-11.md`. Generative
  image-to-video now lives in a separate companion repo with a pluggable
  BYO-key backend; this plugin's motion step is deterministic and local.
