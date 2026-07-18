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

## RESUMEN RÁPIDO (los 4 comandos en orden)

\`\`\`bash
# 1. Copiar plantilla y abrirla
cd ~/hjemmesidendin && cp maler/kunde-data-mal.txt /tmp/kunde-data.txt && code /tmp/kunde-data.txt

# 2. (rellenas en VS Code y guardas con Ctrl+S)

# 3. Generar la web
cd ~/hjemmesidendin && python3 ny-kunde.py <molde> <cliente> /tmp/kunde-data.txt

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
