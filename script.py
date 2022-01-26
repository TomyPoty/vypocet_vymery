#Potřebné knihovny
import urllib.request
import zipfile
import geopandas as gpd
import os
import sys
import shutil


#Kódy katastrálních území v obci Kroměříž (588296)
kod = ["675008","674991","766798","766810","647446","793001","674834","657301","604038","726133","726141"]

#Deklarování proměnných
pocet = 0
vymera = 0.0
vymera_prum = 0.0

#Proměnné pro zápis do CSV
kod_kromeriz = "588296"
delimiter = ";"

#Cyklus, který stáhne parcely podle kódů katastrálního území a sečte jejich výměry
for i in range(11):

    #URL adresa ke stahnutí parcel podle kódu z ČÚZK
    url = 'https://services.cuzk.cz/shp/ku/epsg-5514/'+kod[i]+'.zip'
    #Cesta k ZIP souboru podle kódu
    path_to_zip = './'+kod[i]+'.zip'
    #Cesta ke složce, kam se budou rozbalovat ZIP soubory
    path_to_folder = './files/'
    #Cesta k SHP souboru podle kódu, obsahující polygonové parcely
    path_to_shp = './files/'+kod[i]+'/PARCELY_KN_P.shp'


    #funkce, která stáhne ZIP soubor z ČÚZK do složky, ve které je uložen tento script
    urllib.request.urlretrieve(url, path_to_zip)

    #Extrahování veškerého obsahu ZIP souboru do složky "files"
    with zipfile.ZipFile(path_to_zip, 'r') as extrakce:
        extrakce.extractall(path_to_folder)

    #načtení SHP pomocí funkce z knihovny Geopandas
    data = gpd.read_file(path_to_shp)

    #Cyklus, který projede všechny parcely v KÚ
    for index, row in data.iterrows():
        #Výpočet celkové výměry pomocí funkce z knihovny Geopandas
        vymera = row['geometry'].area + vymera
        #Pomocná proměnná, která ukládá počet parcel v KÚ
        pocet = pocet + 1

    #Info výpis
    print("Výměra pro katastrální území č. "+kod[i]+" vypočtena")

    #Vymazání stáhnutého ZIP souboru (hodnotu výměry máme uloženou, ZIP již nepotřebujeme)
    os.remove(path_to_zip)
    #Konec cyklu

#Po dokončení cyklu vymazání složky s extrahovanými ZIP soubory (soubory již nepotřebujeme)
shutil.rmtree(path_to_folder)

#Výpočet průměrné výměry všech parcel v obci Kroměříž a zaokrouhlení na 3 des. místa
vymera_prum = round(vymera/pocet, 3)

#vytvoření CSV a zapsání kódu obce a průměrné výměry (oddělovač ;)
csv = open("vymera.csv", "w")
csv.write(kod_kromeriz + delimiter + str(vymera_prum))
csv.close()

#Info výpis, konec scriptu
print("Průměrná výměra parcel v obci Kroměříž byla zapsána do CSV souboru.")



