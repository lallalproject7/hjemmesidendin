# Rutine: fra bestilling til levert nettside

    cd ~/hjemmesidendin
    cp maler/kunde-data-mal.txt /tmp/data.txt
    code /tmp/data.txt
    python3 ny-kunde.py <mal> <kunde> /tmp/data.txt
    code ~/kunder/<kunde>
    python3 koble-bilder.py <kunde>
    python3 sjekk.py <kunde>

## Maler
rorlegger · elektriker · snekker · maler · renhold · gartner · flyttebyra
(+ samme med -moderne)

## Bildenavn
logo.png · hero.jpg · team.jpg · galleri1.jpg ... galleri6.jpg
Små bokstaver. Under 1 MB.


## Bilder: fra kunde til nettside

Cloudinary brukes kun som mellomstasjon. Kunden laster opp bildene i skjemaet,
de havner i Cloudinary, og derfra tar vi dem videre.

1. Kunden laster opp bildene i bestillingsskjemaet
2. Last ned bildene fra Cloudinary
3. Gi dem riktig navn (se Bildenavn under) og legg dem i kundemappens bilder/
4. Kjør: python3 koble-bilder.py <kundemappe>
5. Optimaliser og legg dem ut med nettsiden på Netlify (betalt plan)
6. Slett bildene i Cloudinary, slik at gratiskvoten ikke fylles opp

Netlify står for hosting, SSL og CDN. Domenet kjopes hos domene.no og
registreres på kundens firma. Sikkerhetskopi er ikke inkludert i Netlify —
det løses med git.


## Bilder steg for steg (kommandoer)

Etter at kunden har sendt inn skjemaet:

    # 1. Last ned bildene fra Cloudinary til kundens bilder-mappe
    #    Gi dem riktig navn: logo, hero, om, galleri1..16, arbeid1..6, tjeneste1..3

    # 2. Optimaliser (originalene lagres i bilder-original/)
    python3 optimize-kundebilder.py <kundemappe>

    # 3. Koble bildene til nettsiden
    python3 koble-bilder.py <kundemappe>

    # 4. Sjekk at alt er på plass
    python3 sjekk.py <kundemappe>

    # 5. Legg ut på Netlify (betalt plan)

    # 6. Slett bildene i Cloudinary så gratiskvoten ikke fylles opp

Bildene skaleres til 1200 px bredde og lagres med kvalitet 82.
Et optimalisert galleribilde havner typisk på 150-250 kB.
Last aldri opp bilder rett fra kameraet - de kan veie 5 MB hver.

Merk: bildene ligger som bakgrunnsbilder i CSS, ikke som img-tagger.
Derfor virker ikke lazy loading. Optimaliseringen i steg 2 er det som
holder nettsiden rask - den er ikke valgfri.
