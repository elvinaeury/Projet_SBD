# Descriptif des données 

## Fichier de données record2.zip

Un dossier comportant tous les csv par année. Obtenu par webScraping du site [Aviation Safety('https://aviation-safety.net/database/')

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

## le fichier **AviationData.txt** 
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

## le fichier **airports.dat.txt** 
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
