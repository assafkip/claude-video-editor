# STORYBOARD.md — recon demo video

Single continuous scene, one camera. The product screen (VC Prep Brief) is the set; the camera and a cursor are the actors. 1920x1080@30, 25s, silent.

## Beats
1. **HOOK (0-2.5s).** Cream canvas. Setup line drops in top-center, yellow marker sweeps "before you walk in." Frame card pops in below (scale 0.94->1, back.out), title bar + pill + toggle visible, "Walk in blind" active (yellow).
2. **BLIND (2.5-6.5s).** Blind panel: tagline-and-a-guess copy, the guess line blurred. Payoff line under frame: "This is what most founders walk in with. A tagline and a guess."
3. **TURN (6-7.5s).** Ink cursor dot flies to "With investor-recon", click-dip, toggle flips (yellow swaps buttons), blind panel drops out, payoff line crossfades to "The side that did the homework runs the room. Make it you."
4. **REVEAL (7.5-14s).** Rows enter one at a time (one new thing at a time), varied eases: thesis (7.6), fit (9.0), KILL red (10.5, slight shake on land), counter green (11.9), honesty (13.1).
5. **ZOOM (14.2-19.2s).** Camera (whole wrap) scales 1.5, transform-origin on the kill row. Non-kill rows dim to 0.45. Kill row border pulses red twice (finite repeat). Hold ~2.5s. Zoom back out 1.0s.
6. **CTA (19.6-25s).** Only allowed exit: wrap fades + drifts down. End card enters: "investor-recon" (mono 800), "The side that did the homework runs the room. Make it you.", "free · six prompts · ~25 min per investor", "github.com/assafkip/investor-recon". Final frame holds >=1.5s.

## Asset audit
| Asset | Source | Status |
|-------|--------|--------|
| Brief copy + design tokens | investor-recon demo brief page | in hand |
| Fonts | Google Fonts (Bricolage Grotesque, JetBrains Mono) | embedded by compiler |
| Cursor | CSS div | build |

No external media. No audio track.
