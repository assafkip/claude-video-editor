#!/usr/bin/env python3
"""Gate for cve-a2-stills-from-anywhere (finding 3).

Heading-aware checks on SKILL.md and README.md — structure-parsed, not
string-grep, so an early 'optional' word cannot hide violations:

SKILL.md:
  1. 'call-actor' and 'Apify MCP' appear nowhere.
  2. 'danitn11' and 'apify' (case-insensitive) appear ONLY in sections whose
     heading contains 'optional' (frontmatter and pre-heading text count as
     non-optional).
  3. A 'stills from anywhere' section exists and lists at minimum:
     AI image tools, screenshots/photos, HyperFrames-rendered HTML.

README.md:
  4. The '## What you need' section does not mention Apify, and the README
     states Node >= 22 for the HyperFrames CLI.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # skills/generate-footage
SKILL = ROOT / "SKILL.md"
README = ROOT.parent.parent / "README.md"

failures = []

HEADING_RE = re.compile(r"^#{1,6}\s+\S")
OPTIONAL_HEADING_RE = re.compile(r"^#{1,6}\s*optional\b", re.IGNORECASE)

def sections(text: str):
    """Yield (heading_or_None, body) pairs. Text before the first heading
    (including YAML frontmatter) gets heading=None. Lines inside fenced
    code blocks are never headings."""
    heading = None
    buf = []
    in_fence = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            buf.append(line)
            continue
        if not in_fence and HEADING_RE.match(line):
            yield heading, "\n".join(buf)
            heading = line
            buf = []
        else:
            buf.append(line)
    yield heading, "\n".join(buf)

def is_optional_heading(heading) -> bool:
    """True only for headings that START with 'Optional' (after #'s) —
    'Not optional: ...' or 'Optionality caveat' do not qualify."""
    return heading is not None and bool(OPTIONAL_HEADING_RE.match(heading))

skill_text = SKILL.read_text()

# 1. hard bans anywhere
for banned in ("call-actor", "Apify MCP"):
    if banned.lower() in skill_text.lower():
        failures.append(f"SKILL.md contains banned string {banned!r}")

# 2. apify/danitn11 only under headings that START with 'Optional'
for heading, body in sections(skill_text):
    in_optional = is_optional_heading(heading)
    for word in ("apify", "danitn11"):
        if word in body.lower() and not in_optional:
            failures.append(
                f"SKILL.md: {word!r} appears under non-optional heading {heading!r}"
            )

# 3. stills-from-anywhere section content
sfa = None
for heading, body in sections(skill_text):
    if heading and "stills from anywhere" in heading.lower():
        sfa = body
        break
if sfa is None:
    failures.append("SKILL.md: no 'stills from anywhere' section heading")
else:
    for needle, label in (
        ("ai image tools", "AI image tools"),
        ("screenshots", "screenshots"),
        ("photos", "photos"),
        ("hyperframes-rendered html", "HyperFrames-rendered HTML"),
    ):
        if needle not in sfa.lower():
            failures.append(f"SKILL.md stills section missing {label!r}")

# 4. README: What-you-need without Apify; Node >= 22 stated
readme_text = README.read_text()
wyn = None
for heading, body in sections(readme_text):
    if heading and "what you need" in heading.lower():
        wyn = body
        break
if wyn is None:
    failures.append("README.md: no 'What you need' section")
else:
    if "apify" in wyn.lower():
        failures.append("README.md 'What you need' still mentions Apify")
    if not re.search(r"node(\.js)?\s*(>=\s*)?2[2-9]\+?", wyn, re.IGNORECASE):
        failures.append("README.md 'What you need' does not state Node >= 22")

if failures:
    for f in failures:
        print(f"FAIL: {f}")
    sys.exit(1)
print("PASS: SKILL.md structure clean (apify optional-only), stills-from-anywhere complete, README requirements updated")
