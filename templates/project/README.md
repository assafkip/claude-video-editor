# video project

Copy this folder next to your footage (or drop clips into `sources/`), start your
agent here, and say what you want:

> edit these into a 60-second promo

The agent (via the `video-studio` skill) inventories the sources, proposes a cut,
waits for your OK, then writes `edit/final.mp4`. Session memory persists in
`project.md` so the next session picks up where you left off.

## Layout
```
sources/        drop raw clips here (mp4/mov)
project.md      session memory — decisions, beat map, render notes (the agent maintains this)
edit/           all outputs land here (cuts, caption renders, final.mp4)
```

## Tips
- Silent screen-recording? The agent adds a silent stereo track and renders `--no-loudnorm`.
- Want captions/motion graphics? Say so ("lower-third captions, no voiceover") — it
  authors a HyperFrames composition and composites the alpha `.mov` overlays.
- Nothing renders until you approve the strategy. Taste is yours; production-correctness
  is the engine's.
