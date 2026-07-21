#!/bin/bash
# Kopierer juridiske maler til alle demoer, med hver demos farger og data

kopier() {
  local mappe=$1 firma=$2 epost=$3 tlf=$4 adr=$5
  local mork=$6 aksent=$7 bak=$8 flate=$9 linje=${10} tekst=${11}
  local dato="15. juli 2026"
  local orgnr="999 999 999"

  for fil in personvern cookies; do
    cp "maler/juridisk/$fil.html" "demoer/$mappe/$fil.html"
    sed -i "s|--jur-mork: #2b2e33|--jur-mork: $mork|; \
            s|--jur-aksent: #a86f43|--jur-aksent: $aksent|; \
            s|--jur-bak: #e5e1d8|--jur-bak: $bak|; \
            s|--jur-flate: #f0ede6|--jur-flate: $flate|; \
            s|--jur-linje: #cfc9bd|--jur-linje: $linje|; \
            s|--jur-tekst: #565c66|--jur-tekst: $tekst|; \
            s|\[FIRMANAVN\]|$firma|g; \
            s|\[EPOST\]|$epost|g; \
            s|\[TELEFON\]|$tlf|g; \
            s|\[ADRESSE\]|$adr|g; \
            s|\[ORGNR\]|$orgnr|g; \
            s|\[DATO\]|$dato|g" "demoer/$mappe/$fil.html"
  done
  echo "✓ $mappe"
}

#      mappe                firma                    epost                      tlf            adresse                          mork      aksent    bak       flate     linje     tekst
kopier "rorlegger"          "Vik Rørservice"         "post@vikror.no"           "912 34 567"   "Rørveien 8, 3722 Skien"         "#0f2847" "#22d3ee" "#dde3e8" "#eef2f5" "#c6d0d8" "#4c545f"
kopier "rorlegger-moderne"  "Vik Rørservice"         "post@vikror.no"           "912 34 567"   "Rørveien 8, 3722 Skien"         "#232b36" "#e58348" "#e4e1dc" "#f0ede8" "#d2ccc4" "#4c545f"
kopier "elektriker"         "Nord Elektro"           "post@nordelektro.no"      "913 45 678"   "Strømveien 4, 3722 Skien"       "#16232e" "#b4551d" "#e6e0d6" "#f1ece2" "#d4cdc0" "#4c545f"
kopier "elektriker-moderne" "Nord Elektro"           "post@nordelektro.no"      "913 45 678"   "Strømveien 4, 3722 Skien"       "#0d1424" "#2563eb" "#dee1e8" "#eaedf2" "#c8ccd6" "#4c545f"
kopier "snekker"            "Lund Snekkerverksted"   "post@lundsnekker.no"      "914 56 789"   "Håndverksveien 3, 3735 Skien"   "#1e3b2f" "#c17a54" "#e4e0d5" "#efebe1" "#d2ccbf" "#52604c"
kopier "snekker-moderne"    "Lund Snekkerverksted"   "post@lundsnekker.no"      "914 56 789"   "Håndverksveien 3, 3735 Skien"   "#3f4429" "#ae804b" "#e5e2d4" "#f0ede0" "#d3cebd" "#52604c"
kopier "maler"              "Palett Malerservice"    "post@palettmaler.no"      "915 67 890"   "Fargeveien 12, 3722 Skien"      "#2b3a55" "#3d5a99" "#dfe2e8" "#eaedf2" "#c9cfd9" "#4c545f"
kopier "maler-moderne"      "Kulør Maler"            "post@kulormaler.no"       "915 67 890"   "Fargeveien 12, 3722 Skien"      "#2d2a3e" "#e8734f" "#e3e0e6" "#eeebf0" "#cdc9d4" "#4c545f"
kopier "renhold"            "Skinnende Rent"         "post@skinnenderent.no"    "916 78 901"   "Renveien 5, 3722 Skien"         "#0e5b63" "#14a098" "#dde5e5" "#e9efef" "#c5d2d2" "#4c545f"
kopier "renhold-moderne"    "Skinnende Rent"         "post@skinnenderent.no"    "916 78 901"   "Renveien 5, 3722 Skien"         "#2b2733" "#7c5cbf" "#e3e1e8" "#eeecf2" "#cdc9d6" "#4c545f"
kopier "gartner"            "Grønn Hage"             "post@gronnhage.no"        "917 89 012"   "Hageveien 12, 3722 Skien"       "#2f4a2c" "#4c7c3f" "#e3e5da" "#eff0e7" "#d0d3c4" "#52604c"
kopier "gartner-moderne"    "Grønn Hage"             "post@gronnhage.no"        "917 89 012"   "Hageveien 12, 3722 Skien"       "#17211a" "#c4703f" "#e4e2da" "#f0eee6" "#d1cec2" "#4d514e"
kopier "flyttebyra"         "Grenland Flyttebyrå"    "post@grenlandflytt.no"    "918 90 123"   "Lagerveien 8, 3722 Skien"       "#23272e" "#e8613c" "#e2e3e5" "#eeeff0" "#ccced2" "#4c545f"
kopier "flyttebyra-moderne" "Grenland Flyttebyrå"    "post@grenlandflytt.no"    "918 90 123"   "Lagerveien 8, 3722 Skien"       "#2d2440" "#e8b93f" "#e3e0e6" "#efedf1" "#cdc9d4" "#5b5568"
kopier "portefolje"         "DittFirma"              "post@dittfirma.no"        "912 34 567"   "Skien"                          "#2b2e33" "#a86f43" "#e5e1d8" "#f0ede6" "#cfc9bd" "#565c66"

echo ""
echo "Ferdig – 15 mapper × 2 filer"
kopier "fotograf"           "Nordlys Foto"           "hei@nordlysfoto.no"       "950 00 000"   "Strandgaten 12, 5013 Bergen"    "#1f1c18" "#a8814f" "#faf7f2" "#f1ece3" "#e4ddd0" "#55504a"
kopier "fotograf-moderne"   "Blende Studio"          "hei@blendestudio.no"      "950 00 000"   "Torggata 15, 0181 Oslo"         "#0c0b09" "#ff5c1f" "#f5f2ec" "#eae6de" "#a09a90" "#55504a"
