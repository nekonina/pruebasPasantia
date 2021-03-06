
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
import pandas as pd
from time import perf_counter 
from sklearn.metrics import silhouette_score
import math
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt 
import scipy.cluster.hierarchy as shc 
from sklearn.preprocessing import StandardScaler, normalize

datos1 = pd.read_csv('250TriviasNorSca.csv')
datos2 = pd.read_csv('250TriviasNor.csv')
datos3 = pd.read_csv('250TriviasSca.csv')
datos4 = pd.read_csv('250TriviasScaNor.csv')

#topeCentros = round(math.sqrt(datos1.shape[0]/2))

datos5 = pd.read_csv('250Data1.csv')
datos6 = pd.read_csv('250Data2.csv')
datos7 = pd.read_csv('250Data3.csv')

#datos5 = pd.read_csv('500Data1.csv')
#datos6 = pd.read_csv('500Data2.csv')
#datos7 = pd.read_csv('500Data3.csv')
#
#datos5 = pd.read_csv('1500Data1.csv')
#datos6 = pd.read_csv('1500Data2.csv')
#datos7 = pd.read_csv('1500Data3.csv')
#
#datos5 = pd.read_csv('1000Data1.csv')
#datos6 = pd.read_csv('1000Data2.csv')
#datos7 = pd.read_csv('1000Data3.csv')

topeCentros = round(math.sqrt(datos5.shape[0]/2))


## CORRER LOS CASOS SIN PASAR LA DATA POR EL PCA
#for i in range(5):
#    parameters = {'init':('k-means++', 'random'), 'n_init':list(range(10,16)), 'n_clusters': list(range(2,topeCentros+1)), 'max_iter':list(range(200,600, 50))}
#    kmean = KMeans()
#    estimador = GridSearchCV(kmean, parameters)
#    suscritas = pd.read_csv('250TriviasScaNor.csv')
#    t1_start = perf_counter()
#    
#    estimador.fit(suscritas)
#    
#    t1_stop = perf_counter()
#    print("Elapsed time: ", t1_stop-t1_start)
#    
#    #encontrar el mejor estimador:
#    print(estimador.best_estimator_)
#    
#    print("The average silhouette_score is :", silhouette_score(suscritas, estimador.best_estimator_.labels_))


##CORRER LOS CASOS PASANDOLOS POR EL PCA
#for i in range(5):
#    susc = pd.read_csv('250TriviasNor.csv')
#    parameters = {'init':('k-means++', 'random'), 'n_init':list(range(10,16)), 'n_clusters': list(range(2,topeCentros+1)), 'max_iter':list(range(200,600, 50))}
#    kmean = KMeans()
#    pca = PCA(.9)
#    pca.fit(suscritas)
#    print(pca.get_precision)
#    susc = pca.transform(suscritas)
#    susc = pd.DataFrame(susc)
#    
#    estimador = GridSearchCV(kmean, parameters)
#    
#    t1_start = perf_counter()
#    
#    estimador.fit(susc)
#    
#    t1_stop = perf_counter()
#    print("Elapsed time: ", t1_stop-t1_start)
#    
#    #encontrar el mejor estimador:
#    print(estimador.best_estimator_)
#    
##    susc.columns = ['P1', 'P2']
##    plt.figure(figsize =(6, 6))
##    plt.title('k = 10') 
##    plt.scatter(susc['P1'], susc['P2'],  
##               c = estimador.best_estimator_.predict(susc), cmap ='rainbow') 
##    plt.show()
#
#    print("The average silhouette_score is :", silhouette_score(susc, estimador.best_estimator_.labels_))
#



###PROBANDO EL CLUSTER JERARQUICO
##    parameters1 = {'n_clusters': [topeCentros], 'affinity':('euclidean', 'l1', 'l2')}
#for i in range (2,topeCentros+1):
#    for j in range(3):
#        model = AgglomerativeClustering(n_clusters = i)
##        pca = PCA(.9) 
##        suscritas = pca.fit_transform(suscritas) 
##        suscritas = pd.DataFrame(suscritas) 
##        
#        #suscritas.columns = ['P1', 'P2']     
#        #plt.figure(figsize =(8, 8)) 
#        #plt.title('Visualising the data') 
#        #Dendrogram = shc.dendrogram((shc.linkage(suscritas, method ='ward'))) 
#        
#        
#        t1_start = perf_counter()
#        model.fit(datos3)
#        
#        t1_stop = perf_counter()
#        print("Elapsed time: ", t1_stop-t1_start)
#        
#    #    plt.figure(figsize =(6, 6))
#    #    title = 'k = ' + str(i)
#    #    plt.title(title) 
#    #    plt.scatter(suscritas['P1'], suscritas['P2'],  
#    #               c = model.fit_predict(suscritas), cmap ='rainbow') 
#    #    plt.show()
#        
#        #encontrar el mejor estimador:
#        print(model.get_params())
#        print("The average silhouette_score is :", silhouette_score(datos3, model.labels_), 'for i = ', i)


def clustering(data):  
    pca = PCA(.9) 
    data = pca.fit_transform(data) 
    data= pd.DataFrame(data) 
    for i in range(3):
        model = AgglomerativeClustering(n_clusters = topeCentros)
        
        t1_start = perf_counter()
        model.fit(data)
        
        t1_stop = perf_counter()
        print("Elapsed time: ", t1_stop-t1_start)
#        #encontrar el mejor estimador:
#        print(model.get_params())
        
    print("The average silhouette_score is :", silhouette_score(data, model.labels_))



## 3 dataset escalados para el agglomerative
#scaler = StandardScaler() 
#susc = scaler.fit_transform(datos5)
#suscritas = pd.DataFrame(susc)
#
#scaler = StandardScaler() 
#susc1 = scaler.fit_transform(datos6)
#suscritas1 = pd.DataFrame(susc1)
#
#scaler = StandardScaler() 
#susc2 = scaler.fit_transform(datos7)
#suscritas2 = pd.DataFrame(susc2)
#
#resultados1 = clustering(suscritas)
#resultados2 = clustering(suscritas1)
#resultados3 = clustering(suscritas2)


##Data normalizada para el agglomerative
#susc = normalize(datos5)
#suscritas = pd.DataFrame(susc)
#
#susc1 = normalize(datos6)
#suscritas1 = pd.DataFrame(susc1)
#
#susc2 = normalize(datos7)
#suscritas2 = pd.DataFrame(susc2)
#
#resultados1 = clustering(suscritas)
#resultados2 = clustering(suscritas1)
#resultados3 = clustering(suscritas2)
    

##Data normalizada y escalada para el agglomerative
#susc = normalize(datos5)
#scaler = StandardScaler() 
#susc = scaler.fit_transform(susc)
#suscritas = pd.DataFrame(susc)
#
#susc1 = normalize(datos6)
#scaler = StandardScaler() 
#susc1 = scaler.fit_transform(susc1)
#suscritas1 = pd.DataFrame(susc1)
#
#susc2 = normalize(datos7)
#scaler = StandardScaler() 
#susc2 = scaler.fit_transform(susc2)
#suscritas2 = pd.DataFrame(susc2)
#
#resultados1 = clustering(suscritas)
#resultados2 = clustering(suscritas1)
#resultados3 = clustering(suscritas2)
        
#        
        
##Data escalada y normalizada para el agglomerative
#
#scaler = StandardScaler() 
#susc = scaler.fit_transform(datos5)
#susc = normalize(susc)
#suscritas = pd.DataFrame(susc)
#
#
#scaler = StandardScaler() 
#susc1 = scaler.fit_transform(datos6)
#susc1 = normalize(susc1)
#suscritas1 = pd.DataFrame(susc1)
#
#
#scaler = StandardScaler() 
#susc2 = scaler.fit_transform(datos7)
#susc2 = normalize(susc2)
#suscritas2 = pd.DataFrame(susc2)
#
#resultados1 = clustering(suscritas)
#resultados2 = clustering(suscritas1)
#resultados3 = clustering(suscritas2)
#
