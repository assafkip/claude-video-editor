#!/usr/bin/env bash
# kipi video kit — render commands. Run from the kit dir after you've edited an EDL.
set -euo pipefail

# Engine lives here (its own git repo). render.py does the cut + overlay composite.
VIDEO_USE="${VIDEO_USE:-$HOME/Developer/video-use}"
HF_VERSION="0.6.70"   # pin — the composition was built against this

# ---------------------------------------------------------------------------
# STEP 1 — render the caption overlays (one .mov per caption, alpha channel).
# The composition reads {num,label,text} from --variables. Render --format mov
# (ProRes 4444 yuva) — webm came out OPAQUE, mov carries the alpha. Repeat per
# caption, writing to captions/renders/capN_<beat>.mov (the EDL points at these).
# ---------------------------------------------------------------------------
cap() {  # cap <num> <LABEL> <text> <outfile>
  ( cd captions && npx --yes "hyperframes@${HF_VERSION}" render index.html \
      --format mov \
      --variables "{\"num\":\"$1\",\"label\":\"$2\",\"text\":\"$3\"}" \
      -o "renders/$4.mov" )
}
# Example (the tutorial's 6 captions) — edit text, then re-run:
# cap 01 INTAKE     "Drop raw intel. Get the network."      cap1_intake
# cap 02 UNDERSTAND "Agent proposes the schema. You approve." cap2_understand
# cap 03 PROCESS    "Consolidate, type, cluster — automatic." cap3_process
# cap 04 INVESTIGATE "The crew pivots and grows the graph."   cap4_investigate
# cap 05 DELIVER    "One synthesized brief. Sourced."         cap5_deliver
# cap 06 GRAPH      "The whole network, one canvas."          cap6_graph

# ---------------------------------------------------------------------------
# STEP 2 — composite: cut per the EDL + burn the caption overlays on top.
#   --no-subtitles  (captions ARE the overlays; no burned-in subs)
#   --no-loudnorm   (source is silent; skip loudness pass)
# ---------------------------------------------------------------------------
compose() {  # compose <edl.json> <out.mp4>
  python3 "$VIDEO_USE/helpers/render.py" "$1" -o "$2" --no-subtitles --no-loudnorm
}
# compose edls/edl_walkthrough.json walkthrough_final.mp4
# compose edls/edl_teaser.json      teaser_final.mp4

echo "Source the functions: 'source render-cmd.sh', then call cap ... and compose ..."
