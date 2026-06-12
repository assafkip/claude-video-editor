# Claude video editor

**Use Claude to edit videos and add captions — or generate a video from nothing.**
Drop your footage in a folder, tell Claude what you want, get `final.mp4` back.
No timeline, no menus, no presets.

> edit these into a 60-second promo with lower-third captions, no voiceover

> research the Stonehenge bluestone debate and make me a narrated explainer

![Demo: the opening of a 2:46 research explainer made entirely with this plugin](docs/demo.gif)

*This whole video — 16 painted scenes, documentary camera moves, atmosphere, the storytelling voiceover, 51 timed captions — was made by talking to Claude with this plugin. No camera, no timeline, no video-generation service: still keyframes animated deterministically with the [animate-stills recipe](recipes/04-animate-stills.md), narration by ElevenLabs v3. First 14 seconds above, silent; [watch the full video with sound](docs/demo.mp4).*

## What it can do
- **Cut** filler words (`umm`, `uh`), false starts, and dead space between takes
- **Captions** — burned-in subtitles or animated lower-thirds, in your style
- **Color grade** every segment (cinematic, neutral, or a custom look)
- **Motion graphics** — title cards, callouts, kinetic text, audio-reactive bits, scene transitions (HTML + GSAP, rendered with transparency)
- **Speed ramps** for slow stretches
- **Transcribe** any video to word-level text
- **Turn a website into a video** (capture a URL, animate it)
- **Build videos from stills** — narration-first explainers from keyframes you source ANYWHERE (AI image tools, screenshots, photos, HTML the engine renders itself), animated deterministically with camera moves + atmosphere; expressive ElevenLabs v3 narration with audio tags
- Works for anything: talking heads, tutorials, montages, promos, shorts, travel, interviews, fully generated explainers

Claude never watches the video frame by frame. It **reads** it (transcript + on-demand
timeline previews), so it cuts on word boundaries and stays cheap and fast. It proposes
a cut, waits for your OK, renders, checks every cut for jumps and audio pops, then shows
you the result.

## What you need

No keys or accounts ship with this repo. Everything below is yours, stored locally, and gitignored.

**Tools** (install.sh checks all of these):

| Tool | Used for |
|---|---|
| `ffmpeg` | every cut, mux, and export |
| Node 22+ | the HyperFrames CLI (`npx hyperframes`) |
| Google Chrome | headless rendering of compositions |
| Python 3.10+ | the video-use engine + helper scripts |

**Keys and accounts:**

| Key | Needed for | Where it lives | Cost |
|---|---|---|---|
| [ElevenLabs API key](https://elevenlabs.io/app/settings/api-keys) | transcription (editing) and v3 voiceover (generation) | `$ELEVENLABS_API_KEY` env var, or `skills/video-use/.env` — local only, gitignored | free tier covers transcription; v3 TTS uses plan credits |

That's the only key. Still keyframes for generated videos come from any image
source you already use (AI image tools, screenshots, photos, or HTML the
engine renders itself) — see the generate-footage skill.

## Install
```bash
git clone https://github.com/assafkip/claude-video-editor && cd claude-video-editor
./install.sh
```
`install.sh` checks the prereqs (`ffmpeg`, Node 22+, headless Chrome, Python), sets up
the engine, and asks once for an [ElevenLabs key](https://elevenlabs.io/app/settings/api-keys)
(used for transcription and v3 voiceover). The key is written to a local `.env` that git ignores — verify with `git check-ignore skills/video-use/.env`.

Then register it with Claude Code:
```bash
/plugin marketplace add ./           # from the repo dir
/plugin install claude-video-editor
```

## Use
```bash
cp -r templates/project ~/my-video && cd ~/my-video
# drop clips into sources/, open Claude Code, then:
```
> edit these into a launch video

Outputs land in `edit/`. Your session is remembered in `project.md` so next time picks
up where you left off.

## What's inside
Three open-source layers plus a generation layer, bundled to work together:
- [**video-use**](https://github.com/browser-use/video-use) — the cutting engine (transcribe, cut, grade, subtitle, render)
- [**HyperFrames**](https://github.com/heygen-com/hyperframes) — the motion-graphics engine (HTML + GSAP overlays)
- [**hyperframes-student-kit**](https://github.com/nateherkai/hyperframes-student-kit) — motion-design examples and craft
- **generate-footage** — narration-first videos from still keyframes (sourced from any image tool, screenshots, or the engine's own HTML renders), animated deterministically with HyperFrames camera moves + atmosphere, ElevenLabs v3 voiceover with audio tags

## Recipes & worked examples
Step-by-step production recipes and the real project files behind them ship in the repo:
- [`recipes/`](recipes/) — three worked methods: a launch video from pure HTML, a tutorial edit from a screen recording, and a website-to-promo capture.
- [`examples/promo/`](examples/promo/) — the complete project behind a real launch video: DESIGN, SCRIPT, STORYBOARD, the HyperFrames composition, and vendored fonts. Pattern-match it; don't start from a blank file.
- [`examples/captions/`](examples/captions/) — the caption-overlay composition and render commands from the tutorial recipe.

## License

**Use it, modify it, share it — don't sell it.** The code in this repo is
[MIT + Commons Clause](LICENSE): all MIT freedoms except the right to sell the
software itself. Using it to make videos — including paid client work and
commercial videos for your own business — is permitted use, not a sale.

Vendored components keep their own upstream licenses (see `LICENSES/`):
video-use, HyperFrames, and hyperframes-student-kit. Nothing here changes
their terms.

---

## Built by Assaf Kipnis

Built and released free. Issues and PRs welcome.
