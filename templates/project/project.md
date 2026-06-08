# <project name> — edit session

**Source(s):** <files in sources/> (duration, resolution, audio? silent?)
**Date:** <YYYY-MM-DD>
**Goal:** <what this video is — promo / teaser / tutorial / short>

## Decisions
- <voiceover or captions-only? approved caption copy?>
- <pacing, hero shot, brand look>
- <output(s): e.g. full walkthrough + 60s teaser>

## Beat map (source timestamps)
- <beat 1 — source 0:00-0:08>
- <beat 2 — ...>

## Pipeline notes
- <silent source → silent stereo track added?>
- <speed-ramps: which stretches, what factor, pre-rendered setpts clips?>
- <captions: HyperFrames composition path, rendered --format mov (alpha)>
- <composite flags used>

## Outputs
- `edit/final.mp4` — <duration, what it is>
- EDL(s): `edit/<edl>.json`

## To re-render after a tweak
`<engine>/.venv/bin/python <engine>/helpers/render.py <edl> -o edit/<out>.mp4 --no-subtitles --no-loudnorm`
