# Descriptif des données 

## Fichier de données traitees [données traitées](https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/donnees_traitees.zip) 

Vous trouverez [ici](https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/nettoyage.md) le dossier expliquant le nettoyage des données.

```
identifiant,week_day,date,time,type_event,phase,location,country,total_occupants,total_fatalities,aircraft_damage,aircraft_fate,type_aircraft,number_engines,type_engines,first_flight,cycles,total_airframe_hours,registration,c_n_msn,operator,nature,flight_number,departure_airport_name,departure_airport_IATA,departure_airport_ICAO,departure_airport_country,destination_airport_name,destination_airport_IATA,destination_airport_ICAO,destination_airport_country,crew_number,passengers_number,crew_fatalities,passengers_fatalities,collision_casualties,ground_casualties,status
20200102-0,Thursday,02-JAN-2020,-,A1, Unknown (UNK),5 km (3.1 mls) from  Geneina Airport (EGN),Sudan,18,18, Damaged beyond repair,-,Antonov An-12A,-,-,1962,-,-, -, 2340606,Sudan AF,Military,-,Geneina Airport,EGN,HSCN,Sudan,Khartoum-Civil Airport,KRT,HSSS,Sudan,7,11,7,11,-,-,-
20200103-0,Friday,03-JAN-2020,09:15,A1, En route (ENR),near Haputale,Sri Lanka,4,4, Damaged beyond repair,-,Harbin Yunshuji Y-12 II,-,-,1990,-,-, SCL-857, 0021,Sri Lanka AF,Military,-,Wirawila Airport,WRZ,VCCW,Sri Lanka,Colombo-Ratmalana Airport,RML,VCCC,Sri Lanka,4,0,4,0,-,-,-
20200105-0,Sunday,05-JAN-2020,-,C1, Taxi (TXI),Manda Bay-Camp Simba Air Base,Kenya,3,2, Destroyed, Written off (damaged beyond repair),Beechcraft B300 King Air 350,-,-,-,-,-, registration unknown,-,L3 Technologies,Military,-,-,-,-,-,-,-,-,-,3,0,2,0,-,-,-
20200108-0,Wednesday,08-JAN-2020,06:18,C1, En route (ENR),near Sabashahr,Iran,176,176, Destroyed, Written off (damaged beyond repair),Boeing 737-8KV (WL),2,CFMI CFM56-7B24E,2016,-,-, UR-PSR, 38124/5977,Ukraine International Airlines,International Scheduled Passenger,PS752,Tehran-Imam Khomeini International Airport,IKA,OIIE,Iran,Kiev-Borispol Airport,KBP,UKBB,Ukraine,9,167,9,167,-,-,-
20200109-0,Thursday,09-JAN-2020,-,A1, Landing (LDG),Goma Airport (GOM),Democratic Republic of the Congo,67,0, Substantial, Written off (damaged beyond repair),Lockheed C-130BZ Hercules,-,-,1962,-,-, 403, 3750,South African AF,Military,-,Beni Airport,BNC,FZNP,Democratic Republic of the Congo,Goma Airport,GOM,FZNA,Democratic Republic of the Congo,8,59,0,0,-,-,-
```

## Fichier de données [record2.zip](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/record2.zip)

Un dossier comportant tous les csv par année. Obtenu par webScraping du site [Aviation Safety](https://aviation-safety.net/database/)

Ce sont les données brutes avant nettoyage obtenues grâce au deuxieme web scraping récupérant les données générales sur les accidents. Nous avons toutefois crée un identifiant pour pouvoir croiser nos deux jeux de données (obtenus par web scraping). 

- **un identifiant**: unique obtenu à partir de l'url de la page d'accident
- **une date**: de l'accident
- **type**: type d'avion
- **registration**: numéro/ immatriculation
- **operator**: Compagnie aérienne
- **fat.**: nombre de victimes
- **location**: localisation de l'accident
- une colonne vide à supprimer  qui contenait les drapeaux 
- **pic**: colonne vide à supprimer qui contenait initialement une image
- **cat**: catégorie de l'accident 


```
identifiant,date,type,registration,operator,fat.,location, ,pic,cat

20200102-0,02-JAN-2020,Antonov An-12A,-,Sudan AF,18,near Geneina Airp...,, ,A1
20200103-0,03-JAN-2020,Harbin Yunshuji Y-12 II,SCL-857,Sri Lanka AF,4,near Haputale,, ,A1
20200105-0,05-JAN-2020,Beech B300 King Air 350, ,L3 Technologies,2,Manda Bay-Ca...,, ,C1
20200108-0,08-JAN-2020,Boeing 737-8KV (WL),UR-PSR,Ukraine International Airlines,176,near Sabashahr,,,C1
20200109-0,09-JAN-2020,Lockheed C-130BZ Hercules,403,South African AF,0,Goma Airport...,, ,A1

```
##  Fichier de données [bonnes_donnees2.zip](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/bonnes_donnees2.zip)

Ce sont les données brutes avant nettoyage obtenues grâce au premier web scraping récupérant des données plus précises sur les accidents.

- **un identifiant**: unique obtenu à partir de l'url de la page d'accident permettra de croiser les données 
- **Status**: Statut des informations. Final: rapport d'enquête final officiel. Préliminaire - Officiel: rapport d'enquête préliminaire officiel. Préliminaire: informations de presse et d'autres informations non officielles 
- **Date**: date de l'accident
- **Time**: heure de l'accident
- **Type**: type d'avion, nom
- **Operator**: compagnie aérienne
- **On behalf of**: en cas de location, quelle compagnie aérienne a prêté l'avion.
- **Leased from**: Propriétaire de l'avion, mais ne l'utilisant pas au moment de l'accident.
- **Registration**:
- **C/n / msn**: Numéro de série / numéro de construction du fabricant.
- **First Flight**: année de premier vol
- **Total airframe hrs**: Nombre total d'heures de vol au moment de l'accident.
- **Year built**: année de construction (jamais référencé donc à enlever)
- **Engines**: Nombre et type (modèle et marque) de moteurs.
- **Cycles**: Nombre total de décollages et d'atterrissages au moment de l'accident.
- **Crew:** nombre de décès sur nombre d'équipage
- **Passengers**: nombre de décès sur nombre de passagers
- **Ground casualties**: nombre de victimes au sol
- **Collision casualties**: nombre de victimes dû à une collision
- **Aircraft damage**: Décrit les dommages à l'avion à la suite de l'événement.
- **Aircraft fate**:
- **Location**: localisation de l'accident 
- **Phase**: phase de vol 
- **Nature**: nature du vol (militaire...)
- **Departure airport**: aéroport de départ, de la forme (nom, IATA,ICAO)
- **Destination airport**: aéroport de destination de la forme (nom, IATA,ICAO)
- **Flightnumber**: numéro de vol
- **Probable cause**: on ne l'a pas récupéré au final donc colonne vide
- Total:
```
Identifiant:,Status:,Date:,Time:,Type:,Operator:,Operating for:,On behalf of:,Leased from:,Registration:,C/n / msn:,First flight:,Total airframe hrs:,Year built:,Engines:,Cycles:,Crew:,Passengers:,Ground casualties:,Collision casualties:,Aircraft damage:,Aircraft fate:,Location:,Phase:,Nature:,Departure airport:,Destination airport:,Flightnumber:,Probable cause:,Total:
20200102-0,,Thursday 2 January 2020,,Antonov An-12A,Al Quwwat al-Jawwiya As-Sudaniya (Sudanese Air Force),,,, -, 2340606, 1962,,,,,Fatalities: 7 / Occupants: 7,Fatalities: 11 / Occupants: 11,,, Damaged beyond repair,,"5 km (3.1 mls) from  Geneina Airport (EGN) Sudan) ", Unknown (UNK),Military,"Geneina Airport (EGN/HSCN), Sudan","Khartoum-Civil Airport (KRT/HSSS), Sudan",,,Fatalities: 18 / Occupants: 18 
20200103-0,,Friday 3 January 2020,09:15,Harbin Yunshuji Y-12 II,Sri Lanka Air Force,,,, SCL-857, 0021, 1990,,,,,Fatalities: 4 / Occupants: 4,Fatalities: 0 / Occupants: 0,,, Damaged beyond repair,,"near Haputale (   Sri Lanka) ", En route (ENR),Military,"Wirawila Airport (WRZ/VCCW), Sri Lanka","Colombo-Ratmalana Airport (RML/VCCC), Sri Lanka",,,Fatalities: 4 / Occupants: 4 
20200105-0,,Sunday 5 January 2020,,Beechcraft B300 King Air 350,L3 Technologies,,,, registration unknown, , ,,,,,Fatalities: 2 / Occupants: 3,Fatalities: 0 / Occupants: 0,,, Destroyed, Written off (damaged beyond repair),"Manda Bay-Camp Simba Air Base (   Kenya) ", Taxi (TXI),Military,?,?,,,Fatalities: 2 / Occupants: 3 
20200108-0,,Wednesday 8 January 2020,06:18,Boeing 737-8KV (WL),Ukraine International Airlines,,,, UR-PSR, 38124/5977, 2016-06-21  (3 years 7 months),,, 2 CFMI CFM56-7B24E,,Fatalities: 9 / Occupants: 9,Fatalities: 167 / Occupants: 167,,, Destroyed, Written off (damaged beyond repair),"near Sabashahr (   Iran) ", En route (ENR),International Scheduled Passenger,"Tehran-Imam Khomeini International Airport (IKA/OIIE), Iran","Kiev-Borispol Airport (KBP/UKBB), Ukraine",PS752,,Fatalities: 176 / Occupants: 176 
20200109-0,,Thursday 9 January 2020,,Lockheed C-130BZ Hercules,South African Air Force - SAAF,,,, 403, 3750, 1962,,,,,Fatalities: 0 / Occupants: 8,Fatalities: 0 / Occupants: 59,,, Substantial, Written off (damaged beyond repair),"Goma Airport (GOM) (Democratic Republic of the Congo) ", Landing (LDG),Military,"Beni Airport (BNC/FZNP), Democratic Republic of the Congo","Goma Airport (GOM/FZNA), Democratic Republic of the Congo",,,Fatalities: 0 / Occupants: 67 
```



## le fichier [AviationData.txt](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/AviationData.txt)
C'est un fichier texte qui donne les incidents et accidents d'avions (separateur: '|')

Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date |

```
Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date | 
20200222X95241 | Accident | WPR20CA093 | 02/22/2020 | Columbia, CA | United States | 38.030556 | -120.414444 | O22 |  | Non-Fatal | Substantial | Airplane | N462 | Aviat | A1 | No | 1 |  | Part 91: General Aviation |  | Personal |  |  |  | 1 |  |  |  | Preliminary | 02/25/2020 | 
20200222X62353 | Accident | CEN20FA096 | 02/22/2020 | Rogers, MN | United States | 45.198055 | -93.652778 |  | N/A | Fatal(1) | Destroyed | Airplane | N3266Q | Beech | A36 | No | 1 | Reciprocating | Part 91: General Aviation |  | Personal |  | 1 |  |  |  | VMC | MANEUVERING | Preliminary | 02/26/2020 | 
20200220X10054 | Accident | CEN20FA093 | 02/20/2020 | Coleman, TX | United States | 32.050833 | -99.570000 |  | N/A | Fatal(3) | Destroyed | Airplane | N860J | Beech | 200 | No |  |  | Part 91: General Aviation |  | Personal |  | 3 |  |  |  | IMC | CRUISE | Preliminary | 02/26/2020 | 
20200219X80403 | Accident | WPR20CA092 | 02/18/2020 | Colexico, CA | United States |  |  |  |  | Unavailable | Substantial |  | N288NS | Bell | OH 58A | No |  |  | Part 137: Agricultural |  | Aerial Application |  |  |  |  |  |  |  | Preliminary | 02/21/2020 | 
```

*Attention pas mal de données manquantes on dirait.*

## le fichier [airports.dat.txt](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/airports.dat.txt) 
C'est un fichier texte qui donne des informations sur les différents aéroports localisation .. peut être utile pour la table aéroport! et contient les différents codes IATA ICAO utiles pour identifier les aéroports

| données       | explications    |   
| :------------ | --------------: |
| Airport ID    |     Unique OpenFlights identifier for this airport. |    
| Name          | Name of airport.| 
|  City         | Main city served by airport |    
| Country | Country or territory where airport is located. |
| IATA | géocode à trois lettre décrivant des aéroport |
| ICAO |  code ICAO  | 
| Latitude | Decimal degrees, usually to six significant digits. Negative is South, positive is North. |
| Longitude | Decimal degrees, usually to six significant digits. Negative is West, positive is East. |
| Altitude | In feet  |
| Timezone | Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5. |
| DST | Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). |
| Tz databae time zone | Timezone in "tz" (Olson) format, eg. "America/Los_Angeles". |
| Type | dans ce document  des types airports ( *donc à enlever ?*) |
| Source | source des données ( *à enlever*) |
