#!/usr/bin/env bash
# video-studio installer — verifies runtime deps, sets up the video-use engine,
# and prompts for the transcription key. Idempotent: safe to re-run.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
say() { printf "\033[36m▸ %s\033[0m\n" "$*"; }
warn() { printf "\033[33m!  %s\033[0m\n" "$*"; }

# ---------------------------------------------------------------------------
# 1) Runtime deps (declared, not vendored — these are system binaries).
# ---------------------------------------------------------------------------
PKG=""
if command -v brew  >/dev/null 2>&1; then PKG="brew install"
elif command -v apt-get >/dev/null 2>&1; then PKG="sudo apt-get install -y"
elif command -v winget  >/dev/null 2>&1; then PKG="winget install"; fi

need() {  # need <bin> <install-name> <required|optional>
  if command -v "$1" >/dev/null 2>&1; then
    say "$1 ok ($("$1" --version 2>&1 | head -1 | cut -c1-40))"
  else
    if [ "$3" = required ]; then
      warn "$1 MISSING — install with:  ${PKG:-<your package manager>} $2"
      MISSING=1
    else
      warn "$1 missing (optional) — ${PKG:-pkg} $2"
    fi
  fi
}
MISSING=0
say "Checking runtime…"
need ffmpeg  ffmpeg  required
need ffprobe ffmpeg  required
need node    node    required      # Node 20+ for the HyperFrames CLI
need npx     node    required
need python3 python  required
need yt-dlp  yt-dlp  optional       # only for downloading online sources
# Headless Chrome (HyperFrames renders through it):
if [ -d "/Applications/Google Chrome.app" ] || command -v google-chrome >/dev/null 2>&1 \
   || command -v chromium >/dev/null 2>&1; then say "chrome ok"
else warn "Chrome/Chromium not found — HyperFrames renders need it. Install Google Chrome."; fi
[ "${MISSING:-0}" = 1 ] && { warn "Install the required deps above, then re-run."; exit 1; }

# ---------------------------------------------------------------------------
# 2) video-use engine: its own Python venv + deps (the cut/transcribe/render code).
# ---------------------------------------------------------------------------
VU="$ROOT/skills/video-use"
say "Setting up the video-use engine venv…"
if command -v uv >/dev/null 2>&1; then ( cd "$VU" && uv venv --quiet && uv pip install -e . --quiet )
else python3 -m venv "$VU/.venv" && "$VU/.venv/bin/pip" install -q -e "$VU"; fi
say "engine ready: $VU/.venv"

# ---------------------------------------------------------------------------
# 3) Transcription key (ElevenLabs Scribe). Stored in the engine's .env.
# ---------------------------------------------------------------------------
ENV="$VU/.env"
if [ ! -f "$ENV" ] || ! grep -q ELEVENLABS_API_KEY "$ENV" 2>/dev/null; then
  printf "\nElevenLabs API key (transcription) — get one at elevenlabs.io/app/settings/api-keys\n"
  printf "Paste it (or press Enter to skip and add later to %s): " "$ENV"
  read -r KEY || true
  [ -n "${KEY:-}" ] && echo "ELEVENLABS_API_KEY=$KEY" >> "$ENV" && say "key saved to $ENV"
  [ -z "${KEY:-}" ] && warn "skipped — add ELEVENLABS_API_KEY=... to $ENV before transcribing"
else
  say "ElevenLabs key already set"
fi

# ---------------------------------------------------------------------------
# 4) HyperFrames CLI sanity (motion-graphics render path).
# ---------------------------------------------------------------------------
say "Checking HyperFrames render path…"
npx --yes hyperframes@0.6.70 doctor || warn "hyperframes doctor reported issues (see above)"

cat <<EOF

$(say "video-studio installed.")
  Skills:   $ROOT/skills  (video-studio orchestrator + video-use + hyperframes family)
  Engine:   $VU/.venv
  Template: $ROOT/templates/project  (copy it next to your footage)

Next: register the plugin with your agent (see README), then:
  cp -r "$ROOT/templates/project" ~/my-video && cd ~/my-video
  # drop clips into sources/, start your agent, say: "edit these into a 60s promo"
EOF
