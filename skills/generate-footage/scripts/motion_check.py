#!/usr/bin/env python3
"""motion_check.py — prove a rendered video actually moves.

Samples frame pairs (grayscale, downscaled) via ffmpeg inside [t1, t2] and
computes mean absolute pixel difference per pair. A composition that rendered
stills (broken timeline, paused playback, dead GSAP) produces near-zero
diffs; real camera motion over a still produces clearly positive diffs.

The gate is the MEDIAN of the sampled pair diffs, which resists one-off
spikes from caption toggles, fades, or compression flicker. Pick t1/t2
inside ONE scene window so scene cuts cannot fake motion.

Usage:
    python3 motion_check.py video.mp4 --t1 1.0 --t2 5.0 --min-diff 3 [--samples 3]

Exit 0: median pair diff > min-diff (motion proven).
Exit 1: below threshold (stills, or timestamps sit in a hold).
Exit 2: extraction failed (bad file, timestamp beyond duration) — ffmpeg
        stderr is included in the message.

Stdlib + ffmpeg only.
"""
import argparse
import statistics
import subprocess
import sys

SIZE = 160  # comparison resolution (SIZE x SIZE gray)


def frame_bytes(video: str, t: float) -> bytes:
    cmd = [
        "ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", video,
        "-frames:v", "1", "-vf", f"format=gray,scale={SIZE}:{SIZE}",
        "-f", "rawvideo", "-",
    ]
    proc = subprocess.run(cmd, capture_output=True)
    if proc.returncode != 0 or len(proc.stdout) != SIZE * SIZE:
        err = proc.stderr.decode(errors="replace").strip()
        print(f"FAIL: could not extract frame at t={t}s "
              f"(rc={proc.returncode}, got {len(proc.stdout)} bytes, "
              f"expected {SIZE * SIZE}). ffmpeg: {err or 'no stderr'}")
        sys.exit(2)
    return proc.stdout


def pair_diff(video: str, ta: float, tb: float) -> float:
    a = frame_bytes(video, ta)
    b = frame_bytes(video, tb)
    return sum(abs(x - y) for x, y in zip(a, b)) / len(a)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--t1", type=float, required=True)
    ap.add_argument("--t2", type=float, required=True)
    ap.add_argument("--min-diff", type=float, default=3.0)
    ap.add_argument("--samples", type=int, default=3,
                    help="frame pairs sampled across [t1, t2] (default 3)")
    args = ap.parse_args()

    if args.t2 <= args.t1:
        print("FAIL: --t2 must be greater than --t1")
        return 2
    n = max(1, args.samples)
    span = args.t2 - args.t1
    diffs = []
    for k in range(n):
        ta = args.t1 + span * k / (n + 1)
        tb = args.t1 + span * (k + 2) / (n + 1)
        d = pair_diff(args.video, ta, tb)
        diffs.append(d)
        print(f"  pair {k + 1}: t={ta:.2f}s vs t={tb:.2f}s -> diff {d:.2f}")

    med = statistics.median(diffs)
    if med > args.min_diff:
        print(f"PASS: median gray diff {med:.2f} > {args.min_diff} "
              f"across {n} pairs in [{args.t1}, {args.t2}]s — real motion")
        return 0
    print(f"FAIL: median gray diff {med:.2f} <= {args.min_diff} — "
          f"frames are (near-)identical, render may be stills")
    return 1


if __name__ == "__main__":
    sys.exit(main())
