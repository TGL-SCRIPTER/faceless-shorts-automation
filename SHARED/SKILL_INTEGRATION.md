# Faceless Shorts skill integration

This repository uses the user's separately installed `faceless-shorts` skill as its production reference. The ZIP was inspected; it is not copied into this public repository.

## Six-style catalogue with mandatory 2D adaptation

All six skill styles may be used, but the final output must be genuine 2D animation. For styles originally designed around 3D, preserve their mood, composition, pacing, storytelling devices, palettes, and visual identity while rebuilding every scene as 2D artwork and 2D motion.

### Native 2D styles
- `inside-out`: flat 2D illustrated explainers with simple characters and cutaway diagrams.
- `stick-story`: 2D stick figures, illustrated rooms, and step cards.
- `paper-atlas`: 2D cut-paper scenes, maps, timelines, and period figures.

### Styles requiring 2D conversion
- `deep-dive`: convert cinematic 3D documentary visuals into layered 2D illustrations, drawn environments, parallax made from flat layers, animated diagrams, and hand-drawn details. No 3D underwater or other 3D scenes.
- `night-file`: convert 3D mystery visuals into 2D illustrated noir scenes, flat silhouettes, textured backgrounds, graphic shadows, maps, documents, and 2D camera pans. No 3D sets or volumetric effects.
- `tall-tale`: convert 2D-character/3D-world scenes into fully illustrated 2D characters and fully 2D backgrounds, with flat perspective, layered depth, and 2D transitions. No 3D world.

## Non-negotiable 2D test

Allowed: hand-drawn or vector 2D artwork, flat shapes, 2D compositing, layered parallax using flat artwork, 2D camera pans/zooms, frame-by-frame animation, cut-paper animation, and 2D motion graphics.

Not allowed: 3D models, 3D geometry, 3D-rendered frames, 3D environments, 3D camera scenes, or a 3D scene merely rendered to look flat. A style name never overrides this rule. If a template cannot be adapted cleanly, redesign it as original 2D artwork or choose another style.

## Production workflow from the skill

1. Read the selected style's complete `STYLE.md` and inspect its example project before planning.
2. If the selected style is one of the three conversion styles, write a 2D conversion plan before production: original visual elements to preserve, 2D replacements, and a check confirming no 3D assets remain.
3. Plan the title, conversational narration, cut-by-cut shot list, caption chunks, sources, and new components. Keep the three-agent uniqueness rules in force.
4. For a new project, use the skill's `new_video.sh` with the selected style only after verifying the template can produce compliant 2D output; adapt `script.json` and `src/shots.js` as needed.
5. The skill supports local Kokoro TTS, Whisper word timing, estimated timing for captions-only drafts, FFmpeg audio mixing, headless Chrome capture, and MP4 rendering.
6. Run visual/audio checks and inspect the contact sheet and key frames. A render is not complete until reviewed for genuine 2D output.

## Voice and agent separation

The skill's local Kokoro voice presets are examples, not a guarantee of three distinguishable voices. Each agent must record the actual voice provider and preset used. Claude and OpenCode must not share a voice; prefer three clearly distinct voices. If an agent cannot use a different voice, mark the batch as blocked rather than silently duplicating a voice.

## Environment and cost notes

The skill describes a no-API-key local workflow, but it is not zero-effort or guaranteed to work on every machine. Its setup checks Node.js 22+, FFmpeg, Chrome, and Python 3.10+; it creates a Python environment and downloads Kokoro model files (about 340 MB) and a Whisper model (about 0.5 GB), plus Python packages. Rendering speed depends heavily on GPU availability. Do not run setup scripts, install packages, download models, or modify the user's machine without explicit approval. No paid service or API key may be introduced without approval.

## Content and rights checks

Use original narration and shots. Verify factual claims and record reliable sources. For health topics, be accurate and avoid gore or frightening misinformation. For real cases, treat people respectfully and avoid unsupported accusations. The skill's examples and included assets are references, not permission to copy third-party creators' work or reuse assets without checking their licences.

## Project-specific override

Repository rules take precedence whenever stricter than the skill: exactly three agent outputs, genuine 2D only, cross-agent topic/angle/hook/story/style uniqueness, different voices, source names (not URLs) in the public description, and a coordinator-only all-three upload gate. Agents must never upload individually.
