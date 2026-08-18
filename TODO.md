# TODO – Hjemmesidendin

Mapa de pendientes del proyecto. Actualizar a medida que se completen tareas.

---

## ✅ COMPLETADO
- Tienda completa (index) con todas las secciones
- 7 demos con diseño e identidad propia
- 7 formularios de pedido específicos por bransje + selector
- Formulario de endringsrunde + oppdatering
- Páginas legales (personvern, vilkar) — FALTAN rellenar marcadores
- Contador de capacidad (backend listo, se activa en Netlify)
- netlify.toml optimizado (caché + seguridad)
- Botones de compra en tienda y demos

---

## 🎁 HERRAMIENTA GRATIS: VISITTKORT-GENERATOR (regalo/SEO)
- Página gratis-visittkort.html: generador de visittkort con QR, 5 diseños, selector de color, descarga PDF (imprenta 91×61mm) + PNG — COMPLETADO
- Sección de enganche "Gratis gave" en el index (banner verdoso + mini tarjeta) que enlaza al generador — COMPLETADO
- Estrategia: página propia dedicada para SEO ("gratis visittkort", "lag visittkort") + gancho en index
- Coste: 0 (todo en el navegador, librerías gratis vía CDN, Netlify estático)
- [ ] Al publicar: verificar que Google indexe la página (no lleva noindex)

## 🆕 NUEVAS DEMOS PLANIFICADAS (ampliar más allá de oficios)
Objetivo: captar más mercado con gremios de mayor volumen. Sistema compartido (molde + formulario + sjekk-samsvar.py).
- [ ] **Spa/Peluquería/Belleza** (frisør, hudpleie, negler, massasje) — EMPEZAR POR ESTA (fácil, visual, alto volumen). Secciones: hero + tjenester con precios + galleri + om oss + timebestilling/kontakt
- [ ] **Consultor/Coach/Terapeuta** (servicios personalizados) — base flexible. Secciones: hero + om meg + tjenester + bakgrunn + timebestilling/kontakt
- [ ] **Restaurante/Kafé** — al final (reto: menú actualizable vía oppdatering). Secciones: hero + meny + om oss + åpningstider/kart + kontakt/reservas

### Demo Spa — decisiones de construcción (sesión actual)
- Diseño **Serene**: estilo inmersivo (hero grande con nombre gigante + categorías verticales a todo el ancho), fondo claro. Mantener como está por ahora.
- **6 categorías**: Hår (incl. extensions + hårkur), Skjegg (barba, categoría propia para atraer hombres), Hudpleie, Negler, Vipper & bryn, Massasje
- Tratamientos por categoría en **acordeón desplegable** (clic en categoría → se abre lista con precios)
- 3 diseños del gremio: Serene (en rediseño), Bloom (hecho), Lyx (pendiente — oscuro lujo)
- Nombres ficticios: Serene = "Salong Serene", Bloom = "Bloom Studio", Lyx = "Salong Noir" (pendiente). Todos en Oslo.

### Formulario inteligente de spa (bestill-spa.html) — PENDIENTE, construir DESPUÉS de la demo
Debe permitir al cliente personalizar su web:
- **Elegir qué tratamientos incluir**: checkboxes por tratamiento predefinido (cada salón marca los suyos, no todos ofrecen lo mismo)
- **Añadir tratamientos extra/diferentes**: campos dinámicos para nombre + precio de servicios que no están en la lista predefinida
- **Mostrar precios o no**: toggle para decidir si la web muestra precios "fra" o solo nombres de tratamientos
- Los tratamientos elegidos + extras rellenan los marcadores del molde (acordeón de categorías)
- Nota: es un formulario complejo (checkboxes, campos dinámicos, toggle). Construir cuando la demo/molde estén cerrados.

### Reservas — 3 opciones en el formulario de pedido (bestill-spa.html)
1. **Cal.com**: nosotros lo configuramos/embebemos en la web, el cliente lo gestiona después (gratis)
2. **Sistema propio del cliente** (Reservio, Fixit, Timma, etc.): el cliente pasa su enlace/URL para conectarlo a la web
3. **Sin reservas**: el botón se convierte en "Kontakt oss" (tel/formulario)
- NOTA técnica: la lista de precios de la web y los servicios de Cal.com son listas SEPARADAS (la web no lee de Cal.com). Cal.com se puede EMBEBER (widget/botón), no solo enlazar. "Reserva integrada" = Cal.com embebido, NO sistema propio con backend (eso rompería el modelo estático).

### Decisiones sobre reservas (timebestilling)
- Botón "Bestill time" = MARCADOR de URL (flexible): el cliente pone su enlace de reserva
- Cal.com = mejor opción GRATIS (reservas/tipos de evento ilimitados) — usar en el escaparate/demo
- Timma (timma.no) = la que usan salones reales en Skien (ej. Kirkerudklinikken), pero es de pago
- El molde permite cualquier sistema: Cal.com, Timma, Reservio, etc.

---
## 🚀 SIGUIENTE PASO: PUBLICAR EN NETLIFY (Fase 2)
- [ ] Conectar repositorio de GitHub a Netlify
- [ ] Deploy (publish = ".", sin build command)
- [ ] Renombrar site a hjemmesidendin.netlify.app
- [ ] Activar Forms (Enable form detection) + Trigger deploy
- [ ] Configurar variable de entorno ADMIN_KEY (para el contador)
- [ ] Probar flujo completo en la URL en vivo (formularios, contador)

---

## 🏢 IDENTIDAD DE EMPRESA (cuando tenga tiempo)
- [ ] Crear Gmail de empresa (ej: hjemmesidendin@gmail.com)
- [ ] Crear cuenta GitHub de empresa (separada de lallalproject7)
- [ ] Crear cuenta Netlify de empresa
- [ ] Mover/subir repositorio a la cuenta nueva
- [ ] Todas las cuentas del negocio bajo el mismo email

## 🔒 SEGURIDAD (tareas propias, importante)
- [ ] Activar 2FA en: email, GitHub, Netlify, Cloudinary, Stripe
- [ ] Contraseñas únicas por cuenta (usar Bitwarden)
- [ ] Regla personal: nunca entrar a servicios desde enlaces de emails

## 💳 NEGOCIO / PAGOS (Fase 3 – para vender de verdad)
- [ ] Registrar ENK en Brønnøysund (requisito para Stripe y dominio)
- [ ] Crear cuenta Stripe + Payment Links
- [ ] Conectar botones de pago (ahora apuntan a "#" o takk.html)
- [ ] Webhook Stripe → contador (descuento automático de plazas)
- [ ] Registrar dominio hjemmesidendin.no
- [ ] Configurar email post@hjemmesidendin.no
- [ ] Rellenar TODOS los [MARCADORES] en personvern.html y vilkar.html
      ([DATO], [DITT FIRMANAVN], [DITT ORG.NR], [DITT NAVN], [DIN E-POST])

---

## ⚡ OPTIMIZACIÓN DE IMÁGENES (cuando lleguen fotos reales de clientes)
- [ ] Crear cuenta Cloudinary (con email de empresa)
- [ ] Reemplazar placeholders CSS por <img> de Cloudinary en cada web
- [ ] URLs con transformaciones: f_auto,q_auto,w_800
- [ ] Añadir loading="lazy" a cada <img>
- [ ] Minificar CSS antes de producción

## 🎨 PRODUCCIÓN DE WEBS DE CLIENTES (cuando llegue el primer pedido)
- [ ] Crear snippets de color por demo (bloques :root con nombre,
      ej: /* SNEKKER – Valnøtt */) para copiar-pegar según el color elegido
- [ ] Un repositorio GitHub por cliente
- [ ] Un site Netlify por cliente
- [ ] Dominio del cliente apuntando a su site

---

## 📋 ANTES DEL LANZAMIENTO PÚBLICO
- [ ] Revisión de todos los textos noruegos por un nativo
- [ ] Hoja de cálculo de seguimiento de pedidos
- [ ] Plantillas de emails de estado (confirmación, entrega, etc.)
- [ ] Probar todo el recorrido de compra de punta a punta

---

## 🎨 SISTEMA DE PERSONALIZACIÓN DE COLOR (funcionalidad premium — diseñar DESPUÉS de todas las demos)
- Selector de color VISUAL (clic, sin escribir códigos — el cliente no se equivoca)
- Rangos CURADOS (no libre total) para que siempre se vea profesional
- Color principal (hero): gama curada de ~12-16 colores que combinan
- Fondo: 3-4 tonos muy claros (gris, beige, crema, lavanda claro)
- Color secundario/contraste: generado del principal, o 2-3 opciones que combinen
- Opciones de hero: foto sí/no, completo/mitad, textura sí/no, typing sí/no, palabras del hero (de opciones que damos)
- Snippet muy organizado para construir sin trabajo manual
- Objetivo: que el cliente no tema que su web sea igual a otras
- Considerar cobrarlo como extra premium (+X kr) vs. diseño estándar



---

## 🏭 SISTEMA DE PLANTILLAS CON MARCADORES (hacer ANTES de despegar la tienda — preparar el "stock")

**Objetivo:** tener plantillas listas para rellenar rápido cada vez que se venda una web, sin construir desde cero ni buscar dónde va cada dato.

**Qué construir:**
1. **Snippets que generen cada demo CON marcadores ya puestos**
   - Ej: escribir `rorlegger-plantilla` + Tab → aparece todo el HTML del rørlegger con `[FIRMANAVN]`, `[TITTEL]`, `[TELEFON]`, etc. en vez de datos de ejemplo (Nordvik Rør, etc.)
   - Un snippet por cada demo (14 en total: 7 oficios × 2 diseños)
   - Al vender: generar plantilla al instante + reemplazar marcadores (Ctrl+H) con la info del cliente

2. **Formularios de pedido detallados por secciones** (bestill-*.html)
   - Preguntas explicativas, agrupadas por sección de la web, en orden
   - Cada pregunta con ejemplo y campo del tamaño correcto
   - El cliente rellena ordenado → la info llega lista para copiar a los marcadores

**Marcadores a definir por demo** (ejemplos): [FIRMANAVN], [HERO_TITTEL], [HERO_FRASE], [TELEFON], [EPOST], [ADRESSE], [ORG_NR], [SERVICE_1..6], [OM_OSS_TEKST], [AAR_ERFARING], [ANTALL_JOBBER], [PRIS_*], etc. — ajustados a cada sección de cada demo.

**Flujo final al vender:**
1. Cliente rellena formulario bestill → info ordenada por secciones
2. Generar plantilla con snippet (`[oficio]-plantilla` + Tab)
3. Buscar-reemplazar cada marcador con la respuesta del cliente
4. Añadir sus fotos reales (Cloudinary)
5. Web lista en minutos

**Nota:** los snippets ya creados (14 legales/HTML) son para construir; estos serían para rellenar al vender. Se combinan.


---

## 🏭 SISTEMA DE PLANTILLAS + FORMULARIOS INTELIGENTES (hacer ANTES de despegar — preparar el "stock")

**Visión:** el cliente rellena un formulario visual y ordenado → recibe todo estructurado y listo para pegar → rellenar una web toma minutos.

**Las 4 piezas del sistema:**

**1. Snippets que generan cada demo CON marcadores**
- Ej: `rorlegger-plantilla` + Tab → todo el HTML del rørlegger con `[FIRMANAVN]`, `[TITTEL]`, `[TELEFON]`, `[SERVICE_1]`, etc. en vez de datos de ejemplo
- Uno por demo (14 total: 7 oficios × 2 diseños)

**2. Formularios de pedido detallados por secciones (bestill-*.html)**
- Preguntas explicativas ("El título grande que ve la gente al entrar, ej: 'Rørlegger i Bergen'")
- Agrupadas por sección de la web, EN EL ORDEN de la página
- Cada pregunta: explicación + ejemplo + campo del tamaño correcto (corto/mediano/párrafo, cantidad exacta de campos)

**3. El formulario DEVUELVE el texto ya organizado y estructurado**
- En vez de email desordenado → salida lista para copiar:


- Coincide con los marcadores del código → copiar-reemplazar directo

**4. Selectores de color VISUALES integrados en el formulario**
- El cliente elige colores haciendo clic (sin escribir hex)
- Rangos curados de colores escandinavos (evitar que teman "web igual a otras")
- Los colores elegidos salen también en el texto organizado, para pegar en el CSS
- Opciones de hero: foto sí/no, completo/mitad, textura sí/no, typing sí/no
- Considerar cobrar la personalización de color como premium

**Flujo final al vender:**
1. Cliente rellena formulario visual (textos por sección + colores por clic)
2. Formulario devuelve todo organizado con marcadores
3. Generar plantilla con snippet (`[oficio]-plantilla` + Tab)
4. Copiar-reemplazar marcadores con la salida del formulario
5. Añadir fotos reales del cliente (Cloudinary)
6. Web personalizada lista en minutos

**Notas técnicas:**
- El "formulario que devuelve texto organizado" se hace con JS (recoge los campos y genera el bloque de texto formateado)
- Los selectores de color: reutilizar el concepto de la muestra del maler, pero para elegir la paleta de SU web
- Definir marcadores consistentes por sección de cada demo (requiere sesión concentrada — un error se replica a todas las ventas)


ok entonces terminemos de hacer los Template + placeholder substitution" o scaffolding faltantes. luego me ensenas como utilizarlo simulando que ya tengo un cliente. luego hacemos una pagina de om oss bien chevera para mi tienda. luego hacemos el enkel y creamos dominio y email profesional. y publico en netlify ponemos clave. probramos todo el flujo y como me llega el email y si todo funciona. luego hacemos stripe con mi cuenta bancaria personal, activamos vipps y dejamos todo listo. cuando tengo mas 40.000 kr vendido abro cuenta bancaria para la tienda y cambio a AS y luego conecto con fiver con venda los 50.000 kr para llevar contabilidad y pagar taxes. no se nada deso, asi que me recomiendas para llevar el control de todo para tener todo listo para empezar las contabilidad cuando toque? ademas que herramientas me recomiendas para llevar el control de los pedidos de mi clientes por orden y fecha y clasificacion, asi como los trabajos entregados etc, y llevar registro de todos mi clientes, paginas creadas, actualizacions, pagos anuales, etc, no se como llevar el control de todo. y no quiero depender de ti para hacer todos mis trabajos cuando mi tienda despegue.


En Noruega tienes bokføringsplikt desde la primera venta. Desde la factura número 1 debes guardar comprobantes, numerar facturas correlativamente y llevar registro — durante 5 años

ENK tiene regnskapsplikt (årsregnskap) solo si factura más de 50.000 kr. Skattemelding for enkeltpersonforetak.

Næringsoppgave — con una analogía
Si trabajas para una empresa: tu jefe le manda a Skatteetaten un informe: "a Lallal le pagué 500.000 kr este año". Skatteetaten ya lo sabe todo. Tú solo confirmas tu skattemelding.
Si trabajas para ti: nadie informa por ti. Skatteetaten no tiene ni idea de si vendiste 0 kr o 500.000 kr. Ni de qué gastaste.
La næringsoppgave es tú haciendo ese informe. Es el papel donde le dices a Skatteetaten:

"Mi negocio este año: ingresé 89.000 kr, gasté 12.000 kr, gané 77.000 kr."

Por qué es obligatorio: porque sin ese papel, Skatteetaten no sabe sobre qué cobrarte impuestos. Tú pagas impuestos sobre el beneficio (77.000), no sobre lo que facturaste (89.000). Si no declaras los gastos, pagarías de más. Si no declaras los ingresos, es fraude.
Y el detalle clave: tu ENK no es una empresa aparte de ti. Legalmente sois la misma persona. Por eso el negocio no hace su propia declaración — se cuelga de la tuya, como un anexo

Qué es SAF-T
Es un formato estándar (XML) para exportar toda tu contabilidad, desarrollado para simplificar el intercambio de datos contables entre las empresas y Skatteetaten.
Piénsalo así: si mañana Skatteetaten te hace una inspección (bokettersyn), no quieren que les mandes 200 PDFs sueltos. Quieren un archivo con todo, en un formato que su sistema pueda leer automáticamente. Ese archivo es el SAF-T.



Tu flujo de venta — y dónde duele
Lo que va a pasar:
1. Cliente rellena formulario  → Netlify te manda email (el CONTENIDO)
2. Va a la página takk
3. Reserva semana + paga        → Cal.com te manda email (la FECHA)
                                → Stripe te manda email (el DINERO)
4. Tú haces la factura          → Conta/Fiken
5. Construyes la web            → ny-kunde.py
6. Entregas                     → email al cliente
El problema honesto: tres emails de tres sistemas que no se hablan. Netlify no sabe que pagó. Cal.com no sabe qué contenido mandó. Stripe no sabe qué compró exactamente.
Lo que los une: el email del cliente. Aparece en los tres. Es tu clave



Cómo optimizarlo (sin backend)
1. Filtros de Gmail — que se ordenen solos
Crea 3 etiquetas y 3 filtros:

Remitente Netlify → etiqueta 📋 Bestillinger
Remitente Cal.com → etiqueta 📅 Bookinger
Remitente Stripe → etiqueta 💰 Betalinger

Así abres una carpeta y ves solo pedidos, otra y ves solo pagos. Cinco minutos de configurar, orden para siempre.
2. La hoja de cálculo = tu única verdad
Los tres emails llegan, tú apuntas una fila:
FechaClienteEmailServicioPrecioUkeBetaltFakturaLevert15.07Nordvik Rørpost@...Nettside890030✅#12⏳
Esa fila es tu control. Los emails son solo la materia prima.
3. La factura en 3 clics
En Conta/Fiken creas una vez tus productos: "Nettside 8.900 kr", "Årsavgift 777 kr", "Ny seksjon 790 kr"… Luego cada factura es: elegir cliente → elegir producto → marcar "pagada con Stripe" → enviar. Treinta segundos.
4. Una rutina escrita (RUTINER.md en tu repo)
CUANDO LLEGA UN PEDIDO:
1. Apuntar fila en Sheets
2. Verificar que llegaron los 3 emails (contenido + reserva + pago)
3. Crear factura en Fiken → enviar al cliente
4. Copiar datos del resumen a kunde-data.txt
5. python3 ny-kunde.py <oficio> <cliente> kunde-data.txt
6. Descargar fotos de Cloudinary → optimizar → bilder/
7. Revisar con Live Server
8. Deploy
9. Email de entrega + marcar ✅ en Sheets
Eso es lo que de verdad te hace independiente. No mi ayuda — tu checklist.

---

## 🔍 REVISIÓN RIGUROSA POR GREMIO (demo ↔ formulario ↔ molde)

Método validado: para cada gremio, comprobar que las tres piezas piden y muestran
exactamente lo mismo. Errores encontrados con este método: moldes con fotos de
Unsplash, formularios que imponen el tipo de obra, huecos sin numerar, textos de
demo escritos a fuego en los moldes.

- [x] maler / maler-moderne (Fargerom 11 fotos, Sjatteret 10)
- [x] snekker (5 + hero + team + logo, títulos libres)
- [x] snekker-moderne (huecos y marcadores) — falta decidir el campo KATEGORI
- [ ] fotograf / fotograf-moderne — moldes con Unsplash, form pide 6 y la demo enseña 16
- [ ] rorlegger / rorlegger-moderne
- [ ] elektriker / elektriker-moderne
- [ ] gartner / gartner-moderne
- [ ] renhold / renhold-moderne
- [ ] flyttebyra / flyttebyra-moderne
- [ ] portefolje

## 🛡️ MEJORAR EL SISTEMA DE CHEQUEO (sjekk.py + test-alt.sh)

El test pasaba en vacío durante semanas porque buscaba archivos que ya no existían.
Prioridad alta: lo que no se comprueba, se rompe sin avisar.

- [ ] Fallar si un glob no encuentra archivos (causa raíz del fallo silencioso)
- [ ] Cuadre por gremio: nº de fotos en demo == campos en formulario == huecos en molde
- [ ] Cuadrar también los TEXTOS: servicios, proyectos y títulos
      (el formulario pedía 6 servicios y la demo tenía 3; lo detectó Lallal a ojo, no el script)
- [ ] Ningún molde debe contener unsplash ni URLs externas de imagen
- [ ] Todo hueco de imagen debe estar numerado (photo-galleriN, photo-hero, photo-om)
- [ ] Los moldes no deben tener textos de la demo: exigir marcadores
- [ ] Enlaces internos rotos en toda la tienda (encontró 13 de una vez)
- [ ] Llaves balanceadas en cada CSS (fallo recurrente por pegados cortados)
- [ ] IDs duplicados en HTML (rompen la navegación del menú)
- [ ] Matriz de completitud: cada gremio con demo, form, molde y línea en kopier-juridisk

## 🖼️ FLUJO DE IMÁGENES (decidido)

Cloudinary solo como tránsito: el cliente sube las fotos desde el formulario.
Después se descargan, se alojan en Netlify (plan de pago, el más económico) y se
borran de Cloudinary para no superar el límite mensual gratuito.

- [ ] Contratar el plan de pago de Netlify
- [ ] Documentar el paso de descarga y borrado en RUTINER.md
- [ ] Definir tamaños y compresión antes de subir a Netlify

## 💰 PRECIOS (pendiente de aplicar)

Nuevo modelo: 7 700 kr de pago único + 2 000 kr al año.
Baja la barrera de entrada y aumenta el ingreso recurrente.

- [x] Cambiar 8 900 → 7 700 en toda la tienda
- [x] Cambiar 1 200 → 2 000 en toda la tienda
- [ ] Revisar los textos del FAQ que explican qué cubre la cuota anual
- [ ] Verificar qué cubre de verdad cada servicio antes de prometerlo:
      Netlify (hosting, SSL, CDN, formularios con límite mensual),
      domene.no (dominio .no, ~150–250 kr/año),
      copias de seguridad: NO las hace Netlify — hay que montarlas con git

## 🆕 NUEVOS GREMIOS (webs estáticas)

- [ ] Fisioterapeuta
- [ ] Entrenador personal
- [ ] Ingeniero / consultor
- [ ] Restaurante (ojo: suelen querer menú actualizable, choca con el modelo estático)

## 💾 COPIAS DE SEGURIDAD DE LAS WEBS DE CLIENTES

Ahora mismo las webs generadas viven solo en ~/kunder/ del portátil.
Si se promete copia de seguridad, hay que resolverlo antes.

- [ ] Un repositorio git por cliente
- [ ] Documentar cómo restaurar una web desde cero


## 🎨 MEJORAS DE LA TIENDA (diseño y profesionalismo)
Objetivo: que la tienda (index) se vea más elegante y profesional.
- [ ] Revisar y mejorar la paleta de colores de la tienda
- [ ] Identificar secciones que se ven pobres o poco profesionales
- [ ] Rediseñar/pulir esas secciones (espaciado, tipografía, jerarquía visual)
- [ ] Mantener la sobriedad noruega — nada genérico ni exagerado

## 🍽️ NUEVA DEMO: RESTAURANTE (web estática)
Demo para restaurantes / pequeños restaurantes noruegos. SIN compra online.
Contenido típico de una web de restaurante en Noruega:
- [ ] Menú con lista de precios (secciones: forrett, hovedrett, dessert, drikke)
- [ ] Datos de contacto (teléfono, email, dirección)
- [ ] Horario de apertura (åpningstider)
- [ ] Ubicación / mapa
- [ ] Fotos del local y los platos
- [ ] Posible: reservas por teléfono/email (ikke online booking)
- [ ] Posible: enlaces a redes sociales
NOTA (de TODO previo): los restaurantes suelen querer menú actualizable,
lo que choca con el modelo estático. Decidir cómo manejarlo:
¿menú fijo? ¿servicio de actualización aparte? ¿un formato fácil de editar?


## 🎨 REDISEÑO DE COLORES DE LA TIENDA (decidido, pendiente de ejecutar)
Paleta ELEGIDA (fondo oscuro tipo editor de código):
- Fondo principal: #0e0e10 (negro cálido); fondo alterno: #141418; superficie: #18181c
- Líneas/bordes: #26262c
- Texto principal: #f5f5f2 (blanco cálido); secundario: #a0a0a8; tenue: #8a8a92
- ACENTO PRINCIPAL (acción: botones, precio, título destacado): verde manzana #9dd649
  (texto sobre verde: #16240a)
- ACENTO SECUNDARIO (navegación e info: enlaces, "din" del logo, iconos info): celeste #a5d8f3
- ACENTO DE ÉNFASIS (puntual: badges "Populær", detalles): rojo coral #e05a4d
Regla de uso: verde=acción, celeste=info/navegación, rojo=énfasis puntual. Nunca compitiendo.

DIAGNÓSTICO (importante para el chat nuevo):
- css/style.css tiene 2804 líneas y ~366 colores FIJOS (hex a mano), solo ~159 usos de var().
- La tienda NO es "clara": ya tiene secciones oscuras pintadas a mano (hero con degradados
  verde bosque, etc.) MEZCLADAS con secciones claras. Por eso cambiar solo el :root no funcionó
  ("todo del mismo color") — la mayoría de colores no usan variables.
- Por tanto el rediseño hay que hacerlo SECCIÓN POR SECCIÓN (32 secciones marcadas con
  comentarios /* ---- X ---- */), convirtiendo colores fijos a las variables nuevas.
- Estrategia recomendada: (1) definir las variables nuevas en :root, (2) ir sección por sección
  (Hero, Header, Sections, Steps, Bransjer, Pris, FAQ, Footer, etc.) cambiando los hex fijos por
  var(--...), (3) revisar visualmente cada una antes de pasar a la siguiente.
- Copia de seguridad previa: css/style.css.bak-colores (por si acaso).
- El intento inicial (solo :root) se REVIRTIÓ; la tienda está como estaba antes del intento.
