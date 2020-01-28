#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 14:55:15 2020

@author: ubicutus-010
"""

import pandas as pd
from time import perf_counter
from sklearn.feature_extraction.text import CountVectorizer

datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

d = []
paises = []
t1_start = perf_counter()

for i in range(5837):
    if (str(datos.country[i]) != 'nan' and str(datos.cast[i]) != 'nan' and str(datos.title[i]) != 'nan'):
        
        dic = {'iden' : datos.show_id[i],
                'title' : datos.title[i].replace(' ',''),
                'director' : datos.director[i],
                'cast' : datos.cast[i].replace(' ',''),
                'added' :datos.date_added[i],
                'release_year' :datos.release_year[i],
                'rating' : datos.rating[i],
                'duration' : datos.duration[i],
                'listed_in' : datos.listed_in[i],
                'description' : datos.description[i],
                'tipo': datos.type[i],
                }
        
        country = datos.country[i].replace(' ','')
        country = country.replace(',',' ')
        paises.append(country)
        d.append(dic)

count = CountVectorizer()
temp = count.fit_transform(paises)
final = temp.toarray().tolist()

df3 = pd.DataFrame(d)
df3['country'] = final
t1_stop = perf_counter()
print("Elapsed time for df3:", t1_stop-t1_start)

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

t1_start = perf_counter()
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
t1_stop = perf_counter()
print("Elapsed time for df5:", t1_stop-t1_start)