#!/usr/bin/env python3
"""Lager testdata fra datamalen – brukes av test-alt.sh"""
verdier = {
    "FIRMANAVN": "Testbedrift AS", "EPOST": "post@test.no",
    "TELEFON": "900 00 000", "TELEFON_LENKE": "+4790000000",
    "ADRESSE": "Testveien 1, 3700 Skien", "ORGNR": "123 456 789",
    "DATO": "1. august 2026",
    "FARGE_HOVED": "#c1440e", "FARGE_MORK": "#1a2b3c",
    "FARGE_SEKUNDAER": "#e8b93f", "FARGE_BAKGRUNN": "#e6e0d6",
    "TYPED_ORD": "a | b | c",
}
ut = []
for linje in open("maler/kunde-data-mal.txt", encoding="utf-8"):
    linje = linje.strip()
    if not linje or linje.startswith("#") or "=" not in linje:
        continue
    felt = linje.split("=")[0].strip()
    if felt in verdier:
        v = verdier[felt]
    elif felt.endswith("_HEX"):
        v = "#8a9a7b"
    elif felt.endswith("_PRIS"):
        v = "fra 100 kr"
    else:
        v = "Testverdi " + felt.split("_")[-1].lower()
    ut.append(felt + "=" + v)
open("/tmp/t.txt", "w", encoding="utf-8").write("\n".join(ut) + "\n")
print("  (testdata: " + str(len(ut)) + " felt fra datamalen)")
