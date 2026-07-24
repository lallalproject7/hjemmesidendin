#!/usr/bin/env python3
"""
Sjekker at demo, skjema og mal ber om og viser det samme.
Bruk: python3 sjekk-samsvar.py
"""
import re, os, glob

def les(sti):
    return open(sti, encoding="utf-8").read() if os.path.exists(sti) else ""

def tell_bilder_demo(h):
    """Bildeplasser i demoen: img-tagger + kjente bakgrunnsklasser."""
    n = len(re.findall(r'<img\b', h))
    for m in re.finditer(r'class="([^"]+)"', h):
        kl = m.group(1)
        if re.search(r'\b(vb\d+|vf-arbeid\d+|pb\d+|photo-galleri\d+|photo-hero|photo-om|hero-blokk|om-visual|om-foto|hero-foto-inner)\b', kl):
            n += 1
    return n


def tell_tekstfelt(skjema):
    """Grupper av tekstfelt i skjemaet: tjeneste1_tittel -> {'tjeneste': 6}"""
    ut = {}
    for navn in set(re.findall(r'name="([a-z]+)(\d+)_[a-z]+"', skjema)):
        pass
    for gruppe, nr in re.findall(r'name="([a-z]+)(\d+)_[a-z]+"', skjema):
        ut[gruppe] = max(ut.get(gruppe, 0), int(nr))
    return ut


def tell_tekstblokker(demo):
    """Hvor mange tjenester/prosjekter demoen faktisk viser."""
    ut = {}
    ut["tjeneste"] = len(re.findall(r'class="tjeneste(?:["\s])', demo)) + \
                     len(re.findall(r'class="tjeneste-enkel"', demo)) + \
                     len(re.findall(r'class="tjeneste-rad"', demo))
    ut["prosjekt"] = len(re.findall(r'class="prosjekt"', demo)) + \
                     len(re.findall(r'class="arbeid-kort"', demo))
    ut["galleri"] = len(re.findall(r'class="verk[ "]', demo)) + \
                    len(re.findall(r'data-kat=', demo))
    return {k: v for k, v in ut.items() if v}


bransjer = sorted({os.path.basename(p).replace("bestill-", "").replace(".html", "")
                   for p in glob.glob("bestill-*.html")})

print("bransje          skjema  demo(kl/mod)  mal(kl/mod)   status")
print("─" * 66)
feil = 0
for b in bransjer:
    skjema = les(f"bestill-{b}.html")
    felt = len(set(re.findall(r'data-type="([^"]+)"', skjema)))

    rader = []
    for variant in (b, f"{b}-moderne"):
        demo = les(f"demoer/{variant}/index.html")
        mal  = les(f"maler/demoer/{variant}/index.html")
        if not demo:
            rader.append((None, None, None)); continue
        d_ant = tell_bilder_demo(demo)
        m_ant = len(set(re.findall(r'photo-(?:galleri\d+|arbeid\d+|tjeneste\d+|hero|om)', mal)))
        unsplash = "unsplash" in mal
        rader.append((d_ant, m_ant, unsplash))

    demo_tekst = "/".join(str(r[0]) if r[0] is not None else "-" for r in rader)
    mal_tekst  = "/".join(str(r[1]) if r[1] is not None else "-" for r in rader)

    problemer = []
    for i, r in enumerate(rader):
        if r[0] is None: continue
        navn = "klassisk" if i == 0 else "moderne"
        if r[2]: problemer.append(f"unsplash i mal ({navn})")
        if r[1] == 0: problemer.append(f"mal mangler bildeplasser ({navn})")
        elif abs(r[0] - r[1]) > 1: problemer.append(f"demo {r[0]} vs mal {r[1]} ({navn})")

    maks_mal = max([r[1] for r in rader if r[1] is not None] or [0])
    if felt and maks_mal and felt + 2 < maks_mal:
        problemer.append(f"skjema {felt} felt, mal trenger {maks_mal}")

    # Tekstfelt: ber skjemaet om flere enn demoen viser?
    felt_tekst = tell_tekstfelt(skjema)
    for i, variant in enumerate((b, f"{b}-moderne")):
        demo = les(f"demoer/{variant}/index.html")
        if not demo: continue
        navn = "klassisk" if i == 0 else "moderne"
        vist = tell_tekstblokker(demo)
        for gruppe, ant in felt_tekst.items():
            if gruppe in vist and ant > vist[gruppe]:
                problemer.append(f"skjema ber om {ant} {gruppe}, demo viser {vist[gruppe]} ({navn})")

    status = "ok" if not problemer else "; ".join(problemer)
    if problemer: feil += 1
    print(f"{b:16} {felt:>4}   {demo_tekst:>10}   {mal_tekst:>10}   {status}")

print("─" * 66)
print(f"{len(bransjer) - feil} av {len(bransjer)} bransjer uten avvik")
