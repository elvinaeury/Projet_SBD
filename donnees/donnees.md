
## fichier de données record2.zip

Ce sont les données brutes avant nettoyage obtenues grâce au deuxieme web scraping récupérant les données générales sur les accidents. Nous avons toutefois crée un identifiant pour pouvoir croiser les deux tables. 

Un dossier comportant tous les csv par année. 
Une ligne contient tout d'abord 
- un identifiant: unique obtenu à partir de l'url de la page d'accident
- une date: de l'accident
- type: type d'avion
- registration: numéro/ immatriculation
- operator: Ccompagnie aérienne
- fat.: nombre de victimes
- location:
- une colonne vide à supprimer 
- pic: colonne vide à supprimer qui contenait initialement une image
- cat: catégorie de l'accident 


```
identifiant,date,type,registration,operator,fat.,location, ,pic,cat

20200102-0,02-JAN-2020,Antonov An-12A,-,Sudan AF,18,near Geneina Airp...,, ,A1
20200103-0,03-JAN-2020,Harbin Yunshuji Y-12 II,SCL-857,Sri Lanka AF,4,near Haputale,, ,A1
20200105-0,05-JAN-2020,Beech B300 King Air 350, ,L3 Technologies,2,Manda Bay-Ca...,, ,C1
20200108-0,08-JAN-2020,Boeing 737-8KV (WL),UR-PSR,Ukraine International Airlines,176,near Sabashahr,,,C1
20200109-0,09-JAN-2020,Lockheed C-130BZ Hercules,403,South African AF,0,Goma Airport...,, ,A1

```
