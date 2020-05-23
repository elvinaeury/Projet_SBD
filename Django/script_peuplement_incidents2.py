#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/home/destash/anaconda3/bin python3

from appliweb.models import airports, accidents_events, aircrafts, fatalities_report, flight_info, departure_airport, destination_airport
from django.core.exceptions import ObjectDoesNotExist
import csv #,datetime

annees = [k for k in range(1919,2021)]
annees.append(1900)

#annees = [2007]

lignes_problematiques = {}
nbAirports = 0

for annee in annees :
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
            #print("cycles : ",cycles, "--", type(cycles))
            #print("total_occupants : ", total_occupants, type(total_occupants))
            
            ####champs entiers
            """
            for champ in [total_occupants,total_fatalities,number_engines,first_flight,cycles,total_airframe_hours,
            crew_fatalities,passengers_fatalities,collision_casualties,ground_casualties,crew_number,passengers_number] :
                if not(champ==None) :
                    champ = int(float(champ))
            """

            if not(total_occupants==None) :
                total_occupants = int(float(total_occupants))

            if not(total_fatalities==None) :
                total_fatalities = int(float(total_fatalities))

            if not(number_engines==None) :
                number_engines = int(float(number_engines))
            
            if not(first_flight==None) :
                first_flight = int(float(first_flight))

            if not(cycles==None) :
                cycles = int(float(cycles))

            if not(total_airframe_hours==None) :
                total_airframe_hours = int(float(total_airframe_hours))

            if not(crew_fatalities==None) :
                crew_fatalities = int(float(crew_fatalities))

            if not(passengers_fatalities==None) :
                passengers_fatalities = int(float(passengers_fatalities))

            if not(collision_casualties==None) :
                collision_casualties = int(float(collision_casualties))

            if not(ground_casualties==None) :
                ground_casualties = int(float(ground_casualties))

            if not(crew_number==None) :
                crew_number = int(float(crew_number))

            if not(passengers_number==None) :
                passengers_number = int(float(passengers_number))
            
            #print("cycles : ",cycles, "--", type(cycles))
            #print("total_occupants : ", total_occupants, type(total_occupants))
            #break
            """
            ###champs floatants
            for champ in [total_airframe_hours] :
                if not(champ==None) :
                    champ = float(champ)
            """

            #enregistrement des tables

            ###enregistrement dans la table accidents_events
            try :
                accident = accidents_events.objects.get(identifiant=identifiant)
                print(f"""
                Année {annee}, ligne {indice + 1}, table accidents_events : rien à ajouter \n
                    identifiant = {identifiant} existe déjà
                """)
            except ObjectDoesNotExist as err :
                try : 
                    accident = accidents_events(identifiant=identifiant,week_day=week_day,date=date,time=time,type_event=type_event,
                    phase=phase,location=location,country=country,total_occupants=total_occupants,
                    total_fatalities=total_fatalities,aircraft_damage=aircraft_damage,aircraft_fate=aircraft_fate)
                    
                    accident.save()
                    print(f"Ajout accidents_events : identifiant = {identifiant}")
                except Exception as e :
                    echec = f"""
                    Annee {annee} ligne {indice + 1} : echec table accidents_events \n
                        identifiant = {identifiant}\n
                        Erreur = {e}
                    """
                    lignes_problematiques_par_annee.append(echec)
                    continue

            ###enregistrement dans la table aircrafts
            try :
                aircraft = aircrafts.objects.get(id_aircraft=accident)
                print(f"""
                Année {annee}, ligne {indice + 1}, table aircrafts : rien à ajouter \n
                    Enregistrement lié à accident.identifiant = {accident.identifiant} existe déjà
                """)
            except ObjectDoesNotExist as err :
                try :
                    aircraft = aircrafts(id_aircraft=accident,type_aircraft=type_aircraft,number_engines=number_engines,type_engines=type_engines,first_flight=first_flight,
                    cycles=cycles,total_airframe_hours=total_airframe_hours,registration=registration,c_n_msn=c_n_msn)

                    aircraft.save()
                    print(f"Ajout table aircrafts : accident.identifiant = {accident.identifiant}")
                except Exception as e :
                    echec = f"""
                    Annee {annee} ligne {indice + 1} : echec table aircrafts \n
                        identifiant = {identifiant}\n
                        Erreur = {e}
                    """
                    lignes_problematiques_par_annee.append(echec)
                    continue
            
            ###enregistrement dans la table fatalities_report
            try : 
                report = fatalities_report.objects.get(id_report=accident)
                print(f"""
                Année {annee}, ligne {indice + 1}, table fatalities_report : rien à ajouter \n
                    Enregistrement lié à accident.identifiant = {accident.identifiant} existe déjà
                """)
            except ObjectDoesNotExist as err :
                try :
                    report = fatalities_report(id_report=accident,crew_fatalities=crew_fatalities,
                    passengers_fatalities=passengers_fatalities,collision_casualties=collision_casualties,ground_casualties=ground_casualties,status=status)

                    report.save()
                    print(f"Ajout table fatalities_report : accident.identifiant = {accident.identifiant}")
                except Exception as e :
                    echec = f"""
                    Annee {annee} ligne {indice + 1} : echec table fatalities_report \n
                        identifiant = {identifiant}\n
                        Erreur = {e}
                    """
                    lignes_problematiques_par_annee.append(echec)
                    continue
            ###enregistrement dans la table flight_info
            try : 
                flight = flight_info.objects.get(id_flight=accident,)
                print(f"""
                Année {annee}, ligne {indice + 1}, table flight_info : rien à ajouter \n
                    Enregistrement lié à accident.identifiant = {accident.identifiant} existe déjà
                """)
            except ObjectDoesNotExist as err :
                try :
                    flight = flight_info(id_flight=accident,operator=operator,nature=nature,
                    flight_number=flight_number,crew_number=crew_number,passengers_number=passengers_number)

                    flight.save()
                    print(f"Ajout table flight_info : accident.identifiant = {accident.identifiant}")
                except Exception as e :
                    echec = f"""
                    Annee {annee} ligne {indice + 1} : echec table flight_info \n
                        identifiant = {identifiant}\n
                        Erreur = {e}
                    """
                    lignes_problematiques_par_annee.append(echec)
                    continue
            
            ###enregistrement dans la table departure_airport
            if not(departure_airport_ICAO == None) : #l'aéroport de départ est connu dans les donées
                try :
                    airport = departure_airport.objects.get(flight=flight)
                    print(f"""
                    Année {annee}, ligne {indice + 1}, table departure_airport : rien à ajouter \n
                        Enregistrement lié à accident.identifiant = {accident.identifiant} existe déjà
                    """)
                except ObjectDoesNotExist as err1 :
                    try :
                        #l'aéroport de départ existe déjà dans la table aéroport
                        departure = airports.objects.get(code_icao=departure_airport_ICAO)
                        
                        airport = departure_airport(flight=flight,icao=departure)
                        airport.save()
                        print(f"Ajout table departure_airport : accident.identifiant = {accident.identifiant}")
                    except ObjectDoesNotExist as err2 :
                        #l'aérport de départ n'existe pas encore dans la table aéroport
                        #on l'enregistre mais avec lat = lng = alt = None car ces champs ne sont pas renseignés dans ce jeu de données
                        try :
                            departure = airports(code_iata=departure_airport_IATA,code_icao=departure_airport_ICAO,
                            name=departure_airport_name,country=departure_airport_country,latitude=None,longitude=None,altitude=None)
                            
                            departure.save()
                            nbAirports += 1
                            print(f"Ajout table airports : code_icao = {departure_airport_ICAO}")

                            #on enregistre enfin la relation entre flight et aeroport dans la departure_airport
                            airport = departure_airport(flight=flight,icao=departure)

                            airport.save()
                            print(f"Ajout table departure_airport : accident.identifiant = {accident.identifiant}")
                        except Exception as e :
                            #problème à déboger comme dans les autres except Exception précédemment
                            echec = f"""
                            Annee {annee} ligne {indice + 1} : echec table departure_airport \n
                                identifiant = {identifiant}\n
                                Erreur = {e}
                            """
                            lignes_problematiques_par_annee.append(echec)
                            continue

            ###enregistrement dans la table destination_airport
            ######## même traitement que pour departure_airport
            if not(destination_airport_ICAO == None) : #l'aéroport de destination est connu dans les donées
                try :
                    airport = destination_airport.objects.get(flight=flight)
                    print(f"""
                    Année {annee}, ligne {indice + 1}, table destination_airport : rien à ajouter \n
                        Enregistrement lié à accident.identifiant = {accident.identifiant} existe déjà
                    """)
                except ObjectDoesNotExist as err1 :
                    try :
                        #l'aéroport de destination existe déjà dans la table aéroport
                        destination = airports.objects.get(code_icao=destination_airport_ICAO)
                        
                        airport = destination_airport(flight=flight,icao=destination)
                        airport.save()
                        print(f"Ajout table destination_airport : accident.identifiant = {accident.identifiant}")
                    except ObjectDoesNotExist as err2 :
                        #l'aérport de destination n'existe pas encore dans la table aéroport
                        #on l'enregistre mais avec lat = lng = alt = None car ces champs ne sont pas renseignés dans ce jeu de données
                        try :
                            destination = airports(code_iata=destination_airport_IATA,code_icao=destination_airport_ICAO,
                            name=destination_airport_name,country=destination_airport_country,latitude=None,longitude=None,altitude=None)
                            
                            destination.save()
                            nbAirports += 1
                            print(f"Ajout table airports : code_icao = {destination_airport_ICAO}")

                            #on enregistre enfin la relation entre flight et aeroport dans la destination_airport
                            airport = destination_airport(flight=flight,icao=destination)

                            airport.save()
                            print(f"Ajout table destination_airport : accident.identifiant = {accident.identifiant}")
                        except Exception as e :
                            #problème à déboger comme dans les autres except Exception précédemment
                            echec = f"""
                            Annee {annee} ligne {indice + 1} : echec table destination_airport \n
                                identifiant = {identifiant}\n
                                Erreur = {e}
                            """
                            lignes_problematiques_par_annee.append(echec)
                            continue

        if len(lignes_problematiques_par_annee) > 0 :
            lignes_problematiques[annee] = lignes_problematiques_par_annee
        print(f"""
        ----------------------------------------------------------------------------------------------\n
         Traitement année {annee} achevé \n
        -----------------------------------------------------------------------------------------------\n
        """)

#aéroports ajoutés à la table airports pour infos :
print(f"Nombre d'aéroports ajoutés : {nbAirports} \n")
#infos de débogage si nécessaire
print(f"""
************************************************************************\n
Détails de problèmes : \n
{len(lignes_problematiques)} année(s) problématique(s) au total :
""")
for annee in lignes_problematiques :
    print(f"    ---> Année {annee} : {len(lignes_problematiques[annee])}  lignes problématiques au total : \n")
    for echec in lignes_problematiques[annee] :
        print(f"        -- {echec}")
print("""
*************************************************************************\n
""")