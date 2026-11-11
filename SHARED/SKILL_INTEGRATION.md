# Faceless Shorts skill integration

This repository uses the user's separately installed `faceless-shorts` skill as its production reference. The skill is not copied into this public repository.

## Six-style catalogue with mandatory 2D adaptation

All six skill styles may be used, but the final output must be genuine 2D animation. For styles originally designed around 3D, preserve their mood, composition, pacing, storytelling devices, palettes, and visual identity while rebuilding every scene as 2D artwork and 2D motion.

### Native 2D styles
- `inside-out`: flat 2D illustrated explainers with simple characters and cutaway diagrams.
- `stick-story`: 2D stick figures, illustrated rooms, and step cards.
- `paper-atlas`: 2D cut-paper scenes, maps, timelines, and period figures.

### Styles requiring 2D conversion
- `deep-dive`: layered 2D illustrations, drawn environments, flat-layer parallax, animated diagrams, and hand-drawn details.
- `night-file`: 2D illustrated noir scenes, flat silhouettes, textured backgrounds, graphic shadows, maps, documents, and 2D camera pans.
- `tall-tale`: fully illustrated 2D characters and fully 2D backgrounds, with flat perspective, layered depth, and 2D transitions.

## Non-negotiable 2D test
Allowed: hand-drawn/vector 2D artwork, flat shapes, 2D compositing, layered parallax using flat artwork, 2D pans/zooms, frame-by-frame animation, cut-paper animation, and 2D motion graphics.
Not allowed: 3D models, geometry, rendered frames, environments, camera scenes, or 3D scenes merely rendered to look flat.

## Production workflow
1. Read the selected style's complete `STYLE.md` and inspect its example project before planning.
2. For conversion styles, write a 2D conversion plan before production.
3. Plan title, narration, shot list, caption chunks, sources, and new components. Compare against all four assignments and recent topic history.
4. Use the skill's project template only after verifying it produces compliant 2D output.
5. The skill may use local TTS, Whisper timing, FFmpeg, headless Chrome, and MP4 rendering. Verify the user's actual machine/tool availability.
6. Inspect the contact sheet and key frames. A render is not complete until reviewed.

## Agent character and voice separation
Each agent must use only its own fixed original character in `SHARED/AGENT_CHARACTERS.json`. Character identity, palette, silhouette, and signature motion remain consistent. Do not imitate provider logos or mascots.
Record actual voice provider/preset. Prefer four distinguishable voices; do not fabricate voice capability.

## Environment and cost
The local workflow may require Node.js, FFmpeg, Chrome, Python, packages, and model downloads. Do not install dependencies, download models, modify machine settings, or introduce paid services/API keys without explicit approval.

## Content and rights
Use original narration and shots. Verify factual claims and record reliable sources. Avoid harmful, deceptive, age-inappropriate, or sensational misinformation. Check licences for all assets.

## Project-specific override
Repository rules take precedence whenever stricter: four-agent target, genuine 2D only, exclusive agent characters, cross-agent uniqueness, sectioned descriptions with source/publisher names only (no URLs), persistent queue, and coordinator-only publishing.
