#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:54:48 2020

@author: ubicutus-010
"""

import pandas as pd
from time import perf_counter 

datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

#dataframe vacio y agregando con append
df1 = pd.DataFrame(columns = columns)
t1_start = perf_counter()

for i in range(5837):
    iden = datos.show_id[i]
    title = datos.title[i]
    director = datos.director[i]
    cast = datos.cast[i]
    country = datos.country[i]
    added = datos.date_added[i]
    release_year = datos.release_year[i]
    rating = datos.rating[i]
    duration = datos.duration[i]
    listed_in = datos.listed_in[i]
    description = datos.description[i]
    tipo = datos.type[i]
    
    temporal = pd.DataFrame([[iden,title,director, cast, country, added, release_year, rating ,duration,listed_in,description,tipo]], columns = columns)
    df1 = df1.append(temporal, ignore_index=True)
t1_stop = perf_counter()
print("Elapsed time for df1:", t1_stop-t1_start)

# dataframe vacio y agregando con loc
df2 = pd.DataFrame(columns = columns)
t1_start = perf_counter()

for i in range(5837):
    iden = datos.show_id[i]
    title = datos.title[i]
    director = datos.director[i]
    cast = datos.cast[i]
    country = datos.country[i]
    added = datos.date_added[i]
    release_year = datos.release_year[i]
    rating = datos.rating[i]
    duration = datos.duration[i]
    listed_in = datos.listed_in[i]
    description = datos.description[i]
    tipo = datos.type[i]
    
    df2.loc[i] = [iden,title,director, cast, country, added, release_year, rating ,duration,listed_in,description,tipo]

t1_stop = perf_counter()
print("Elapsed time for df2:", t1_stop-t1_start)

#prueba con una lista de diccionarios convertidas a dataFrame
d = []
t1_start = perf_counter()

for i in range(5837):
    dic = {'iden' : datos.show_id[i],
            'title' : datos.title[i],
            'director' : datos.director[i],
            'cast' : datos.cast[i],
            'country' : datos.country[i],
            'added' :datos.date_added[i],
            'release_year' :datos.release_year[i],
            'rating' : datos.rating[i],
            'duration' : datos.duration[i],
            'listed_in' : datos.listed_in[i],
            'description' : datos.description[i],
            'tipo': datos.type[i],
            }
    d.append(dic)

df3 = pd.DataFrame(d)
t1_stop = perf_counter()
print("Elapsed time for df3:", t1_stop-t1_start)

#se crea un dataframe vacio y se va concatenando con un df temporal
df4 = pd.DataFrame(columns = columns)
t1_start = perf_counter()

for i in range(5837):
    iden = datos.show_id[i]
    title = datos.title[i]
    director = datos.director[i]
    cast = datos.cast[i]
    country = datos.country[i]
    added = datos.date_added[i]
    release_year = datos.release_year[i]
    rating = datos.rating[i]
    duration = datos.duration[i]
    listed_in = datos.listed_in[i]
    description = datos.description[i]
    tipo = datos.type[i]
    
    temporal = pd.DataFrame([[iden,title,director, cast, country, added, release_year, rating ,duration,listed_in,description,tipo]], columns = columns)
    df4 = pd.concat([df4,temporal])
t1_stop = perf_counter()
print("Elapsed time for df4:", t1_stop-t1_start)

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
t1_start = perf_counter() 
  
for i in range(5837):
    iden.append(datos.show_id[i])
    title.append(datos.title[i])
    director.append(datos.director[i])
    cast.append(datos.cast[i])
    country.append(datos.country[i])
    added.append(datos.date_added[i])
    release_year.append(datos.release_year[i])
    rating.append(datos.rating[i])
    duration.append(datos.duration[i])
    listed_in.append(datos.listed_in[i])
    description.append(datos.description[i])
    tipo.append(datos.type[i])
    
df5 = pd.DataFrame({'iden': iden, 'title' : title, 'director':director, 'cast': cast, 'country': country, 'added': added, 'release_year': release_year, 'rating':rating, 'duration': duration, 'listed_in': listed_in, 'description':description, 'tipo': tipo})
t1_stop = perf_counter()
print("Elapsed time for df5:", t1_stop-t1_start)