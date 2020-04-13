# Descriptif des données 

## Fichier de données [record2.zip](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/record2.zip)

Un dossier comportant tous les csv par année. Obtenu par webScraping du site [Aviation Safety](https://aviation-safety.net/database/)

Ce sont les données brutes avant nettoyage obtenues grâce au deuxieme web scraping récupérant les données générales sur les accidents. Nous avons toutefois crée un identifiant pour pouvoir croiser nos deux jeux de données (obtenus par web scraping). 

- **un identifiant**: unique obtenu à partir de l'url de la page d'accident
- **une date**: de l'accident
- **type**: type d'avion
- **registration**: numéro/ immatriculation
- **operator**: Ccompagnie aérienne
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


 - **First Flight**: année de premier vol
 - **Total airframe hrs**:
 - **Year built**:
 - **Engines**:
 ```
 Identifiant:,Status:,Date:,Time:,Type:,Operator:,Operating for:,On behalf of:,Leased from:,Registration:,C/n / msn:,First flight:,Total airframe hrs:,Year built:,Engines:,Cycles:,Crew:,Passengers:,Ground casualties:,Collision casualties:,Aircraft damage:,Aircraft fate:,Location:,Phase:,Nature:,Departure airport:,Destination airport:,Flightnumber:,Probable cause:,Total:
 20200102-0,,Thursday 2 January 2020,,Antonov An-12A,Al Quwwat al-Jawwiya As-Sudaniya (Sudanese Air Force),,,, -, 2340606, 1962,,,,,Fatalities: 7 / Occupants: 7,Fatalities: 11 / Occupants: 11,,, Damaged beyond repair,,"5 km (3.1 mls) from  Geneina Airport (EGN) Sudan) ", Unknown (UNK),Military,"Geneina Airport (EGN/HSCN), Sudan","Khartoum-Civil Airport (KRT/HSSS), Sudan",,,Fatalities: 18 / Occupants: 18 
 20200103-0,,Friday 3 January 2020,09:15,Harbin Yunshuji Y-12 II,Sri Lanka Air Force,,,, SCL-857, 0021, 1990,,,,,Fatalities: 4 / Occupants: 4,Fatalities: 0 / Occupants: 0,,, Damaged beyond repair,,"near Haputale (   Sri Lanka) ", En route (ENR),Military,"Wirawila Airport (WRZ/VCCW), Sri Lanka","Colombo-Ratmalana Airport (RML/VCCC), Sri Lanka",,,Fatalities: 4 / Occupants: 4 
 20200105-0,,Sunday 5 January 2020,,Beechcraft B300 King Air 350,L3 Technologies,,,, registration unknown, , ,,,,,Fatalities: 2 / Occupants: 3,Fatalities: 0 / Occupants: 0,,, Destroyed, Written off (damaged beyond repair),"Manda Bay-Camp Simba Air Base (   Kenya) ", Taxi (TXI),Military,?,?,,,Fatalities: 2 / Occupants: 3 
 20200108-0,,Wednesday 8 January 2020,06:18,Boeing 737-8KV (WL),Ukraine International Airlines,,,, UR-PSR, 38124/5977, 2016-06-21  (3 years 7 months),,, 2 CFMI CFM56-7B24E,,Fatalities: 9 / Occupants: 9,Fatalities: 167 / Occupants: 167,,, Destroyed, Written off (damaged beyond repair),"near Sabashahr (   Iran) ", En route (ENR),International Scheduled Passenger,"Tehran-Imam Khomeini International Airport (IKA/OIIE), Iran","Kiev-Borispol Airport (KBP/UKBB), Ukraine",PS752,,Fatalities: 176 / Occupants: 176 
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


```
- données venant du site web [Aviation safety](https://aviation-safety.net/database/) récupérées  (avec clé primaire)

```
Status:,Date:,Time:,Type:,Operator:,Leased from:,Registration:,C/n / msn:,First flight:,Total airframe hrs:,Year built:,Engines:,Cycles:,Crew:,Passengers:,Ground casualties:,Collision casualties:,Aircraft damage:,Aircraft fate:,Location:,Phase:,Nature:,Departure airport:,Destination airport:,Flightnumber:,Probable cause:,Total:
Preliminary,Monday 2 January 2017,,Reims Cessna F406 Caravan II,Air Excel,, 5H-WOW, F406-0060, 1991,,,,,Fatalities: 0 / Occupants: 1,Fatalities: 0 / Occupants: 5,,, Substantial,,"Sasakwa Airstrip (   Tanzania) ", Unknown (UNK),Passenger,?,?,,,Fatalities: 0 / Occupants: 6 
Preliminary,Monday 2 January 2017,12:20,Let L-410UVP,Doren Air Congo,, 9Q-CZR, 851336, 1985,,,,,Fatalities: 0 / Occupants: 2,Fatalities: 0 / Occupants: 0,,, Substantial,,"Shabunda Airport (   Democratic Republic of the Congo) 
", Landing (LDG),Cargo,"Bukavu-Kavumu Airport (BKY/FZMA), Democratic Republic of the Congo","Shabunda Airport (FZMW), Democratic Republic of the Congo",,,Fatalities: 0 / Occupants: 2 
Preliminary - official,Monday 2 January 2017,16:43,Hawker 800XP,Pinnacle Air Charter,, N910JD, 258420, 1999,,, 2 Honeywell TFE731-SER,,Fatalities: 0 / Occupants: 2,Fatalities: 0 / Occupants: 0,,, Substantial,,"Scottsdale Airport, AZ (SCF) (   United States of America) 
", Landing (LDG),Private,"Tucson International Airport, AZ (TUS/KTUS), United States of America","Scottsdale Airport, AZ (SCF/KSDL), United States of America",,,Fatalities: 0 / Occupants: 2 


```
- autre format de données provenant également du site web [Aviation safety](https://aviation-safety.net/database/) (avec clé primaire)


```
date,type,registration,operator,fat.,location, ,pic,cat
03-JAN-2014,Boeing 737-8H4 (WL),N8327A,Southwest Airlines,0,Las Vegas-Mc...,, ,A2
05-JAN-2014,Boeing 767-3W0ER,HS-BKE,"Orient Thai Airlines, op.for Saudi Arabian",0,Madinah-Moha...,, ,A2
05-JAN-2014,Canadair Challenger 601-3R,N115WF,Vineland Corporation,1,Aspen-Pitkin...,,,A1
05-JAN-2014,Airbus A320-231,VT-ESH,Air India,0,Jaipur Inter...,,,A1
07-JAN-2014,Fokker 50,C5-SSA,South Supreme Airlines,0,Aweil Airport,, ,A2
```
