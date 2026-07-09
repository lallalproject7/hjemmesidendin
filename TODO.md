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