# Recipe 3 - Website to promo (your landing page is the footage)

You have a live site and want a social ad or product tour without designing anything new. The engine captures your site - colors, fonts, screenshots, assets - and builds the video in your own brand.

## When to use this one

- A 15-30 second social ad for a product that already has a landing page
- A "product tour" video for a launch post
- You are making videos for clients: capture theirs, deliver same-day

## The method

1. **Capture.** In the engine project:
   ```bash
   npx hyperframes capture https://yoursite.com
   ```
   This pulls the palette, fonts, copy, and full-page screenshots into `capture/`.

2. **DESIGN.md from the capture.** Tell Claude Code: "Read the capture and write DESIGN.md: exact hex colors with roles, the two font families, and five things this brand would never do." The never-do list is what keeps the output from drifting generic.

3. **SCRIPT before storyboard.** Narration or on-screen text first - scene durations come from the words, not from guessing. 15s = ~35 spoken words. Silent + text-carried is the right default for feeds.

4. **Storyboard with the site's own assets.** Screenshots pan and zoom (the capture has them full-page), real UI elements slide in as cards, the brand's buttons become the CTA. Do not invent visuals the site does not have - the authenticity is the point.

5. **Build, check, render.** Same loop as Recipe 1: composition from the three docs, `npm run check` until clean, `npm run render`.

## Format targets

| Where | Size | Length |
|-------|------|--------|
| X / LinkedIn feed | 1920x1080 | 20-30s |
| Instagram / TikTok / Shorts | 1080x1920 | 15-30s |
| Product Hunt gallery | 1920x1080 | 30-60s |
| GitHub README | GIF 640px | 10-25s loop |

Render once per aspect ratio - reflow the layout in CSS, do not letterbox.

## The gotchas

- Capture before you write anything. Guessing brand colors from memory produces a video the owner does not recognize.
- Screenshots beat re-built UI. A real screenshot panning slowly reads as true; a rebuilt mock reads as an ad.
- One message per video. If the site has five features, that is five videos, not one long one.
