# Rules for spoken Mongolian TTS lines

Sources:
- what native reviewers changed in real scripts
- ElevenLabs v4 documentation
- a linguist-style research report: mostly expert judgment, with its educator quotes and ElevenLabs claims checked

Treat these as strong defaults, not law; native speakers override them.

## Contents
1. The 12 rules
2. Particles
3. Red-flag phrasings → spoken replacements
4. Before and after
5. Open questions to ask a native speaker

## 1. The 12 rules

1. **Pick one register and keep it.**
   - Students: older-sibling tone. No «та», no overt «чи». Use the bare imperative with a softener («хар даа»), the topic marker «чинь», and "let's" forms («нэмье», «шалгаад үзье»).
   - Parents and adults: «та», warm and short.
   - Friends and comedy: «чи».
   *Why:* «та» to a teenager sounds like an advert or a machine translation, and an overt «чи» on every line sounds bossy.
2. **Short phrases: 5–8 words between «.» and «—».** *Why:* the voice resets its pitch at each boundary. Long written sentences flatten into a monotone.
3. **Punctuation is the only pause control.** Eleven v3/v4 have no SSML break tags. Use «—» or «.»; never «…» (hesitant, glitchy) or colons (choppy).
4. **Link actions with -аад/-ээд, not chains of -ж.** «орлуулаад бодвол», not «орлуулж бодож эхэлбэл». *Why:* -ж chains are written style.
5. **For a step you're demonstrating, use -хаар/-хээр ("when we…") rather than -вал/-вэл ("if…").** «наймд хуваахаар … тав гарна». *Why:* -вал sounds hypothetical and textbook-like. -хаар sounds like it's happening in front of you.
6. **Kill English calques:**
   - «асуулт … асууж байна» ("the question asks") → «бодлого чинь … хэд вэ л гээд байгаа юм»
   - «x, y хоёрын алийг нь ч» ("neither of") → «x, y хоёрыг тус тусад нь»
   - passives («нэмэгдэнэ», «солигдсон») → active, or "let's" («нэмье»)
   - nominalizations («шалгалт хийсний үр дүнд») → verbs («шалгаад үзэхээр»)
   - a «та / танд» for every English "you" → drop the pronoun
7. **No bureaucratic verbs.** гүйцэтгэх, хэрэгжүүлэх and тодорхойлох become бодох, олох, гаргах and хийх.
8. **Particle budget: at most one end-particle per line.** Too few sounds cold, and too many sounds nagging or folksy. See the table.
9. **Latin letters stay bare.** Never `x-ийг`. The hyphen makes the voice pause and switch language mid-word. Put the case on the next word («x, игрек хоёрыг») or restructure («x ч биш, игрек ч биш»).
10. **Spell everything in full Cyrillic.** The voice shortens байна and шүү дээ by itself. Chat spellings (бна, шд, бз, сольцон) can't be pronounced properly. Numbers go in words.
11. **Spoken connectors at turns, not every line.** «За», «Тэгэхээр», «Одоо», «Харин», «Гол нь».
12. **Questions that sound like a person.** «… гэж үү?» (really?) for a hook or loop question; «… бол?» (I wonder) for a challenge; «… биз?» (right?) to confirm what's on screen. Avoid the flat «… ёстой юу?».

## 2. Particles

| Particle | Job | Example | Watch out |
|---|---|---|---|
| дээ / даа | softens; makes an order an invitation | Тоонуудыг нь хар даа. | On every line it sounds weary |
| л | "just / only" | x нэмэх y хэд вэ л гээд байгаа юм. | One per sentence |
| ч | "not even / neither" | x ч биш, y ч биш | Never after a hyphenated Latin letter |
| биз / биз дээ | "right?" (confirms) | Байраа сольсон байгаа биз? | A heavy fall sounds scolding |
| юм | explains ("the thing is") | … гээд байгаа юм. | Fine after -ж байгаа |
| шүү | "mind you" (emphasis) | … хэрэггүй шүү. | At most once per script |
| шүү дээ | "you know" (obvious) | Амархан шүү дээ. | More than once sounds impatient |
| чинь | topic on screen ("this… here") | Бодлого чинь … | Not twice in one sentence |
| байх | "probably" | | Never on facts or math steps |
| юм шиг | "seems like" | Хэцүү юм шиг санагдаж магадгүй. | Hooks only, never in a solution |
| хө | folksy "my friend" | | Avoid for young urban audiences |

## 3. Red-flag phrasings → spoken replacements

| Sounds like | Robotic | Spoken |
|---|---|---|
| Calque | Асуулт чинь … асууж байна. | Бодлого чинь … хэд вэ л гээд байгаа юм. |
| Calque | x, y хоёрын алийг нь ч олох хэрэггүй. | x, y хоёрыг тус тусад нь олох хэрэггүй. |
| -ж chain | Шууд орлуулж бодож эхэлбэл… | Шууд орлуулаад бодвол… |
| Bureaucratic | үйлдлийг гүйцэтгэх | бодох / хийх |
| Passive | Тоонууд солигдсон байна. | Тоонууд нь байраа сольсон байна. |
| Nominal | Шалгалт хийсний үр дүнд… | Шалгаад үзэхээр… |
| "You" calque | Та хоёр талыг нь хуваавал танд хариу гарна. | Хоёр талыг нь хуваахаар хариу нь гарна. |
| Calque | товчлолын зам | дөт зам («Би дөт замаар гаргая.») |
| Written past | …нисэн гарав. / …бэлэглэв. | …нисээд гарчихлаа. / …өгчихлөө. (spoken -аад + -чихлаа in story narration) |
| Written condition | …сонгосон бол. | …сонгосон уу? (spoken question to the viewer) |
| Colon list | Тоонуудыг нь хар: гурав, тав, … | За, тоонуудыг нь хар даа. Гурав, тав. … |

## 4. Before and after (a real script; the native-reviewed direction)

| Robotic | Spoken | Rules |
|---|---|---|
| Энэ бодлогод x, y хоёрын алийг нь ч олох хэрэггүй. | Энэ бодлого дээр x, игрек хоёрыг тус тусад нь олох хэрэггүй. | 6, 9 |
| Шууд орлуулж бодож эхэлбэл урт, бас алдах амархан. | Шууд орлуулаад бодвол урт болно. Бас алдахад амархан. | 2, 4 |
| Асуулт чинь x-ийг ч биш, y-ийг ч биш, x нэмэх y-ийг асууж байна. | Гол нь бодлого чинь x ч биш, игрек ч биш — x нэмэх игрек хэд вэ л гээд байгаа юм. | 6, 9, 11 |
| Хоёр талыг нь найманд хуваавал … тав гарна. | Хоёр талыг нь наймд хуваахаар … тав гарна. | 5 |
| Тэгэхээр x, y хоёрыг заавал тус тусад нь олох ёстой юу? | Тэгэхээр x, игрек хоёрыг заавал тус тусад нь олох ёстой гэж үү? | 12 |
| Далан гэж хэлмээр санагдаж байгаа биз? | Дал гэж хэлмээр санагдаж байгаа биз? | 10: a number said on its own takes its standalone form (дал, жар, ная, ер); the -н form (далан, жаран, наян, ерэн) goes before a noun («далан градус»). Native correction, 2026-10-30 |

## 5. Open questions to ask a native speaker
- **«хариу» or «хариулт» for a numerical answer.** The research says «хариу». One native reviewer wrote «хариулт нь гучин нэг».
- **«наймд» or «найманд»** for the dative of eight in speech.
- **How much -чих- feels natural.** Real speech uses a lot, but some TTS voices mispronounce it.

- **Bare imperative or -аарай/-ээрэй for teenagers.** Rule 1 uses the bare imperative with a softener («хар даа»). A second-reader review (2026-11-09) argued that bare «дар», «сонго» sound cold to 15–19-year-olds and that «дараарай», «сонгоорой» sound like a friendly tutor. Not yet settled by audition or a native reviewer; watch for repetition when many lines end in -аарай.
