# Faceless Shorts skill integration

This repository's production reference is the user's separately installed `faceless-shorts` skill. The ZIP was inspected; it is not copied into this public repository.

## Approved style whitelist (strict 2D)

Use only these three styles from the skill:
- `inside-out`: flat 2D illustrated explainers with simple characters and cutaway diagrams.
- `stick-story`: 2D stick figures, illustrated rooms, and step cards.
- `paper-atlas`: 2D cut-paper scenes, maps, timelines, and period figures.

Do not use `deep-dive` or `night-file` (3D). Do not use `tall-tale` (2D characters in a 3D world). If a proposed style or asset introduces 3D geometry, 3D rendering, volumetric lighting, or a 3D environment, reject or redesign it as genuine 2D.

## Production workflow from the skill

1. Read the selected style's complete `STYLE.md` and inspect its example project before planning.
2. Plan the title, conversational narration, cut-by-cut shot list, caption chunks, sources, and new components. Keep the user's three-agent uniqueness rules in force.
3. For a new project, use the skill's `new_video.sh` with an approved style, then adapt `script.json` and `src/shots.js`.
4. The skill supports local Kokoro TTS, Whisper word timing, estimated timing for captions-only drafts, FFmpeg audio mixing, headless Chrome capture, and MP4 rendering.
5. Run its visual/audio checks and inspect the contact sheet and key frames. A render is not complete until it has been reviewed.

## Voice and agent separation

The skill's local Kokoro voice presets are examples, not a guarantee of three distinguishable voices. Each agent must record the actual voice provider and preset used. Claude and OpenCode must not share a voice; prefer three clearly distinct voices. If an agent cannot use a different voice, mark the batch as blocked rather than silently duplicating a voice.

## Environment and cost notes

The skill describes a no-API-key local workflow, but it is not zero-effort or guaranteed to work on every machine. Its setup checks Node.js 22+, FFmpeg, Chrome, and Python 3.10+; it creates a Python environment and downloads Kokoro model files (about 340 MB) and a Whisper model (about 0.5 GB), plus Python packages. Rendering speed depends heavily on GPU availability. Do not run setup scripts, install packages, download models, or modify the user's machine without explicit approval. No paid service or API key may be introduced without approval.

## Content and rights checks

Use original narration and shots. Verify factual claims and record reliable sources. For health topics, be accurate and avoid gore or frightening misinformation. For real cases, treat people respectfully and avoid unsupported accusations. The skill's examples and included assets are references, not permission to copy third-party creators' work or reuse assets without checking their licences.

## Important project-specific override

The repository's rules take precedence whenever they are stricter than the skill. In particular: exactly three agent outputs, strict 2D only, cross-agent topic/angle/hook/story/style uniqueness, different voices, source names (not URLs) in the public description, and a coordinator-only all-three upload gate. Agents must never upload individually.
