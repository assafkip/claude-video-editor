#!/usr/bin/env python3
"""
tts_v3.py — ElevenLabs eleven_v3 narration with audio-tag support.

Part of the generate-footage skill. Stdlib only, no pip deps.
Key resolution order:
  1. $ELEVENLABS_API_KEY
  2. <plugin>/skills/video-use/.env  (written by install.sh)

Usage:
  python3 tts_v3.py --probe                                  # models + voices
  python3 tts_v3.py --voice <voice_id> --stability 0.0 \
                    --script SCRIPT.md --out narration.mp3   # generate

Audio tags ([excited], [whispers], [shouts], [dramatic tone], [softly],
[warmly]) go directly in the script text — eleven_v3 performs them.
Stability: 0.0 Creative (max expressiveness), 0.5 Natural, 1.0 Robust.
"""
import argparse, json, os, sys, urllib.request, urllib.error

API = "https://api.elevenlabs.io/v1"


def load_key():
    v = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if v:
        return v
    env_path = os.path.normpath(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "..", "video-use", ".env"))
    if os.path.exists(env_path):
        for line in open(env_path):
            line = line.strip()
            if line.startswith("ELEVENLABS_API_KEY="):
                v = line.split("=", 1)[1].strip().strip('"').strip("'")
                if v:
                    return v
    sys.exit("no ELEVENLABS_API_KEY in env or skills/video-use/.env")


def get(path, key):
    req = urllib.request.Request(API + path, headers={"xi-api-key": key})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def probe(key):
    models = get("/models", key)
    has_v3 = any(m.get("model_id") == "eleven_v3" for m in models)
    print("=== models ===")
    for m in models:
        print(f"  {m.get('model_id','?'):32s} | {m.get('name','')}")
    print(f"\neleven_v3 available: {has_v3}")
    voices = get("/voices", key).get("voices", [])
    print(f"\n=== {len(voices)} voices ===")
    for v in voices:
        lab = v.get("labels", {}) or {}
        print(f"  {v.get('voice_id')} | {v.get('name')} | "
              f"{lab.get('gender','?')}/{lab.get('accent','?')}/{lab.get('description','?')}")


def synth(key, voice, model, script_path, out_path, stability):
    text = open(script_path).read().strip()
    body = json.dumps({
        "text": text,
        "model_id": model,
        "voice_settings": {"stability": stability, "similarity_boost": 0.75},
    }).encode()
    url = f"{API}/text-to-speech/{voice}?output_format=mp3_44100_128"
    req = urllib.request.Request(
        url, data=body,
        headers={"xi-api-key": key, "Content-Type": "application/json",
                 "Accept": "audio/mpeg"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"TTS failed {e.code}: {e.read().decode()[:400]}")
    open(out_path, "wb").write(data)
    print(f"wrote {out_path} ({len(data)} bytes) model={model} voice={voice} stability={stability}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", action="store_true")
    ap.add_argument("--voice", default="JBFqnCBsd6RMkjVDRZzb")  # George — warm storyteller
    ap.add_argument("--model", default="eleven_v3")
    ap.add_argument("--script", default="SCRIPT.md")
    ap.add_argument("--out", default="narration.mp3")
    ap.add_argument("--stability", type=float, default=0.5)
    a = ap.parse_args()
    key = load_key()
    if a.probe:
        probe(key)
        return
    synth(key, a.voice, a.model, a.script, a.out, a.stability)


if __name__ == "__main__":
    main()
