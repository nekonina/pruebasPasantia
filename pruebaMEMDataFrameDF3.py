#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:54:48 2020

@author: ubicutus-010
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

#prueba con una lista de diccionarios convertidas a dataFrame
d = []

paises = []

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

memF = memory_usage_psutil()
print("mem final for df3:", memF)

