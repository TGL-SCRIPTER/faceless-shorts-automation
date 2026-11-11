# Trend-aware topic and adaptive style selection

## Purpose
Select topics with promising audience-interest signals, then choose or invent the most suitable original 2D visual style for each topic. This process improves decision quality; it cannot predict or guarantee virality.

## Research procedure
1. Generate a shortlist of candidate topics relevant to the channel's educational/fun-fact identity.
2. Check current YouTube Shorts and audience-interest signals using tools actually available to the agent. Use YouTube search/trending surfaces, Google Trends or other reputable public trend sources when accessible.
3. Record the date/time checked, region, language, source names, observed signal, and any data limitations.
4. Look for more than one independent signal where possible: recent interest growth, repeated questions/comments, strong current relevance, or comparable Shorts with recent engagement.
5. Check the channel's topic history and the current four-agent batch for duplicates and saturation.
6. Fact-check the central claim before committing. Reject topics without credible supporting evidence.
7. Score candidates with the rubric below, select the best fit, and explain the choice.

## Candidate scoring (0–100)
- Audience interest / trend evidence: 0–25
- Curiosity and hook potential: 0–20
- Visual storytelling potential in 2D: 0–15
- Broad relevance / shareability: 0–15
- Credibility and source quality: 0–15
- Freshness and low overlap with recent channel topics: 0–10

Subtract up to 20 points for strong saturation, weak evidence, misleading framing risk, or poor fit with channel identity. Record deductions and reasoning.

The score is a comparative editorial score, not a measured probability of going viral. Never write "X% chance of going viral" unless a genuinely validated predictive model and its calibration evidence exist; this project currently has no such model.

## Style selection after topic selection
1. Write a one-sentence summary of the topic and intended audience takeaway.
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
`candidate_topics`, `trend_sources`, `trend_checked_at`, `trend_region`, `trend_language`, `trend_signals`, `editorial_score`, `score_rationale`, `selected_style_id`, `style_type` (existing/adapted/new), `style_fit_rationale`, and optional `custom_style_spec_path`.
