#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/home/destash/anaconda3/bin python3

from appliweb.models import airports, accidents_events, aircrafts, fatalities_report, flight_info, departure_airport, destination_airport
from django.core.exceptions import ObjectDoesNotExist
import csv #,datetime

annees = [k for k in range(1919,2021)]
annees.append(1900)

annees = [2007]

lignes_problematiques = []
nbtour = 0

for annee in annees :
    nbtour +=1
    indice = 0
    lignes_problematiques_par_annee = []

    chemin = f"../../nettoyage/donnees_traitees/data_{annee}.csv"

    with open(chemin, encoding="utf-8") as csvfile :
        f = csv.reader(csvfile)
        next(f) #on ignore le header
        for liste in f :
            indice += 1
            
            #valeur nulle pour les champs non renseignés
            for j,champ in enumerate(liste) :
                if champ == "-" :
                    liste[j] = None

            #récupération des différents champs

            identifiant = liste[0] #0
            week_day = liste[1] #1
            date = liste[2] #2 #identifiant[:8]  identifiant[:8] est déjà sous la forme AAAAMMJJ (A :année, M : mois, J : jour)
            time = liste[3] #3
            type_event = liste[4] #4
            phase = liste[5] #5
            location = liste[6] #6
            country = liste[7] #7
            total_occupants = liste[8] #8
            total_fatalities = liste[9] #9
            aircraft_damage = liste[10] #10
            aircraft_fate = liste[11] #11
            type_aircraft = liste[12] #12
            number_engines = liste[13] #13
            type_engines = liste[14] #14
            first_flight = liste[15] #15
            cycles = liste[16] #16
            total_airframe_hours = liste[17] #17
            registration = liste[18] #18
            c_n_msn = liste[19] #19
            operator = liste[20] #20
            nature = liste[21] #21
            flight_number = liste[22] #22
            departure_airport_name = liste[23] #23
            departure_airport_IATA = liste[24] #24
            departure_airport_ICAO = liste[25] #25
            departure_airport_country = liste[26] #26
            destination_airport_name = liste[27] #27
            destination_airport_IATA = liste[28] #28
            destination_airport_ICAO = liste[29] #29
            destination_airport_country = liste[30] #30
            crew_number = liste[31] #31
            passengers_number = liste[32] #32
            crew_fatalities = liste[33] #33
            passengers_fatalities = liste[34] #34
            collision_casualties = liste[35] #35
            ground_casualties = liste[36] #36
            status = liste[37] #37

            #conversion des champs dans leurs types tels que prévus dans le modèle (models.py)
            
            """
            ###champs timestamp
            if not(time==None) :
                time = time.split(sep=":")
                date = datetime.datetime(year=int(date[:4]),month=int(date[4:6]),day=int(date[6:]),hour=int(time[0]),minute=int(time[1]))
            else :
                date = datetime.datetime(year=int(date[:4]),month=int(date[4:6]),day=int(date[6:]))
            """

            ####champs entiers
            for champ in [total_occupants,total_fatalities,number_engines,first_flight,cycles,total_airframe_hours,
            crew_fatalities,passengers_fatalities,collision_casualties,ground_casualties,crew_number,passengers_number] :
                if not(champ==None) :
                    champ = int(float(champ))
            
            """
            ###champs floatants
            for champ in [total_airframe_hours] :
                if not(champ==None) :
                    champ = float(champ)
            """

            #enregistrement des tables

            ###enregistrement dans la table accidents_events
            try:
                accident = accidents_events.objects.get(identifiant=identifiant)
                print(f"Année {annee} : rien à ajouter car identifiant = {identifiant} existe déjà")
            except ObjectDoesNotExist as err :
                accident = accidents_events(identifiant=identifiant,week_day=week_day,date=date,type_event=type_event,
                phase=phase,location=location,country=country,total_occupants=total_occupants,
                total_fatalities=total_fatalities,aircraft_damage=aircraft_damage,aircraft_fate=aircraft_fate)
                
                accident.save()
                print(f"Ajout accidents_events : identifiant = {identifiant}")


            ###enregistrement dans la table aircrafts
            """
            try:
                aircraft = aircrafts(id_aircraft=accident)
            except ObjectDoesNotExist as err :
            """
            """
            aircraft = aircrafts(id_aircraft=accident,type_aircraft=type_aircraft,number_engines=number_engines,type_engines=type_engines,first_flight=first_flight,
            cycles=cycles,total_airframe_hours=total_airframe_hours,registration=registration,c_n_msn=c_n_msn)

            aircraft.save()
            print(f"Ajout aircrafs : accident.identifiant = {accident.identifiant}")
            """

            ###enregistrement dans la table fatalities_report

            ###enregistrement dans la table flight_info

            ###enregistrement dans la table departure_airport

            ###enregistrement dans la table destination_airport

        print(f"""
        ----------------------------------------------------------------------------------------------\n
        Annéee {annee} : indice = {indice} \n
        -----------------------------------------------------------------------------------------------\n
        """)
print(f"""
************************************************************************\n
nbtour = {nbtour} \n
*************************************************************************\n
""")