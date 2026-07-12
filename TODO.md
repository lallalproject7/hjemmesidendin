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