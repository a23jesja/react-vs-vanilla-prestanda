# -*- coding: utf-8 -*-
# las_lighthouse.py
#
# Det här skriptet läser in alla mina Lighthouse-resultat (JSON-filer) för
# samtliga sex testomgångar (Vanilla och React, vid 500, 1000 och 2000 produkter)
# och plockar ut de tre mätvärden jag analyserar: LCP, TBT och Speed Index.
#
# Skriptet sparar CSV-filer där Vanilla och React ligger i separata kolumner,
# en körning per rad. Det gör att jag enkelt kan rita linjediagram i Google
# Sheets med en linje för Vanilla och en för React.
#
# CSV-filerna använder komma som kolumnavgränsare och punkt som decimaltecken
# (vanlig engelsk CSV), vilket Google Sheets importerar utan problem.
#
# En JSON-fil per körning, t.ex. react2000_001.json (React, 2000 produkter, körning 1).

import json
import os

# Hur många körningar jag gjorde per omgång
ANTAL = 100

# Mappen där JSON-filerna ligger
MAPP = "lighthouse_json"

# De tre datamängderna jag testade
DATAMANGDER = [500, 1000, 2000]


# Funktion som öppnar en JSON-fil och hämtar de tre mått jag vill ha.
# Lighthouse sparar tiderna i millisekunder. Jag räknar om LCP och Speed Index
# till sekunder och behåller TBT i millisekunder.
def hamta_matt(filnamn):
    fil = open(filnamn, encoding="utf-8")
    data = json.load(fil)
    fil.close()

    lcp_ms = data["audits"]["largest-contentful-paint"]["numericValue"]
    tbt_ms = data["audits"]["total-blocking-time"]["numericValue"]
    si_ms = data["audits"]["speed-index"]["numericValue"]

    lcp_s = lcp_ms / 1000
    si_s = si_ms / 1000

    return lcp_s, tbt_ms, si_s


# Funktion som läser in alla 100 körningar för en viss version och datamängd.
# Returnerar tre listor: lcp, tbt och speed index.
def las_omgang(prefix):
    lcp_lista = []
    tbt_lista = []
    si_lista = []
    for i in range(1, ANTAL + 1):
        # Gör numret tresiffrigt (001, 002, ... 100)
        if i < 10:
            nummer = "00" + str(i)
        elif i < 100:
            nummer = "0" + str(i)
        else:
            nummer = str(i)
        sokvag = os.path.join(MAPP, prefix + "_" + nummer + ".json")
        if not os.path.exists(sokvag):
            print("Varning: hittade inte", sokvag)
            continue
        lcp, tbt, si = hamta_matt(sokvag)
        lcp_lista.append(lcp)
        tbt_lista.append(tbt)
        si_lista.append(si)
    return lcp_lista, tbt_lista, si_lista


# Läs in alla sex omgångar och spara i en ordbok
data = {}
for antal_produkter in DATAMANGDER:
    van_prefix = "van" + str(antal_produkter)
    react_prefix = "react" + str(antal_produkter)
    data[("Vanilla", antal_produkter)] = las_omgang(van_prefix)
    data[("React", antal_produkter)] = las_omgang(react_prefix)
    print("Klar med", antal_produkter, "produkter")


# Funktion som skriver en CSV för en datamängd.
# Kolumner: Korning, Vanilla_LCP, React_LCP, Vanilla_TBT, React_TBT,
#           Vanilla_SpeedIndex, React_SpeedIndex
# Då kan jag rita ett linjediagram per mått med Vanilla och React som två linjer.
def skriv_csv(antal_produkter):
    van_lcp, van_tbt, van_si = data[("Vanilla", antal_produkter)]
    react_lcp, react_tbt, react_si = data[("React", antal_produkter)]

    filnamn = "lighthouse_" + str(antal_produkter) + ".csv"
    fil = open(filnamn, "w", encoding="utf-8")
    fil.write("Korning,Vanilla_LCP_s,React_LCP_s,Vanilla_TBT_ms,React_TBT_ms,Vanilla_SpeedIndex_s,React_SpeedIndex_s\n")

    # Hur många rader (om någon omgång saknar filer tar jag den kortaste)
    antal_rader = min(len(van_lcp), len(react_lcp))

    for i in range(antal_rader):
        rad = [
            str(i + 1),
            str(round(van_lcp[i], 3)),
            str(round(react_lcp[i], 3)),
            str(round(van_tbt[i], 1)),
            str(round(react_tbt[i], 1)),
            str(round(van_si[i], 3)),
            str(round(react_si[i], 3)),
        ]
        fil.write(",".join(rad) + "\n")
    fil.close()
    print("Skrev", filnamn, "med", antal_rader, "rader")


# Skriv en CSV per datamängd
for antal_produkter in DATAMANGDER:
    skriv_csv(antal_produkter)


# Egna funktioner för medelvärde och median
def medel(lista):
    return sum(lista) / len(lista)


def median(lista):
    sorterad = sorted(lista)
    mitten = len(sorterad) // 2
    if len(sorterad) % 2 == 0:
        return (sorterad[mitten - 1] + sorterad[mitten]) / 2
    else:
        return sorterad[mitten]


# Skriv ut en sammanfattning så jag ser medel och median för varje grupp
print("")
print("=== Sammanfattning (medel / median) ===")
for antal_produkter in DATAMANGDER:
    for version in ["Vanilla", "React"]:
        lcp_lista, tbt_lista, si_lista = data[(version, antal_produkter)]
        if len(lcp_lista) == 0:
            continue
        print("")
        print(version, antal_produkter, "produkter")
        print("  LCP (s):         medel", round(medel(lcp_lista), 3), " median", round(median(lcp_lista), 3))
        print("  TBT (ms):        medel", round(medel(tbt_lista), 1), " median", round(median(tbt_lista), 1))
        print("  Speed Index (s): medel", round(medel(si_lista), 3), " median", round(median(si_lista), 3))

print("")
print("Klart! Tre CSV-filer (en per datamängd) har skapats.")
print("Vanilla och React ligger i separata kolumner, redo för diagram i Google Sheets.")
