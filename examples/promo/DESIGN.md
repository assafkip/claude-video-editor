# DESIGN.md — investor-recon launch video (worked example)

## Style Prompt
Cute neo-brutalist paper UI on warm cream. Thick ink borders, hard offset shadows, yellow marker highlights. A friendly, hand-built aesthetic with zero corporate gloss. The video dramatizes a real product screen (the VC Prep Brief), so the screen is the hero; motion is confident and snappy, never floaty.

## Colors
- `#fef7ec` cream — canvas background
- `#1a1a1a` ink — borders, text, hard shadows
- `#fffdf8` paper — card/frame background
- `#ffd23f` yellow — highlight marker, active toggle
- `#c0392b` red — the deal-killing objection row
- `#0a8f3c` green — counter row, "cites every claim" pill
- `#c98a00` amber — "Not found" honesty marker
- `#2f6df0` blue — citation chips
- `#6a6a6a` dim — secondary text

## Typography
- Bricolage Grotesque (600/700/800) — display, body
- JetBrains Mono (400/700) — labels, citations, brand

## Motion
- Snappy entrances: y+fade, power3.out / back.out(1.4) / expo.out, 0.45-0.7s
- The camera zoom is the one slow move: power2.inOut, 1.2s
- Hard shadows never animate independently of their card

## What NOT to Do
- No gradients, no glassmorphism, no dark mode
- No corporate blue, no Inter/Roboto
- No floaty 2s+ eases, no linear easing
- No element appears fully formed (entrances on everything)
