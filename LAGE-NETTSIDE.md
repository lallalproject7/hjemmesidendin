# CÓMO GENERAR UNA WEB — Guía paso a paso

Guía detallada con los comandos EXACTOS para crear la web de un cliente,
desde que te llega el email hasta que verificas que todo está bien.

Reemplaza siempre:
- `<molde>`   → el oficio + diseño (ej: elektriker, rorlegger-moderne)
- `<cliente>` → nombre corto del cliente (ej: skien-elektro)

---

## ANTES DE EMPEZAR

Ten a mano el email de Netlify con los datos del cliente.
Decide dos cosas:
1. Qué molde eligió el cliente (oficio + diseño klassisk/moderne)
2. Qué nombre corto le pondrás a su carpeta (sin espacios, en minúsculas,
   con guiones: ej. "nordvik-ror", "skien-elektro")

Moldes disponibles:
\`\`\`
elektriker · elektriker-moderne
flyttebyra · flyttebyra-moderne
gartner    · gartner-moderne
maler      · maler-moderne
renhold    · renhold-moderne
rorlegger  · rorlegger-moderne
snekker    · snekker-moderne
\`\`\`
(sin "-moderne" = diseño klassisk)

---

## PASO 1 — COPIAR LA PLANTILLA Y ABRIRLA EN VS CODE

Este comando hace 2 cosas de golpe: copia la plantilla en blanco a un
archivo temporal, y la abre en VS Code para que la rellenes.

\`\`\`bash
cd ~/hjemmesidendin && cp maler/kunde-data-mal.txt /tmp/kunde-data.txt && code /tmp/kunde-data.txt
\`\`\`

Explicación de cada parte:
- \`cd ~/hjemmesidendin\` → entra en la carpeta del proyecto
- \`cp maler/kunde-data-mal.txt /tmp/kunde-data.txt\` → copia la plantilla
  vacía a /tmp/ (temporal, no ensucia el proyecto)
- \`code /tmp/kunde-data.txt\` → abre ese archivo en VS Code

---

## PASO 2 — RELLENAR LOS DATOS (en VS Code)

En VS Code, ahora tienes /tmp/kunde-data.txt abierto. Rellena cada campo
copiando del email del cliente. El formato es NOMBRE=valor, así:

\`\`\`
FIRMANAVN=Skien Elektro
EPOST=post@skienelektro.no
TELEFON=911 22 333
FARGE_HOVED=#b4551d
HERO_TITTEL=Elektriker i Skien
\`\`\`

Reglas importantes:
- El valor va DESPUÉS del =, sin comillas
- No borres las líneas que empiezan con # (son notas, el script las ignora)
- Los campos que no apliquen a ese oficio, déjalos vacíos
- Guarda con Ctrl+S cuando termines

---

## PASO 3 — GENERAR LA WEB

Con los datos ya rellenados y guardados, corre el script:

\`\`\`bash
cd ~/hjemmesidendin && python3 ny-kunde.py <molde> <cliente> /tmp/kunde-data.txt
\`\`\`

Ejemplo real:
\`\`\`bash
cd ~/hjemmesidendin && python3 ny-kunde.py elektriker skien-elektro /tmp/kunde-data.txt
\`\`\`

Qué hace: copia la plantilla del molde, reemplaza todos los marcadores
[FIRMANAVN], [TELEFON]... con los datos, calcula los tonos de color, y
guarda la web lista en ~/kunder/<cliente>/

Si sale error "Mappen finnes allerede" → ya existe una carpeta con ese
nombre. Usa otro nombre, o borra la anterior si era una prueba:
\`\`\`bash
rm -rf ~/kunder/<cliente>
\`\`\`

---

## PASO 3.5 — AÑADIR IMÁGENES Y LOGO (si el cliente las envió)

Si el cliente mandó fotos o logo, este es el momento. Si no mandó
ninguna, salta al PASO 4 (la web funciona igual, con placeholders de
color y el logo de texto).

### 3.5.1 Abrir la carpeta bilder/ del cliente en VS Code

```bash
code ~/kunder/<cliente>
```

En el panel izquierdo (Explorer) verás la carpeta bilder/. Está vacía
al principio — es normal.

### 3.5.2 Meter las imágenes (arrastrar desde Windows)

1. Abre el Explorador de Windows con las fotos del cliente (ej: Downloads)
2. Pon las dos ventanas lado a lado (VS Code y el explorador de Windows)
3. Arrastra cada imagen y suéltala sobre la carpeta bilder/ en el panel
   izquierdo de VS Code
4. Cuando VS Code pregunte, elige "Copy"

### 3.5.3 Nombrar las imágenes CORRECTAMENTE (clic derecho → Rename)

El nombre decide dónde va en la web. Renombra cada una así:

    logo.png       → el logo (arriba). Reemplaza el logo de texto.
    hero.jpg       → la imagen grande principal
    team.jpg       → foto del equipo / sobre nosotros
    galleri1.jpg   → primera foto de la galería
    galleri2.jpg   → segunda foto de la galería
    ... hasta galleri6.jpg

Formatos aceptados: .jpg .jpeg .png .webp .svg

SOBRE EL LOGO:
- Si el cliente NO manda logo → la web usa el nombre escrito como logo
  (se ve bien igual). No haces nada.
- Si el cliente SÍ manda logo → guárdalo como logo.png. El script lo
  pone automáticamente y esconde el texto.

### 3.5.4 Verificar que las imágenes llegaron

```bash
ls -la ~/kunder/<cliente>/bilder/
```

Debes ver tus imágenes con los nombres correctos.

### 3.5.5 Conectar las imágenes a la web

```bash
cd ~/hjemmesidendin && python3 koble-bilder.py <cliente>
```

Qué hace: mira la carpeta bilder/, y según el nombre de cada imagen la
conecta al lugar correcto de la web (hero, galería, equipo, logo).

Si nombraste mal un archivo, el script te avisa:
    ? Ukjente filnavn: mifoto.jpg
      Gyldige navn: logo · hero · team · galleri1–6
En ese caso, renombra el archivo y corre el comando otra vez.

Puedes correr koble-bilder.py las veces que quieras.

NOTA SOBRE EL PESO: las fotos de cámara/móvil suelen ser pesadas (2–5 MB).
Para producción conviene optimizarlas (Cloudinary, pendiente en el TODO).
Para pruebas no importa.


---

## PASO 4 — VERIFICAR QUE TODO ESTÁ BIEN (automático)

Corre el inspector de calidad:

\`\`\`bash
cd ~/hjemmesidendin && python3 sjekk.py <cliente>
\`\`\`

Ejemplo:
\`\`\`bash
cd ~/hjemmesidendin && python3 sjekk.py skien-elektro
\`\`\`

Qué revisa: que no queden marcadores [XXX] sin rellenar, que el CSS y las
páginas legales estén bien. Corrige lo que marque antes de continuar.

---

## PASO 5 — VERIFICAR VISUALMENTE (con tus ojos)

Abre la web del cliente en VS Code y míralas con Live Server:

\`\`\`bash
code ~/kunder/<cliente>
\`\`\`

En VS Code: abre index.html → botón "Go Live" (abajo a la derecha).

Revisa con los ojos:
- ¿Se ve bien en móvil y en escritorio?
- ¿Los colores del cliente están correctos?
- ¿Las fotos cargan? (si ya las añadiste)
- ¿Hay algún [MARCADOR] suelto que sjekk.py no atrapó?
- ¿Los textos están completos y sin errores?
- ¿Los enlaces funcionan?

---

## PASO 6 — PUBLICAR LA WEB (DEPLOY A NETLIFY)

Hasta ahora la web solo existe en tu PC. Este paso la sube a internet.

REQUISITO: cuenta de Netlify (idealmente la cuenta de EMPRESA).
Arquitectura: 1 repositorio GitHub + 1 site Netlify por cliente.

### 6.1 Crear un repositorio para el cliente en GitHub

Bajo tu cuenta de empresa, crea un repo nuevo con el nombre del cliente
(ej: skien-elektro). Vacío, sin README.

### 6.2 Subir la web del cliente a ese repositorio

    cd ~/kunder/<cliente>
    git init
    git add -A
    git commit -m "Initial website for <cliente>"
    git branch -M main
    git remote add origin https://github.com/<cuenta-empresa>/<cliente>.git
    git push -u origin main

### 6.3 Conectar el repo a Netlify

1. Entra a Netlify → "Add new site" → "Import an existing project"
2. Elige GitHub → selecciona el repo del cliente
3. Configuración de build:
   - Build command: (dejar vacío)
   - Publish directory: .  (un punto)
4. "Deploy site"

En segundos la web queda en vivo en una dirección tipo:
   <algo-aleatorio>.netlify.app

### 6.4 Cambiar el nombre del site (opcional pero recomendado)

En Netlify: Site settings → Change site name → pon el nombre del cliente:
   <cliente>.netlify.app

Ya puedes enseñarle esta URL al cliente mientras se conecta el dominio.

---

## PASO 7 — CONECTAR EL DOMINIO .no

Este paso le da al cliente su dirección propia (ej: skienelektro.no)
en vez de la de netlify.app.

REQUISITO: ENK registrada (necesitas el organisasjonsnummer para
comprar dominios .no como empresa — hasta 100 dominios).

### 7.1 Comprar el dominio en domene.no

1. Entra a domene.no y busca el dominio (ej: skienelektro.no)
2. Si está libre, añádelo al carrito
3. Paga con tarjeta o Vipps → se registra en minutos
NOTA: el dominio .no se ALQUILA (pago anual), no se compra para siempre.

### 7.2 Añadir el dominio al site en Netlify

1. En el site del cliente en Netlify:
   Domain settings → Add a domain → escribe el dominio (skienelektro.no)
2. Netlify te mostrará unos DNS records (direcciones técnicas).
   Anótalos — los necesitas en el paso siguiente.

### 7.3 Apuntar el dominio hacia Netlify (en domene.no)

1. En domene.no, entra a la configuración DNS del dominio
2. Pega los DNS records que te dio Netlify
   (esto conecta "el dominio" → "la web en Netlify")
3. Guarda

### 7.4 Esperar la propagación

El cambio tarda de minutos a 24 horas en activarse en todo el mundo.
Cuando termine, el dominio del cliente muestra su web.

### 7.5 SSL (candado de seguridad https)

Netlify activa el certificado SSL automático y gratis una vez el
dominio está conectado. No tienes que hacer nada — solo esperar a que
aparezca "https" con el candado.

---

## TIEMPOS (para tu plazo de ~7 días)

- Construir la web (datos + imágenes):  1–4 días
- Deploy a Netlify:                      minutos
- Comprar dominio .no:                   minutos
- Propagación DNS del dominio:           de minutos a 24 horas
- SSL automático:                        automático tras la propagación

El dominio es el paso más rápido. Lo que toma tiempo es construir bien
la web. Puedes entregar en cliente.netlify.app y conectar el dominio
después, sin que el cliente espere.


---

## RESUMEN RÁPIDO (los 4 comandos en orden)

\`\`\`bash
# 1. Copiar plantilla y abrirla
cd ~/hjemmesidendin && cp maler/kunde-data-mal.txt /tmp/kunde-data.txt && code /tmp/kunde-data.txt

# 2. (rellenas en VS Code y guardas con Ctrl+S)

# 3. Generar la web
cd ~/hjemmesidendin && python3 ny-kunde.py <molde> <cliente> /tmp/kunde-data.txt

# 3.5. Imágenes (si las hay): meterlas en bilder/ y conectarlas
python3 koble-bilder.py <cliente>

# 4. Verificar automático
cd ~/hjemmesidendin && python3 sjekk.py <cliente>

# 5. Verificar visual
code ~/kunder/<cliente>
\`\`\`

---

## NOTA SOBRE EL ARCHIVO TEMPORAL

Usamos /tmp/kunde-data.txt porque /tmp/ se borra sola al reiniciar el PC.
Así no acumulas datos de clientes sueltos en el proyecto. El script
además guarda una copia del .txt dentro de ~/kunder/<cliente>/ por si la
necesitas después.
