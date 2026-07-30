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

## 8. LOS DOS VOCABULARIOS (concepto clave)

El formulario y el molde NO hablan el mismo idioma. Tú eres el puente.

**El formulario** (bestill-<oficio>.html) → habla en "resumen legible".
El cliente rellena campos normales (om_navn, tall_aar…) y el JavaScript
arma un texto que te llega por email con etiquetas en noruego:

    ── OM OSS ──
    Navn utad: Jonas Lien
    År i bransjen: 12

**El molde** (maler/demoer/<oficio>/) → habla en "marcadores":

    [OM_NAVN] har [OM_ERFARING] år i faget.

**El puente eres tú:** copias los valores del email al kunde-data.txt,
y ny-kunde.py mete cada valor en su marcador.

    email → kunde-data.txt → ny-kunde.py → web del cliente

### ⚠️ La regla de oro

Si añades o cambias un marcador en un molde, TIENES que tocar también
el formulario (el campo + su línea en el resumen del JS). Si no, el molde
pide un dato que el formulario nunca recoge, y no te enteras hasta que
vendes.

El guardián de esto es **sjekk-samsvar.py**: su aviso "form asks more
than demo shows" salta justo cuando molde y formulario se desalinean.
Córrelo siempre después de tocar un molde o un formulario.

---

## 9. FLUJO DE TRABAJO AL VENDER (resumen)

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



# Detección de bugs — ciclo demo → formulario → scaffolding

*Guía para el chat nuevo. Basada en los verificadores reales de Lallal (sjekk-samsvar.py, sjekk.py, test-alt.sh).*

---

## El ciclo y dónde se rompe

Tres piezas que deben estar sincronizadas:

1. **Demo** (`demoer/portefolje-X/`) = el escaparate que ve el cliente. Puede tener Unsplash y datos de ejemplo.
2. **Molde** (`maler/demoer/portefolje-X/`) = la plantilla con `[MARCADORES]`. NO puede tener Unsplash ni datos de demo.
3. **Formulario** (`bestill-portefolje.html`) = lo que el cliente rellena. Sus `name="..."` deben corresponder a los marcadores del molde.

**La regla de oro (los "dos vocabularios"):** si cambias un marcador en el molde, tienes que cambiar también el formulario, o el dato nunca llega. El puente es manual (email → `kunde-data.txt`).

**Dónde se rompe normalmente:**
- Se añade un marcador al molde pero el formulario no lo pide → hueco vacío en la web del cliente.
- Queda una identidad de demo (un nombre inventado) dentro del molde → el cliente ve el nombre de otro.
- Queda una imagen de Unsplash en el molde → el cliente ve una foto que no es suya.
- El nº de huecos de foto del demo ≠ el del molde → fotos que sobran o faltan.

---

## Qué caza cada verificador (tus scripts reales)

### `sjekk-samsvar.py` — revisa el SISTEMA entero (moldes ↔ demos ↔ formulario)
FAIL (bloquean):
- **Molde no existe** para un demo del escaparate.
- **Imágenes externas en el molde** (Unsplash, o url()/img apuntando a un archivo de imagen). *No* marca Google Fonts ni mapas embebidos (eso es intencional).
- **Identidad de demo filtrada en el molde** — nombres prohibidos: Nordvik, Fossum, Voltek, Berg Maler, Lund, Lien, Grønn Hage, Trygg Flytt, Klar Renhold.
- **Marcadores que el modelo de datos no puede rellenar** (marcador en el molde sin campo que lo alimente).

WARNING (informan, no bloquean):
- Nombres de hueco de foto raros.
- Nº de huecos de foto demo vs molde no cuadra.
- El formulario pide más tjeneste/prosjekt de los que muestra el demo.

Nota: quita comentarios CSS/HTML antes de escanear (así "Unsplash" escrito en un comentario NO cuenta como fallo). Colores automáticos que deriva `ny-kunde.py` (FARGE_HOVED_MORK, etc.) no se exigen en el modelo de datos.

### `sjekk.py <kunde>` — revisa la web de UN cliente antes de entregar
Revisa: (1) archivos existen, (2) marcadores sin rellenar, (3) datos de demo que quedaron, (4) banner de demo, (5) que el firmanavn cuadre, (6) enlaces internos, (7) imágenes (¿conectadas?), (8) placeholders que quedaron. Resultado: 🟢 KLAR / 🟡 con advertencias / 🔴 IKKE KLAR.

### `test-alt.sh` — prueba que el sistema funciona
(1) Los scripts existen y son Python válido. (2) Manejo de errores: cada script (ny-kunde.py, sjekk.py, koble-bilder.py) avisa bien cuando falta argumento o no encuentra el cliente/molde.

---

## Checklist antes de entregar / antes de push

1. `python3 sjekk-samsvar.py` → 0 FAIL (los WARNING se valoran).
2. Si hay un cliente en curso: `python3 sjekk.py <kunde>` → 🟢.
3. `bash test-alt.sh` → todo ✓.
4. Revisar visualmente con Live Server.
5. Limpiar `.bak` (ya están en `.gitignore` con `*.bak*`).
6. `git add -A && git commit -m "..." && git push`.

---

## Estado actual (para no reinventar)

**Demos de portafolio (escaparate):** Klassisk, Moderne, Teknisk — los 3 pulidos.
- **Klassisk** → reenfocado a **interiorista** (Silje Ranvik): hero, tjenester, om meg (sin foto, con 4 credenciales de trayectoria), y 6 proyectos con 3 fotos cada uno (1 grande + 2 libres, sin antes/después).
- **Teknisk** → maskiningeniør Aksel Movik; cada proyecto con 4 pares etiqueta+valor propios (año + rol comunes, los otros 2 varían).
- **Moderne** → Sindre Vollan; foto-credencial redonda + fotos de proyecto más gruesas.

**FAIL actuales (esperados):** faltan los moldes `portefolje-moderne` y `portefolje-teknisk`. Se crearán en la fase de scaffolding.

**Moldes:** `maler/demoer/portefolje` (clásico) solo tiene marcadores en las páginas legales; su `index.html` aún NO está templado. Hay que templarlo desde el demo interiorista nuevo.

**Formulario:** `bestill-portefolje.html` YA existe y YA tiene sección de proyectos (6 bloques). Los `name=` del formulario mandan sobre los marcadores del molde.

---

## Decisiones de diseño YA tomadas (aplicar en molde + formulario)

1. **Datos técnicos de cada proyecto = 4 pares "etiqueta libre + valor"** (`[P1_LABEL1]`/`[P1_VERDI1]`...). El cliente rellena etiqueta Y valor, así cada proyecto muestra sus datos propios y se ve único. NO usar etiquetas fijas.
2. **Testimonios/citas de cada proyecto = OPCIONALES** en formulario y scaffolding.
3. **Campo "info extra" por proyecto = OPCIONAL** — texto libre para datos específicos que el cliente quiera añadir, que el demo no muestra por defecto.
4. **Fotos pequeñas del proyecto = SIN título/etiqueta** (lo opcional se reserva para texto con valor, no para etiquetas decorativas → mantiene el scaffolding simple).

**Siguiente paso previsto:** templar el molde del clásico (interiorista) usando los nombres que ya usa `bestill-portefolje.html`; después, moldes de Teknisk y Moderne.