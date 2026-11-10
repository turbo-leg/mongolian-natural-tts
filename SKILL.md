---
name: mongolian-natural-speech-tts
description: Write and fix Mongolian (Cyrillic) lines so an ElevenLabs text-to-speech voice sounds like a real person talking, not a textbook or a translation. Covers spoken word choice, sentence rhythm, particles, register (чи/та), how to write Latin letters and numbers, Eleven v4 audio tags, and A/B auditions of takes. Use it whenever you write or edit Mongolian narration, voiceover, ad copy, reel or short scripts, dialogue or any text that ElevenLabs (or another TTS) will speak. Also use it when a Mongolian AI voice "sounds robotic", "sounds off", "too formal" or "like Google Translate", and when choosing delivery tags, even if the user doesn't mention TTS by name.
---

# Mongolian natural speech for TTS

The usual reason a Mongolian TTS voice sounds robotic is the **text, not the voice**. Lines written like a textbook or translated from English give the model nothing to perform: long chains of clauses, bookish verbs, English sentence shapes, bare endings with no particle. Fix the words first, then the delivery tags, then audition.

## Workflow

1. **Pick the register from the audience** (it changes everything else):
   - teenagers or students: an older sibling or tutor (ах/эгч). Drop the pronoun; use bare imperatives with softeners, and "let's" forms.
   - parents or adults: «та», still spoken, short and warm, not official.
   - comedy, friends, games: casual «чи», with slang allowed in the spoken sense. Still spell it in full Cyrillic (rule 10).
2. **Write or rewrite each line** with the rules in `references/rules.md`. Read that file the first time in a session. It holds the 12 rules, the particle table, the red-flag phrasings and before/after examples.
3. **Self-check every line** against the checklist below. Fix it before showing anyone.
4. **Spell-check** the Cyrillic with any Mongolian spell checker you trust. It checks spelling only, not naturalness. For naturalness, a second reader helps: see `prompts/fluency-review.md`.
5. **Add delivery tags.** Eleven v4 / v3 only; see `references/audio-tags.md`. One tag at the start of each line, chosen by the line's job: hook, explanation or question. Tags are performance input. Keep them out of on-screen text and captions.
6. **Audition, don't argue.** When two wordings or tags compete, voice both with `scripts/tag_lab.py` and let the user listen. A line that sounds wrong under *every* tag has a wording problem; rewrite it instead of re-tagging.
7. **A native speaker has the final say.** Rules are judgment calls. When a native reviewer's wording differs from these rules, theirs wins; note the difference so the rules can improve.

## Self-check (every line)

- About 5–8 words between full stops or «—». Long sentences are split.
- No «…» (sounds hesitant and can glitch). No colons. Pauses come from «.» and «—» only.
- No hyphenated case endings on Latin letters (`x-ийг`). Restructure instead: «x ч биш, y ч биш», «x, игрек хоёрыг».
- At most one end-particle per line. «шүү» or «шүү дээ» at most once per script.
- No passives, no nominalizations, no bureaucratic verbs (гүйцэтгэх, хэрэгжүүлэх, тодорхойлох).
- No «асуулт … асууж байна» or other English calques.
- Every -чих- form has a plain fallback, because some voices mispronounce it. Audition them.
- Numbers are written as words. No chat spellings (бна, шд, бз).
- Number forms: standalone when the number stands alone («хорь нэмээд»), the -н form only before a noun («хорин хувь»). Easy to miss in dialogue and arithmetic lines.
- The meaning is unchanged from the source. This matters most for math, facts and claims.

## Letters, numbers and mixed English

- **Latin letters inside Mongolian lines:** what works differs by voice, so audition it. Tested on one Eleven v4 voice: a plain Latin **x** worked, and «икс» was mangled. Plain **y** sounded wrong, and writing **«игрек»** fixed it. Start there for a new voice and confirm with one audition.
- **English sentences** (worked examples, quotes) stay in English with Latin letters. Short English loanwords that Mongolians really say (апп, коммент, IELTS, SAT) are fine inside Mongolian.
- **Spell out numbers** in words, in the case the sentence needs («наймд хуваахаар», «гучин нэг»).
- **Latin acronyms read as letters** (A, B): spell them the way they're said, «Эй», «Би».

## Output format when rewriting

For each line give: **the original → the rewrite → a short reason** (which rule). Give two options where the choice is genuinely open. Then give the TTS input lines, with tags, as a copy-ready block, separate from the clean caption text.

## Files

- `references/rules.md`: the 12 rules with the reason for each, the particle table, red-flag phrasings and before/after examples. Read it before writing.
- `references/audio-tags.md`: how v4 tags behave, tested results per voice, and how to run a tag test. Read it before tagging, and add new test results to it.
- `scripts/tag_lab.py`: voices lines × tags (or several wordings) and builds one HTML page to compare by ear. It caches by input text, so re-runs only pay for new takes. Run `python scripts/tag_lab.py --help`.
