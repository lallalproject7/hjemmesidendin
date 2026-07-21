#!/usr/bin/env python3
"""
Optimiza las imágenes de img/demoer/ para web.
Reduce tamaño y peso sin pérdida visible de calidad.
"""
import os
from PIL import Image

CARPETA = os.path.expanduser("~/hjemmesidendin/img/demoer")
BACKUP = os.path.expanduser("~/hjemmesidendin/img/demoer-original")
ANCHO_MAX = 800   # ancho máximo en píxeles
CALIDAD = 82      # calidad JPEG (0-100)

# 1. Hacer copia de seguridad de los originales (solo la primera vez)
if not os.path.exists(BACKUP):
    os.makedirs(BACKUP)
    for f in os.listdir(CARPETA):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            src = os.path.join(CARPETA, f)
            dst = os.path.join(BACKUP, f)
            Image.open(src).save(dst)
    print(f"✓ Copia de seguridad creada en {BACKUP}")

# 2. Optimizar cada imagen
total_antes = 0
total_despues = 0

for f in sorted(os.listdir(CARPETA)):
    if not f.lower().endswith((".jpg", ".jpeg", ".png")):
        continue
    ruta = os.path.join(CARPETA, f)
    antes = os.path.getsize(ruta)
    total_antes += antes

    img = Image.open(ruta)

    # Convertir a RGB si hace falta (para guardar como JPEG)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    # Redimensionar si es más ancha que ANCHO_MAX
    if img.width > ANCHO_MAX:
        alto = int(img.height * ANCHO_MAX / img.width)
        img = img.resize((ANCHO_MAX, alto), Image.LANCZOS)

    # Guardar optimizada
    img.save(ruta, "JPEG", quality=CALIDAD, optimize=True)

    despues = os.path.getsize(ruta)
    total_despues += despues
    print(f"  {f}: {antes//1024} KB → {despues//1024} KB")

print(f"\n✓ Total: {total_antes//1024//1024} MB → {total_despues//1024} KB")