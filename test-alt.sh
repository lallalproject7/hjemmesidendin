#!/bin/bash
echo "╔════════════════════════════════════════════════╗"
echo "║  TEST AV HELE SYSTEMET                         ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# ── 1. Finnes skriptene og er de kjørbare? ──
echo "── 1. SKRIPT ──"
for s in ny-kunde.py koble-bilder.py sjekk.py; do
  if [ ! -f "$s" ]; then echo "  ✗ $s MANGLER"; continue; fi
  if python3 -c "import ast; ast.parse(open('$s').read())" 2>/dev/null; then
    echo "  ✓ $s – gyldig Python"
  else
    echo "  ✗ $s – SYNTAKSFEIL:"
    python3 -c "import ast; ast.parse(open('$s').read())" 2>&1 | tail -2 | sed 's/^/      /'
  fi
done

# ── 2. Feilhåndtering ──
echo ""
echo "── 2. FEILHÅNDTERING ──"
python3 ny-kunde.py 2>&1 | head -5 | grep -q "Lager\|Bruk\|usage" && echo "  ✓ ny-kunde.py: viser hjelp uten argumenter" || echo "  ⚠ ny-kunde.py: uklar melding uten argumenter"
python3 ny-kunde.py finnesikke test /tmp/x.txt 2>&1 | grep -q "Fant ikke" && echo "  ✓ ny-kunde.py: fanger ukjent mal" || echo "  ✗ ny-kunde.py: fanger IKKE ukjent mal"
python3 sjekk.py finnesikke 2>&1 | grep -q "Fant ikke" && echo "  ✓ sjekk.py: fanger ukjent kunde" || echo "  ✗ sjekk.py: fanger IKKE ukjent kunde"
python3 koble-bilder.py finnesikke 2>&1 | grep -q "Fant ikke" && echo "  ✓ koble-bilder.py: fanger ukjent kunde" || echo "  ✗ koble-bilder.py: fanger IKKE ukjent kunde"

# ── 3. Malenes filstruktur ──
echo ""
echo "── 3. MALENES FILER ──"
MANGLER=0
for d in maler/demoer/*/; do
  n=$(basename $d)
  for f in index.html css/style.css personvern.html cookies.html; do
    [ -f "$d$f" ] || { echo "  ✗ $n mangler $f"; MANGLER=$((MANGLER+1)); }
  done
done
[ $MANGLER -eq 0 ] && echo "  ✓ Alle $(ls -d maler/demoer/*/ | wc -l) maler har alle 4 filene"

# ── 4. Datafilen dekker alle markører ──
echo ""
echo "── 4. DATAMAL vs MARKØRER ──"
python3 << 'PY'
import re, os, glob
felt = set()
for l in open("maler/kunde-data-mal.txt", encoding="utf-8"):
    if "=" in l and not l.startswith("#"):
        felt.add(l.split("=")[0].strip())
auto = {"FARGE_HOVED_MORK","FARGE_HOVED_LYS","FARGE_MORK_DYP","FARGE_MORK_LYS"}
mangler = {}
for d in sorted(glob.glob("maler/demoer/*/")):
    m = set()
    for f in ["index.html","css/style.css","personvern.html","cookies.html"]:
        p = os.path.join(d, f)
        if os.path.exists(p):
            m |= set(re.findall(r'\[([A-Z][A-Z_0-9]*)\]', open(p, encoding="utf-8").read()))
    savner = m - felt - auto
    if savner: mangler[os.path.basename(d.rstrip("/"))] = savner
if mangler:
    for k, v in mangler.items():
        print(f"  ✗ {k}: mangler i datamal → {', '.join(sorted(v))}")
else:
    print("  ✓ Datamalen dekker alle markører i alle maler")
PY

# ── 5. Full generering av hver mal ──
echo ""
echo "── 5. GENERERING AV HVER MAL ──"
python3 lag-testdata.py
OK=0; FEIL=0
for d in maler/demoer/*/; do
  m=$(basename $d)
  rm -rf ~/kunder/test-$m
  UT=$(python3 ny-kunde.py $m test-$m /tmp/t.txt 2>&1)
  S=$(python3 sjekk.py test-$m 2>&1)
  if echo "$UT" | grep -q "IKKE ble fylt"; then
    echo "  ✗ $m – ufylte markører: $(echo "$UT" | grep -oP '^\s+\[\K[A-Z_0-9]+' | tr '\n' ' ')"
    FEIL=$((FEIL+1))
  elif echo "$S" | grep -q "🔴"; then
    echo "  ✗ $m – $(echo "$S" | grep -A5 'FEIL' | grep '·' | head -2 | tr '\n' ' ')"
    FEIL=$((FEIL+1))
  else
    echo "  ✓ $m"
    OK=$((OK+1))
  fi
  rm -rf ~/kunder/test-$m
done
rm -f /tmp/t.txt

echo ""
echo "════════════════════════════════════════"
echo "  $OK av $((OK+FEIL)) maler fungerer"
echo "════════════════════════════════════════"

# ── 6. JS-SYNTAKS I SKJEMAENE ──
echo ""
echo "── 6. SKJEMAENES JAVASCRIPT ──"
python3 << 'PYJS'
import re, glob
Q, NL = chr(34), chr(10)
feil = 0
for f in sorted(glob.glob("bestill-*.html")) + ["oppdatering.html", "endringsrunde.html"]:
    m = re.search(r'<script>(.*?)</script>', open(f, encoding="utf-8").read(), re.S)
    if not m: continue
    n = sum(1 for l in m.group(1).split(NL) if l.count(Q) % 2 != 0 and "//" not in l)
    if n:
        print("  x " + f + " - " + str(n) + " linjer med odde antall anforselstegn")
        feil += 1
if feil == 0:
    print("  ok Alle skjemaer har gyldig JS-syntaks")
PYJS
