#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:22:57 2020

@author: Nadia
"""


import requests
from bs4 import BeautifulSoup
import re
import time
import numpy as np
import numpy.random 
import csv 



#On va faire une requête HTTP
URL = 'https://aviation-safety.net/database/'




def page_principale(annee):
   return(f'https://aviation-safety.net/database/dblist.php?Year={annee}')


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



def liste_page_par_annee(annee):
    L = toutes_les_pages_par_annee(annee)
    links = []
    
    for i in range(len(L)):      
        l = page_par_annee(L[i])
        links.append(l)
    
    return links    #liste  de liste des pages 




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
            valeur = td[1]     #mettre un re (class )
            dico[cle.text] = valeur.text
            
           
    
    cles = ['Identifiant:','Status:', 'Date:', 'Time:', 'Type:', 'Operator:','Operating for:', 'On behalf of:', 'Leased from:', 'Registration:', 'C/n / msn:', 'Year built:',
              'Engines:', 'Total airframe hrs:', 'First flight:',   'Cycles:', 'Crew:', 'Passengers:', 'Ground casualties:', 
            'Collision casualties:', 'Aircraft damage:',  'Aircraft fate:', 'Location:', 'Phase:', 'Nature:', 'Departure airport:', 
            'Destination airport:', 'Flightnumber:', 'Probable cause:', 'Total:']
        
        
    
    d = { k:v for k,v in dico.items() if k in cles}


    return d

def donnees_par_annee(annee):
    #accidents = lien_a_enlever()
    accidents = liste_page_par_annee(annee)
    donnees = []
    
    delays = [7, 4, 6, 5, 2, 10, 9, 12, 13]
    delay = np.random.choice(delays)
    for i in range(len(accidents)):
        for j in range(len(accidents[i])):
            print(i,j)
            url_ij = accidents[i][j]
            donnee = donnees_par_accident(url_ij)
            donnees.append(donnee)
            if j%39 == 0:
                time.sleep(delay)
    #time.sleep(delay)

    return donnees 


def lien_a_enlever():
    l = liste_page_par_annee(1964)
    del l[1][63]
    return l


def fichier_csv(annee):
    data_annee = donnees_par_annee(annee)
    #data_total = donnees(URL)
     #data_annee = donnees_par_accident('https://aviation-safety.net/database/record.php?id=19941126-1')
    delays = [7, 4, 6, 5, 2, 10, 9, 12, 13]
    delay = np.random.choice(delays)
    
    with open(f'/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/bonnes_donnees2/data_{annee}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Identifiant:', 'Status:', 'Date:', 'Time:', 'Type:', 'Operator:','Operating for:', 'On behalf of:', 'Leased from:', 'Registration:', 'C/n / msn:', 'First flight:', 
            'Total airframe hrs:', 'Year built:',  'Engines:', 'Cycles:', 'Crew:', 'Passengers:', 'Ground casualties:', 
            'Collision casualties:','Aircraft damage:', 'Aircraft fate:', 'Location:', 'Phase:', 'Nature:', 'Departure airport:', 
            'Destination airport:', 'Flightnumber:', 'Probable cause:', 'Total:']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for j in range(len(data_annee)):
            writer.writerow(data_annee[j])
            if j%55 == 0:
                time.sleep(delay)
            else: pass
        
        
        
        
        
        
        
        
#probleme annee 2011   57   , 58 ,59  "AttributeError: 'NoneType' object has no attribute 'findAll'"
   #         probleme annee 1940, 1941 (35, 36, 37), 1942 (32,33,34,35), 2009
        # https://aviation-safety.net/database/record.php?id=19410403-0
        #https://aviation-safety.net/database/record.php?id=19410404-0
        #https://aviation-safety.net/database/record.php?id=19410407    you are the issue !!!!!  il n'y a absolument rien sur cette page 
        
"""     
   1940: derniere page 52 ?
   1941:  https://aviation-safety.net/database/record.php?id=19410407
   1942: 32,33,34,35
   1944
   1970       45 
        
        
        
      """


"""
2012 66 de la premiere ou deuxieme page ?
2010   70 premiere page ?
1969 55 ?
1970    45 parmi premieres pages

1964  [1,63



2000
2002
"""

# try:
#      fichier_csv(2012)
# except AttributeError:
#      pass


"""

https://aviation-safety.net/database/record.php?id=19691206          1969 soucis       0,55    

'https://aviation-safety.net/database/record.php?id=19400409'         1940             0,16      3,55

'https://aviation-safety.net/database/record.php?id=19420208'     1942               1,33

 """      
     
""" 
  File "<ipython-input-25-3de89db07d96>", line 1, in <module>
    fichier_csv(1940)

  File "/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/sanstitre1.py", line 133, in fichier_csv

  File "/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/sanstitre1.py", line 120, in donnees_par_annee

  File "/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/sanstitre1.py", line 93, in donnees_par_accident

AttributeError: 'NoneType' object has no attribute 'findAll'


def lien_a_enlever():
    l = liste_page_par_annee(1944)
    return l


 """