# vypocet_vymery
Skript, který vypočítá průměrnou výměru parcel v obci Kroměříž [588296]


### Vysvětlení skriptu:
- Skript stáhne ZIP soubory jednotlivých katastrálních území obce Kroměříž z ČÚZK
- ZIP soubory extrahuje do složky
- Načte z extrahovaných složek SHP soubory "PARCELY_KN_P" a vypočítá průměrnou výměru všech parcel.
- Výsledek uloží do nově vytvořeného CSV souboru ve formátu [kód_obce;průměrná_výměra]
### Použité knihovny:
- urllib.request
- zipfile
- geopandas
- os
- sys
- shutil
### Python verze:
- Python 3.9.5 (Conda version kvůli knihovně Geopandas)
