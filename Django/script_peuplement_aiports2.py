#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/home/destash/anaconda3/bin python3

from appliweb.models import airports 
from django.core.exceptions import ObjectDoesNotExist
import csv

lignes_problematiques = []
indice = 0
with open("../../donnees/airports.dat.txt", encoding="utf-8") as csvfile :
    f = csv.reader(csvfile)
    for liste in f :
        indice += 1
        num = liste[0]
        nom = liste[1]
        ville = liste[2]
        if len(ville) == 0 :
            ville = None
        pays = liste[3]
        iata = liste[4]
        if iata == r"\N" :
            iata = None
        icao = liste[5]
        
        try :
            lat = float(liste[6])
        except ValueError as v :
            echec = f"erreur ligne {indice} : id = {num} --- lat = {liste[6]}"
            lignes_problematiques.append(echec)
            print(echec)
            #input("(press a key...)")
            continue
        
        try :
            lng = float(liste[7])
        except ValueError as v :
            echec = f"erreur ligne {indice} : id = {num} --- lng = {liste[7]}"
            lignes_problematiques.append(echec)
            print(echec)
            #input("(press a key...)")
            continue  
        
        try :
            alt = float(liste[8])
        except ValueError as v :
            echec = f"erreur ligne {indice} : id = {num} --- alt = {liste[8]}"
            lignes_problematiques.append(echec)
            print(echec)
            #input("(press a key...)")
            continue
        
        #print(f"iata = {iata} ---- icao = {icao}")
        try :
            airport = airports.objects.get(code_icao=icao)
        except ObjectDoesNotExist as err :
            aiport = airports(code_iata=iata,code_icao=icao,name=nom,city=ville,country=pays,latitude=lat,longitude=lng,altitude=alt)
            aiport.save()
            print(f"ajout : iata = {iata} --- icao = {icao} --- name = {nom}")

#infos pour débugger 
print("--------------------------------------------------------------------------------------------------\n")
print(f"{len(lignes_problematiques)} lignes problématiques au total :")
for k,echec in enumerate(lignes_problematiques) :
    print(f"  {k+1}) {echec}")
print("--------------------------------------------------------------------------------------------------\n")