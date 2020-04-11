#  Explication processus web scraping 

## Introduction


On voulait récupérer les données du site Aviation Safety qui nous semblait très complet. Cependant celui ci ne proposait pas de dataset à télécharger comme nous avions l'habitude de trouver. 
On a donc réalisé des recherches pour trouver un moyen de récupérer ces données.

Nous avons donc découvert la notion de web scraping.
Nous la réalisons sur python grâce aux modules `BeautifulSoup` et `requests` notamment.





## script python: web_scrap_new.py

Ce fichier python sert à récupérer plusieurs fichiers csv par année donnant des informations plus précises sur les accidents.

#### La fonction `page_principale(annee)` 

```python
def page_principale(annee):
   return(f'https://aviation-safety.net/database/dblist.php?Year={annee}')
```

Cette fonction renvoie juste le lien de la premiere page d'accidents: un lien comme celui ci ['https://aviation-safety.net/database/dblist.php?Year=2020']

#### La fonction `toutes_les_pages_par_annee(year)`

Cette fonction renvoie comme son nom l'indique une liste des toutes les pages d'accidents par année. En effet certaines années comportent plusieurs pages d'accident comme en 1945 (pendant la seconde Guerre Mondiale) où on a 15 pages d'accidents. (Il y a 100 accidents par page). Il est donc question de récupérer tous les liens et les mettre dans la même liste.

#### La fonction `page_par_annee(Li)`

Cette fonction prend en argument un lien (provenant de la fonction `toutes_les_pages_par_annee`) donc un lien d'une page où plusieurs accidents sont référencés. Et cette fonction va récuperer tous les urls envoyant à chaque page d'accident


#### La fonction `liste_page_par_annee(annee)` 

Cette fonction renvoie pour une année donnée une liste de tous les urls des accidents. Elle récupère les urls donnés par la fonction `page_par_année`.

**Par exemple** : L'année 1945 contient 15 pages d'accidents. On récupère le lien de la première page par la fonction `page_principale(annee)`. A partir de ce lien la fonction `toutes_les_pages_par_annee(year)` va récupérer les liens des 14 autres pages d'accidents pour les mettre dans la même liste. Pour chaque page d'accidents, la fonction `page_par_annee(Li)` va récupérer tous les urls renvoyant à chaque accident individuellement.
Enfin la fonction `liste_page_par_annee(annee)`rassemble tous ces liens. 


#### La fonction `donnees_par_accident(url)` 

C'est la fonction qui va récupérer nos données. 
On a choisi de donner une structure de dictionnaire pour plusieurs raisons: 
- C'est ce qui se prêtait le mieux à la page html qui nous était fournie. 
- On peut prendre les différentes clés qui nous intéressent 



#### la fonction `lien_a_enlever()` 

Cette fonction n'est utile que rarement: quand certaines pages web ne fonctionnent pas pendant le webscraping. On enlève donc de la liste les pages d'accidents qui empêchent le fonctionnement de l'algorithme.


#### La fonction `fichier_csv(annee)`

Cette fonction prend en argument une année. C'est la fonction qui va permettre l'écriture du fichier csv 
On y utilise la fonction `csv.DictWriter`

## script python: web_scrapping_record.py

Ce fichier python sert à récupérer plusieurs fichiers csv par année donnant les informations générales sur les accidents.


#### les fonctions `page_princpale(annee)` et `toutes_les_pages_par_annee(year)`ne changent pas du précédent script

#### la fonction `liens_par_annee` 
Renvoie  une liste de listes des données générales des accidents 


#### la fonction fichier_csv 
permet l'écriture des fichiers csv par année, ici c'est beaucoup plus simple et rapide que précedemment notamment car l'utilisation des listes est plus rapide à écrire

### fichier de données record2

Un fichier avec tous les documents csv.
Une ligne contient tout d'abord 

## Difficultés rencontrées

Nous avons rencontré plusieurs difficultés 
