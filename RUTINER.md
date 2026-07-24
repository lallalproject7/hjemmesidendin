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
