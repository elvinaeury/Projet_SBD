





## script python: web_scrap_new.py

Ce fichier python sert à récupérer plusieurs fichiers csv par année donnant des informations plus précises sur les accidents.

-la fonction `page_principale(annee)` renvoie juste le lien de la premiere page d'accidents: un lien comme celui ci ['https://aviation-safety.net/database/dblist.php?Year=2020']

- la fonction `toutes_les_pages_par_annee(year)`renvoie comme son nom l'indique une liste des toutes les pages d'accidents par année. En effet certaines années comportent plusieurs pages d'accident comme en 1945 (pendant la seconde Guerre Mondiale) où on a 15 pages d'accidents. (Il y a 100 accidents par page). Il est donc question de récupérer tous les liens et les mettre dans la même liste.

- la fonction `page_par_annee(Li)`


- la fonction `liste_page_par_annee(annee)` renvoie pour une année donnée une liste de tous les urls des accidents.

- la fonction `donnees_par_accident(url)` 

- la fonction `lien_a_enlever()` n'est utile que rarement: quand certaines pages web ne fonctionnent pas pendant le wbscrapping. On enlève donc de la liste les pages d'accidents qui empêchent le fonctionnement de l'algorithme.



- la fonction `fichier_csv(annee)` prend en argument une année. C'est la fonction qui va permettre l'écriture du fichier csv 
On y utilise la fonction `csv.DictWriter`

## script python: web_scrapping_record.py

Ce fichier python sert à récupérer plusieurs fichiers csv par année donnant les informations générales sur les accidents.




### fichier de données record2

Un fichier avec tous les documents csv.
Une ligne contient tout d'abord 
