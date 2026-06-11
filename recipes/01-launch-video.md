# Recipe 1 - The launch video (no footage needed)

Build a product launch video from nothing but HTML. This is the recipe behind a real, shipped launch video; the exact project that produced it ships in `examples/promo/`. Type-to-video, deterministic, renders the same every time.

## When to use this one

You have a product but no footage. No screen recording, no talking head. You want a 20-30 second autoplay video for X, a landing page, Show HN, or Product Hunt.

## The method (one sitting, ~1-2 hours with Claude)

1. **DESIGN.md first.** Your colors, fonts, motion rules, and a "what NOT to do" list. Steal the structure from `examples/promo/DESIGN.md`. Without this, every AI-generated composition drifts to generic startup blue.

2. **SCRIPT.md - silent, text-carried.** Social feeds autoplay muted. Write the story as on-screen text beats with timestamps, not narration. The arc that works for product videos: **problem state -> the turn -> the reveal cascade -> zoom on the one detail that matters -> CTA card.**

3. **STORYBOARD.md - one continuous scene.** Skip scene cuts. Make the product screen the set, and a cursor + a camera the actors. A zoom reads as product; cuts read as ad. See `examples/promo/STORYBOARD.md` for the beat structure.

4. **Build the composition.** Tell Claude Code: "Build the HyperFrames composition from these three docs, using examples/promo/index.html as the pattern." The template shows the working shapes: ground-state `tl.set()` at t=0, entrance-only animation, a camera div with `transform-origin` on the zoom target, a fake cursor click, the end card.

5. **Check, then render.** `npm run check` until clean, `npm run render` for the MP4.

6. **Self-review with the contact sheet.** `npx hyperframes snapshot .` makes a 5-frame contact sheet. Look at it before you publish. You are checking: text overflow, wrong font fallback, elements visible before their entrance, the zoom framing.

7. **GIF derivative** for READMEs and posts that want a loop:
   ```bash
   ffmpeg -i render.mp4 -vf "fps=10,scale=640:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4" out.gif
   ```

## The gotchas that cost me renders

- **Vendor your fonts.** Google Fonts links fail in the sandboxed renderer and your type silently falls back to a generic font. Download the woff2 files and use `@font-face` (see the template's `assets/fonts/`).
- **Camera zooms trigger overflow errors.** The layout inspector flags content pushed off-canvas by the zoom. That is intentional - mark the camera container with `data-layout-allow-overflow`.
- **Hide future elements with `tl.set(..., 0)`,** not CSS. The CSS state is the layout ground truth; the timeline owns visibility.
- **Never `repeat: -1`.** Infinite loops break the capture engine. Compute finite repeats.
- **One new thing on screen at a time.** The eye cannot track two reveals at once.
