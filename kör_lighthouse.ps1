# kor_lighthouse.ps1
#
# Det här skriptet kör Lighthouse 100 gånger på samma sida och sparar
# en JSON-fil per körning. Jag ändrar adressen och namnet längst upp
# och kör om skriptet en gång för varje version och datamängd.

# Adressen till sidan jag testar just nu
$adress = "http://localhost:8000/vanilla-js/"

# Början på filnamnen (van2000 betyder Vanilla med 2000 produkter)
$namn = "van2000"

# Hur många gånger jag kör
$antal = 3

# Skapa en mapp för resultaten om den inte redan finns
mkdir lighthouse_json -Force

# Loopa från 1 till 100
for ($i = 1; $i -le $antal; $i++) {

    # Gör numret tresiffrigt (001, 002, ... 100) så filerna hamnar i rätt ordning
    $nr = $i.ToString("000")

    # Bygg ihop sökvägen till filen som ska sparas
    $fil = "lighthouse_json\$namn" + "_" + "$nr.json"

    # Skriv ut hur långt jag kommit
    Write-Host "Kör test $i av $antal"

    # Själva Lighthouse-kommandot:
    #   --output=json        sparar resultatet som JSON
    #   --only-categories     mäter bara prestanda (inte SEO, tillgänglighet osv.)
    #   --preset=desktop      kör i desktop-läge, samma som i studien
    #   --chrome-flags        kör Chrome utan fönster (headless) för stabila mätningar
    lighthouse $adress --output=json --output-path=$fil --only-categories=performance --preset=desktop --quiet --chrome-flags="--headless"
}

Write-Host "Klart med $antal körningar för $namn"
