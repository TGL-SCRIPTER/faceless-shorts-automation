# Educational trend and adaptive style selection

## Channel scope
This channel makes educational explainers and interesting, verified facts. Trends are useful only when they reveal a subject people want to understand.

**Allowed topic families:** science, space and astronomy, technology and computing, engineering, nature and animals, history, geography, inventions, and useful everyday "how/why" explanations.

**Not eligible:** reaction videos, reaction commentary, drama, gossip, prank/reaction compilations, memes as the main content, and trends that provide no meaningful educational takeaway. Do not make a reaction video just because reactions are trending.

## Research procedure
1. Generate candidate educational questions and fact-based topics relevant to the channel.
2. Check current educational interest and YouTube Shorts signals using tools actually available to the agent. Use YouTube search/trending surfaces, Google Trends or reputable public sources when accessible.
3. Record the date/time checked, region, language, source names, observed signal, and data limitations.
4. Look for more than one independent signal where possible: rising search interest, repeated audience questions, current educational relevance, or comparable educational Shorts with recent engagement.
5. Check topic history and the current four-agent batch for duplicates and saturation.
6. Fact-check the central claim before committing. Reject topics without credible supporting evidence.
7. Score candidates with the rubric below and select the best educational fit.

## Candidate scoring (0–100)
- Educational value and clarity of learning takeaway: 0–25
- Audience interest / educational trend evidence: 0–20
- Curiosity and hook potential: 0–15
- Visual storytelling potential in 2D: 0–15
- Credibility and source quality: 0–15
- Freshness and low overlap with recent channel topics: 0–10

Subtract up to 20 points for strong saturation, weak evidence, misleading framing risk, or poor fit with channel identity. Record deductions and reasoning.

The score is a comparative editorial score, not a measured probability of going viral. Never write "X% chance of going viral"; this project has no validated predictive model. A trend score does not guarantee reach.

## Style selection after topic selection
1. Write the educational question and the one-sentence learning takeaway.
2. Compare at least two relevant styles from the existing library when practical.
3. Choose the style that makes the concept easiest to understand and most engaging without sacrificing factual clarity.
4. If no existing style fits well, create an original topic-specific style. Do not invent a new style simply to make every video look different.
5. Verify feasibility with the actual renderer, available assets, timeline, and agent capabilities before choosing an elaborate treatment.
6. Keep the agent's assigned presenter consistent and unbranded; the style may change, the character identity may not.

## Required custom style specification
Save new style specifications under `SHARED/CUSTOM_STYLES/<style-id>.md` and register them in `SHARED/CUSTOM_STYLES/REGISTRY.json`. Include:
- Unique style ID and display name
- Creator agent and creation date
- Topic and why the style fits
- Visual grammar, composition, palette, and background treatment
- Agent character integration
- Motion language and scene transitions
- Captions, typography, contrast, and mobile readability
- Sample storyboard of at least 4 shots
- Production requirements and fallback simplification
- Accessibility/readability and 2D compliance check

## Ethical trend selection
- No fabricated statistics, fake urgency, misleading thumbnails, deceptive hooks, or false claims.
- Do not exploit tragedies, disasters, private individuals, or sensitive events for views.
- Avoid dangerous challenges, harmful misinformation, and age-inappropriate subjects.
- A trend is a research clue, not proof that a fact is true.
- If trend data is unavailable, state that and use a clearly labelled editorial judgment rather than inventing metrics.

## Agent handoff fields
Every assignment and finished-video report should include:
`candidate_topics`, `trend_sources`, `trend_checked_at`, `trend_region`, `trend_language`, `trend_signals`, `educational_takeaway`, `editorial_score`, `score_rationale`, `selected_style_id`, `style_type` (existing/adapted/new), `style_fit_rationale`, and optional `custom_style_spec_path`.
