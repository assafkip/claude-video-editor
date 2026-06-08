# Catalog Intent Map — "User Says X → Install Y"

Used by `/make-a-video` Gate 5. Translates beginner language into `npx hyperframes add <block>` commands.

## The map

| User says… | Install |
|---|---|
| "title card / opener / kinetic type" | hand-build — registry has no kinetic-type block; see MOTION_PHILOSOPHY §3.3 |
| "logo reveal / outro / final card" | `logo-outro` |
| "film grain / texture on everything" | `grain-overlay` (component) |
| "shimmer on my logo / light glint" | `shimmer-sweep` (component) |
| "smooth transition / soft fade" | `transitions-blur` · `transitions-dissolve` |
| "energetic transition / fast cut / punchy" | `whip-pan` · `cinematic-zoom` · `glitch` |
| "cinematic transition / premium morph" | `cross-warp-morph` · `swirl-vortex` |
| "act break / dramatic flash" | `flash-through-white` · `light-leak` |
| "zoom-through text" | `cinematic-zoom` |
| "color change on same scene" | `chromatic-radial-split` — or hand-build the CSS-variable recolor in MOTION_PHILOSOPHY §3.5 |
| "phone showcase / mobile demo" | `app-showcase` |
| "3D UI reveal / perspective product" | `ui-3d-reveal` |
| "macOS notification popup" | `macos-notification` |
| "chart / data viz / bar graph" | `data-chart` |
| "flowchart / decision tree / node diagram" | `flowchart` |
| "grid tile transition / pixelate wipe" | `grid-pixelate-wipe` (component) · `transitions-grid` |
| "TikTok follow overlay" | `tiktok-follow` |
| "Instagram follow overlay" | `instagram-follow` |
| "YouTube subscribe lower-third" | `yt-lower-third` |
| "Twitter/X post card" | `x-post` |
| "Reddit post card" | `reddit-post` |
| "Spotify now-playing card" | `spotify-card` |
| "thermal / heat distortion" | `thermal-distortion` |
| "ripple / water / concentric waves" | `ripple-waves` |
| "iris / circular reveal" | `sdf-iris` |
| "domain warp / noise dissolve" | `domain-warp-dissolve` |
| "ridged burn / fire effect" | `ridged-burn` |
| "gravitational lens / warp" | `gravitational-lens` |

For the full catalog browse live with `npx hyperframes catalog --type block` and `npx hyperframes catalog --type component`.

---

## Install + wire workflow

1. **From inside the project folder:**
   ```bash
   npx hyperframes add <block-name>
   ```
2. **Block installs to** `<project>/compositions/<block-name>.html` (or `<project>/compositions/components/<name>.html` for components).
3. **Immediately scope its CSS.** Catalog blocks ship with top-level `html, body { ... }` rules. When loaded as a sub-composition via `data-composition-src`, those rules bleed into the parent document.
   - Open the installed file
   - Wrap the `html, body { ... }` rule under `[data-composition-id="<block-id>"]`
   - Do the same for any other un-scoped global rule
4. **Wire into `index.html`:**
   ```html
   <template
     data-composition-src="compositions/<block-name>.html"
     data-start="..."
     data-duration="..."
     data-track-index="..."></template>
   ```
5. **Apply the user's palette.** Most blocks accept CSS variables at the top of the file — find them and override with the user's hex codes from `style-profile.md`.

---

## Components vs. blocks

- **Blocks** are standalone sub-compositions — their own timeline, their own root `<div>`. Reference via `data-composition-src`. Examples: `logo-outro`, `app-showcase`, `tiktok-follow`.
- **Components** are snippets you merge *into* an existing composition's HTML. Paste the component's DOM + CSS + a slice of its script into the host composition. Examples: `grain-overlay`, `shimmer-sweep`, `grid-pixelate-wipe`.

The installer handles the distinction automatically; you mainly need to know which to reach for when planning the storyboard.

---

## When NOT to install

Catalog blocks buy production velocity. When you have time, hand-building hero moments (kinetic-type openers, logo reveals) usually looks better than installing a block — the MOTION_PHILOSOPHY reference spot installs **zero** blocks.

**Rule of thumb for this skill:**
- Transitions and social/UI overlays → install
- Hero opener and final CTA → hand-build unless the user is on a tight deadline
- Film grain and shimmer → always install (they're components, meant to be dropped in)

---

## Gotchas

- After installing a block, always run `npx hyperframes lint` — the installer can create `data-composition-id` collisions if you already have one with the same name.
- Blocks ship with their own fonts. If the user specified custom fonts in the style profile, override the block's font family with a scoped rule.
- Some blocks (notably `logo-outro`) expect specific asset filenames — read the installed file and rename / re-path to the user's logo.
- Shader blocks (the 14 shader transitions) use WebGL. In the Studio's software WebGL fallback, they can stall the master composition preview. Gate 7 routes users to individual composition URLs to work around this.
