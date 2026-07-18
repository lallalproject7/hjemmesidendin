#!/usr/bin/env python3
"""
Lager en tilleggsseksjon tilpasset kundens design.
Bruk: python3 ny-seksjon.py <kunde> <type> <datafil>
Eks:  python3 ny-seksjon.py skien-elektro faq /tmp/seksjon.txt

Typer: faq · apningstider · sertifiseringer · priser
       dekningskart · prosess · sosiale · google
"""
import sys, os, re

FELLES_CSS = '''
/* ===== TILLEGGSSEKSJON: {navn} ===== */
.hsd-seksjon {{
    padding-block: 4.5rem;
    background: var(--hsd-bak);
}}
.hsd-ramme {{
    width: min(1100px, 90%);
    margin-inline: auto;
}}
.hsd-seksjon h2 {{
    color: var(--hsd-mork);
    margin-bottom: .5rem;
}}
.hsd-lead {{
    color: var(--hsd-tekst);
    margin-bottom: 2rem;
    max-width: 60ch;
}}
'''

def _les(sti):
    d = {}
    for l in open(sti, encoding="utf-8"):
        l = l.strip()
        if not l or l.startswith("#") or "=" not in l:
            continue
        k, v = l.split("=", 1)
        if v.strip():
            d[k.strip()] = v.strip()
    return d


def faq(d):
    par = []
    for i in range(1, 8):
        sp = d.get(f"FAQ_{i}_SP")
        svar = d.get(f"FAQ_{i}_SVAR")
        if sp and svar:
            par.append((sp, svar))
    if not par:
        return None, None, "Ingen spørsmål utfylt (FAQ_1_SP / FAQ_1_SVAR ...)"

    rader = "\n".join(
        f'''                <details class="hsd-faq">
                    <summary>{sp}</summary>
                    <p>{svar}</p>
                </details>''' for sp, svar in par)

    html = f'''    <!-- ===== FAQ ===== -->
    <section class="hsd-seksjon" id="faq">
        <div class="hsd-ramme">
            <h2>{d.get("FAQ_TITTEL", "Ofte stilte spørsmål")}</h2>
            <p class="hsd-lead">{d.get("FAQ_LEAD", "Spørsmål vi får ofte. Finner du ikke svaret? Ta gjerne kontakt.")}</p>
            <div class="hsd-faq-liste">
{rader}
            </div>
        </div>
    </section>'''

    css = FELLES_CSS.format(navn="FAQ") + '''
.hsd-faq-liste { display: grid; gap: .8rem; max-width: 780px; }
.hsd-faq {
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    overflow: hidden;
}
.hsd-faq summary {
    padding: 1.1rem 1.3rem;
    cursor: pointer;
    font-weight: 600;
    color: var(--hsd-mork);
    list-style: none;
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    transition: color .15s ease;
}
.hsd-faq summary::-webkit-details-marker { display: none; }
.hsd-faq summary::after {
    content: "+";
    color: var(--hsd-hoved);
    font-size: 1.3rem;
    line-height: 1;
    flex-shrink: 0;
}
.hsd-faq[open] summary::after { content: "–"; }
.hsd-faq summary:hover { color: var(--hsd-hoved); }
.hsd-faq p {
    padding: 0 1.3rem 1.2rem;
    color: var(--hsd-tekst);
    margin: 0;
}
'''
    return html, css, f"{len(par)} spørsmål"


def apningstider(d):
    DAGER = [("MAN","Mandag"),("TIR","Tirsdag"),("ONS","Onsdag"),("TOR","Torsdag"),
             ("FRE","Fredag"),("LOR","Lørdag"),("SON","Søndag")]
    rader = []
    for kode, navn in DAGER:
        tid = d.get(f"TID_{kode}")
        if not tid:
            continue
        stengt = ' hsd-stengt' if tid.lower().startswith("stengt") else ''
        rader.append(f'''                <div class="hsd-dag{stengt}">
                    <span>{navn}</span>
                    <strong>{tid}</strong>
                </div>''')
    if not rader:
        return None, None, "Ingen dager utfylt (TID_MAN, TID_TIR ...)"

    note = d.get("TID_NOTE")
    note_html = f'\n            <p class="hsd-note">{note}</p>' if note else ""

    html = f'''    <!-- ===== ÅPNINGSTIDER ===== -->
    <section class="hsd-seksjon" id="apningstider">
        <div class="hsd-ramme">
            <h2>{d.get("TID_TITTEL", "Åpningstider")}</h2>
            <p class="hsd-lead">{d.get("TID_LEAD", "Når du finner oss – og når vi er på jobb.")}</p>
            <div class="hsd-dager">
{chr(10).join(rader)}
            </div>{note_html}
        </div>
    </section>'''

    css = FELLES_CSS.format(navn="Åpningstider") + '''
.hsd-dager {
    max-width: 480px;
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    overflow: hidden;
}
.hsd-dag {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: .9rem 1.3rem;
    border-bottom: 1px solid var(--hsd-linje);
}
.hsd-dag:last-child { border-bottom: none; }
.hsd-dag span { color: var(--hsd-tekst); }
.hsd-dag strong { color: var(--hsd-mork); font-weight: 600; }
.hsd-stengt strong { color: var(--hsd-tekst); font-weight: 400; opacity: .7; }
.hsd-note {
    margin-top: 1rem;
    font-size: .9rem;
    color: var(--hsd-tekst);
    max-width: 480px;
}
'''
    return html, css, f"{len(rader)} dager"



def sertifiseringer(d):
    par = []
    for i in range(1, 7):
        n = d.get("SERT_%d_NAVN" % i)
        t = d.get("SERT_%d_TEKST" % i)
        if n:
            par.append((n, t or ""))
    if not par:
        return None, None, "Ingen sertifiseringer utfylt (SERT_1_NAVN ...)"
    kort = chr(10).join(
        '                <div class="hsd-sert">' + chr(10) +
        '                    <h3>%s</h3>' % n + chr(10) +
        ('                    <p>%s</p>' % t + chr(10) if t else '') +
        '                </div>' for n, t in par)
    garanti = d.get("SERT_GARANTI")
    g_html = (chr(10) + '            <div class="hsd-garanti"><strong>Garanti:</strong> %s</div>' % garanti) if garanti else ""
    html = ('    <!-- ===== SERTIFISERINGER ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="sertifiseringer">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("SERT_TITTEL", "Godkjenninger og garantier") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("SERT_LEAD", "Papirene i orden – så du vet hva du får.") + chr(10) +
        '            <div class="hsd-serter">' + chr(10) + kort + chr(10) +
        '            </div>' + g_html + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Sertifiseringer") + """
.hsd-serter { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; }
.hsd-sert {
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    padding: 1.4rem;
    border-top: 3px solid var(--hsd-hoved);
}
.hsd-sert h3 { color: var(--hsd-mork); font-size: 1.02rem; margin-bottom: .4rem; }
.hsd-sert p { color: var(--hsd-tekst); font-size: .9rem; margin: 0; }
.hsd-garanti {
    margin-top: 1.4rem;
    padding: 1.1rem 1.4rem;
    background: var(--hsd-mork);
    color: #fff;
    border-radius: var(--radius, 10px);
    font-size: .95rem;
}
@media (max-width: 900px) { .hsd-serter { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .hsd-serter { grid-template-columns: 1fr; } }
"""
    return html, css, "%d sertifiseringer" % len(par)


def priser(d):
    rader = []
    for i in range(1, 9):
        tj = d.get("PRIS_%d_TJENESTE" % i)
        pr = d.get("PRIS_%d_PRIS" % i)
        if tj:
            rader.append((tj, pr or "Etter avtale"))
    if not rader:
        return None, None, "Ingen priser utfylt (PRIS_1_TJENESTE ...)"
    linjer = chr(10).join(
        '                <div class="hsd-prisrad"><span>%s</span><strong>%s</strong></div>' % (tj, pr)
        for tj, pr in rader)
    note = d.get("PRIS_NOTE")
    n_html = (chr(10) + '            <p class="hsd-note">%s</p>' % note) if note else ""
    html = ('    <!-- ===== PRISER ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="priser">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("PRIS_TITTEL", "Priser") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("PRIS_LEAD", "Faste priser, ingen overraskelser.") + chr(10) +
        '            <div class="hsd-priser">' + chr(10) + linjer + chr(10) +
        '            </div>' + n_html + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Priser") + """
.hsd-priser {
    max-width: 640px;
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    overflow: hidden;
}
.hsd-prisrad {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
    padding: 1rem 1.4rem;
    border-bottom: 1px solid var(--hsd-linje);
}
.hsd-prisrad:last-child { border-bottom: none; }
.hsd-prisrad span { color: var(--hsd-tekst); }
.hsd-prisrad strong { color: var(--hsd-hoved); font-weight: 700; white-space: nowrap; }
"""
    return html, css, "%d priser" % len(rader)


def dekningskart(d):
    omr = [o.strip() for o in (d.get("KART_OMRADER", "")).split("|") if o.strip()]
    if not omr:
        return None, None, "Ingen omrader utfylt (KART_OMRADER=Skien | Porsgrunn | ...)"
    brikker = chr(10).join('                <span class="hsd-omrade">%s</span>' % o for o in omr)
    base = d.get("KART_BASE", "")
    b_html = ('            <p class="hsd-base">Vi holder til i <strong>%s</strong></p>' % base + chr(10)) if base else ""
    note = d.get("KART_NOTE")
    n_html = (chr(10) + '            <p class="hsd-note">%s</p>' % note) if note else ""
    html = ('    <!-- ===== DEKNINGSKART ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="dekning">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("KART_TITTEL", "Områdene vi dekker") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("KART_LEAD", "Her jobber vi til vanlig.") + chr(10) +
        b_html + '            <div class="hsd-omrader">' + chr(10) + brikker + chr(10) +
        '            </div>' + n_html + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Dekningskart") + """
.hsd-base { color: var(--hsd-tekst); margin-bottom: 1.2rem; }
.hsd-base strong { color: var(--hsd-mork); }
.hsd-omrader { display: flex; flex-wrap: wrap; gap: .7rem; }
.hsd-omrade {
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-left: 3px solid var(--hsd-hoved);
    border-radius: 6px;
    padding: .6rem 1.1rem;
    color: var(--hsd-mork);
    font-weight: 500;
    font-size: .95rem;
}
"""
    return html, css, "%d omrader" % len(omr)


def prosess(d):
    steg = []
    for i in range(1, 7):
        t = d.get("STEG_%d_TITTEL" % i)
        b = d.get("STEG_%d_TEKST" % i)
        if t:
            steg.append((i, t, b or ""))
    if not steg:
        return None, None, "Ingen steg utfylt (STEG_1_TITTEL ...)"
    kort = chr(10).join(
        '                <div class="hsd-steg">' + chr(10) +
        '                    <span class="hsd-steg-nr">%02d</span>' % i + chr(10) +
        '                    <h3>%s</h3>' % t + chr(10) +
        ('                    <p>%s</p>' % b + chr(10) if b else '') +
        '                </div>' for i, t, b in steg)
    html = ('    <!-- ===== SLIK JOBBER VI ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="prosess">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("STEG_TITTEL", "Slik jobber vi") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("STEG_LEAD", "Fra første kontakt til ferdig jobb.") + chr(10) +
        '            <div class="hsd-steg-liste">' + chr(10) + kort + chr(10) +
        '            </div>' + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Slik jobber vi") + """
.hsd-steg-liste { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.4rem; }
.hsd-steg { position: relative; padding-top: .5rem; }
.hsd-steg-nr {
    display: block;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--hsd-hoved);
    line-height: 1;
    margin-bottom: .6rem;
    opacity: .35;
}
.hsd-steg h3 { color: var(--hsd-mork); font-size: 1.05rem; margin-bottom: .4rem; }
.hsd-steg p { color: var(--hsd-tekst); font-size: .92rem; margin: 0; }
@media (max-width: 900px) { .hsd-steg-liste { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .hsd-steg-liste { grid-template-columns: 1fr; } }
"""
    return html, css, "%d steg" % len(steg)


def sosiale(d):
    KANALER = [("FB", "Facebook"), ("IG", "Instagram"), ("LI", "LinkedIn"),
               ("YT", "YouTube"), ("TT", "TikTok")]
    lenker = [(navn, d["SOS_" + kode]) for kode, navn in KANALER if d.get("SOS_" + kode)]
    if not lenker:
        return None, None, "Ingen lenker utfylt (SOS_FB, SOS_IG ...)"
    knapper = chr(10).join(
        '                <a href="%s" class="hsd-sos" target="_blank" rel="noopener">%s</a>' % (u, n)
        for n, u in lenker)
    html = ('    <!-- ===== SOSIALE MEDIER ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="sosiale">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("SOS_TITTEL", "Følg oss") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("SOS_LEAD", "Se hva vi jobber med for tiden.") + chr(10) +
        '            <div class="hsd-sosiale">' + chr(10) + knapper + chr(10) +
        '            </div>' + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Sosiale medier") + """
.hsd-sosiale { display: flex; flex-wrap: wrap; gap: .8rem; }
.hsd-sos {
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    padding: .8rem 1.5rem;
    color: var(--hsd-mork);
    text-decoration: none;
    font-weight: 600;
    transition: all .15s ease;
}
.hsd-sos:hover {
    background: var(--hsd-hoved);
    border-color: var(--hsd-hoved);
    color: #fff;
}
"""
    return html, css, "%d kanaler" % len(lenker)


def google(d):
    lenke = d.get("G_LENKE")
    if not lenke:
        return None, None, "Mangler G_LENKE (lenke til Google-profilen)"
    stjerner = d.get("G_STJERNER", "")
    antall = d.get("G_ANTALL", "")
    vis = ""
    if stjerner:
        vis = ('            <div class="hsd-g-tall">' + chr(10) +
               '                <strong>%s</strong>' % stjerner + chr(10) +
               '                <span class="hsd-g-stjerner">★★★★★</span>' + chr(10) +
               ('                <span class="hsd-g-antall">%s anmeldelser</span>' % antall + chr(10) if antall else '') +
               '            </div>' + chr(10))
    be_om = d.get("G_BE_OM", "").lower() in ("ja", "yes", "1")
    knapper = '                <a href="%s" class="hsd-g-knapp" target="_blank" rel="noopener">Les anmeldelsene på Google</a>' % lenke
    if be_om:
        knapper += (chr(10) + '                <a href="%s" class="hsd-g-knapp hsd-g-tom" target="_blank" rel="noopener">Gi oss en anmeldelse</a>' % lenke)
    tp = d.get("G_TRUSTPILOT")
    if tp:
        knapper += (chr(10) + '                <a href="%s" class="hsd-g-knapp hsd-g-tom" target="_blank" rel="noopener">Se oss på Trustpilot</a>' % tp)
    html = ('    <!-- ===== GOOGLE-ANMELDELSER ===== -->' + chr(10) +
        '    <section class="hsd-seksjon" id="anmeldelser">' + chr(10) +
        '        <div class="hsd-ramme">' + chr(10) +
        '            <h2>%s</h2>' % d.get("G_TITTEL", "Anmeldelser fra kundene våre") + chr(10) +
        '            <p class="hsd-lead">%s</p>' % d.get("G_LEAD", "Ekte tilbakemeldinger, hentet fra Google.") + chr(10) +
        vis + '            <div class="hsd-g-knapper">' + chr(10) + knapper + chr(10) +
        '            </div>' + chr(10) + '        </div>' + chr(10) + '    </section>')
    css = FELLES_CSS.format(navn="Google-anmeldelser") + """
.hsd-g-tall {
    display: flex;
    align-items: center;
    gap: .8rem;
    background: var(--hsd-flate);
    border: 1px solid var(--hsd-linje);
    border-radius: var(--radius, 10px);
    padding: 1.2rem 1.6rem;
    margin-bottom: 1.4rem;
    max-width: fit-content;
}
.hsd-g-tall strong { font-size: 2rem; color: var(--hsd-mork); line-height: 1; }
.hsd-g-stjerner { color: #fbbc04; font-size: 1.2rem; letter-spacing: .1em; }
.hsd-g-antall { color: var(--hsd-tekst); font-size: .9rem; }
.hsd-g-knapper { display: flex; flex-wrap: wrap; gap: .8rem; }
.hsd-g-knapp {
    background: var(--hsd-hoved);
    color: #fff;
    border-radius: var(--radius, 10px);
    padding: .8rem 1.5rem;
    text-decoration: none;
    font-weight: 600;
    transition: opacity .15s ease;
}
.hsd-g-knapp:hover { opacity: .88; }
.hsd-g-tom {
    background: transparent;
    color: var(--hsd-mork);
    border: 1px solid var(--hsd-linje);
}
.hsd-g-tom:hover { border-color: var(--hsd-hoved); color: var(--hsd-hoved); opacity: 1; }
"""
    return html, css, "Google-lenke + %d knapper" % (1 + int(be_om) + int(bool(tp)))


SEKSJONER = {
    "faq": faq,
    "apningstider": apningstider,
    "sertifiseringer": sertifiseringer,
    "priser": priser,
    "dekningskart": dekningskart,
    "prosess": prosess,
    "sosiale": sosiale,
    "google": google,
}

# ── Kjør ──
if len(sys.argv) != 4:
    print(__doc__); sys.exit(1)

kunde, type_, datafil = sys.argv[1], sys.argv[2], sys.argv[3]
mappe = os.path.expanduser(f"~/kunder/{kunde}")

if not os.path.isdir(mappe):
    print(f"✗ Fant ikke kunden: {mappe}"); sys.exit(1)
if type_ not in SEKSJONER:
    print(f"✗ Ukjent type: {type_}\n  Gyldige: {', '.join(SEKSJONER)}"); sys.exit(1)
if not os.path.exists(datafil):
    print(f"✗ Fant ikke datafilen: {datafil}"); sys.exit(1)

css_sti = os.path.join(mappe, "css", "style.css")
if "--hsd-hoved" not in open(css_sti, encoding="utf-8").read():
    print("✗ Kundens CSS mangler alias (--hsd-*). Er siden laget fra en oppdatert mal?")
    sys.exit(1)

html, css, melding = SEKSJONER[type_](_les(datafil))
if not html:
    print(f"✗ {melding}"); sys.exit(1)

# CSS – erstatt hvis den finnes fra før
merke = f"/* ===== TILLEGGSSEKSJON: "
s = open(css_sti, encoding="utf-8").read()
navn = re.search(r'/\* ===== TILLEGGSSEKSJON: ([^=]+) =====', css).group(1).strip()
s = re.sub(rf'\n/\* ===== TILLEGGSSEKSJON: {re.escape(navn)} =====.*?(?=\n/\* =====|\Z)', '', s, flags=re.S)
open(css_sti, "w", encoding="utf-8").write(s.rstrip() + "\n\n" + css)

# HTML – lagres til fil, du limer den inn der du vil ha den
ut = os.path.join(mappe, f"SEKSJON-{type_}.html")
open(ut, "w", encoding="utf-8").write(html + "\n")

print(f"\n✓ Seksjon '{type_}' laget ({melding})")
print(f"  CSS lagt til:  {css_sti}")
print(f"  HTML klar i:   {ut}")
print(f"\n  Neste: åpne {ut}, kopier innholdet,")
print(f"  og lim det inn i index.html der seksjonen skal stå.")
