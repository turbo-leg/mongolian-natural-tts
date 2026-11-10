"""Voice lines x delivery tags with ElevenLabs and build one HTML page to compare them by ear.

python tag_lab.py --voice <VOICE_ID> --round examples/round-tags.json --out ./tag-lab
  round.json: {"lines": {"id": "text", ...}, "tags": [["id", "[tag]" or ""], ...]}
Options: --model eleven_v4  --stability 0.5  --similarity 0.75  --key-file path (else $ELEVENLABS_API_KEY)
Takes are cached by their exact input text, so re-running only pays for new combinations.
"""
import argparse
import base64
import html
import json
import os
import pathlib
import urllib.request


def api_key(path):
    if path:
        return pathlib.Path(path).read_text(encoding='utf-8').strip()
    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        raise SystemExit('Set ELEVENLABS_API_KEY or pass --key-file')
    return key


def synth(out, take, text, args, key):
    audio, meta = out / f'{take}.mp3', out / f'{take}.json'
    settings = {'stability': args.stability, 'similarity_boost': args.similarity}
    if audio.exists() and meta.exists():
        cached = json.loads(meta.read_text(encoding='utf-8'))
        if cached.get('input') == text and cached.get('voice') == args.voice and cached.get('model') == args.model and cached.get('settings') == settings:
            return
    req = urllib.request.Request(
        f'https://api.elevenlabs.io/v1/text-to-speech/{args.voice}',
        data=json.dumps({'text': text, 'model_id': args.model, 'voice_settings': settings}).encode(),
        headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=120) as r:
        audio.write_bytes(r.read())
    meta.write_text(json.dumps({'input': text, 'voice': args.voice, 'model': args.model, 'settings': settings}, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  voiced {take}', flush=True)


def page(lines, tags, title):
    head = ''.join(f'<th class="h">{html.escape(t)}<br><code>{html.escape(g) or "—"}</code></th>' for t, g in tags)
    rows = ''.join(
        f'<tr><th><b>{html.escape(lid)}</b><br><span>{html.escape(text)}</span></th>'
        + ''.join(f'<td><div class="t">{html.escape(tid)}</div><audio controls preload="none" src="{html.escape(lid)}-{html.escape(tid)}.mp3"></audio></td>' for tid, _ in tags)
        + '</tr>' for lid, text in lines.items())
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>
body{{margin:0;background:#F7F6F2;color:#0F2847;font-family:Inter,Arial,sans-serif}}main{{padding:32px 20px}}h1{{font:36px Georgia,serif;margin:0 0 6px}}
table{{border-collapse:collapse;width:100%}}th,td{{border-top:2px solid #0F2847;padding:10px 8px;vertical-align:top;text-align:left}}
th span{{font-weight:400;font-size:14px}}th.h{{font-size:13px}}code{{font-size:11px;color:#DE6B53}}.t{{font-size:12px;margin-bottom:4px}}audio{{width:150px}}div.w{{overflow-x:auto}}
</style></head><body><main><h1>{html.escape(title)}</h1><p>Same voice and settings; only the tag or wording changes. Pick one per row, and note any take that broke (sound effect, accent drift, English creeping in).</p>
<div class="w"><table><tr><th>line</th>{head}</tr>{rows}</table></div></main>
<script>document.querySelectorAll('audio').forEach(a=>a.onplay=()=>document.querySelectorAll('audio').forEach(o=>{{if(o!==a)o.pause()}}))</script></body></html>'''


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--voice', required=True)
    p.add_argument('--round', required=True, help='JSON file with "lines" and "tags"')
    p.add_argument('--out', default='tag-lab')
    p.add_argument('--model', default='eleven_v4')
    p.add_argument('--stability', type=float, default=0.5)
    p.add_argument('--similarity', type=float, default=0.75)
    p.add_argument('--key-file')
    args = p.parse_args()
    r = json.loads(pathlib.Path(args.round).read_text(encoding='utf-8'))
    lines, tags = r['lines'], [tuple(t) for t in r['tags']]
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    key = api_key(args.key_file)
    for lid, text in lines.items():
        for tid, tag in tags:
            synth(out, f'{lid}-{tid}', f'{tag} {text}'.strip(), args, key)
    (out / 'index.html').write_text(page(lines, tags, f'Tag lab · {args.voice} · {args.model}'), encoding='utf-8')
    print(f'{len(lines) * len(tags)} takes -> {out / "index.html"}')


if __name__ == '__main__':
    main()
