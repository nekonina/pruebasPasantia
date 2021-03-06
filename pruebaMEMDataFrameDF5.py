#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:26:25 2020

@author: ubicutus-010
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
count = CountVectorizer()

datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem
#se crean listas con cada dato, y al final se juntan en un solo diccionario, el cual se transforma en el dataFrame

iden = []
title = []
director = []
cast = []
country = []
added = []
release_year = []
rating = []
duration = []
listed_in = []
description = []
tipo = []

for i in range(5837):
    if (str(datos.country[i]) != 'nan' and str(datos.cast[i]) != 'nan' and str(datos.title[i]) != 'nan'):
        iden.append(datos.show_id[i])
        title.append(datos.title[i].replace(' ',''))
        director.append(datos.director[i])
        cast.append(datos.cast[i].replace(' ',''))
        pais = datos.country[i].replace(' ','')
        pais = pais.replace(',',' ')
        country.append(pais)
        added.append(datos.date_added[i])
        release_year.append(datos.release_year[i])
        rating.append(datos.rating[i])
        duration.append(datos.duration[i])
        listed_in.append(datos.listed_in[i])
        description.append(datos.description[i])
        tipo.append(datos.type[i])
        
count = CountVectorizer()
temp = count.fit_transform(country)
final = temp.toarray().tolist()  
df5 = pd.DataFrame({'iden': iden, 'title' : title, 'director':director, 'cast': cast, 'country': final, 'added': added, 'release_year': release_year, 'rating':rating, 'duration': duration, 'listed_in': listed_in, 'description':description, 'tipo': tipo})

memF = memory_usage_psutil()
print("mem final for df5:", memF)