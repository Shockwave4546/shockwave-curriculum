# Voice options

Azure Speech voice candidates explored for narrating presentations, kept so this doesn't
need to be re-derived next time we want to add more options. Samples live in
`docs/voice-samples/` (same narration line for every candidate, so they're directly
comparable). Regeneration recipe: [azure-tts-process.md](azure-tts-process.md).

Resource: `joechan-9338-resource` / `rg-joe.chan-6204` / `westus3`.

## Liked

- **Andrew** — `en-US-AndrewMultilingualNeural` ([sample](voice-samples/andrew.mp3))
- **Ryan** — `en-US-RyanMultilingualNeural` ([sample](voice-samples/ryan.mp3)) — used for Ch.25
- **Jenny (Multilingual)** — `en-US-JennyMultilingualNeural` ([sample](voice-samples/jenny-multilingual.mp3)) — used for Ch.1. Multilingual upgrade of the original `en-US-JennyNeural` (which felt too robotic).
- **Cora** — `en-US-CoraMultilingualNeural` ([sample](voice-samples/cora.mp3))

## Other Multilingual Neural candidates tried (not yet picked)

Male: Brian, Davis, Christopher.
Female: Emma, Ava, Nancy (5 style variants), Serena (7 style variants), Amanda, Phoebe (3 style variants), Evelyn.

All in the same pricing tier as the "Liked" voices above. Samples in `voice-samples/`.

## HD tier — tried, passed on

- **Ethan** — `en-US-Ethan:MAI-Voice-2` ([sample](voice-samples/ethan-hd.mp3))
- **Harper** — `en-US-Harper:MAI-Voice-2` ([sample](voice-samples/harper-hd.mp3))

## Pricing (Azure's public rate card, checked September 2026)

| Tier | Rate | Notes |
|---|---|---|
| Standard / Multilingual Neural | $16 / 1M characters | Jenny, Andrew, Ryan, Cora, and everything else in "Liked"/"Other candidates" above |
| Neural HD (MAI-Voice-2 family) | $22 / 1M characters | Cut from $30 in March 2026. Azure's pricing page doesn't break out MAI-Voice-2 as its own line item — this assumes it bills at the general Neural HD rate, since that's the voice type Azure's own API reports for it (`VoiceType: "NeuralHD"`) |
| Free tier | 500,000 characters/month | No expiration; standard neural quality |

Source: [Azure Text to Speech Pricing (2026)](https://texttolab.com/blog/azure-text-to-speech-pricing)

## Full candidate list (for finding more later)

Pulled live from `GET https://westus3.tts.speech.microsoft.com/cognitiveservices/voices/list`
(see azure-tts-process.md for the auth header). 73 `en-US` voices existed as of this check,
across three `VoiceType`s: `Neural` (standard + Multilingual generation), `NeuralHD`
(MAI-Voice-2 family), and a few `DragonHDFlashLatestNeural` HD-flash voices (Jimmie, Tiana,
Tyler) not yet sampled. Re-run that query to see the current full list before picking more —
Azure adds voices fairly often.

## Rotation idea (open question, not yet decided)

Considering rotating different voices across presentations rather than using one voice for
everything — undecided whether that's per-presentation, per-chapter, or per group of
consecutive chapters. Revisit once more chapters exist to see how it feels in practice.
