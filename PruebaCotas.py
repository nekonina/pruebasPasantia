#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:10:29 2020

@author: ubicutus-010
"""

import pandas as pd
import math
from sklearn.cluster import AgglomerativeClustering

data1 = pd.read_csv('70Data0.csv')
data2 = pd.read_csv('70Data1.csv')
data3 = pd.read_csv('70Data2.csv')
data4 = pd.read_csv('70Data3.csv')
data5 = pd.read_csv('70Data4.csv')
data6 = pd.read_csv('70Data5.csv')
data7 = pd.read_csv('70Data6.csv')
data8 = pd.read_csv('70Data7.csv')
data9 = pd.read_csv('70Data8.csv')
data10 = pd.read_csv('70Data9.csv')

data11 = pd.read_csv('200Data.csv')
data12 = pd.read_csv('200Data1.csv')
data13 = pd.read_csv('200Data2.csv')
data14 = pd.read_csv('200Data3.csv')
data15 = pd.read_csv('200Data4.csv')
data16 = pd.read_csv('200Data0.csv')
data17 = pd.read_csv('200Data5.csv')
data18 = pd.read_csv('200Data6.csv')
data19 = pd.read_csv('200Data7.csv')
data20 = pd.read_csv('200Data8.csv')

# lista de datasets con 70 trivias cada una
datos = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10]
topeCentros = round(math.sqrt(data1.shape[0]/2))
n = len(data1)

# lista de datasets con 200 trivias cada una
#topeCentros = round(math.sqrt(data11.shape[0]/2))
#datos  = [data11, data12, data13, data14, data15, data16,data17, data18, data19, data20]
#n = len(data11)

#m = 20      #numero de trivias suscritas
m = n//3
m2 = round(m*0.40)
m3 = round(m*0.65)
nn = n-m

k = 25   #numero total de sugerencias
k2 = round(k*0.40)
k3 = round(k*0.65)

kbig = round(k *0.7)    #proporcion
kmed = round(k *0.25)
ksmall = k - kbig - kmed

#categorizando las trivias en suscritas y pub
dataType = [0 for i in range(m)]    #trivias suscritas
pub = [1 for i in range(nn)]        #trivias publicadas
dataType.extend(pub)


def getIndexCluster(gr, index, topeCentros):
    
    p = len(index)
    big = []
    ind = []
    notin =[]
    for i in range(p):
        if (index[i][1] == 0 ):
            big.append([index[i], gr[index[i]]])
    
    big.sort(key=lambda tup: tup[1], reverse = True)

    for i in range(len(big)):
        temp = big[i][0][0]
        ind.append(temp)
    
    for i in range(topeCentros):
        if (not i in ind):
            notin.append(i)

    return ind, notin

def clustering(data):  
    
    model = AgglomerativeClustering(n_clusters = topeCentros)
    model.fit(data)
#    print(model.labels_)
#    print("The average silhouette_score is :", silhouette_score(data, model.labels_))
    data['label'] =  model.labels_
    
    return data

def getData(j,i, realIndex, cuenta1, kbig, data, sugerencias):
    cluster = cuenta1.groups[(realIndex,1)]
    ite = len(cluster)
    if ((kbig - len(cluster) - j) < 0):
        ite = kbig -j
        
    j = j + ite
    i = i + ite
    
    for q in range(ite):
        inst= cluster.values[q]
        temp = data[inst: inst+1]
        sugerencias = pd.concat([sugerencias, temp])
        
    return sugerencias, i , j

def getImportance(data1Sus, m2, m3):
    
    categorias = data1Sus.columns.tolist()[:-8]

    categ1 = []
    cantidades1 = []
    
    categ2 = []
    cantidades2 = []
    
    categ3 = []
    cantidades3 = []
    
    for i in range(len(categorias)):
        name = categorias[i]
        #print(name)
        pos = data1Sus.groupby([name]).size().index.values.tolist()
        if (1 in pos):
            #contamos las trivias que tengan seteado estge features en true (1)
            cuenta1 = data1Sus.groupby([name]).size()[1]
            if(cuenta1>= m3):
                categ1.append(name)
                cantidades1.append(cuenta1)
            elif(cuenta1>= m2):
                categ2.append(name)
                cantidades2.append(cuenta1)
            else:
                categ3.append(name)
                cantidades3.append(cuenta1)
            
    preferencias1 = pd.DataFrame({'categoria': categ1, 'cantidad': cantidades1}).sort_values('cantidad',ascending=False)
    preferencias2 = pd.DataFrame({'categoria': categ2, 'cantidad': cantidades2}).sort_values('cantidad',ascending=False)
    preferencias3 = pd.DataFrame({'categoria': categ3, 'cantidad': cantidades3}).sort_values('cantidad',ascending=False)
#    print(' ')
    return preferencias1, preferencias2, preferencias3

def getComparacion(sugerencia, suscritos): 
    if len(suscritos) == 0:
        return 0, 0
    elif len(sugerencia) == 0:
        temp = str(0) + '/' + str(len(suscritos))
        return temp, 0
    else: 
        categoriaSug = sugerencia['categoria'].tolist()
        categoriaSus = suscritos['categoria'].tolist()
        count = 0
        for i in range(len(categoriaSug)):
            if (categoriaSug[i] in categoriaSus):
                count += 1
                
        resultado = str(count) + '/' + str(len(categoriaSus))
        porcentaje = (count*100)/ len(categoriaSus)
        
        return resultado, porcentaje

lista = []

## Prueba de proporcion
yesNotIn = []
for i in range(10):
    data = datos[i]
    data['type'] = dataType
    data = clustering(data)
    
    cuenta1 = data.groupby(['label','type'])
    grupos = cuenta1.size()
#    print(grupos, '//n')

    index = grupos.index.values.tolist()
    indexClusters, notin = getIndexCluster(grupos, index,topeCentros)
    
    print(notin)
    sugerencias = pd.DataFrame({})
    i1 = 0
    indexCluster = 0
    indexCluster2 = 0
    indexCluster1 = len(indexClusters) -1
    j = 0
    j1 = 0
    
    if (notin == []):
        yesNotIn.append(i+1)
        ksmall = k - kbig
        #print("Todos los clusters tienen trivias suscritas")
        while (i1 < k):
            if (j < kbig):
                realIndex = indexClusters[indexCluster]
                sugerencias, i1, j = getData( j, i1, realIndex, cuenta1, kbig, data, sugerencias)
                indexCluster += 1
    
            else:
                
                realIndex = indexClusters[indexCluster1]
                sugerencias, i1, j1 = getData( j1, i1, realIndex, cuenta1, ksmall, data, sugerencias)
                indexCluster1 -= 1


        lista.append(sugerencias)
        
    else:
        j2 = 0
        #print("Al menos un clusters sin trivias suscritas")
        while (i1 < k):
            if (j2 < ksmall):
                if(len(notin) < indexCluster2+1):
                    aux = ksmall -j2
                    j2 = ksmall
                    kbig = kbig + aux
                else:
                    realIndex = notin[indexCluster2]
                    sugerencias, i1, j2 = getData( j2, i1, realIndex, cuenta1, ksmall, data, sugerencias)
                    indexCluster2 += 1
#                    print(len(sugerencias), '3')
            elif (j < kbig):
                realIndex = indexClusters[indexCluster]
                sugerencias, i1, j = getData( j, i1, realIndex, cuenta1, kbig, data, sugerencias)
                indexCluster += 1
#                print(len(sugerencias), '1')
                
            elif(j1 < kmed):
                
                realIndex = indexClusters[indexCluster]
                sugerencias, i1, j1 = getData( j1, i1, realIndex, cuenta1, kmed, data, sugerencias)
                indexCluster1 -= 1
#                print(len(sugerencias), '2')
                

        lista.append(sugerencias)
        

data1Sus = datos[0][0:m]

data2Sus = datos[0][0:m]

data3Sus = data3[0:m]

data4Sus = datos[0][0:m]

data5Sus = datos[0][0:m]
        
data6Sus = datos[0][0:m]

data7Sus = datos[0][0:m]

data8Sus = datos[0][0:m]

data9Sus = datos[0][0:m]

data10Sus = datos[0][0:m]
#
importante1Sus, medianamenteImpor1Sus, pocoImpor1Sus = getImportance(data1Sus,m2, m3)
importante2Sus, medianamenteImpor2Sus, pocoImpor2Sus = getImportance(data2Sus,m2, m3)
importante3Sus, medianamenteImpor3Sus, pocoImpor3Sus = getImportance(data3Sus,m2, m3)
importante4Sus, medianamenteImpor4Sus, pocoImpor4Sus = getImportance(data4Sus,m2, m3)
importante5Sus, medianamenteImpor5Sus, pocoImpor5Sus = getImportance(data5Sus,m2, m3)        
importante6Sus, medianamenteImpor6Sus, pocoImpor6Sus = getImportance(data6Sus,m2, m3)
importante7Sus, medianamenteImpor7Sus, pocoImpor7Sus = getImportance(data7Sus,m2, m3)
importante8Sus, medianamenteImpor8Sus, pocoImpor8Sus = getImportance(data8Sus,m2, m3)
importante9Sus, medianamenteImpor9Sus, pocoImpor9Sus = getImportance(data9Sus,m2, m3)
importante10Sus, medianamenteImpor10Sus, pocoImpor10Sus = getImportance(data10Sus,m2, m3)
#
importanteSus = [importante1Sus, importante2Sus, importante3Sus,importante4Sus,importante5Sus,importante6Sus,importante7Sus,importante8Sus,importante9Sus,importante10Sus]
medianamenteImporSus = [medianamenteImpor1Sus, medianamenteImpor2Sus, medianamenteImpor3Sus,medianamenteImpor4Sus,medianamenteImpor5Sus,medianamenteImpor6Sus,medianamenteImpor7Sus,medianamenteImpor8Sus,medianamenteImpor9Sus,medianamenteImpor10Sus]
pocoImporSus = [pocoImpor1Sus, pocoImpor2Sus, pocoImpor3Sus,pocoImpor4Sus,pocoImpor5Sus,pocoImpor6Sus,pocoImpor7Sus,pocoImpor8Sus,pocoImpor9Sus,pocoImpor10Sus]

importante1Sug, medianamenteImpor1Sug, pocoImpor1Sug = getImportance(lista[0], k2,k3)
importante2Sug, medianamenteImpor2Sug, pocoImpor2Sug = getImportance(lista[1], k2,k3)
importante3Sug, medianamenteImpor3Sug, pocoImpor3Sug = getImportance(lista[2], k2,k3)
importante4Sug, medianamenteImpor4Sug, pocoImpor4Sug = getImportance(lista[3], k2,k3)
importante5Sug, medianamenteImpor5Sug, pocoImpor5Sug = getImportance(lista[4], k2,k3)       
importante6Sug, medianamenteImpor6Sug, pocoImpor6Sug = getImportance(lista[5],k2, k3)
importante7Sug, medianamenteImpor7Sug, pocoImpor7Sug = getImportance(lista[6],k2, k3)
importante8Sug, medianamenteImpor8Sug, pocoImpor8Sug = getImportance(lista[7],k2, k3)
importante9Sug, medianamenteImpor9Sug, pocoImpor9Sug = getImportance(lista[8],k2, k3)
importante10Sug, medianamenteImpor10Sug, pocoImpor10Sug = getImportance(lista[9],k2, k3)

importanteSug = [importante1Sug, importante2Sug, importante3Sug,importante4Sug,importante5Sug,importante6Sug,importante7Sug,importante8Sug,importante9Sug,importante10Sug]
medianamenteImporSug = [medianamenteImpor1Sug, medianamenteImpor2Sug, medianamenteImpor3Sug,medianamenteImpor4Sug,medianamenteImpor5Sug,medianamenteImpor6Sug,medianamenteImpor7Sug,medianamenteImpor8Sug,medianamenteImpor9Sug,medianamenteImpor10Sug]
pocoImporSug = [pocoImpor1Sug, pocoImpor2Sug, pocoImpor3Sug,pocoImpor4Sug,pocoImpor5Sug,pocoImpor6Sug,pocoImpor7Sug,pocoImpor8Sug,pocoImpor9Sug,pocoImpor10Sug]

for i in range(10):
    
    resultadoImportante, porcentajeImp = getComparacion(importanteSug[i], importanteSus[i])
    resultadoMedioImportante, porcentajeMedioImp = getComparacion(medianamenteImporSug[i], medianamenteImporSus[i] )
    resultadoPocoImportante, porcentajePocoImp = getComparacion(pocoImporSug[i],pocoImporSus[i])
    print("\n")
    print("cluster ", i+1   )
    print(resultadoImportante, porcentajeImp)
    print(resultadoMedioImportante, porcentajeMedioImp)
    print(resultadoPocoImportante, porcentajePocoImp)


    
###Prueba de cota individual con 200 ejemplos
#n = len(data11)
#m = 31  
#nn = n-m
#
#topeCentros = round(math.sqrt(data11.shape[0]/2))
#datos2  = [data11, data12, data13, data14, data15, data16,data17, data18, data19, data20]

#dataType = [0 for i in range(m)]    #trivias suscritas
#pub = [1 for i in range(nn)]        #trivias publicadas
#dataType.extend(pub)
#
#for i in range(4):
#    data = datos2[i]
#    data['type'] = dataType
#    data = clustering(data)
#    
#    cuenta1 = data.groupby(['label','type'])
#    grupos = cuenta1.size()
#    print(grupos, '//n')

data20 = pd.read_csv('100DataSinPCA.csv')