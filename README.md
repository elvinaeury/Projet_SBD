# Projet_SBD



Composition du trinôme: 
Destin ASHUZA CIRUMANGA
Nadia GHERNAOUT
Elvina GOVENDASAMY

Le sujet:
**Incidents d'avions à travers le monde.**

## Table of contents
* [TO-DO list](#to-do-list)
* [Requêtes à lancer](#requêtes-à-lancer)
* [Partie visualisation](#partie-visualisation)
* [Données](#données)

## TO-DO List

- [x] Choisir toutes les données et les récuperer
- [ ] Remplir le GitHub public avec plus de renseignements pour les profs
- [x] Créer un [modèle relationnel](https://github.com/elvinaeury/projet_test/blob/master/modele_relationnel/description_modele_relationnel.md) une fois que toutes les données ont été récupérées
- [x] Se renseigner sur le web scrapping (avec module `beautiful-soup`)
- [x] [Web Scrapping](https://github.com/elvinaeury/projet_test/blob/master/Web_scrapping/web.md) (En cours)



## Requêtes à lancer
- Quels sont les endroits où il y a le plus d’accidents/ incidents (entre des certaines dates)
- Afficher quels types d'accides ou incidents ont fait le plus de blessés/morts
- Donner un aéroport de départ et les incidents qui qui se sont passés et leur distance par rapport à cet aéroport et des caractéristiques sur ces accidents 
- Combien d'accidents par année ? (puis graphique)
- liste des accidents par :
  - par année
  - par type d'avion
  - par localisation
- landing ? take-off ? during flight ?



### Partie visualisation
- viualiser une carte du monde qui affiche par des points les lieu où il y a eu des accidents (pendant une certaine période)
- bonus: quand on passe la souris sur ces différents points on a plus renseignements quant à l'incident voire ajouter des photos si possible


## Données

- le fichier **AviationData.txt** est un fichier texte qui donne les incidents et accidents d'avions (separateur: '|')

Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date |

```
Event Id | Investigation Type | Accident Number | Event Date | Location | Country | Latitude | Longitude | Airport Code | Airport Name | Injury Severity | Aircraft Damage | Aircraft Category | Registration Number | Make | Model | Amateur Built | Number of Engines | Engine Type | FAR Description | Schedule | Purpose of Flight | Air Carrier | Total Fatal Injuries | Total Serious Injuries | Total Minor Injuries | Total Uninjured | Weather Condition | Broad Phase of Flight | Report Status | Publication Date | 
20200222X95241 | Accident | WPR20CA093 | 02/22/2020 | Columbia, CA | United States | 38.030556 | -120.414444 | O22 |  | Non-Fatal | Substantial | Airplane | N462 | Aviat | A1 | No | 1 |  | Part 91: General Aviation |  | Personal |  |  |  | 1 |  |  |  | Preliminary | 02/25/2020 | 
20200222X62353 | Accident | CEN20FA096 | 02/22/2020 | Rogers, MN | United States | 45.198055 | -93.652778 |  | N/A | Fatal(1) | Destroyed | Airplane | N3266Q | Beech | A36 | No | 1 | Reciprocating | Part 91: General Aviation |  | Personal |  | 1 |  |  |  | VMC | MANEUVERING | Preliminary | 02/26/2020 | 
20200220X10054 | Accident | CEN20FA093 | 02/20/2020 | Coleman, TX | United States | 32.050833 | -99.570000 |  | N/A | Fatal(3) | Destroyed | Airplane | N860J | Beech | 200 | No |  |  | Part 91: General Aviation |  | Personal |  | 3 |  |  |  | IMC | CRUISE | Preliminary | 02/26/2020 | 
20200219X80403 | Accident | WPR20CA092 | 02/18/2020 | Colexico, CA | United States |  |  |  |  | Unavailable | Substantial |  | N288NS | Bell | OH 58A | No |  |  | Part 137: Agricultural |  | Aerial Application |  |  |  |  |  |  |  | Preliminary | 02/21/2020 | 
```

*Attention pas mal de données manquantes on dirait.*

- le fichier **airports.dat.txt** est un fichier texte qui donne des informations sur les différents aéroports localisation .. pas directement en lien avec les incidents mais peut être pratique

| données       | explications    |   
| :------------ | --------------: |
| Airport ID    |     Unique OpenFlights identifier for this airport. |    
| Name          | Name of airport.| 
|  City         | Main city served by airport |    
| Country | Country or territory where airport is located. |
| IATA | géocode à trois lettre décrivant des aéroport |
| ICAO |  code ICAO ( *utile ? (voir si utilisé dans d'autres bases sinon à enlever* ) | 
| Latitude | Decimal degrees, usually to six significant digits. Negative is South, positive is North. |
| Longitude | Decimal degrees, usually to six significant digits. Negative is West, positive is East. |
| Altitude | In feet (*utile ?*) |
| Timezone | Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5. |
| DST | Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). |
| Tz databae time zone | Timezone in "tz" (Olson) format, eg. "America/Los_Angeles". |
| Type | dans ce document  des types airports ( *donc à enlever ?*) |
| Source | source des données ( *à enlever*) |

```
1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports"
2,"Madang Airport","Madang","Papua New Guinea","MAG","AYMD",-5.20707988739,145.789001465,20,10,"U","Pacific/Port_Moresby","airport","OurAirports"
3,"Mount Hagen Kagamuga Airport","Mount Hagen","Papua New Guinea","HGU","AYMH",-5.826789855957031,144.29600524902344,5388,10,"U","Pacific/Port_Moresby","airport","OurAirports"
4,"Nadzab Airport","Nadzab","Papua New Guinea","LAE","AYNZ",-6.569803,146.725977,239,10,"U","Pacific/Port_Moresby","airport","OurAirports"
5,"Port Moresby Jacksons International Airport","Port Moresby","Papua New Guinea","POM","AYPY",-9.443380355834961,147.22000122070312,146,10,"U","Pacific/Port_Moresby","airport","OurAirports"
```
- données venant du site web [Aviation safety](https://aviation-safety.net/database/) à récupérer via le web scrapping

```
Status:,Date:,Time:,Type:,Operator:,Leased from:,Registration:,C/n / msn:,First flight:,Total airframe hrs:,Year built:,Engines:,Cycles:,Crew:,Passengers:,Ground casualties:,Collision casualties:,Aircraft damage:,Aircraft fate:,Location:,Phase:,Nature:,Departure airport:,Destination airport:,Flightnumber:,Probable cause:,Total:
Preliminary,Monday 2 January 2017,,Reims Cessna F406 Caravan II,Air Excel,, 5H-WOW, F406-0060, 1991,,,,,Fatalities: 0 / Occupants: 1,Fatalities: 0 / Occupants: 5,,, Substantial,,"Sasakwa Airstrip (   Tanzania) ", Unknown (UNK),Passenger,?,?,,,Fatalities: 0 / Occupants: 6 
Preliminary,Monday 2 January 2017,12:20,Let L-410UVP,Doren Air Congo,, 9Q-CZR, 851336, 1985,,,,,Fatalities: 0 / Occupants: 2,Fatalities: 0 / Occupants: 0,,, Substantial,,"Shabunda Airport (   Democratic Republic of the Congo) 
", Landing (LDG),Cargo,"Bukavu-Kavumu Airport (BKY/FZMA), Democratic Republic of the Congo","Shabunda Airport (FZMW), Democratic Republic of the Congo",,,Fatalities: 0 / Occupants: 2 
Preliminary - official,Monday 2 January 2017,16:43,Hawker 800XP,Pinnacle Air Charter,, N910JD, 258420, 1999,,, 2 Honeywell TFE731-SER,,Fatalities: 0 / Occupants: 2,Fatalities: 0 / Occupants: 0,,, Substantial,,"Scottsdale Airport, AZ (SCF) (   United States of America) 
", Landing (LDG),Private,"Tucson International Airport, AZ (TUS/KTUS), United States of America","Scottsdale Airport, AZ (SCF/KSDL), United States of America",,,Fatalities: 0 / Occupants: 2 



```




