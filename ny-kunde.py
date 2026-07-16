#!/usr/bin/env python3
"""
Lager kundens nettside fra en mal.
Bruk: python3 ny-kunde.py <mal> <kundemappe> <datafil>
Eks:  python3 ny-kunde.py snekker lund-snekkerverksted kunde-data.txt
"""
import sys, os, shutil, re

if len(sys.argv) != 4:
    print(__doc__)
    sys.exit(1)

mal, kunde, datafil = sys.argv[1], sys.argv[2], sys.argv[3]
kilde = f"maler/demoer/{mal}"
mal_dir = os.path.expanduser(f"~/kunder/{kunde}")

if not os.path.isdir(kilde):
    print(f"✗ Fant ikke malen: {kilde}")
    sys.exit(1)
if os.path.exists(mal_dir):
    print(f"✗ Mappen finnes allerede: {mal_dir}")
    sys.exit(1)

# Les data
data = {}
tomme = []
for linje in open(datafil, encoding="utf-8"):
    linje = linje.strip()
    if not linje or linje.startswith("#") or "=" not in linje:
        continue
    n, v = linje.split("=", 1)
    if v.strip():
        data[n.strip()] = v.strip()
    else:
        tomme.append(n.strip())

# Kopier og erstatt
os.makedirs(os.path.expanduser("~/kunder"), exist_ok=True)
shutil.copytree(kilde, mal_dir)

endret = 0
for rot, _, filer in os.walk(mal_dir):
    for fil in filer:
        if not fil.endswith((".html", ".css")):
            continue
        sti = os.path.join(rot, fil)
        h = open(sti, encoding="utf-8").read()
        orig = h
        for n, v in data.items():
            h = h.replace(f"[{n}]", v)
        if h != orig:
            open(sti, "w", encoding="utf-8").write(h)
            endret += 1

# Sjekk hva som gjenstår
rest = set()
for rot, _, filer in os.walk(mal_dir):
    for fil in filer:
        if fil.endswith((".html", ".css")):
            rest |= set(re.findall(r"\[[A-Z_0-9]+\]", open(os.path.join(rot, fil), encoding="utf-8").read()))

shutil.copy(datafil, os.path.join(mal_dir, "kunde-data.txt"))

print(f"\n✓ Laget: {mal_dir}")
print(f"  {endret} filer oppdatert, {len(data)} verdier satt")
if tomme:
    print(f"\n⚠ Tomme felt i datafilen ({len(tomme)}): {', '.join(tomme)}")
if rest:
    print(f"\n⚠ Markører som IKKE ble fylt ut ({len(rest)}):")
    for m in sorted(rest):
        print(f"    {m}")
else:
    print("  Alle markører er fylt ut ✓")
