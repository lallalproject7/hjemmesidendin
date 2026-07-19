# FLUJO DE ACTUALIZACIONES — Hjemmesidendin

Cómo procesar un pedido de actualización (cliente que YA tiene web y
quiere añadir una sección extra, pagada aparte).

---

## EL FLUJO COMPLETO (resumen)

```
1. Cliente rellena oppdatering.html → elige sección + rellena datos
2. Te llega un email con el resumen (formato legible)
3. Buscas la carpeta del cliente:  python3 finn-kunde.py <texto>
4. Conviertes el resumen al formato del script (a mano, ver tablas)
5. Generas la sección:  python3 ny-seksjon.py <cliente> <tipo> <datos>
6. Pegas el HTML generado en el index.html del cliente
7. Deploy + cobras
```

Todos los comandos se ejecutan desde ~/hjemmesidendin

---

## PASO 1 — RECIBIR EL PEDIDO

El cliente llena oppdatering.html, elige una sección (ej: FAQ – 790 kr),
rellena sus datos, y pulsa "Lag oppsummering". Te llega un email de
Netlify con un resumen que incluye:
- Bedrift (nombre de empresa)
- Domene (dominio)
- La sección elegida y sus datos

---

## PASO 2 — ENCONTRAR LA CARPETA DEL CLIENTE

El email trae el nombre de empresa. Búscalo:

```bash
cd ~/hjemmesidendin
python3 finn-kunde.py <texto>
```

Ejemplos:
```bash
python3 finn-kunde.py skien
python3 finn-kunde.py skienelektro.no
```

Te dice en qué carpeta está (ej: skien-elektro).

---

## PASO 3 — CONVERTIR EL RESUMEN AL FORMATO DEL SCRIPT

El email llega en formato legible. El script ny-seksjon.py necesita
formato NOMBRE=valor. Abre un archivo temporal y traduce a mano:

```bash
code /tmp/seksjon.txt
```

Usa las TABLAS DE TRADUCCIÓN de más abajo según la sección.

---

## PASO 4 — GENERAR LA SECCIÓN

```bash
cd ~/hjemmesidendin
python3 ny-seksjon.py <cliente> <tipo> /tmp/seksjon.txt
```

IMPORTANTE — el nombre del tipo en el script:
El formulario y el script usan nombres distintos en 2 casos.
Usa SIEMPRE el nombre del script:

| El cliente pidió (email) | Escribe en el comando |
|--------------------------|------------------------|
| Dekningskart             | dekningskart           |
| Sertifiseringer          | sertifiseringer        |
| FAQ                      | faq                    |
| Priser/pakker            | priser                 |
| Åpningstider             | apningstider           |
| Slik jobber vi           | prosess                |
| Sosiale medier           | sosiale                |
| Google-anmeldelser       | google                 |

---

## PASO 5 — PEGAR EN LA WEB DEL CLIENTE

El script genera SEKSJON-<tipo>.html en la carpeta del cliente.
Ábrelo, copia el HTML, y pégalo en su index.html donde vaya.

```bash
code ~/kunder/<cliente>
```

---

## PASO 6 — DEPLOY + COBRAR

Sube el cambio (git push del repo del cliente) y cobra el servicio.

---

# TABLAS DE TRADUCCIÓN (email → formato script)

Para cada sección: a la izquierda lo que ves en el email, a la derecha
lo que escribes en /tmp/seksjon.txt

---

## PRISER (precios)

Email:
```
  Befaring – Gratis
  Timepris – 890 kr
Notat: Alle priser inkl. mva.
```

/tmp/seksjon.txt:
```
PRIS_1_TJENESTE=Befaring
PRIS_1_PRIS=Gratis
PRIS_2_TJENESTE=Timepris
PRIS_2_PRIS=890 kr
PRIS_NOTE=Alle priser inkl. mva.
```
(Opcionales: PRIS_TITTEL, PRIS_LEAD)

---

## FAQ (preguntas frecuentes)

Email:
```
Sp 1: Gir dere gratis befaring?
   Svar: Ja, alltid.
```

/tmp/seksjon.txt:
```
FAQ_1_SP=Gir dere gratis befaring?
FAQ_1_SVAR=Ja, alltid.
```
(Hasta 5 pares. Opcionales: FAQ_TITTEL, FAQ_LEAD)

---

## APNINGSTIDER (horarios)

Email:
```
  Mandag   07:00–16:00
  Tirsdag  07:00–16:00
  ...
Notat: ...
```

/tmp/seksjon.txt:
```
TID_MAN=07:00–16:00
TID_TIR=07:00–16:00
TID_ONS=07:00–16:00
TID_TOR=07:00–16:00
TID_FRE=07:00–15:00
TID_LOR=Stengt
TID_SON=Stengt
TID_NOTE=...
```
(Opcionales: TID_TITTEL, TID_LEAD)

---

## SERTIFISERINGER (certificaciones)

Email:
```
Sertifisering 1: Godkjent installatør – DSB-registrert
Garanti: 5 års garanti
```

/tmp/seksjon.txt:
```
SERT_1_NAVN=Godkjent installatør
SERT_1_TEKST=DSB-registrert
SERT_GARANTI=5 års garanti
```
(Hasta 6. Opcionales: SERT_TITTEL, SERT_LEAD)

---

## DEKNINGSKART (áreas de cobertura)

Email:
```
Base:     Skien sentrum
Områder:
Skien | Porsgrunn | Bamble
Notat: ...
```

/tmp/seksjon.txt:
```
KART_BASE=Skien sentrum
KART_OMRADER=Skien | Porsgrunn | Bamble
KART_NOTE=...
```
(Opcionales: KART_TITTEL, KART_LEAD)

---

## PROSESS (cómo trabajamos)

Email:
```
Steg 1: Kontakt
   Du ringer, vi svarer samme dag.
```

/tmp/seksjon.txt:
```
STEG_1_TITTEL=Kontakt
STEG_1_TEKST=Du ringer, vi svarer samme dag.
```
(Hasta 6. Opcionales: STEG_TITTEL, STEG_LEAD)

---

## SOSIALE (redes sociales)

Email:
```
  Facebook: https://facebook.com/...
  Instagram: https://instagram.com/...
```

/tmp/seksjon.txt:
```
SOS_FB=https://facebook.com/...
SOS_IG=https://instagram.com/...
```
(Códigos: SOS_FB, SOS_IG, SOS_LI, SOS_YT, SOS_TT)
(Opcionales: SOS_TITTEL, SOS_LEAD)

---

## GOOGLE (reseñas)

Email:
```
Google-lenke:  https://g.page/...
Visning:       ...
Be om-knapp:   Ja
Trustpilot:    ...
```

/tmp/seksjon.txt:
```
G_LENKE=https://g.page/...
G_STJERNER=4.9
G_ANTALL=47
G_BE_OM=ja
G_TRUSTPILOT=...
```
(Opcionales: G_TITTEL, G_LEAD)

---

## NOTA SOBRE LA CONVERSIÓN MANUAL

Por ahora la conversión email → formato script se hace a mano con estas
tablas. Cuando tengas varias actualizaciones reales y veas los formatos
exactos, se puede valorar un script conversor o que el formulario genere
el formato directo. No optimizar antes de tener datos reales.

Recuerda: ny-seksjon.py te avisa si falta algún dato, así que si te
equivocas en el formato, el script te lo dice.