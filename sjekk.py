#!/usr/bin/env python3
"""
Sjekker kundens nettside før levering.
Bruk: python3 sjekk.py <kundemappe>
"""
import sys, os, re

if len(sys.argv) != 2:
    print(__doc__); sys.exit(1)

kunde = sys.argv[1]
mappe = os.path.expanduser(f"~/kunder/{kunde}")
if not os.path.isdir(mappe):
    print(f"✗ Fant ikke: {mappe}"); sys.exit(1)

ok, advarsel, feil = [], [], []

def les(*p):
    sti = os.path.join(mappe, *p)
    return open(sti, encoding="utf-8").read() if os.path.exists(sti) else None

html = les("index.html")
css  = les("css", "style.css")
pv   = les("personvern.html")
ck   = les("cookies.html")

# 1. Filer finnes
for navn, inn in [("index.html", html), ("css/style.css", css),
                  ("personvern.html", pv), ("cookies.html", ck)]:
    (ok if inn else feil).append(f"{navn} {'finnes' if inn else 'MANGLER'}")

# 2. Markører
for navn, inn in [("index.html", html), ("css/style.css", css),
                  ("personvern.html", pv), ("cookies.html", ck)]:
    if not inn: continue
    m = sorted(set(re.findall(r'\[[A-Z][A-Z_0-9]*\]', inn)))
    if m: feil.append(f"{navn}: ufylte markører → {', '.join(m)}")
if not any("markører" in f for f in feil):
    ok.append("Ingen ufylte markører")

# 3. Demo-data
DEMO = ["Fossum", "Nordvik", "Lund Snekker", "Lien Snekker", "Berg Maler",
        "Klar Renhold", "Grønn Hage", "Trygg Flytt", "Voltek", "999 999 999",
        "lundsnekker", "nordvikror", "fossumelektro", "bergmaler", "klarrenhold",
        "gronnhage", "tryggflytt", "voltek", "liensnekker"]
rest = set()
for inn in [html, css, pv, ck]:
    if inn:
        rest |= {d for d in DEMO if d in inn}
if rest: feil.append(f"Demo-data igjen: {', '.join(sorted(rest))}")
else: ok.append("Ingen demo-data")

# 4. Demo-banner
if html and "demo-bestill" in html:
    feil.append("demo-bestill-banner ligger igjen (skal ikke være hos kunden)")
elif html:
    ok.append("Ingen demo-banner")

# 5. Firmanavn stemmer overens
if html and pv:
    f1 = re.search(r'<title>([^<–|]*)', html)
    f2 = re.search(r'class="jur-merke">([^<]*)</a>', pv)
    if f1 and f2:
        a, b = f1.group(1).strip(), f2.group(1).strip()
        if b and b in a: ok.append(f"Firmanavn matcher: {b}")
        else: feil.append(f"Firmanavn ulikt: index='{a}' vs personvern='{b}'")

# 6. Interne lenker
if html:
    for lenke in set(re.findall(r'href="(?!http|#|mailto|tel)([^"]+)"', html)):
        if not os.path.exists(os.path.join(mappe, lenke.split("#")[0])):
            feil.append(f"Død lenke: {lenke}")
    if not any("Død lenke" in f for f in feil):
        ok.append("Alle interne lenker fungerer")

# 7. Bilder
bmappe = os.path.join(mappe, "bilder")
GYLDIGE = ["logo", "hero", "team", "om"] + [f"galleri{i}" for i in range(1, 7)] + [f"arbeid{i}" for i in range(1, 7)]
if os.path.isdir(bmappe):
    filer = [f for f in os.listdir(bmappe) if not f.startswith(".")]
    if not filer:
        advarsel.append("bilder/ er tom – placeholders vises")
    for f in filer:
        navn, ext = os.path.splitext(f)
        if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
            advarsel.append(f"bilder/{f} – ukjent filtype"); continue
        if navn.lower() not in GYLDIGE:
            advarsel.append(f"bilder/{f} – feil navn (gyldige: {', '.join(GYLDIGE[:4])}...)")
        elif navn != navn.lower():
            advarsel.append(f"bilder/{f} – bruk små bokstaver: {navn.lower()}{ext.lower()}")
        mb = os.path.getsize(os.path.join(bmappe, f)) / 1_000_000
        if mb > 1: advarsel.append(f"bilder/{f} er {mb:.1f} MB – bør optimaliseres (under 1 MB)")
    # Er bildene koblet?
    if filer and css and "KUNDENS BILDER" not in css:
        feil.append("Bilder finnes, men er IKKE koblet → kjør: python3 koble-bilder.py " + kunde)
    elif filer and css:
        ok.append(f"{len(filer)} bilder koblet")

# 8. Placeholders igjen
if css:
    aktive = set(re.findall(r'\.photo-([a-z0-9]+)\s*\{[^}]*background-image', css))
    alle = set(re.findall(r'photo-([a-z0-9]+)', html or "")) - {"placeholder"}
    mangler = alle - aktive
    if mangler:
        advarsel.append(f"Uten bilde ({len(mangler)}): {', '.join(sorted(mangler))} – grå placeholder vises")

# Rapport
print(f"\n{'═'*46}\n  SJEKK: {kunde}\n{'═'*46}")
for x in ok: print(f"  ✓ {x}")
if advarsel:
    print(f"\n  ⚠ ADVARSLER ({len(advarsel)}):")
    for x in advarsel: print(f"    · {x}")
if feil:
    print(f"\n  ✗ FEIL ({len(feil)}):")
    for x in feil: print(f"    · {x}")
print()
if feil:   print("  🔴 IKKE KLAR – rett feilene over\n")
elif advarsel: print("  🟡 KLAR, men sjekk advarslene\n")
else:      print("  🟢 KLAR TIL LEVERING\n")
sys.exit(1 if feil else 0)
