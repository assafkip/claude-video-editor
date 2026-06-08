# video-studio

**Use Claude to edit videos and add captions.** Drop your footage in a folder, tell
Claude what you want, get `final.mp4` back. No timeline, no menus, no presets.

> edit these into a 60-second promo with lower-third captions, no voiceover

## What it can do
- **Cut** filler words (`umm`, `uh`), false starts, and dead space between takes
- **Captions** — burned-in subtitles or animated lower-thirds, in your style
- **Color grade** every segment (cinematic, neutral, or a custom look)
- **Motion graphics** — title cards, callouts, kinetic text, audio-reactive bits, scene transitions (HTML + GSAP, rendered with transparency)
- **Speed ramps** for slow stretches
- **Transcribe** any video to word-level text
- **Turn a website into a video** (capture a URL, animate it)
- Works for anything: talking heads, tutorials, montages, promos, shorts, travel, interviews

Claude never watches the video frame by frame. It **reads** it (transcript + on-demand
timeline previews), so it cuts on word boundaries and stays cheap and fast. It proposes
a cut, waits for your OK, renders, checks every cut for jumps and audio pops, then shows
you the result.

## Install
```bash
git clone https://github.com/<you>/video-studio && cd video-studio
./install.sh
```
`install.sh` checks the prereqs (`ffmpeg`, Node 20+, headless Chrome, Python), sets up
the engine, and asks once for an [ElevenLabs key](https://elevenlabs.io/app/settings/api-keys)
(used for transcription).

Then register it with Claude Code:
```bash
/plugin marketplace add ./           # from the repo dir
/plugin install video-studio
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
Three open-source layers, bundled to work together:
- [**video-use**](https://github.com/browser-use/video-use) — the cutting engine (transcribe, cut, grade, subtitle, render)
- [**HyperFrames**](https://github.com/heygen-com/hyperframes) — the motion-graphics engine (HTML + GSAP overlays)
- [**hyperframes-student-kit**](https://github.com/nateherkai/hyperframes-student-kit) — motion-design examples and craft

Each keeps its own license (see `LICENSES/`). This bundle is MIT.
