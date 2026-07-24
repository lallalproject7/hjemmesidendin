#!/usr/bin/env python3
"""
Kobler bildene i kundens bilder/-mappe til nettsiden.
Kjør ETTER at du har lagt bildene i mappen.

Bruk: python3 koble-bilder.py <kundemappe>
Eks:  python3 koble-bilder.py skien-elektro

Filnavn som gjenkjennes:
  logo.png · hero.jpg · team.jpg · galleri1.jpg ... galleri16.jpg · prosjekt1.jpg ... · arbeid1.jpg ...
"""
import sys, os, re

if len(sys.argv) != 2:
    print(__doc__); sys.exit(1)

mappe = os.path.expanduser(f"~/kunder/{sys.argv[1]}")
if not os.path.isdir(mappe):
    print(f"✗ Fant ikke: {mappe}"); sys.exit(1)

bildemappe = os.path.join(mappe, "bilder")
css_sti = os.path.join(mappe, "css", "style.css")
os.makedirs(bildemappe, exist_ok=True)

kart = {"hero": ".photo-hero", "team": ".photo-om", "om": ".photo-om"}
for i in range(1, 17):
    kart[f"galleri{i}"] = f".photo-galleri{i}"
    kart[f"prosjekt{i}"] = f".photo-galleri{i}"
    kart[f"arbeid{i}"] = f".photo-arbeid{i}"
    kart[f"tjeneste{i}"] = f".photo-tjeneste{i}"

css, funnet, ukjent, logo = [], [], [], None
for fil in sorted(os.listdir(bildemappe)):
    navn, ext = os.path.splitext(fil)
    if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
        continue
    if navn.lower() == "logo":
        logo = fil; continue
    klasse = kart.get(navn.lower())
    if not klasse:
        ukjent.append(fil); continue
    css.append(f'{klasse} {{\n    background-image: url("../bilder/{fil}");\n'
               f'    background-size: cover;\n    background-position: center;\n}}')
    css.append(f'{klasse} span {{ display: none; }}')
    funnet.append(fil)

if logo:
    css.append(f'.logo-mark {{\n    background-image: url("../bilder/{logo}");\n'
               f'    background-size: contain;\n    background-repeat: no-repeat;\n'
               f'    background-position: center;\n    font-size: 0;\n'
               f'    width: 2.2rem;\n    height: 2.2rem;\n}}')
    funnet.append(logo)

# Fjern gammel bilde-CSS (så du kan kjøre på nytt)
h = open(css_sti, encoding="utf-8").read()
h = re.sub(r'\n*/\* ===== KUNDENS BILDER ===== \*/.*$', '', h, flags=re.S)

if css:
    h += "\n\n/* ===== KUNDENS BILDER ===== */\n" + "\n".join(css) + "\n"
open(css_sti, "w", encoding="utf-8").write(h)

print(f"\n✓ {mappe}")
if funnet:
    print(f"  {len(funnet)} bilder koblet:")
    for f in funnet: print(f"    · {f}")
else:
    print("  ⚠ Ingen bilder funnet – legg dem i bilder/ og kjør på nytt")
if ukjent:
    print(f"\n  ? Ukjente filnavn ({len(ukjent)}): {', '.join(ukjent)}")
    print("    Gyldige navn: logo · hero · team · galleri1–16 · prosjekt1–16 · arbeid1–16")

# ===== Fjern blokker uten bilde =====
import glob as _glob
brukte = {os.path.splitext(f)[0].lower() for f in funnet}
fjernet = []
for html_sti in _glob.glob(os.path.join(mappe, "*.html")):
    h = open(html_sti, encoding="utf-8").read()
    original = h
    for m in list(re.finditer(r'<(\w+)[^>]*data-blokk="([^"]+)"', h)):
        tag, navn = m.group(1), m.group(2)
        if navn.lower() in brukte:
            continue
        start = m.start()
        dyp, pos = 0, start
        while True:
            aapne = h.find("<" + tag, pos)
            lukke = h.find("</" + tag + ">", pos)
            if lukke == -1:
                break
            if aapne != -1 and aapne < lukke:
                dyp += 1; pos = aapne + len(tag) + 1
            else:
                dyp -= 1; pos = lukke + len(tag) + 3
                if dyp == 0:
                    break
        h = h[:start] + h[pos:]
        fjernet.append(navn)
    if h != original:
        open(html_sti, "w", encoding="utf-8").write(h)
if fjernet:
    print("  Fjernet", len(fjernet), "blokker uten bilde:", ", ".join(sorted(set(fjernet))))
