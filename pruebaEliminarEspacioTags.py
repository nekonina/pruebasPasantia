#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:19:12 2020

@author: ubicutus-010
"""

import pandas as pd
import numpy as np
from time import perf_counter 

datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

country = []
countryOriginal = []

for i in range(5837):
    country.append(datos.country[i])
country_test = [x for x in country if str(x) != 'nan']

t1_start = perf_counter()

for i in range(5410):
    countryOriginal.append(country_test[i].replace(' ', ''))
t1_stop = perf_counter()
print("Elapsed time:", t1_stop-t1_start)
memF = memory_usage_psutil()
print("mem utilizada:", memF)