#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 16:30:12 2020

@author: ubicutus-010
"""

import pandas as pd
import numpy as np
from time import perf_counter

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    import os
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem


datos = pd.read_csv('netflix_titles_nov_2019.csv')
columns = ['show_id','title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating','duration','listed_in', 'description','type'  ]

country = []

t1_start = perf_counter()
for i in range(5837):
    country.append(datos.country[i])

t1_stop = perf_counter()
print("Elapsed time append:", t1_stop-t1_start)

country1 = []
t1_start = perf_counter()
for i in range(5837):
    country1 = country1 + [datos.country[i]]
    
t1_stop = perf_counter()
print("Elapsed time concatenacion de lista con +: ", t1_stop-t1_start)

country2 = []
t1_start = perf_counter()
for i in range(5837):
    country2.extend([datos.country[i]])
    
t1_stop = perf_counter()
print("Elapsed time concatenacion de lista con un extend: ", t1_stop-t1_start)

country3 = []
t1_start = perf_counter()
for i in range(5837):
    country3.insert(i+1,datos.country[i])
    
t1_stop = perf_counter()
print("Elapsed time insert en la lista: ", t1_stop-t1_start)

memF = memory_usage_psutil()
print("mem final for df3:", memF)