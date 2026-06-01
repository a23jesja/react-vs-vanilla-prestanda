# -*- coding: utf-8 -*-
# las_lighthouse.py
#
# Det här skriptet läser in mina Lighthouse-resultat (JSON-filer) och plockar ut
# de tre mätvärden jag är intresserad av: LCP, TBT och Speed Index.
# Sedan ritar jag ett linjediagram per mått där alla 100 körningar syns, så att
# spridningen (bruset) mellan mätningarna blir tydlig. Jag räknar även ut
# medelvärde och median för varje mått.
#
# Jag kör Lighthouse från kommandotolken och får då en JSON-fil per körning,
# till exempel van2000_001.json (Vanilla, 2000 produkter, körning nummer 1).

import json
import matplotlib.pyplot as plt

# Hur många körningar jag gjorde per version
ANTAL = 100

# Vilken datamängd jag tittar på just nu (ändras till 500 eller 1000 för de andra)
PRODUKTER = 2000

# Början på filnamnen för de två versionerna
vanilla_prefix = "van2000"
react_prefix = "react2000"


# En egen funktion som öppnar en JSON-fil och hämtar de tre mått jag vill ha.
# Lighthouse sparar tiderna i millisekunder, så jag delar LCP och Speed Index
# med 1000 för att få sekunder (samma enhet som jag använder i rapporten).
# TBT behåller jag i millisekunder eftersom det är den enhet jag redovisar det i.
def hamta_matt(filnamn):
    fil = open(filnamn, encoding="utf-8")   # öppna filen
    data = json.load(fil)                   # läs in JSON-innehållet
    fil.close()                             # stäng filen

    # Hämta de tre värdena. De ligger under "audits" i JSON-filen.
    lcp_ms = data["audits"]["largest-contentful-paint"]["numericValue"]
    tbt_ms = data["audits"]["total-blocking-time"]["numericValue"]
    si_ms = data["audits"]["speed-index"]["numericValue"]

    # Räkna om till sekunder där det behövs
    lcp = lcp_ms / 1000
    si = si_ms / 1000
    tbt = tbt_ms

    return lcp, tbt, si


# Här samlar jag alla värden. En lista per mått och version.
vanilla_lcp = []
vanilla_tbt = []
vanilla_si = []
react_lcp = []
react_tbt = []
react_si = []

# Loopa igenom körning 1 till 100 och läs in båda versionerna
for i in range(1, ANTAL + 1):

    # Gör numret tresiffrigt så filerna hamnar i rätt ordning (001, 002, ... 100)
    if i < 10:
        nummer = "00" + str(i)
    elif i < 100:
        nummer = "0" + str(i)
    else:
        nummer = str(i)

    # Läs in Vanilla-körningen och spara värdena i listorna
    lcp, tbt, si = hamta_matt(vanilla_prefix + "_" + nummer + ".json")
    vanilla_lcp.append(lcp)
    vanilla_tbt.append(tbt)
    vanilla_si.append(si)

    # Läs in React-körningen och spara värdena i listorna
    lcp, tbt, si = hamta_matt(react_prefix + "_" + nummer + ".json")
    react_lcp.append(lcp)
    react_tbt.append(tbt)
    react_si.append(si)

    # Skriv ut hur långt jag kommit var tionde körning så jag ser att det jobbar
    if i % 10 == 0:
        print("Läst in", i, "av", ANTAL, "körningar")


# En egen funktion som räknar ut medelvärdet (summan delat på antalet)
def medel(lista):
    return sum(lista) / len(lista)


# En egen funktion som räknar ut medianen (mittenvärdet i en sorterad lista).
# Är antalet jämnt tar jag genomsnittet av de två mittenvärdena.
def median(lista):
    sorterad = sorted(lista)
    mitten = len(sorterad) // 2
    if len(sorterad) % 2 == 0:
        return (sorterad[mitten - 1] + sorterad[mitten]) / 2
    else:
        return sorterad[mitten]


# Skriv ut medelvärde och median för varje mått och version
print("")
print("Resultat för", PRODUKTER, "produkter")
print("")
print("LCP (sekunder):")
print("  Vanilla - medel:", round(medel(vanilla_lcp), 3), "median:", round(median(vanilla_lcp), 3))
print("  React   - medel:", round(medel(react_lcp), 3), "median:", round(median(react_lcp), 3))
print("")
print("TBT (millisekunder):")
print("  Vanilla - medel:", round(medel(vanilla_tbt), 1), "median:", round(median(vanilla_tbt), 1))
print("  React   - medel:", round(medel(react_tbt), 1), "median:", round(median(react_tbt), 1))
print("")
print("Speed Index (sekunder):")
print("  Vanilla - medel:", round(medel(vanilla_si), 3), "median:", round(median(vanilla_si), 3))
print("  React   - medel:", round(medel(react_si), 3), "median:", round(median(react_si), 3))


# x-axeln är körningarna 1 till 100
korningar = list(range(1, ANTAL + 1))

# Diagram 1: LCP i sekunder.
# markersize=3 och linewidth=1 gör punkterna och linjerna små nog att 100
# körningar inte blir en enda röra.
plt.figure()
plt.plot(korningar, vanilla_lcp, marker="o", markersize=3, linewidth=1, label="Vanilla")
plt.plot(korningar, react_lcp, marker="o", markersize=3, linewidth=1, label="React")
plt.title("LCP (sekunder) - " + str(PRODUKTER) + " produkter")
plt.xlabel("Körning")
plt.ylabel("LCP (sekunder)")
plt.legend()
plt.grid(True)
plt.savefig("lcp_" + str(PRODUKTER) + ".png")

# Diagram 2: TBT i millisekunder
plt.figure()
plt.plot(korningar, vanilla_tbt, marker="o", markersize=3, linewidth=1, label="Vanilla")
plt.plot(korningar, react_tbt, marker="o", markersize=3, linewidth=1, label="React")
plt.title("TBT (millisekunder) - " + str(PRODUKTER) + " produkter")
plt.xlabel("Körning")
plt.ylabel("TBT (millisekunder)")
plt.legend()
plt.grid(True)
plt.savefig("tbt_" + str(PRODUKTER) + ".png")

# Diagram 3: Speed Index i sekunder
plt.figure()
plt.plot(korningar, vanilla_si, marker="o", markersize=3, linewidth=1, label="Vanilla")
plt.plot(korningar, react_si, marker="o", markersize=3, linewidth=1, label="React")
plt.title("Speed Index (sekunder) - " + str(PRODUKTER) + " produkter")
plt.xlabel("Körning")
plt.ylabel("Speed Index (sekunder)")
plt.legend()
plt.grid(True)
plt.savefig("speedindex_" + str(PRODUKTER) + ".png")

print("")
print("Klart! Tre diagram sparade som PNG-filer.")
