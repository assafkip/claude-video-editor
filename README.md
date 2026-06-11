# Claude video editor

**Use Claude to edit videos and add captions — or generate a video from nothing.**
Drop your footage in a folder, tell Claude what you want, get `final.mp4` back.
No timeline, no menus, no presets.

> edit these into a 60-second promo with lower-third captions, no voiceover

> make me a 90-second anime-style explainer with an excited voiceover

## What it can do
- **Cut** filler words (`umm`, `uh`), false starts, and dead space between takes
- **Captions** — burned-in subtitles or animated lower-thirds, in your style
- **Color grade** every segment (cinematic, neutral, or a custom look)
- **Motion graphics** — title cards, callouts, kinetic text, audio-reactive bits, scene transitions (HTML + GSAP, rendered with transparency)
- **Speed ramps** for slow stretches
- **Transcribe** any video to word-level text
- **Turn a website into a video** (capture a URL, animate it)
- **Generate footage from prompts** — AI keyframes (text-to-image), animated clips (Wan 2.2 image-to-video), expressive ElevenLabs v3 narration with audio tags; an 8-scene 85s video costs ~$3 in generation (needs an [Apify](https://apify.com) account for the image/video models)
- Works for anything: talking heads, tutorials, montages, promos, shorts, travel, interviews, fully generated explainers

Claude never watches the video frame by frame. It **reads** it (transcript + on-demand
timeline previews), so it cuts on word boundaries and stays cheap and fast. It proposes
a cut, waits for your OK, renders, checks every cut for jumps and audio pops, then shows
you the result.

## Install
```bash
git clone https://github.com/assafkip/claude-video-editor && cd claude-video-editor
./install.sh
```
`install.sh` checks the prereqs (`ffmpeg`, Node 20+, headless Chrome, Python), sets up
the engine, and asks once for an [ElevenLabs key](https://elevenlabs.io/app/settings/api-keys)
(used for transcription).

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
- **generate-footage** — AI keyframes + image-to-video clips (via Apify actors) and ElevenLabs v3 voiceover with audio tags, for videos built from prompts instead of recordings

Each keeps its own license (see `LICENSES/`). This bundle is MIT.

---

## Built by Assaf

The demo video on [claudedaddy.io](https://claudedaddy.io) was made with this editor, by typing sentences.

The engine here is free and stays free. **[The Launch Video Kit ($49)](https://claudedaddy.gumroad.com/l/launch-video-kit)** adds the production system around it: three recipes (launch video from pure HTML, tutorial edit from a screen recording, website-to-promo), the worked templates behind the demo video, and a one-paste setup that installs everything for you.

More tools at [claudedaddy.io](https://claudedaddy.io).
