# video-studio

**Edit any video by conversation.** Drop footage in a folder, tell your agent what you
want, get `final.mp4` back. A self-contained Claude Code plugin that bundles three
layers into one pipeline — no presets, no menus, no timeline-scrubbing.

```
Transcribe ─▶ Pack ─▶ LLM reasons ─▶ EDL ─▶ Render ─▶ Self-eval
                                                          └─ issue? fix + re-render
```

The LLM never watches the video. It **reads** it — transcript + on-demand timeline
PNGs — so it cuts on word boundaries instead of drowning in frames.

## What's bundled (the three layers)
| Layer | Skills | Does |
|-------|--------|------|
| **Cut engine** | `video-use` | transcribe, cut filler/dead-space, color grade, audio fades, subtitle burn, the render composite |
| **Motion** | `hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `gsap`, `website-to-hyperframes` | HTML+GSAP overlays rendered through headless Chrome to alpha `.mov` |
| **Craft** | `make-a-video`, `short-form-video`, `docs/MOTION_PHILOSOPHY.md` | storyboard, brand system, pacing, taste |
| **Orchestrator** | `video-studio` | routes between them; the standard edit loop |

Upstreams (vendored, with licenses in `LICENSES/`): [video-use](https://github.com/browser-use/video-use)
· [HyperFrames](https://github.com/heygen-com/hyperframes) · [hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit).

## Install
```bash
git clone <this-repo> video-studio && cd video-studio
./install.sh          # checks ffmpeg/node/chrome, sets up the engine venv, prompts for the key
```
Then register it with your agent:
- **Claude Code (plugin):** add this dir as a plugin marketplace → `/plugin marketplace add <path>` then `/plugin install video-studio`. Skills auto-load.
- **Or symlink the skills** into your agent's skills dir: `ln -sfn "$PWD/skills/"* ~/.claude/skills/`.

**Runtime prereqs** (declared, not bundled — `install.sh` checks them): `ffmpeg`,
Node 20+, headless Chrome, `python3`, an ElevenLabs API key (transcription). `yt-dlp`
optional for online sources.

## Use
```bash
cp -r templates/project ~/my-video && cd ~/my-video
# drop clips into sources/, start your agent, then:
```
> edit these into a 60-second promo with lower-third captions, no voiceover

It inventories the sources, proposes a cut, waits for your OK, renders to
`edit/final.mp4`, self-evaluates every cut boundary, and persists the session in
`project.md`.

## Why bundle it
Three repos that already compose, packaged as one installable, shareable unit. Clone
once, run `install.sh`, edit anything — talking heads, montages, tutorials, promos,
shorts. See `skills/video-studio/SKILL.md` for the loop and the hard rules.

## License
This bundle: MIT. Vendored components retain their own licenses — see `LICENSES/`.
