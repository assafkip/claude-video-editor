# Recipe 2 - The tutorial edit (screen recording -> captioned walkthrough)

Turn a raw screen recording into a captioned product walkthrough plus a 60-90 second teaser. No voiceover, no timeline software. The caption composition and render commands ship in `examples/captions/`.

## When to use this one

You recorded yourself using the product (or just recorded the screen while it ran). The recording is long, slow in the middle, and silent. You want the polished version people actually watch.

## Locked decisions (the house style that works)

- **No voiceover.** Lower-third caption pills carry the explanation. Approved copy only - write the captions as text first, get them right, then render.
- **Open wide, then push in.** Show the whole product surface first, then detail. Save the hero shot for last.
- **Two cuts per source:** the full walkthrough + a 60-90s teaser. Same EDL format, different ranges.

## The pipeline

1. **Prep the source.** The render engine's audio path needs a track; add silent stereo audio to your screen recording first:
   ```bash
   ffmpeg -i source.mov -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 -shortest -c:v copy -c:a aac source_a.mp4
   ```

2. **Speed-ramp the boring middle.** Long processing stretches get pre-rendered as sped clips (45-50x via `setpts`), then referenced as their own EDL sources. The viewer sees "it worked for 20 minutes" in 25 seconds.

3. **Write the captions as a beat list.** One line each: what is on screen, what the caption says. 5 seconds per caption is the floor.

4. **Render each caption as a transparent overlay.** The composition in `examples/captions/` takes `{num, label, text}` as variables. Render with `--format mov` - ProRes 4444 carries the alpha channel; webm renders opaque. `render-cmd.sh` has the exact commands.

5. **Cut with an EDL, composite with the engine.** The EDL JSON: `sources` (your clips), `ranges` (the cut, in source seconds), `overlays` (each caption .mov placed on the output timeline). The engine's `render.py` does the cut + overlay composite in one pass.

6. **The teaser** is a second EDL over the same sources: hook beat, one mid-process beat, the hero shot, CTA. 60-90 seconds.

## The gotchas

- webm overlays render OPAQUE. Always `--format mov` for alpha.
- Pin your HyperFrames version in the project; compositions drift across majors.
- Cut on action boundaries in the recording (a click, a screen change), never mid-motion.
- If the walkthrough needs more than 12 captions, the product flow is too long for one video. Split it.
