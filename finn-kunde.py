#!/usr/bin/env python3
"""
Finner hvilken kundemappe som hører til et navn, en e-post eller et domene.
Bruk: python3 finn-kunde.py <søketekst>
Eks:  python3 finn-kunde.py skien
      python3 finn-kunde.py holmmaler.no
      python3 finn-kunde.py "Skien Elektro"
"""
import sys, os

if len(sys.argv) != 2:
    print(__doc__)
    sys.exit(1)

sok = sys.argv[1].lower()
kunder_dir = os.path.expanduser("~/kunder")

if not os.path.isdir(kunder_dir):
    print(f"✗ Fant ikke mappen: {kunder_dir}")
    sys.exit(1)

treff = []
uten_data = []

for mappe in sorted(os.listdir(kunder_dir)):
    sti = os.path.join(kunder_dir, mappe)
    if not os.path.isdir(sti):
        continue
    datafil = os.path.join(sti, "kunde-data.txt")
    if not os.path.exists(datafil):
        uten_data.append(mappe)
        continue
    firmanavn, epost = "", ""
    for linje in open(datafil, encoding="utf-8"):
        if linje.startswith("FIRMANAVN="):
            firmanavn = linje.split("=", 1)[1].strip()
        elif linje.startswith("EPOST="):
            epost = linje.split("=", 1)[1].strip()
    if sok in firmanavn.lower() or sok in epost.lower() or sok in mappe.lower():
        treff.append((mappe, firmanavn, epost))

if treff:
    print(f"\n✓ {len(treff)} treff:\n")
    for mappe, firmanavn, epost in treff:
        print(f"  Mappe:   {mappe}")
        print(f"  Bedrift: {firmanavn or '(mangler)'}")
        print(f"  E-post:  {epost or '(mangler)'}")
        print(f"  Sti:     ~/kunder/{mappe}")
        print()
else:
    print(f"\n✗ Ingen kunder matchet '{sys.argv[1]}'")

if uten_data:
    print(f"  ⚠ Mapper uten kunde-data.txt ({len(uten_data)}): {', '.join(uten_data)}")
