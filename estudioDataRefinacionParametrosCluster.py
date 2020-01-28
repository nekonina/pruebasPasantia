#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:47:13 2020

@author: ubicutus-010
"""
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
import pandas as pd

triviasSuscritas_p1 = pd.read_csv('500Trivias.csv')
triviasSuscritas_p2 = pd.read_csv('500Trivias_1.csv')
triviasSuscritas_p3 = pd.read_csv('500Trivias_2.csv')
triviasSuscritas_p4 = pd.read_csv('500Trivias_3.csv')

triviasPub_1 = pd.read_csv('1000Trivias.csv')
triviasPub_2 = pd.read_csv('1000Trivias_1.csv')
triviasPub_3 = pd.read_csv('2000Trivias.csv')
triviasPub_4 = pd.read_csv('2000Trivias_1.csv')
triviasPub_5 = pd.read_csv('3000Trivias.csv')
triviasPub_6 = pd.read_csv('3000Trivias_1.csv')
triviasPub_7 = pd.read_csv('5000Trivias.csv')
triviasPub_8 = pd.read_csv('5000Trivias_1.csv')

parameters1 = {'init':('k-means++', 'random'), 'n_init':list(range(10,21)), 'n_clusters': list(range(3,11)), 'max_iter':list(range(200,1100, 100))}
kmean = KMeans()
estimador = GridSearchCV(kmean, parameters1)
estimador.fit(triviasPub_1)
#estimador.fit(triviasPub_2)
#estimador.fit(triviasPub_3)
#estimador.fit(triviasPub_4)
#estimador.fit(triviasPub_5)
#estimador.fit(triviasPub_6)
#estimador.fit(triviasPub_7)
#estimador.fit(triviasPub_8)

#encontrar el mejor estimador:
print(estimador.best_estimator_)

#obtener los centros de los mejores estimadores:
print(estimador.best_estimator_.cluster_centers_)

