# FLUJO DE VENTA — Hjemmesidendin

Manual de operaciones: desde que llega un pedido hasta que entregas la web.
Sigue estos pasos EN ORDEN cada vez que vendas.

Leyenda:
- ✅ = ya funciona hoy
- ⏳ [PENDIENTE] = hay que configurarlo antes del lanzamiento real
- 🏢 [EMPRESA] = usa la cuenta de empresa (pendiente de crear)

---

## RESUMEN VISUAL DEL FLUJO

\`\`\`
1. Cliente rellena formulario  →  te llega email con su info      ⏳
2. Cliente paga (Stripe/Vipps) →  te llega email de pago          ⏳
3. Apuntas el pedido en tu hoja de control                        ⏳
4. Generas la web         →  ny-kunde.py                          ✅
5. Añades sus fotos       →  koble-bilder.py                      ✅
6. Añades secciones extra →  ny-seksjon.py (si aplica)            ✅
7. Revisas calidad        →  sjekk.py + Live Server               ✅
8. Publicas               →  GitHub + Netlify (1 repo+site)       ⏳🏢
9. Entregas               →  email al cliente                     ⏳
10. Registras entrega en tu hoja de control                       ⏳
\`\`\`

---

## FASE 1 — RECIBIR EL PEDIDO ⏳

### 1.1 Llega el email del formulario ⏳ [PENDIENTE]
Cuando la tienda esté publicada con Netlify Forms activado, cada pedido
llega a tu email con toda la info que el cliente escribió en bestill-*.html.

**Pendiente de configurar:**
- [ ] Publicar la tienda en Netlify
- [ ] Activar "Enable form detection" en Netlify
- [ ] Verificar que el email llega correctamente

### 1.2 Llega el email del pago ⏳ [PENDIENTE]
- [ ] Configurar Stripe (pago con tarjeta)
- [ ] Configurar Vipps (pago móvil noruego)
- [ ] Conectar los botones de pago de la tienda

### 1.3 Organizar los emails ⏳ [PENDIENTE]
Crear filtros en Gmail para que se ordenen solos:
- [ ] Remitente Netlify → etiqueta "Bestillinger" (pedidos)
- [ ] Remitente Stripe/Vipps → etiqueta "Betalinger" (pagos)

---

## FASE 2 — REGISTRAR EL PEDIDO ⏳

### 2.1 Apuntar en la hoja de control ⏳ [PENDIENTE]
Antes de tocar código, apunta el pedido en tu hoja de cálculo (Google
Sheets). Una fila por pedido:

| Fecha | Cliente | Email | Oficio | Diseño | Precio | Pagado | Entregado |
|-------|---------|-------|--------|--------|--------|--------|-----------|

Esta hoja es tu ÚNICA VERDAD. Los emails son solo materia prima.

**Pendiente:**
- [ ] Crear la hoja de control en Google Sheets

---

## FASE 3 — GENERAR LA WEB ✅

### 3.1 Preparar los datos del cliente
Copia la plantilla de datos en blanco y rellénala con la info del email:

\`\`\`bash
cd ~/hjemmesidendin
cp maler/kunde-data-mal.txt /tmp/kunde-data.txt
code /tmp/kunde-data.txt
\`\`\`

Rellena cada campo con los datos del cliente (FIRMANAVN, TELEFON,
EPOST, colores, textos...). Guarda con Ctrl+S.

NOTA: usamos /tmp/ para no dejar datos de clientes sueltos en el
proyecto. Se borra solo al reiniciar.

### 3.2 Elegir el molde correcto
Los moldes disponibles (oficio + diseño) son:

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

### 3.3 Generar la web
\`\`\`bash
cd ~/hjemmesidendin
python3 ny-kunde.py <molde> <nombre-cliente> /tmp/kunde-data.txt
\`\`\`

Ejemplo real:
\`\`\`bash
python3 ny-kunde.py rorlegger-moderne nordvik-ror /tmp/kunde-data.txt
\`\`\`

Esto crea la web completa en ~/kunder/nordvik-ror/ con todos los
datos del cliente ya puestos y los colores calculados.

---

## FASE 4 — AÑADIR FOTOS ✅

### 4.1 Poner las fotos del cliente
Descarga las fotos que envió el cliente y ponlas en su carpeta:

\`\`\`bash
mkdir -p ~/kunder/<cliente>/bilder
\`\`\`

Copia las fotos ahí con estos nombres exactos:
- logo.png
- hero.jpg
- team.jpg
- galleri1.jpg ... galleri6.jpg

### 4.2 Conectar las fotos al CSS
\`\`\`bash
cd ~/hjemmesidendin
python3 koble-bilder.py <cliente>
\`\`\`

Ejemplo:
\`\`\`bash
python3 koble-bilder.py nordvik-ror
\`\`\`

⏳ [PENDIENTE optimización]: cuando tengas cuenta Cloudinary, optimizar
las imágenes (f_auto, q_auto, w_800) y añadir loading="lazy".

---

## FASE 5 — SECCIONES EXTRA (opcional) ✅

Si el cliente pidió secciones que no vienen en la demo base (FAQ,
tabla de precios, horarios...), genéralas:

\`\`\`bash
cd ~/hjemmesidendin
python3 ny-seksjon.py <cliente> <tipo> [--antall N]
\`\`\`

Tipos disponibles:
\`\`\`
faq · apningstider · sertifiseringer · priser
dekningskart · prosess · sosiale · google
\`\`\`

Luego abre el archivo SEKSJON-*.html que se generó en la carpeta del
cliente, copia el HTML y pégalo en su index.html donde vaya. Reemplaza
los marcadores [...] con los datos reales (Ctrl+H en VS Code).

---

## FASE 6 — REVISAR CALIDAD ✅

### 6.1 Revisión automática
\`\`\`bash
cd ~/hjemmesidendin
python3 sjekk.py <cliente>
\`\`\`

Esto comprueba que no queden marcadores sin rellenar, que el CSS y las
páginas legales estén bien. Corrige lo que marque antes de seguir.

### 6.2 Revisión visual
\`\`\`bash
code ~/kunder/<cliente>
\`\`\`

En VS Code: abre index.html → Go Live (Live Server). Revisa:
- ¿Se ve bien en móvil y escritorio?
- ¿Los colores del cliente están bien?
- ¿Las fotos cargan?
- ¿Los textos están completos, sin [MARCADORES] sueltos?
- ¿Los enlaces funcionan?

---

## FASE 7 — PUBLICAR ⏳🏢

### 7.1 Crear repo del cliente 🏢 [EMPRESA - PENDIENTE]
Bajo la cuenta de EMPRESA (no lallalproject7), crear un repo nuevo
para el cliente: <cliente> (ej: nordvik-ror).

⏳ [PENDIENTE]: crear cuenta de empresa GitHub + configurar Ubuntu
para manejar las dos cuentas (sesión dedicada).

### 7.2 Subir la web a GitHub
\`\`\`bash
cd ~/kunder/<cliente>
git init
git add -A
git commit -m "Initial website for <cliente>"
git branch -M main
git remote add origin https://github.com/<cuenta-empresa>/<cliente>.git
git push -u origin main
\`\`\`

### 7.3 Publicar en Netlify 🏢 [EMPRESA - PENDIENTE]
- Conectar el repo del cliente a Netlify
- Deploy (publish = ".", sin build command)
- Renombrar site: <cliente>.netlify.app
- ⏳ [PENDIENTE dominio]: apuntar el dominio del cliente a su site

---

## FASE 8 — ENTREGAR ⏳

### 8.1 Email de entrega ⏳ [PENDIENTE]
Enviar al cliente un email con:
- La URL de su web
- Cómo pedir cambios (enlace a oppdatering)
- La factura

⏳ [PENDIENTE]: crear plantilla de email de entrega.

### 8.2 Registrar la entrega ⏳
Marcar en la hoja de control: Entregado = ✅ + fecha.

---

## FASE 9 — FACTURACIÓN Y CONTABILIDAD ⏳

⏳ [PENDIENTE - fase posterior]:
- [ ] Registrar ENK en Brønnøysund
- [ ] Configurar Fiken (facturación + contabilidad + SAF-T)
- [ ] Crear factura por cada venta
- [ ] Guardar comprobantes (obligación legal desde la factura #1)

NOTA LEGAL: en Noruega tienes bokføringsplikt (obligación de llevar
registro contable) desde la PRIMERA venta. Numerar facturas
correlativamente y guardar todo 5 años.

---

## CHECKLIST RÁPIDO (para pegar en la pared)

\`\`\`
□ 1. Pedido apuntado en hoja de control
□ 2. Pago confirmado (email Stripe/Vipps)
□ 3. Datos rellenados en /tmp/kunde-data.txt
□ 4. python3 ny-kunde.py <molde> <cliente> /tmp/kunde-data.txt
□ 5. Fotos en bilder/ + python3 koble-bilder.py <cliente>
□ 6. Secciones extra (si aplica) con ny-seksjon.py
□ 7. python3 sjekk.py <cliente>  → sin errores
□ 8. Revisión visual con Live Server
□ 9. Publicar (GitHub repo + Netlify site)
□ 10. Email de entrega + factura
□ 11. Marcar ✅ en hoja de control
\`\`\`

---

## ESTADO ACTUAL DEL SISTEMA (julio 2026)

FUNCIONA HOY:
- ✅ Generación de webs (ny-kunde.py)
- ✅ Conexión de imágenes (koble-bilder.py)
- ✅ Secciones extra (ny-seksjon.py)
- ✅ Revisión de calidad (sjekk.py)

PENDIENTE ANTES DEL LANZAMIENTO:
- ⏳ Publicar la tienda en Netlify + activar Forms
- ⏳ Configurar Stripe + Vipps
- ⏳ Crear hoja de control (Google Sheets)
- ⏳ Filtros de Gmail
- ⏳ Cuenta de empresa (GitHub + Netlify) + config Ubuntu 2 cuentas
- ⏳ Registrar ENK + Fiken (contabilidad)
- ⏳ Dominio propio + email de empresa
- ⏳ Plantillas de emails (entrega, confirmación)
