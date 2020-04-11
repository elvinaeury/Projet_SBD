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

Cette fonction renvoie juste le lien de la premiere page d'accidents: un lien comme [celui ci](https://aviation-safety.net/database/dblist.php?Year=2020)

#### La fonction `toutes_les_pages_par_annee(year)`

```python
def toutes_les_pages_par_annee(year):
    url = page_principale(year)
    reponse = requests.get(url,headers={'User-Agent': 'Wget/1.20.3 (linux-gnu)'})
    annee = [url]   
    
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'lxml')
        spans = soup.findAll('div', {'class':'pagenumbers'}) 
        
        for span in spans:
            les_as = span.findAll('a')
            
            for a in les_as:
                link = a['href']
                annee.append('https://aviation-safety.net/database/dblist.php' + str(link))
    annee = list(set(annee))
    return annee
    
 ```


Cette fonction renvoie comme son nom l'indique une liste des toutes les pages d'accidents par année. En effet certaines années comportent plusieurs pages d'accident comme en 1945 (pendant la seconde Guerre Mondiale) où on a 15 pages d'accidents. (Il y a 100 accidents par page). Il est donc question de récupérer tous les liens et les mettre dans la même liste.

#### La fonction `page_par_annee(Li)`

Cette fonction prend en argument un lien (provenant de la fonction `toutes_les_pages_par_annee`) donc un lien d'une page où plusieurs accidents sont référencés. Et cette fonction va récuperer tous les urls envoyant à chaque page d'accident

```python

def page_par_annee(Li):
    reponse = requests.get(Li,headers={'User-Agent': 'Wget/1.20.3 (linux-gnu)'})
    links = []
    
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'lxml') 
        trs = soup.findAll('tr')
        
        for tr in trs:
            a = tr.find('a')
            link = a['href']
            links.append('https://aviation-safety.net'+ str(link))

           
    motif = re.compile('(.*record.php.*)')
    L = []
    
    for link in links:
        if len(motif.findall(str(link))) != 0:
            L.append(motif.findall(str(link))[0])
        else: pass
    
    return L
 ```


#### La fonction `liste_page_par_annee(annee)` 

Cette fonction renvoie pour une année donnée une liste de tous les urls des accidents. Elle récupère les urls donnés par la fonction `page_par_année`.

```python
def liste_page_par_annee(annee):
    L = toutes_les_pages_par_annee(annee)
    links = []
    
    for i in range(len(L)):      
        l = page_par_annee(L[i])
        links.append(l)
    
    return links  
 ```

**Par exemple** : L'année 1945 contient 15 pages d'accidents. On récupère le lien de la première page par la fonction `page_principale(annee)`. A partir de ce lien la fonction `toutes_les_pages_par_annee(year)` va récupérer les liens des 14 autres pages d'accidents pour les mettre dans la même liste. Pour chaque page d'accidents, la fonction `page_par_annee(Li)` va récupérer tous les urls renvoyant à chaque accident individuellement.
Enfin la fonction `liste_page_par_annee(annee)`rassemble tous ces liens. 


#### La fonction `donnees_par_accident(url)` 

C'est la fonction qui va récupérer nos données. 
Voici un extrait d'un exemple de page html, pour mieux comprendre la structure:
```html
<tr>
    <td class="caption">Date:</td>
    <td class="caption">Sunday 9 February 2020</td>
</tr>
<tr>
    <td class="caption">Time:</td><td class="desc">12:20</td></tr> 
<tr>
    <td class="caption" valign="bottom">Type:</td>
    <td class="desc"><img src="//cdn.aviation-safety.net/graphics/ICAOtype/B735.gif" width="200" alt="Silhouette image of generic B735 model" title="Silhouette image of generic B735 model" /><br />
        <a href="/database/types/Boeing-737-500/index">Boeing 737-524 (WL)</a>
    </td>
</tr>
<tr>
    <td class="caption">Operator:</td>
    <td class="desc">
        <a href="/database/operator/airline.php?var=12263">Utair</a>
    </td>
</tr>
```


On a choisi de donner une structure de dictionnaire pour plusieurs raisons: 
- C'est ce qui se prêtait le mieux à la page html qui nous était fournie. 
- On peut prendre les différentes clés qui nous intéressent 
- les mêmes clés n'étaient pas toujours référencées dans les pages et pas toujours dans le même ordre, il était donc difficile de songer à utiliser des listes

```python
def donnees_par_accident(url):
    dico = {}
    reponse = requests.get(url,headers={'User-Agent': 'Wget/1.20.3 (linux-gnu)'})
     
    if reponse.ok:
        
        soup = BeautifulSoup(reponse.text, 'lxml')
        table = soup.find('table')
        trs = table.findAll('tr')
        motif = re.compile('\d+.*')     
        identifiant = motif.findall(url)
        dico['Identifiant:'] = identifiant[0]
    
        for tr in trs:
            td = tr.findAll('td')
            cle = td[0]
            valeur = td[1]     
            dico[cle.text] = valeur.text
            
    cles = ['Identifiant:','Status:', 'Date:', 'Time:', 'Type:', 'Operator:','Operating for:', 'On behalf of:', 'Leased from:', 'Registration:', 'C/n / msn:', 'Year built:',
              'Engines:', 'Total airframe hrs:', 'First flight:',   'Cycles:', 'Crew:', 'Passengers:', 'Ground casualties:', 
            'Collision casualties:', 'Aircraft damage:',  'Aircraft fate:', 'Location:', 'Phase:', 'Nature:', 'Departure airport:', 
            'Destination airport:', 'Flightnumber:', 'Probable cause:', 'Total:']       
    
    d = { k:v for k,v in dico.items() if k in cles}

    return d
```

#### la fonction `lien_a_enlever()` 

Cette fonction n'est utile que rarement: quand certaines pages web ne fonctionnent pas pendant le webscraping. On enlève donc de la liste les pages d'accidents qui empêchent le fonctionnement de l'algorithme.


#### La fonction `fichier_csv(annee)`

Cette fonction prend en argument une année. C'est la fonction qui va permettre l'écriture du fichier csv 
On y utilise la fonction `csv.DictWriter`

## script python: web_scrapping_record.py

Ce fichier python sert à récupérer plusieurs fichiers csv par année donnant les informations générales sur les accidents.


#### les fonctions `page_princpale(annee)` et `toutes_les_pages_par_annee(year)` ne changent pas du précédent script

#### la fonction `liens_par_annee` 
Renvoie  une liste de listes des données générales des accidents. En effet ici la structure de liste s'y prête bien car la structure des données est toujours la même pour chaque année et accident. On a les mêmes clés dans le même ordre à chaque fois. Par conséquent la procédure sera  beaucoup plus rapide. 

```python
def liens_par_annee(Li):
    reponse = requests.get(Li,headers={'User-Agent': 'Wget/1.20.3 (linux-gnu)'})
    soup = BeautifulSoup(reponse.text, 'lxml')
    table = soup.find("table")
    output_rows = []
    
    for table_row in table.findAll('tr'):
        a = table_row.find('a')
        link = a['href']
        columns = table_row.findAll('td')
        motif = re.compile('\d+.*')     
        identifiant = motif.findall(link)
        output_row = []
        try:
            output_row.append(identifiant[0])
        except IndexError:
            pass
        
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
        
    return output_rows

```

#### la fonction `fichier_csv`
permet l'écriture des fichiers csv par année, ici c'est beaucoup plus simple et rapide que précedemment notamment car l'utilisation des listes est plus rapide à écrire

```python
def fichier_csv(annee):
    output_rows = liens_pages_par_annee(annee)
    with open(f'/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/record2/data_{annee}.csv', 'w') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(["identifiant","date","type","registration","operator","fat.","location"," ", "pic","cat"])
          writer.writerows(output_rows)
```

### fichier de données record2

Un fichier avec tous les documents csv.
Une ligne contient tout d'abord 

## Difficultés rencontrées

Nous avons rencontré plusieurs difficultés 
