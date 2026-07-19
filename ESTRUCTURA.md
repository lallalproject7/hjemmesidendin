# ESTRUCTURA — Hjemmesidendin

Mapa del proyecto. Explica qué es cada archivo y cómo encaja todo.
Si algún día no recuerdas para qué sirve algo, míralo aquí.

---

## 1. QUÉ ES ESTE PROYECTO

Tienda web que vende páginas web listas para pequeños negocios noruegos
(electricistas, pintores, fontaneros, etc.). El cliente elige una demo,
rellena un formulario, paga, y se le construye su web desde una plantilla.

El proyecto tiene dos partes:
- **La tienda** (archivos HTML) — lo que el cliente ve y usa para comprar.
- **Las herramientas** (scripts .py y .sh) — lo que TÚ usas para construir
  la web de cada cliente después de la venta.

---

## 2. EL FLUJO DE LA TIENDA (cómo navega un cliente)

\`\`\`
index.html  (portada: presenta el servicio)
   │
   ├─► demoer-<oficio>.html   (elige diseño: klassisk o moderne)
   │        │
   │        └─► bestill-<oficio>.html   (formulario de pedido detallado)
   │                 │
   │                 └─► takk-nettside.html   (gracias + siguiente paso)
   │
   ├─► bestill-portefolje.html  (pedido de web de portafolio)
   │        └─► takk-optimalisering.html
   │
   └─► oppdatering.html  (para clientes que ya tienen web y quieren cambios)
            └─► takk-oppdatering.html  /  takk-optimalisering.html

endringsrunde.html  (ronda de cambios durante un proyecto en curso)
   └─► takk-endring.html

takk.html  (página de gracias genérica; enlaza a index, endringsrunde,
            personvern, vilkar)
\`\`\`

**Páginas legales (enlazadas desde el pie de página):**
- \`personvern.html\` — política de privacidad (GDPR)
- \`vilkar.html\` — términos y condiciones

---

## 3. LOS OFICIOS (7 bransjer)

elektriker · flyttebyra · gartner · maler · renhold · rorlegger · snekker

Cada oficio tiene:
- 1 página \`demoer-<oficio>.html\` (selector de diseño)
- 1 página \`bestill-<oficio>.html\` (formulario)
- 2 demos en \`demoer/\` (klassisk + moderne)
- 2 plantillas en \`maler/demoer/\` (klassisk + moderne)

---

## 4. LAS HERRAMIENTAS (scripts que TÚ ejecutas)

### ny-kunde.py — construye la web COMPLETA de un cliente
Copia una plantilla de \`maler/demoer/\`, reemplaza los marcadores
[FIRMANAVN], [TELEFON], etc. con los datos del cliente, calcula tonos
de color automáticamente, y guarda la web en ~/kunder/<cliente>/.

\`\`\`
python3 ny-kunde.py <mal> <kundemappe> <datafil>
python3 ny-kunde.py snekker lund-snekkerverksted kunde-data.txt
\`\`\`

### ny-seksjon.py — construye UNA sección extra (opcional)
Genera una sección adicional (FAQ, precios, horarios...) con marcadores
[...], para añadir a una web que ya existe. El molde está escrito dentro
del propio script (no en una carpeta).

\`\`\`
python3 ny-seksjon.py <cliente> <tipo> [--antall N]
Tipos: faq · apningstider · sertifiseringer · priser
       dekningskart · prosess · sosiale · google
\`\`\`

### koble-bilder.py — conecta las fotos del cliente
Cuando pones las fotos en ~/kunder/<cliente>/bilder/, este script las
enlaza al CSS. Reconoce: logo.png, hero.jpg, team.jpg, galleri1..6.jpg.

\`\`\`
python3 koble-bilder.py <cliente>
\`\`\`

### sjekk.py — revisa la web antes de entregar
Inspector de calidad. Comprueba que el index, el CSS y las páginas
legales estén bien y que no queden marcadores sin rellenar.

\`\`\`
python3 sjekk.py <cliente>
\`\`\`

### kopier-juridisk.sh — copia páginas legales a las demos
Copia personvern y cookies a cada demo, con los colores y datos de
cada una. (Herramienta de mantenimiento de las demos.)

### test-alt.sh — prueba todo el sistema
Ejecuta pruebas automáticas sobre los scripts: ¿existen? ¿son Python
válido? ¿manejan bien los errores? Tu red de seguridad.

### lag-testdata.py — crea un cliente falso para las pruebas
Genera datos de "Testbedrift AS". Lo usa test-alt.sh. No lo usas a mano.

---

## 5. LAS CARPETAS

### demoer/
Las 14 demos que el cliente VE en la tienda (7 oficios × 2 diseños).
Tienen datos de ejemplo bonitos (nombres, precios de mentira).
Cada una: index.html + css/style.css + páginas legales.

### maler/
Las PLANTILLAS (los moldes con marcadores [...]).
- \`maler/demoer/\` — las 14 demos pero con [FIRMANAVN] en vez de datos.
  Esto es lo que copia ny-kunde.py.
- \`maler/juridisk/\` — plantillas de páginas legales.
- \`maler/kunde-data-mal.txt\` — el formulario de datos en blanco que
  rellenas para cada cliente.

### netlify/
Funciones que corren en el servidor de Netlify (el contador de
capacidad "quedan X plazas"). Backend.

### css/
CSS compartido de las páginas de la tienda.

---

## 6. ARCHIVOS DE CONFIGURACIÓN

- \`netlify.toml\` — configuración de Netlify: seguridad (headers),
  caché, y dónde están las funciones.
- \`package.json\` — ficha del proyecto para Node.js. Declara la
  dependencia @netlify/blobs (para el contador).
- \`.gitignore\` — lo que git NO sube a GitHub: la carpeta kunder/
  (webs de clientes = privadas) y kunde-*.txt (datos privados).

---

## 7. LAS DOS "MÁQUINAS" (concepto clave)

El proyecto tiene dos generadores distintos. No confundirlos:

| | ny-kunde.py | ny-seksjon.py |
|---|---|---|
| Construye | La web COMPLETA | Una SECCIÓN suelta |
| Molde | De carpeta maler/demoer/ | Escrito dentro del .py |
| Cuándo | Al crear un cliente nuevo | Para añadir un extra |

---

## 8. FLUJO DE TRABAJO AL VENDER (resumen)

1. Llega el pedido (email del formulario bestill).
2. Copiar maler/kunde-data-mal.txt → kunde-data.txt y rellenarlo.
3. python3 ny-kunde.py <oficio> <cliente> kunde-data.txt
4. Poner fotos en ~/kunder/<cliente>/bilder/ y correr koble-bilder.py
5. (Opcional) Añadir secciones extra con ny-seksjon.py
6. python3 sjekk.py <cliente>  → revisar que todo esté bien
7. Revisar visualmente con Live Server
8. Deploy (GitHub → Netlify)
9. Email de entrega al cliente

---

## DÓNDE VIVE CADA COSA

- **Este proyecto (hjemmesidendin/)** = la fábrica (tienda + herramientas)
- **~/kunder/<cliente>/** = las webs terminadas (FUERA del proyecto,
  no se suben a git)
- **/tmp/** = archivos temporales (se borran al reiniciar)

### finn-kunde.py — encuentra la carpeta de un cliente
Busca en ~/kunder/ por nombre de empresa, email o dominio. Util cuando
llega una actualizacion y necesitas saber que carpeta es. Sin mayusculas.

```
python3 finn-kunde.py <texto>
python3 finn-kunde.py skien
```
