#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 16:48:34 2020

@author: ubicutus-010
"""
from random import randint
import pandas as pd
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

categorias = ['Deporte', 'cineYTelevision','series','Musica','CulturaGeneral','Infantil','juvenil','culinario','vidaNocturna','personalidades']
segmentos = ['hombres', 'mujeres', 'ninos', 'jovenes', 'adultosJovenes','adultos','mayores', 'publicoGeneral']
actividades = ['maquillarse','hobby','cocinar','leer', 'bailar', 'verPeliculas', 'deporte', 'verSeries', 'salir', 'oirMusica', 'salirConAmigos', 'yoga', 'salirDeCompras', 'tiempoEnFamilia']
palabras = ['disney', 'hbo','netflix', 'musicaUrbana', 'rock', 'futbol','oscar','masterChef', 'hobby', 'nickelodion', 'baseball','marvel','DC']
marcas = ['valmy','disney', 'polar', 'adidas', 'cinex', 'netflix', 'puma','nike','h/m','balu', 'hp', 'victorMoreno', 'avilaburguer', 'laMega', 'contigo', 'paramo', 'nestle']
premios = ["Bicicleta", "TortadeCumpleaños","Licuadora","Libro","Cámara","Caramelo","Carro","Gato","Reloj","Bebida","Disco","Timbre","Galleta","Monitor","Perro","Moneda","Pesas","Balón","Regalos","Copas", "Guitarra", "Hamburguesa", "Audífonos", "Casa", "Helado", "Laptop", "Teléfono", "Monumento", "Porcentaje", "Pizza", "Avión","Ruta", "Spa", "Spotify", "Spray", "Piscina",  "Tablet", "Máscara", "Ticket", "Camión", "Camisa", "Sombrilla"]
maxCompetitors = [50,100,150,200,250]
nPrizes = [1,2,3,4,5]
questionType = [1,2,3]
questionQuantity = [1,2,3,4,5,6,7,8,9,10]
choiceQuantity = [1,2,3,4]
rightChoicesQuantity = [1,2,3,4]
nwWinner = [1,2,3,4,5,6,7,8,9,10]
vistglobal = [1,2,5,10,15,20,25,30,35,40]

n = 100

def bagOfWords(listWord):
    count = CountVectorizer()
    temp = count.fit_transform(listWord)
    #final = temp.toarray().tolist()
    
    feature_names = count.get_feature_names()
    final = pd.DataFrame(temp.toarray(), columns=feature_names)
    #final = getColums(final, final.shape[0])
    
    return final 
    
def getAttr(lista, limite = 5):
    lenlista = len(lista)
    if limite != 1 :
        nelementos = randint(1,limite)
        nuevo = ''
        if (lenlista < nelementos ):
            nelementos = lenlista - 1
        i = 0
        while (i<nelementos):
            index = randint(0,lenlista-1)
            if not nuevo  or not(lista[index] in nuevo):
                nuevo = nuevo +' '+ lista[index]
                i+=1
    else:
        index = randint(0,lenlista-1)
        nuevo = lista[index]
    return nuevo

def getPremios(premios, ganadores):
    i = 0
    nuevo = []
    while (i<ganadores):
        index = randint(0,len(premios)-1)
        if premios[index] not in nuevo:
            nuevo.append(premios[index])
        i+=1
    
    prize = ' '.join(nuevo)
    
    return prize
    
def getPorcentaje(valor):
    nmax = valor
    npersonas = randint(0,8)
    #npersonas = randint(1,nmax)
    return npersonas / nmax, npersonas

def getColums(df, nfilas):
    nombres = list(df)
    minimo = nfilas * 0.3
    print('el minimo es:', minimo)
    eliminar = []
    for i in nombres:
        n = df[i].sum()
        print('para: ',i,'tiene: ', n)
        if n <= minimo:
            eliminar.append(i)
    df = df.drop(eliminar, axis= 1)
    
    return df

def get(n):
    triviasCategoria = []
    triviasSegmentos = []
    triviasActividades = []
    triviasPalabras = []
    triviasMarcas = []
    triviaMaxComp = []
    trivianPrizes = []
    triviaQuestionType = []
    triviaQuestionQuantity = []
    triviaChoiceQuantity = []
    triviaRightChoicesQuantity = []
    triviaNwWinner = []
    triviasPremios = []
    triviaPorcentaje = []
    triviaSuscritos = []
    triviasDesuscritos = []
    valor =[]
    countViewInfo = []
    nviewInfo = []
    
    for i in range(n):
        triviaMaxCompT = getAttr(maxCompetitors,1)
        triviaChoiceQuantityT = getAttr(choiceQuantity,1)
        triviaRightChoicesQuantityT = randint(1,triviaChoiceQuantityT)
        triviaNwWinnerT = getAttr(nwWinner,1)
        triviaPorcentajeT, triviasuscritosT = getPorcentaje(triviaMaxCompT)
        triviasDesuscritosT = randint(0,6)
        #desuscritos = round(triviaMaxCompT * 0.2)
        #triviasDesuscritosT = randint(0,desuscritos)
        triviaValor = randint(-2,4)
        if triviaValor == 0:
            vistasGlobales = 0
            nviewInfo.append(0)
        else:
            vistasGlobales = getAttr(vistglobal,1)
            limvistasUsuario = round(vistasGlobales * 0.5)
            if limvistasUsuario < 2:
                vistasUsuarios = 1
            else:
                vistasUsuarios =  randint(1,limvistasUsuario)
            nviewInfo.append(vistasUsuarios)
        
        
        triviasCategoria.append(getAttr(categorias))
        triviasSegmentos.append(getAttr(segmentos,3))
        triviasActividades.append(getAttr(actividades))
        triviasPalabras.append(getAttr(palabras))
        triviasMarcas.append(getAttr(marcas))
        triviaMaxComp.append(triviaMaxCompT)
        trivianPrizes.append(getAttr(nPrizes,1))
        triviaQuestionType.append(getAttr(questionType,1))
        triviaQuestionQuantity.append( getAttr(questionQuantity,1))
        triviaChoiceQuantity.append(triviaChoiceQuantityT)
        triviaRightChoicesQuantity.append(triviaRightChoicesQuantityT)
        triviaNwWinner.append(triviaNwWinnerT)
        triviasPremios.append(getPremios(premios, triviaNwWinnerT))
        triviaPorcentaje.append(triviaPorcentajeT)
        triviaSuscritos.append(triviasuscritosT)
        triviasDesuscritos.append(triviasDesuscritosT)
        valor.append(triviaValor)
        countViewInfo.append(vistasGlobales)
    
    ############# BORRAR ########################
    dataSinProcesar = {
            'triviaMaxComp' : triviaMaxComp,
            'trivianPrizes' : trivianPrizes,
            'triviaQuestionType' : triviaQuestionType,
            'triviaQuestionQuantity' : triviaQuestionQuantity,
            'triviaChoiceQuantity' : triviaChoiceQuantity,
            'triviaRightChoicesQuantity' : triviaRightChoicesQuantity,
            'triviaNwWinner' : triviaNwWinner,
            'triviaPorcentaje' : triviaPorcentaje,
            'triviaSuscritos' : triviaSuscritos,
            'triviasDesuscritos' : triviasDesuscritos,
            'valorUser': valor,
            'countViewInfoUser': countViewInfo,
            'nviewInfo' : nviewInfo,
            }
    trivias = {
            'segmentos': triviasSegmentos,
            'actividades': triviasActividades,
            'categorias': triviasCategoria,
            'palabras': triviasPalabras,
            'marcas': triviasMarcas,
            'premios':  triviasPremios
            }
    trivias = pd.DataFrame(trivias)
    dataSinProcesar = pd.DataFrame(dataSinProcesar)
    triviasSinProcesar = pd.concat([trivias, dataSinProcesar], axis=1,)
    
    return triviasSinProcesar
        
   ############# BORRAR ########################
   
    triviasCategoria = bagOfWords(triviasCategoria) 
    triviasSegmentos = bagOfWords(triviasSegmentos) 
    triviasActividades = bagOfWords(triviasActividades) 
    triviasPalabras = bagOfWords(triviasPalabras) 
    triviasMarcas = bagOfWords(triviasMarcas)
    triviasPremios = bagOfWords(triviasPremios)
    
    trivias = pd.concat([triviasCategoria, triviasSegmentos], axis=1,)
    trivias = pd.concat([trivias, triviasActividades], axis=1,)
    trivias = pd.concat([trivias, triviasPalabras], axis=1,)
    trivias = pd.concat([trivias, triviasMarcas], axis=1,)
    trivias = pd.concat([trivias, triviasPremios], axis=1,)
    
    #CON NORMALIZACION
#    
    prePro = [triviaMaxComp, trivianPrizes, triviaQuestionType, triviaQuestionQuantity,triviaChoiceQuantity,triviaRightChoicesQuantity, triviaNwWinner, triviaSuscritos, triviasDesuscritos,valor, countViewInfo, nviewInfo]
    prePro = preprocessing.normalize(prePro, norm= 'l2').tolist()
    triviaMaxComp= prePro[0]
    trivianPrizes= prePro[1]
    triviaQuestionType= prePro[2]
    triviaQuestionQuantity= prePro[3]
    triviaChoiceQuantity= prePro[4]
    triviaRightChoicesQuantity= prePro[5]
    triviaNwWinner= prePro[6]
    triviaSuscritos= prePro[7]
    triviasDesuscritos= prePro[8]
    valor= prePro[9]
    countViewInfo= prePro[10]
    nviewInfo = prePro[11]
#    
    dataOriginal = {
            'triviaMaxComp' : triviaMaxComp,
            'trivianPrizes' : trivianPrizes,
            'triviaQuestionType' : triviaQuestionType,
            'triviaQuestionQuantity' : triviaQuestionQuantity,
            'triviaChoiceQuantity' : triviaChoiceQuantity,
            'triviaRightChoicesQuantity' : triviaRightChoicesQuantity,
            'triviaNwWinner' : triviaNwWinner,
            'triviaPorcentaje' : triviaPorcentaje,
            'triviaSuscritos' : triviaSuscritos,
            'triviasDesuscritos' : triviasDesuscritos,
            'valorUser': valor,
            'countViewInfoUser': countViewInfo,
            'nviewInfo' : nviewInfo,
            }
    
    
    dataNumerica = pd.DataFrame(dataOriginal)
    
#    #CON SCALADO
#    prePro = StandardScaler().fit_transform(dataNumerica)
#    columns = ['triviaMaxComp',
#            'trivianPrizes' ,
#            'triviaQuestionType' ,
#            'triviaQuestionQuantity' ,
#            'triviaChoiceQuantity' ,
#            'triviaRightChoicesQuantity',
#            'triviaNwWinner',
#            'triviaPorcentaje' ,
#            'triviaSuscritos',
#            'triviasDesuscritos' ,
#            'valorUser',
#            'countViewInfoUser',
#            'nviewInfo']
#    
##    prePro = preprocessing.normalize(prePro)
#    
#    dataNumerica = pd.DataFrame(prePro,columns = columns)
    
    #CON PCA(.9)
    pca = PCA(.9)
    pca.fit(dataNumerica)
    susc = pca.transform(dataNumerica)
    
    dataNumerica = pd.DataFrame(susc)
    
    trivias = pd.concat([trivias, dataNumerica], axis=1,)
    return trivias

## Guarda datos en CSV:
#name = str(n) + 'TriviasNorSca.csv'
#trivias = get(n)
#trivias.to_csv(name, index=False)
#
#name = str(n) + 'TriviasNor.csv'
#trivias = get(n)
#trivias.to_csv(name, index=False)
#
#name1 = str(n) + 'TriviasSca.csv'
#trivias1 = get(n)
#trivias1.to_csv(name1, index=False)

#name1 = str(n) + 'TriviasScaNor.csv'
#trivias1 = get(n)
#trivias1.to_csv(name1, index=False)
    
#name1 = str(n) + 'Data1.csv'
#trivias1 = get(n)
#trivias1.to_csv(name1, index=False)
#
#name1 = str(n) + 'Data2.csv'
#trivias1 = get(n)
#trivias1.to_csv(name1, index=False)
#
#name1 = str(n) + 'Data3.csv'
#trivias1 = get(n)
#trivias1.to_csv(name1, index=False)

#for i in range(5):
#    name1 = str(n)+ 'Data'+str(i+5) + '.csv'
#    trivias1 = get(n)
#    trivias1.to_csv(name1, index=False)
    
#for i in range(4):
#    name1 = str(n)+ 'Data'+str(i+5) + '.csv'
#    trivias1 = get(n)
#    trivias1.to_csv(name1, index=False)
    
#name1 = str(n)+ 'DataSinPCA.csv'
trivias1 = get(n)
#trivias1.to_csv(name1, index=False)