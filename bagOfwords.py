#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:05:35 2020

@author: ubicutus-010
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
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

def bagOfWords(listWord):
    count = CountVectorizer()
    temp = count.fit_transform(listWord)
    final = temp.toarray().tolist()
    return final
    
country = []
countryOriginal = []

for i in range(5837):
    country.append(datos.country[i])
country_test = [x for x in country if str(x) != 'nan']

for i in range(5410):
    countryOriginal.append(country_test[i].replace(' ', ''))
    
t1_start = perf_counter()

countryF = bagOfWords(countryOriginal)
   
t1_stop = perf_counter()

print("Elapsed time:", t1_stop-t1_start)
memF = memory_usage_psutil()
print("mem utilizada:", memF)