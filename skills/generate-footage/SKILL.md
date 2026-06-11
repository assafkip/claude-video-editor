---
name: generate-footage
description: Generate footage from prompts when there is nothing to cut — AI keyframes (text-to-image), animated clips (image-to-video via Wan 2.2), and expressive ElevenLabs v3 voiceover with audio tags. Use when the user wants an explainer, anime-style video, or any video built from generated visuals instead of recorded footage. Output feeds straight into HyperFrames compositions: generated clips become <video> scene tracks, narration drives all beat timings.
---

# generate-footage

The plugin's other entry point. `video-use` edits footage you HAVE. This skill
creates footage you DON'T: painted keyframes, animated clips, and narration —
then hands everything to HyperFrames for composition and render.

Proven pipeline (built 2026-06-11, anime explainer, ~$3 total generation cost):

```
script (with v3 audio tags)
  → eleven_v3 narration            (scripts/tts_v3.py)
  → transcribe                     (npx hyperframes transcribe narration.mp3)
  → lock scene windows to sentence boundaries (word-level timestamps)
  → generate keyframes             (Apify: text-to-image, one per scene)
  → animate keyframes              (Apify: Wan 2.2 image-to-video, 10s/720p)
  → fit clips to scene windows     (ffmpeg trim / setpts stretch)
  → HyperFrames composition        (<video> scene tracks + overlays + captions)
  → lint → draft render → QA frames → final render
```

## Order matters: voice FIRST, visuals second

Generate and transcribe the narration BEFORE building any composition or
generating any clips. The spoken sentence boundaries are the scene windows.
Building visuals first means re-timing everything when the voice lands
differently (v3 reads are non-deterministic in pacing — a 75s estimate can
come out 60s or 85s).

## Voiceover — ElevenLabs v3 with audio tags

`scripts/tts_v3.py` — stdlib-only, no pip deps. Key from `$ELEVENLABS_API_KEY`
or the plugin's `skills/video-use/.env`.

```bash
python3 scripts/tts_v3.py --probe                      # verify eleven_v3 + list voices
python3 scripts/tts_v3.py --voice <id> --stability 0.0 --script SCRIPT.md --out narration.mp3
```

- Audio tags go in the script text: `[excited]`, `[whispers]`, `[shouts]`,
  `[dramatic tone]`, `[softly]`, `[warmly]`. v3 performs them; v2 ignores them.
- Stability: `0.0` = Creative (max expressiveness — hype/anime reads),
  `0.5` = Natural, `1.0` = Robust. A "flat" read is fixed by lowering
  stability and re-tagging the script, not by louder words.
- Delivery levers that work: CAPS on power words, `...` for dramatic pauses,
  `!` for energy. Contrast sells — drop to `[whispers]` right before a shout.
- Audition 2-3 voices on the first sentence before committing. The first
  voice is never the pick.
- v3 may paraphrase slightly (one word here and there). Transcribe and read
  the result; regenerate if a key line drifted.

## Keyframes — Apify text-to-image

Actor: `akash9078/ai-image-generator` (input: `prompt`, `ratio`). ~$0.01/image.
Call via Apify MCP (`call-actor`) when connected, else REST with `APIFY_TOKEN`.

Rules that held up in production:

- **Character consistency**: write ONE character description and prefix every
  prompt with it verbatim ("An original 12-year-old anime hero girl with short
  messy dark indigo hair with a single gold streak, large teal-green eyes, teal
  short-sleeved school hero jacket with gold trim. ..."). Drift across frames
  reads as different shots once there's motion and grading — close enough.
- **Style suffix** on every prompt: ".. dark cinematic shonen anime production
  keyframe, painterly background, dramatic rim lighting, high detail, no text,
  no watermark, no logo".
- **Original characters only.** Never named IP (MHA/Naruto/etc.) — describe the
  energy, not the franchise. Required for anything posted publicly.
- **Silent failures**: the actor can return `ok:true` with `imageUrl:null`.
  That's a content-filter or generation miss — reword emotionally loaded
  phrasing ("frozen in fear" → "stands very still, wide worried eyes") and
  retry.
- **Watermark**: output may carry a small corner mark. Kill it with
  `object-fit: cover` + scale ≥1.06 in composition, or crop in ffmpeg.
- QA every frame (Read the image). One off-style frame (chibi-on-white in a
  dark cinematic set) is a regenerate, not a keep.

## Animation — Apify Wan 2.2 image-to-video

Actor: `danitn11/wan22-lightning-image-to-video`. $0.02/s @480p, $0.035/s
@720p. Input: `imageUrl`, `prompt`, `resolution`, `aspectRatio`, `duration`
(2-10s), `negativePrompt`, `cfgScale` (1.0).

- **Feed it the image actor's own hosted output URL** — the signed
  `api.apify.com/v2/key-value-stores/...` URL works directly as `imageUrl`.
  No upload step.
- **Prompt = motion only.** The image already defines the look. Describe what
  moves: "hair blows upward, lightning arcs intensify, camera slowly pushes
  in". Negative: "blur, distort, low quality, morphing face, text, watermark".
- Generate **10s at 720p** per scene. Output is 16fps 720x720 — soft but
  reads as anime production once graded and in motion.
- Image-to-video preserves the character. Text-to-video would lose it.

## Fitting clips to scene windows

Clips are 10s; scenes are whatever the narration says. ffmpeg per scene:

```bash
# scene shorter than clip → trim
ffmpeg -i s1.mp4 -vf "scale=1080:1080,fps=30" -t 7.1 -an -c:v libx264 -crf 16 s1-fit.mp4
# scene longer than clip → slow-stretch (keep factor ≤ 1.5x — ambient motion hides it)
ffmpeg -i s6.mp4 -vf "setpts=1.441*PTS,scale=1080:1080,fps=30" -t 14.5 -an -c:v libx264 -crf 16 s6-fit.mp4
```

Scale to composition size, normalize fps, strip audio (`-an` — narration is
the only audio track).

## Composition — generated clips in HyperFrames

- Each scene = a plain stacked `<div class="scene">` layer (NO data-* timing
  attrs on it), opacity-gated by the master timeline, z-index ordered.
- Inside each: `<video class="clip" data-start data-duration data-track-index
  muted playsinline>` — the framework owns playback. Video sits in a non-timed
  wrapper div; shakes/moves animate the WRAPPER, never the video element.
- Anime cut language on top: white flash `fromTo(opacity 0.9→0, 0.28s)` at
  every scene boundary, finite-repeat shake on slam moments, Anton impact
  stamps, speed-line overlays (`repeating-conic-gradient` + `mix-blend-mode:
  screen`), dark vignette grade to unify generated footage and make captions
  read.
- Captions burned in (muted autoplay on Reddit/X), phrase-level, timed from
  the transcript words.
- Verify motion in the render: pixel-diff two frames 4s apart inside one
  scene (mean gray diff >3 = real motion; ~0 = you rendered stills).

## Cost reality (2026-06)

| Step | Cost |
|---|---|
| Keyframe (image) | ~$0.01 each |
| Animated clip 10s/720p | ~$0.35 each |
| eleven_v3 narration ~85s | ElevenLabs plan credits |
| Full 8-scene 85s video | ~$3 |
