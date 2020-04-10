#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:35:42 2020

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

def liens_pages_par_annee(annee):
    L = toutes_les_pages_par_annee(annee)
    liste = []
    for i in range(len(L)):
        data = liens_par_annee(L[i])
        liste += data
    return liste



def fichier_csv(annee):
    output_rows = liens_pages_par_annee(annee)
    with open(f'/Users/Nadia/Documents/Maths/DATA_SCIENCES/PROJET_SQL/web_scrapping/record2/data_{annee}.csv', 'w') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(["identifiant","date","type","registration","operator","fat.","location"," ", "pic","cat"])
          writer.writerows(output_rows)


fichier_csv(1900)