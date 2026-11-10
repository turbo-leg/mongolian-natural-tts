# Eleven v4 audio tags for Mongolian lines

## How tags behave
- **Models:** v4 and v3 support Mongolian and audio tags. Multilingual v2 and the Flash models don't support Mongolian. SSML `<break>` only works on those older models, so on v4 control pauses with punctuation.
- **Syntax:** put the tag in square brackets at the start of a line: `[excited] Тэгэхээр…`. A tag can also sit mid-text to change delivery for the rest of a take, for example a question and its answer voiced as one take.
- **Describe the voice, not a sound.** ElevenLabs advises tags that describe vocal quality (`[upbeat, slightly faster]`). Something that reads like a sound cue may come out as a sound effect.
- **Tags aren't spoken,** but they appear in the timestamp alignment as ~0.1–0.2s silent tokens at the start of the take. If you cue visuals or captions from word timings, **skip tokens between `[` and `]`.**
- **Results vary by voice.** Re-test whenever the voice changes, and record the results below.

## Tested results

### Voice A · eleven_v4 · stability 0.5, similarity 0.75 · a Mongolian educational narrator (2026-10-30)
Grid: 3 lines (hook, explanation, viewer question) × 8 tags, judged by ear.

| Tag | Verdict | Notes |
|---|---|---|
| `[playfully, like sharing a secret]` | **Use for hooks** (the first spoken line) | Picked by ear for the hook |
| `[upbeat, slightly faster]` | **Use for body lines** | Tightens pace: the explanation line went from 6.6s to 5.3s |
| `[excited]` | **Use for body lines** | Same tightening; alternate with upbeat so it doesn't feel samey |
| none | Flat | Slowest, most robotic |
| `[warm, friendly teacher voice]` | Flat ("mid") | |
| `[casual, conversational, like talking to a friend]` | Flat ("mid") | |
| `[curious]` | Flat ("mid") | |
| `[confident, clear]` | Flat ("mid") | |

Applied to a full 11-line episode, the tags cut it from 65.8s to 57.6s with the same words.

Other findings with this voice:
- A plain y sounded wrong; «игрек» fixed it. A plain x is fine, and «икс» was mangled.
- -чих- forms were sometimes mispronounced (earlier takes). Keep one or two per script, each with a fallback.
- «…» glitched. Avoid it.

## Running a tag test

`scripts/tag_lab.py` voices every line × tag combination and writes one comparison page.

```
python scripts/tag_lab.py --voice <VOICE_ID> --round round.json --out <folder>
```

`round.json`:
```json
{"lines": {"hook": "…", "explain": "…", "question": "…"},
 "tags": [["none", ""], ["upbeat", "[upbeat, slightly faster]"], ["secret", "[playfully, like sharing a secret]"]]}
```

- **Testing tags:** use three lines that do different jobs (hook, explanation, question) and 5–8 tags.
- **Testing wordings:** put the alternative wordings in `lines` and only the 1–2 chosen tags in `tags`.
- **Ask a listener** for one pick per line, plus anything that broke: a sound effect, accent drift, English creeping in, or the voice changing identity.
- **Record the verdicts** in this file under a name for the voice (keep your private voice IDs out of public copies).

The API key comes from `ELEVENLABS_API_KEY`, or `--key-file`. Never print the key. Each take costs about its character count in credits; takes are cached by input text, so re-runs only pay for new combinations.

### Designed voices (ElevenLabs Voice Design, eleven_ttv_v3) · 2026-11-04
- One report, not yet A/B tested: setting a designed voice's **default language to English** (ElevenLabs → My Voices → Edit) still reads Mongolian and sounds **less synthetic**.
- Voice Design needs sample text of **at least 100 characters**.
