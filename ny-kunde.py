#!/usr/bin/env python3
"""
Lager kundens nettside fra en mal.
Bruk: python3 ny-kunde.py <mal> <kundemappe> <datafil>
Eks:  python3 ny-kunde.py snekker lund-snekkerverksted kunde-data.txt
"""
import re, sys, os, shutil, re

def _rgb(x):
    x = x.lstrip("#")
    return tuple(int(x[i:i+2], 16) for i in (0, 2, 4))

def _hex(r, g, b):
    return "#%02x%02x%02x" % (max(0,min(255,int(r))), max(0,min(255,int(g))), max(0,min(255,int(b))))

def morkere(farge, f=0.78):
    r, g, b = _rgb(farge)
    return _hex(r*f, g*f, b*f)

def lysere(farge, f=0.35):
    r, g, b = _rgb(farge)
    return _hex(r+(255-r)*f, g+(255-g)*f, b+(255-b)*f)


def legg_til_bilder(mappe):
    """Lager CSS for bildene som faktisk ligger i bilder/."""
    bildemappe = os.path.join(mappe, "bilder")
    if not os.path.isdir(bildemappe):
        return []

    # filnavn (uten endelse) -> CSS-klasse
    kart = {"hero": ".photo-hero", "team": ".photo-om", "om": ".photo-om"}
    for i in range(1, 7):
        kart[f"galleri{i}"] = f".photo-galleri{i}"
        kart[f"arbeid{i}"] = f".photo-galleri{i}"

    css, funnet, logo = [], [], None
    for fil in sorted(os.listdir(bildemappe)):
        navn, ext = os.path.splitext(fil)
        if ext.lower() not in (".jpg", ".jpeg", ".png", ".webp", ".svg"):
            continue
        if navn.lower() == "logo":
            logo = fil
            continue
        klasse = kart.get(navn.lower())
        if not klasse:
            print(f"    ? {fil} – ukjent navn, hoppet over")
            continue
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

    if css:
        sti = os.path.join(mappe, "css", "style.css")
        with open(sti, "a", encoding="utf-8") as f:
            f.write("\n\n/* ===== KUNDENS BILDER ===== */\n" + "\n".join(css) + "\n")
    return funnet

def formater_typed(data):
    """TYPED_ORD=a | b | c  ->  "a", "b", "c"  (JS-array-innhold)"""
    if "TYPED_ORD" in data:
        ord_liste = [o.strip() for o in data["TYPED_ORD"].split("|") if o.strip()]
        data["TYPED_ORD"] = ", ".join(f'"{o}"' for o in ord_liste)
    return data

def utled_farger(data):
    """Regner ut avledede fargetoner fra de fire kundevalgte."""
    if "FARGE_HOVED" in data:
        data.setdefault("FARGE_HOVED_MORK", morkere(data["FARGE_HOVED"]))
        data.setdefault("FARGE_HOVED_LYS", lysere(data["FARGE_HOVED"]))
    if "FARGE_MORK" in data:
        data.setdefault("FARGE_MORK_DYP", morkere(data["FARGE_MORK"], 0.7))
        data.setdefault("FARGE_MORK_LYS", lysere(data["FARGE_MORK"], 0.18))
    return data



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

def fjern_tomme_blokker(h, tomme):
    """Marcador vacío con data-blokk -> borra el bloque; si no -> deja vacío."""
    tomme_lower = {t.lower() for t in tomme}
    while True:
        borret = False
        for m in re.finditer(r'<(\w+)[^>]*data-blokk="([^"]+)"', h):
            tag, navn = m.group(1), m.group(2)
            if navn.lower() not in tomme_lower:
                continue
            start = m.start(); dyp, pos = 0, start
            while True:
                aapne = h.find("<" + tag, pos); lukke = h.find("</" + tag + ">", pos)
                if lukke == -1: break
                if aapne != -1 and aapne < lukke:
                    dyp += 1; pos = aapne + len(tag) + 1
                else:
                    dyp -= 1; pos = lukke + len(tag) + 3
                    if dyp == 0: break
            h = h[:start] + h[pos:]; borret = True; break
        if not borret: break
    for t in tomme:
        h = h.replace(f"[{t}]", "")
    return h


def prosess_til_liste(data):
    """Marcador _PROSESS con varias linjer -> _PROSESS_LISTE med <li>."""
    import html as _html
    nye = {}
    for n, v in list(data.items()):
        if n.endswith("_PROSESS"):
            linjer = [l.strip() for l in v.replace("\r","").split("\n") if l.strip()]
            nye[n + "_LISTE"] = "".join(f"<li>{_html.escape(l)}</li>" for l in linjer)
    data.update(nye)
    return data


def lag_sammendrag(data):
    """Junta MN_VERDI1..3 i MN_SAMMENDRAG (kort tekst til prosjektlista)."""
    nye = {}
    for pre in ["M1","M2","M3","M4","M5","M6","T1","T2","T3","T4","T5","T6"]:
        verdier = [data.get(f"{pre}_VERDI{i}","").strip() for i in (1,2,3)]
        verdier = [v for v in verdier if v]
        if verdier:
            nye[f"{pre}_SAMMENDRAG"] = " · ".join(verdier)
    data.update(nye)
    return data


def kompetanse_til_tagger(data):
    """KOMPETANSE=a; b; c -> KOMPETANSE_TAGGER = <span>a</span>..."""
    import html as _html
    if "KOMPETANSE" in data:
        deler = [d.strip() for d in data["KOMPETANSE"].replace("\n",";").split(";") if d.strip()]
        data["KOMPETANSE_TAGGER"] = "".join(f"<span>{_html.escape(d)}</span>" for d in deler)
    # Tagger per prosjekt (moderne): M1_TAGGER -> M1_TAGGER_HTML
    for n in range(1, 7):
        n_key = f"M{n}_TAGGER"
        if n_key in data:
            deler = [d.strip() for d in data[n_key].replace("\n",";").split(";") if d.strip()]
            data[f"M{n}_TAGGER_HTML"] = "".join(f"<span>{_html.escape(d)}</span>" for d in deler)
    return data


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

data = utled_farger(data)
data = formater_typed(data)
data = prosess_til_liste(data)
data = lag_sammendrag(data)
data = kompetanse_til_tagger(data)

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
        h = fjern_tomme_blokker(h, tomme)
        if h != orig:
            open(sti, "w", encoding="utf-8").write(h)
            endret += 1

# Sjekk hva som gjenstår
rest = set()
for rot, _, filer in os.walk(mal_dir):
    for fil in filer:
        if fil.endswith((".html", ".css")):
            rest |= set(re.findall(r"\[[A-Z][A-Z_0-9]*\]", open(os.path.join(rot, fil), encoding="utf-8").read()))

bilder = legg_til_bilder(mal_dir)
shutil.copy(datafil, os.path.join(mal_dir, "kunde-data.txt"))

print(f"\n✓ Laget: {mal_dir}")
print(f"  {endret} filer oppdatert, {len(data)} verdier satt")
if bilder:
    print(f"  {len(bilder)} bilder koblet: {', '.join(bilder)}")
else:
    print("  ⚠ Ingen bilder i bilder/ – placeholders vises")
if tomme:
    print(f"\n⚠ Tomme felt i datafilen ({len(tomme)}): {', '.join(tomme)}")
if rest:
    print(f"\n⚠ Markører som IKKE ble fylt ut ({len(rest)}):")
    for m in sorted(rest):
        print(f"    {m}")
else:
    print("  Alle markører er fylt ut ✓")
