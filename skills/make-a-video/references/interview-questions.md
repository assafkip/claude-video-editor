# Interview Questions — Full Bank

Used by `/make-a-video` Gates 1–3. Ask one at a time via `AskUserQuestion`, multiple-choice where possible.

## Before asking anything — inventory first

Run these to see what already exists so you don't ask for supplied assets:

```bash
ls "<workspace-root>/assets" 2>/dev/null
ls "<project-folder>/assets" 2>/dev/null
```

Reference anything you find by path in the eventual `BRIEF.md`.

---

## Gate 1 · Intent & format

**Q1. What's this video for?**
- Promo / marketing video
- Social ad (TikTok · Reels · Shorts · X)
- Launch teaser
- Product demo
- Tutorial
- Explainer
- Intro / outro card
- Other (describe)

**Q2. Who's the audience?** (open-ended)
Probe: industry · expertise level · platform they'll watch on · what should they feel

**Q3. Target duration?**
- Short — 10–20s
- Promo — 20–45s
- Explainer — 45–90s
- Lesson — 1.5–3 min
- Custom — ask for a number

**Q4. Aspect ratio?**
- 16:9 landscape — 1920×1080
- 9:16 vertical — 1080×1920
- 1:1 square — 1080×1080

**Q5. Frame rate?**
- 30 fps (default, good for everything)
- 60 fps (crisp UI, product demos, game footage)
- 24 fps (cinematic)

**Q6. Platform / delivery constraints?**
- Where will it play? (site hero · TikTok · LinkedIn · YouTube · internal deck · other)
- File-size ceiling?
- Deadline?

---

## Gate 2 · Script & voice

**Q7. Script source?**
- Paste the full script now
- I have an outline — draft the full script for me
- I'll record it myself (need path to voiceover or face-cam file)
- Generate TTS narration from text
- No narration — visuals + music only

**Q8. If TTS:**
- Voice choice (offer from `npx hyperframes tts --help`). Common: `am_adam`, `am_michael` (male US) · `af_bella`, `bf_emma` (female US/UK)
- Speaking pace (normal · slightly faster · slightly slower)

**Q9. If face-cam or recorded voiceover:**
- File path
- Full-screen or corner? (bottom-right · bottom-left · top-right · top-left)
- Need transcription? If yes: `npx hyperframes transcribe <file> --model small.en --json`

**Q10. Captions?**
- Off
- On — hype (bold, punchy, colored accent words)
- On — corporate (clean, single-line, no emphasis)
- On — karaoke (per-word sync, reveal as spoken)
- On — minimal (single sub-line, low contrast)

---

## Gate 3 · Style intake

**Q11. Style guide or brand document?**
- Yes — paste or give path (look for hex codes, fonts, logo rules, spacing rules)
- No

**Q12. Color palette?**
- Paste hex codes. Ask for at least: background · text/primary · accent (the "emotion" color). Optional: surface · border · warn.
- None — use MOTION_PHILOSOPHY defaults (see `style-intake.md`)

**Q13. Fonts?**
- Google Fonts names (e.g. Inter · Montserrat · JetBrains Mono · Bebas Neue · Space Grotesk)
- Font file paths
- None — use Inter + JetBrains Mono defaults

**Q14. Logo file?**
- Path to file
- None — text wordmark instead? Ask for the text and weight/style

**Q15. Reference videos?**
- URLs or file paths — "the vibe I want"
- None

**Q16. Other assets?**
- Screenshots (paths)
- Product photos (paths)
- B-roll clips (paths)
- Music tracks (paths)
- Any SVGs / icons / illustrations (paths)

**Q17. MOTION_PHILOSOPHY aesthetic or different feel?**
- MOTION_PHILOSOPHY: black canvas · chrome-gradient type · perspective grid · whip-pan transitions · 4–6s outro hold
- Different — describe or give references

**Q18. Pacing?**
- Kinetic — 1–2s scenes, energetic (reference-quality motion graphics)
- Balanced — 2–3s scenes (most promos)
- Relaxed — 3–5s scenes (explainers · lessons · luxury feel)

**Q19. Music?**
- None (silence)
- Ambient pad — `data-volume="0.15"` (premium, barely there)
- Music bed — `data-volume="0.4"` (standard promo layer)
- Full music — `data-volume="0.8"` (music-driven edit)
- File path if they have one

**Q20. Outro / call-to-action text?**
- CTA line (e.g. "Get started at example.com")
- Hold duration (4–6s recommended — the longest shot in the whole video)

---

## Sequencing rules

- **One question per `AskUserQuestion` call.** Don't batch. The user can't focus on three questions at once.
- **Multiple-choice over open-ended** when the answer has discrete valid forms.
- **Follow-ups happen inline.** If Q7 = "record it myself," the next question is Q9 (not Q8).
- **Capture every answer to the brief as you go** — short phrases, not full sentences. The `BRIEF.md` at Gate 4 is a synthesis, not a transcript.
- **If an answer is surprising** (e.g. "I want a 4-hour TikTok ad"), confirm before proceeding. Don't assume.
- **Never ask for what's already known.** If the user mentioned a file path earlier or it's sitting in `assets/`, skip that question and just confirm the interpretation.
