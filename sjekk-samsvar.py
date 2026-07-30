#!/usr/bin/env python3
"""
Integrity checker for the template system.

Verifies that every showcase demo (demoer/) has a matching, clean
template (maler/demoer/) that ny-kunde.py can actually fill in.

Two severities:
  FAIL    - deterministic, certain bugs. Any FAIL makes the script exit 1.
  WARNING - fuzzy heuristics. Reported, but never block (exit stays 0).

Usage: python3 sjekk-samsvar.py
"""
import re, os, sys, glob

SHOWCASE = "demoer"
TEMPLATES = "maler/demoer"
DATA_MODEL = "maler/kunde-data-mal.txt"

# Demo identities that must never survive inside a template.
DEMO_NAMES = ["Nordvik", "Fossum", "Voltek", "Berg Maler", "Lund",
              "Lien", "Grønn Hage", "Trygg Flytt", "Klar Renhold"]

# Colour markers ny-kunde.py derives automatically (not in the data model).
AUTO_MARKERS = {"FARGE_HOVED_MORK", "FARGE_HOVED_LYS",
                "FARGE_MORK_DYP", "FARGE_MORK_LYS"}

# Valid photo-hole base names.
VALID_HOLE = re.compile(r'^photo-(hero|om|placeholder|galleri\d+|arbeid\d+|tjeneste\d+)$')

# External IMAGE only: unsplash by name, or url()/<img src> pointing to an image file.
# Deliberately does NOT match Google Fonts or map embeds.
EXTERNAL_IMG = re.compile(
    r'unsplash'
    r'|(?:url\(\s*["\']?|<img\b[^>]*\bsrc\s*=\s*["\'])https?://[^"\')> ]+\.(?:jpe?g|png|webp|gif|avif|svg)',
    re.I)

fails, warnings = [], []


def read(*parts):
    path = os.path.join(*parts)
    return open(path, encoding="utf-8").read() if os.path.isfile(path) else ""


def strip_comments(text):
    """Remove CSS /* ... */ and HTML <!-- ... --> comments before scanning,
    so a note that merely mentions Unsplash is not mistaken for a real image."""
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    return text


def template_files(template_dir):
    """All .html and .css files inside one template folder."""
    out = []
    for root, _, files in os.walk(template_dir):
        for f in files:
            if f.endswith((".html", ".css")):
                out.append(os.path.join(root, f))
    return out


def load_vocabulary():
    """Marker names the data model knows about, plus the auto colours."""
    if not os.path.isfile(DATA_MODEL):
        fails.append(f"Data model missing: {DATA_MODEL} - cannot validate markers")
        return None
    vocab = set(AUTO_MARKERS)
    for line in open(DATA_MODEL, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            vocab.add(line.split("=", 1)[0].strip())
    return vocab


def photo_holes(text):
    return set(re.findall(r'photo-(?:hero|om|galleri\d+|arbeid\d+|tjeneste\d+)', text))


def demo_image_slots(demo_name):
    """Approximate number of image slots a showcase demo shows.
    Counts <img> tags plus CSS background-image declarations."""
    html = read(SHOWCASE, demo_name, "index.html")
    css = read(SHOWCASE, demo_name, "css", "style.css")
    return len(re.findall(r'<img\b', html)) + len(re.findall(r'background-image\s*:', css))


# ---- discover showcase demos ----------------------------------------------
demos = sorted(os.path.basename(p.rstrip("/"))
               for p in glob.glob(f"{SHOWCASE}/*/") if os.path.isdir(p))

if not demos:
    print(f"FAIL: no showcase demos found under {SHOWCASE}/ - checker verified nothing")
    sys.exit(1)

vocab = load_vocabulary()


# ---- per-demo checks -------------------------------------------------------
for demo in demos:
    tmpl_dir = os.path.join(TEMPLATES, demo)

    # FAIL: template does not exist at all
    if not os.path.isdir(tmpl_dir):
        fails.append(f"[{demo}] template missing: {tmpl_dir}/")
        continue

    files = template_files(tmpl_dir)
    if not files:
        fails.append(f"[{demo}] template folder has no html/css files")
        continue

    blob = "\n".join(read(f) for f in files)

    # FAIL: external images only (unsplash, or http url()/<img> to an image file).
    # Fonts (fonts.googleapis/gstatic) and map embeds are NOT flagged.
    if EXTERNAL_IMG.search(strip_comments(blob)):
        hit = next((os.path.relpath(f) for f in files
                    if EXTERNAL_IMG.search(strip_comments(read(f)))), tmpl_dir)
        fails.append(f"[{demo}] external image in template: {hit}")

    # FAIL: demo identity leaked into template
    leaked = [name for name in DEMO_NAMES
              if re.search(r'\b' + re.escape(name) + r'\b', blob)]
    if leaked:
        fails.append(f"[{demo}] demo data left in template: {', '.join(leaked)}")

    # FAIL: markers the data model can't fill
    if vocab is not None:
        used = set(re.findall(r'\[([A-Z][A-Z_0-9]*)\]', blob))
        unknown = sorted(used - vocab)
        if unknown:
            fails.append(f"[{demo}] unknown markers (not in data model): {', '.join(unknown)}")

    # WARNING: odd photo-hole names
    all_holes = set(re.findall(r'photo-[a-z0-9]+', blob))
    odd = sorted(h for h in all_holes if not VALID_HOLE.match(h))
    if odd:
        warnings.append(f"[{demo}] unusual photo names: {', '.join(odd)}")

    # WARNING: image-slot count demo vs template
    d = demo_image_slots(demo)
    t = len(photo_holes(blob))
    if t and d and abs(d - t) > 2:
        warnings.append(f"[{demo}] image slots differ: demo~{d} vs template {t}")


# ---- form cross-check (WARNING only) --------------------------------------
def form_groups(form):
    out = {}
    for group, num in re.findall(r'name="([a-z]+)(\d+)_[a-z]+"', form):
        out[group] = max(out.get(group, 0), int(num))
    return out


def demo_blocks(html):
    out = {}
    out["tjeneste"] = (len(re.findall(r'class="tjeneste[ "]', html))
                       + len(re.findall(r'class="tjeneste-enkel"', html))
                       + len(re.findall(r'class="tjeneste-rad"', html)))
    out["prosjekt"] = (len(re.findall(r'class="prosjekt"', html))
                       + len(re.findall(r'class="arbeid-kort"', html)))
    return {k: v for k, v in out.items() if v}


for form_path in sorted(glob.glob("bestill-*.html")):
    trade = os.path.basename(form_path)[len("bestill-"):-len(".html")]
    form = read(form_path)
    groups = form_groups(form)
    # FAIL: form summary title must match the trade (catches forms copied from another trade)
    def _norm(x): return x.upper().replace("Æ","A").replace("Ø","O").replace("Å","A")
    m_tit = re.search(r"BESTILLING\s*[–-]\s*([A-ZÆØÅ]+)SIDE", form)
    if not m_tit:
        fails.append(f"[{trade}] form summary title missing (BESTILLING - XXXSIDE)")
    else:
        _tit = _norm(m_tit.group(1)); _exp = _norm(trade)
        if _tit not in _exp and _exp not in _tit:
            fails.append(f"[{trade}] form summary says '{m_tit.group(1)}SIDE' - copied from wrong trade?")
    for variant in (trade, f"{trade}-moderne"):
        demo_html = read(SHOWCASE, variant, "index.html")
        if not demo_html:
            continue
        shown = demo_blocks(demo_html)
        for group, asked in groups.items():
            if group in shown and asked > shown[group]:
                warnings.append(
                    f"[{variant}] form asks {asked} {group}, demo shows {shown[group]}")


# ---- report ----------------------------------------------------------------
line = "=" * 60
print(f"\n{line}\n  SAMSVAR - template system check\n{line}")
print(f"  showcase demos: {len(demos)}   templates dir: {TEMPLATES}/\n")

if fails:
    print(f"  FAIL ({len(fails)}):")
    for f in fails:
        print(f"    x {f}")
if warnings:
    print(f"\n  WARNING ({len(warnings)}):")
    for w in warnings:
        print(f"    . {w}")
if not fails and not warnings:
    print("  All templates clean and consistent.")

print()
if fails:
    print("  RESULT: NOT OK - fix the FAILs above\n")
    sys.exit(1)
elif warnings:
    print("  RESULT: OK, but review the warnings\n")
    sys.exit(0)
else:
    print("  RESULT: OK\n")
    sys.exit(0)
