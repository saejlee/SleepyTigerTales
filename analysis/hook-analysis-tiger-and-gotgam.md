# Hook & Retention Analysis — "The Tiger and the Got-gam" (youtube.com/watch?v=7Ac1h5eHEcY)

Scene-by-scene AI analysis of the video (50 scenes, 0:00–6:36). This document maps
what the video does at each moment, why viewers drop off, and what to change in
future scripts.

## TL;DR

The story choice is excellent and the narrator devices ("dear sleepy one",
rhetorical questions) are right for the niche. The video underperforms for four
fixable reasons:

1. **The hook doesn't hook.** The first 14 seconds are pure scene-setting with no
   question, no stakes, no promise. The actual premise (a baby who fears nothing —
   until one strange word) doesn't appear until **2:25**. That's ~2.5 minutes of
   preamble in a format where most drop-off happens in the first 30 seconds.
2. **A mid-video "Comment your answer below" CTA at 4:57.** This is a bedtime
   product. The parent pressed play to make the child *drowsier*. An engagement CTA
   mid-story breaks the spell at the exact moment the child should be drifting off —
   and it signals to the parent that the video isn't safe to leave running.
3. **Severe visual continuity breaks.** The narration says snowy Korean mountains at
   night; the visuals repeatedly cut to bright daylight, a modern supermarket
   street, a house with solar panels, suburban lawns, a city street with neon signs,
   recording equipment, and the tiger randomly wearing a beanie, a green jacket, or
   a blue vest. Parents screening a bedtime video read this as low-quality/AI-sloppy
   and click away; kids notice too.
4. **Flat pacing curve.** Bedtime content should *decelerate* — energy at the start
   (for the algorithm and the still-awake child), then progressively slower, softer,
   more repetitive toward the end. This video holds one speed throughout and ends on
   a reveal rather than a wind-down.

## Scene-level hook timeline

| Time | What happens | Assessment |
|------|--------------|------------|
| 0:00–0:14 | "In the snowy mountains of Korea… lived a very proud tiger named Horangi" | Establishes character but asks nothing. No reason to keep watching yet. |
| 0:14–0:23 | First direct address: "Tonight, dear little one, what do you think…?" | Good device, arrives late. This should be sentence one. |
| 0:23–2:25 | Tiger admires himself, walks downhill, muses | ~2 minutes of padding. The famous story hasn't started. Biggest drop-off zone. |
| 2:25–3:20 | Mother's escalating warnings: fox → bear → tiger | This is the engine of the story and it works. It should start by ~0:40. |
| 4:57–5:06 | "Comment your answer below" | Remove. Move all engagement asks to the description/pinned comment/end screen. |
| 5:06–5:44 | The got-gam moment — instant silence | The best beat in the video. The hook should tease this from second one. |
| 6:31–6:36 | Reveal begins ("got-gam is simply the Korean word…") | Analysis window ends here; the reveal lands late relative to total runtime. |

## What's already working (keep these)

- **Direct address** to the listening child ("dear sleepy one") — this is the
  channel's voice. Keep it, and use it in the first sentence.
- **Rhetorical questions** ("do you notice something strange?") — great for gentle
  engagement without breaking sleepiness. Keep them; just never convert them into
  on-screen CTAs.
- **The misunderstanding engine** (tiger mishears a harmless word as a monster) —
  classic dramatic irony that works even for very young listeners.
- **Horangi as a recurring mascot** — matches the channel name and builds a series
  identity. Reuse the same character design in every video.

## Rules for future scripts (applied in `scripts/`)

1. **Hook in the first 15 seconds** = a question + a promise, spoken over the most
   beautiful shot of the video. Formula: *"Have you ever wondered why X? Tonight,
   I'll tell you the secret."*
2. **Story engine starts before 0:45.** Character intro is one sentence, not two
   minutes.
3. **No CTAs inside the story.** Engagement lives in the title, thumbnail,
   description, pinned comment, and end screen only.
4. **Deceleration curve:** normal pace (min 0–3) → slow (min 3–8) → very slow with
   longer pauses and a repeated lullaby refrain (final minutes). The child should be
   asleep before the video ends — that's the product, and it also maximizes watch
   time because parents let it run.
5. **Continuity sheet per video:** one character design, one time-of-day per act,
   one era (traditional Korea — no power lines, supermarkets, solar panels), one
   palette. Every image prompt must restate the character sheet.
6. **Repetition is a feature.** Folk-tale refrains ("Give me a rice cake and I won't
   gobble you up") are sleep-inducing by design. Lean into them; slow them down on
   each repeat.
