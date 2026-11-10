# mongolian-natural-tts

**Make Mongolian text-to-speech sound like a person talking.** Rules, tested voice settings and a small
audition tool, from producing Mongolian educational videos with ElevenLabs.

> Монгол дуу хоолойны AI-г хүн шиг ярьдаг болгох заавар: юу бичих, яаж бичих, ямар tag ашиглах, яаж
> сонсож шалгах.

The usual reason a Mongolian TTS voice sounds robotic is the **text, not the voice**. Lines written like a
textbook, or translated from English, give the model nothing to perform: long chains of clauses, bookish
verbs, English sentence shapes, bare endings with no particle. Fix the words first, then the delivery
tags, then audition by ear.

## What's inside

| Path | What it is |
|---|---|
| [`references/rules.md`](references/rules.md) | 12 rules for spoken Mongolian TTS lines: register, sentence length, pause control, -аад/-ээд linking, calques to avoid, particles, Latin letters and numbers. A particle table, red-flag phrasings with spoken replacements, before/after examples from a real script, and open questions |
| [`references/audio-tags.md`](references/audio-tags.md) | How ElevenLabs v4 audio tags behave with Mongolian, and tag-by-tag verdicts from a blind listening test |
| [`scripts/tag_lab.py`](scripts/tag_lab.py) | Voices every line × tag (or several wordings) and builds one HTML page to compare takes by ear. Caches by input text, so re-runs only pay for new takes |
| [`prompts/fluency-review.md`](prompts/fluency-review.md) | A prompt for a second-reader fluency check of a script |
| [`SKILL.md`](SKILL.md) | The same knowledge as an agent skill (Claude Code and other agents that read `SKILL.md`) |
| [`examples/`](examples) | Two audition rounds: tags, and competing wordings |

## The five rules that matter most

1. **Pick one register and keep it.** For students, an older-sibling tone: drop «та» and avoid an overt
   «чи» on every line.
2. **5–8 words between full stops.** The voice resets its pitch at each boundary; long written sentences
   flatten into a monotone.
3. **Punctuation is the only pause control** on v3/v4 models (no SSML). Use «.» or «—»; never «…».
4. **Link actions with -аад/-ээд, not chains of -ж.** «орлуулаад бодвол», not «орлуулж бодож эхэлбэл».
5. **Spell everything the way it's said.** Numbers in words; acronyms as letters («Эй», «Би», «кью ар»);
   foreign names phonetically in the voice input («Гүүгл»), even if the screen shows the Latin.

The full set, with reasons and examples, is in [`references/rules.md`](references/rules.md).

## Audition, don't argue

When two wordings or tags compete, voice both and listen:

```bash
export ELEVENLABS_API_KEY=...        # never commit it
python scripts/tag_lab.py --voice <VOICE_ID> --round examples/round-tags.json --out tag-lab
# open tag-lab/index.html, pick one take per row
```

Each take costs about its character count in ElevenLabs credits. Takes are cached by their exact input,
so changing one line only re-voices that line.

## Use it as an agent skill

```bash
git clone https://github.com/turbo-leg/mongolian-natural-tts ~/.claude/skills/mongolian-natural-speech-tts
```

The agent then applies the rules whenever it writes Mongolian narration, and uses `tag_lab.py` for
auditions.

## Contributing

These are judgment calls from one team's scripts and one set of voices, and **native speakers override
them**. The most useful contributions:

- a native correction to a rule or example (say which line and why);
- tag verdicts for another voice or model (add a section to `audio-tags.md`; name the voice, not its private ID);
- answers to the open questions at the end of `rules.md`.

## Licence

The writing (`references/`, `prompts/`, `SKILL.md`, `README.md`) is [CC BY 4.0](LICENSE-docs). The code
(`scripts/`) is [MIT](LICENSE). Made while producing videos for [Primis EduCare](https://primiseducare.com),
a test-prep school in Ulaanbaatar.
