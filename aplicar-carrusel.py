#!/usr/bin/env python3
"""Reconstruye la sección de precio con carrusel de beneficios."""
doc = open("index.html", encoding="utf-8").read()

inicio = doc.find('<section class="section" id="pris">')
if inicio == -1:
    inicio = doc.find('id="pris"')
    inicio = doc.rfind('<section', 0, inicio)
fin = doc.find('</section>', inicio) + len('</section>')
viejo = doc[inicio:fin]

nuevo = '''<section class="section" id="pris">
        <div class="container container-narrow">
            <p class="eyebrow">Fast pris, ingen dyre abonnement</p>
            <h2>Betal for nettsiden én gang</h2>
            <p class="section-lead">Ingen dyre månedsabonnement. Du betaler for nettsiden én gang – og en liten årsavgift som kun dekker det som faktisk holder siden på nett.</p>

            <div class="priskort">
                <p class="pris-belop">8 900 kr <span class="pris-mva">eks. mva<button type="button" class="mva-info" aria-label="Om mva">ⓘ<span class="mva-boks">Prisen er oppgitt uten mva. Vi er ikke mva-registrert ennå – mva legges til først når omsetningen passerer 50 000 kr, i tråd med norske regler. For bedriftskunder er mva uansett fradragsberettiget.</span></button></span></p>
                <p class="pris-under">Engangspris for design og bygging av nettsiden.</p>

                <a href="bestill.html" class="btn btn-primary btn-lg">Bestill nettside</a>

                <div class="pris-lenker">
                    <a href="endringsrunde.html">Slik fungerer endringsrunden</a>
                    <span>·</span>
                    <a href="#oppdateringer">Se priser for oppdateringer</a>
                </div>
            </div>

            <div class="ben-carrusel-wrap">
                <div class="ben-carrusel-track">
                    <div class="ben-kort ben-oransje"><span class="ben-ikon">🌐</span>Komplett nettside tilpasset din bedrift</div>
                    <div class="ben-kort ben-gronn"><span class="ben-ikon">📧</span>Kontaktskjema som sender henvendelser rett til din e-post</div>
                    <div class="ben-kort ben-kobber"><span class="ben-ikon">🌍</span>Vi registrerer domenet ditt – i ditt navn, du eier det</div>
                    <div class="ben-kort ben-gronn2"><span class="ben-ikon">📱</span>Tilpasset mobil, nettbrett og PC</div>
                    <div class="ben-kort ben-oransje"><span class="ben-ikon">⚖️</span>Personvernerklæring og lovpålagte sider inkludert</div>
                    <div class="ben-kort ben-gronn"><span class="ben-ikon">⚡</span>Levert innen 7 virkedager etter oppstart</div>
                    <div class="ben-kort ben-kobber"><span class="ben-ikon">🔄</span>Én gratis endringsrunde – inntil 10 justeringer</div>
                    <div class="ben-kort ben-gronn2"><span class="ben-ikon">🖥️</span>Første år med drift, domene og hosting inkludert</div>
                    <div class="ben-kort ben-oransje"><span class="ben-ikon">🌐</span>Komplett nettside tilpasset din bedrift</div>
                    <div class="ben-kort ben-gronn"><span class="ben-ikon">📧</span>Kontaktskjema som sender henvendelser rett til din e-post</div>
                    <div class="ben-kort ben-kobber"><span class="ben-ikon">🌍</span>Vi registrerer domenet ditt – i ditt navn, du eier det</div>
                    <div class="ben-kort ben-gronn2"><span class="ben-ikon">📱</span>Tilpasset mobil, nettbrett og PC</div>
                </div>
            </div>

            <div class="pris-arsavgift">
                <div>
                    <strong>+ 777 kr / år</strong>
                    <span>eks. mva</span>
                </div>
                <p>Drift, domene og vedlikehold – <strong>første år er inkludert</strong>. Dekker at siden er på nett og domenet ditt fornyes.</p>
            </div>
        </div>
    </section>'''

if doc.count(viejo) == 1:
    doc = doc.replace(viejo, nuevo)
    open("index.html", "w", encoding="utf-8").write(doc)
    print("✓ Sección reconstruida con carrusel (links e info conservados)")
else:
    print(f"⚠ Encontré la sección {doc.count(viejo)} veces. No toqué nada.")