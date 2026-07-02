# Sun & Moon — 50-second pilot (production record)

**Date:** 2026-07-02 · **Final video:** Higgsfield job `5627b968-51cd-4494-90ed-602a9b0cfb33`
`https://d8j0ntlcm91z4.cloudfront.net/user_3FxYeQBlrLmLXDPiwEH0hlq0qRZ/hf_20260702_201014_5627b968-51cd-4494-90ed-602a9b0cfb33.mp4`

A condensed 5-block pilot of `the-sun-and-the-moon.md`, produced to preview the
look before committing to the full 5-minute build.

## Specs

- 5 blocks × 10s = 50 seconds, 1280×720 (16:9)
- Video model: **Seedance 2.0** (`seedance_2_0`, fast mode, 720p) — the full
  video should use `mode: std`, `resolution: 1080p` (same prompts work)
- Style/identity key: nano_banana_pro image, job `07570a48-e8b7-402c-b411-84547925add1`,
  attached to every clip as `image_references`
- Narrator: **Hana** (Seed Audio preset `c25f78a0-714e-42af-8da3-a399cef94968`)
- Assembly: `explainer_video` (block-locked narration, no subtitles, no CTAs)

## Blocks

| # | Narration | Clip job | Voice job |
|---|-----------|----------|-----------|
| 1 | "Have you ever wondered, little one, why the moon watches you sleep? Long ago, there was no moon at all." | `322daf40…` | `9bb4ae4a…` |
| 2 | "On the mountain path, a hungry tiger rumbled: give me a rice cake, and I won't gobble you up." | `cb5161c8…` | `c5e06746…` |
| 3 | "When the tiger knocked at their door, two clever children saw his furry paw, and climbed the tall willow tree." | `aeefca80…` | `7761af22…` |
| 4 | "They asked the sky for help, and down came a rope of gold, lifting them gently up, and up." | `62fc2a21…` | `e943cd70…` |
| 5 | "The sister became the sun. The brother became the moon, watching over every sleeping child. Goodnight, little one." | `0225eec9…` | `710d7ead…` (speech_rate 15) |

## Costs (actual)

~182 credits total: 5 clips × 35 (720p fast) + style key 2 + 7 voice takes ≈ 1.4.
Full 5-minute 1080p Seedance build: 30 clips × 90 = **~2,700 credits**.

## Lessons for the full build

1. **Safety filter false-positives:** prompts with "a small child sleeps under a
   blanket" and "boy helps his little sister climb" were rejected (`nsfw`).
   Fix: show the house exterior instead of a sleeping child; place children
   *already* in the tree rather than climbing. Avoid child + bed/blanket and
   child + physical-contact verbs in prompts.
2. **Rate limits:** both Seedance and Seed Audio allow ~2 submissions per
   ~30s window — batch in pairs with 30s gaps.
3. **Seed Audio (Hana) pace ≈ 0.5s/word.** Keep lines ≤ 18 words for the 10s
   block; the closing line needed `speech_rate: 15` to fit.
4. **Preset interception:** Higgsfield suggests its "3D RENDER" preset for these
   prompts — decline with `declined_preset_id: 5a77643c-b6cc-4efd-bdc6-ab8ff48dfa82`.
5. Keep `generate_audio: true` with ambient-only AUDIO lines — the clip ambience
   sits nicely under the narration.
