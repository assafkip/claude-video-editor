# RCA: generate-footage animation step failed in production (2026-06-11)

## What happened

The first real production run of the `generate-footage` pipeline (a 16-scene,
166s research explainer) generated narration and all 16 keyframes
successfully, then failed at the animation step: 16/16 image-to-video runs
against the Apify actor `danitn11/wan22-lightning-image-to-video` failed.

## Evidence (measured, not assumed)

- Every animation run: status FAILED, exit 1, runtime 1.1-3.0s,
  computeUnits=0 (the container never did real work; no charges).
- Reproduced across three input variants: full production input, minimal
  valid input (imageUrl + prompt only), and cheapest config (480p/2s) with
  an explicit charge cap. Identical instant failure.
- Control: the image actor on the SAME account succeeded repeatedly within
  minutes of the failures (three keyframe regenerations at 22:14-22:18Z;
  video failures at 22:23Z+). The account and platform were healthy; the
  failure was specific to the video actor.
- The same actor had worked earlier the same day (the 85s anime demo).
  It died within ~12 hours with no input change on our side.

## Surface cause

The actor's unowned upstream dependency stopped working. The exact upstream
failure (key, quota, or endpoint) is not observable from outside the actor;
what the evidence proves is that the actor fails instantly on its side
before doing any work, independent of our input or account. With only 2
total users, such failures can go unnoticed indefinitely and no SLA exists.

## Structural root cause

The plugin's only generative-motion path was PROSE in
`skills/generate-footage/SKILL.md` instructing a call to a third-party
2-user actor: an unowned single point of failure, not code, with no
fallback, no deterministic alternative, and no honest failure mode. By
contrast, the voiceover step was already a committed script (`tts_v3.py`)
calling a first-party API directly: that step did not fail.

Contributing factor (cause type: design assumption): the pipeline treated
"animate stills" as necessarily generative. A deterministic alternative is
available in-repo: HyperFrames renders HTML/GSAP compositions to video
(camera moves and atmosphere layers over still keyframes, the technique
behind the repo's existing promo example in `examples/promo/`). cve-a3
implements and verifies this path with a pixel-diff motion gate; until that
gate passes, treat the deterministic path as the designed direction rather
than established fact.

## What did NOT fail (blameless scope)

- HyperFrames, video-use, hyperframes-student-kit: untouched, healthy.
- ElevenLabs v3 narration (`tts_v3.py`): 166.2s narration generated and
  transcribed cleanly.
- Keyframe generation: 16/16 produced (3 required prompt-level retries for
  content drift, all caught by frame QA).

## Action items

- [ ] cve-a2: rewrite `generate-footage` as "stills from anywhere" — keyframes
  are PNGs from any source; demote Apify to one optional bullet with this
  outage documented as the caveat. Gate: `check_skill_md.py`.
- [ ] cve-a3: add the deterministic `animate-stills` recipe (manifest-driven
  HyperFrames template, camera language + atmosphere over stills) with
  motion proven by pixel-diff (`motion_check.py`), Node >= 22 precondition.
- [ ] claude-video-generator (separate repo): generative image-to-video moves
  OUT of this plugin into its own repo with a pluggable BYO-key backend
  script, honest BLOCKED exit semantics, and a required live smoke test.
  The editor never depends on it; composition is via `sources/` files.

## Verification

Ran the failing actor 18 times across three input variants on 2026-06-11:
got exit 1 in under 3s with computeUnits=0 every time (runIds include
M0b9x4GDLNeq5gOca, 3olNbuWciQZmz1LTf, SrDM6QnTInyehv527). Ran the image
actor on the same account in the same window: SUCCEEDED. Each action item
above closes only with verified + reviewed + findings_triaged receipts in
the governing PRD.
