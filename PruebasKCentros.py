
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

suscritas = pd.read_csv('250TriviasNorSca.csv')
suscritas1 = pd.read_csv('250TriviasScalada.csv')
suscritas2 = pd.read_csv('250TriviasNor.csv')
topeCentros = round(math.sqrt(suscritas.shape[0]/2))
parameters = {'init':('k-means++', 'random'), 'n_init':list(range(10,16)), 'n_clusters': list(range(2,topeCentros+1)), 'max_iter':list(range(200,600, 50))}
kmean = KMeans()


# CORRER LOS CASOS SIN PASAR LA DATA POR EL PCA
for i in range(5):
    estimador = GridSearchCV(kmean, parameters)
    suscritas = pd.read_csv('250TriviasNorSca.csv')
    t1_start = perf_counter()
    
    estimador.fit(suscritas)
    
    t1_stop = perf_counter()
    print("Elapsed time: ", t1_stop-t1_start)
    
    #encontrar el mejor estimador:
    print(estimador.best_estimator_)
    
    print("The average silhouette_score is :", silhouette_score(suscritas, estimador.best_estimator_.labels_))
    

#CORRER LOS CASOS PASANDOLOS POR EL PCA
for i in range(5):
    suscritas = pd.read_csv('250TriviasNorSca.csv')
    pca = PCA(.9)
    pca.fit(suscritas)
    susc = pca.transform(suscritas)
    susc = pd.DataFrame(susc)
    susc.columns = ['P1', 'P2'] 
    
    estimador = GridSearchCV(kmean, parameters)
    
    t1_start = perf_counter()
    
    estimador.fit(susc)
    
    t1_stop = perf_counter()
    print("Elapsed time: ", t1_stop-t1_start)
    
    #encontrar el mejor estimador:
    print(estimador.best_estimator_)
    
    #plt.figure(figsize =(6, 6))
    #plt.title('k = 10') 
    #plt.scatter(susc['P1'], susc['P2'],  
    #           c = estimador.best_estimator_.predict(susc), cmap ='rainbow') 
    #plt.show()
    
    print("The average silhouette_score is :", silhouette_score(susc, estimador.best_estimator_.labels_))




##PROBANDO EL CLUSTER JERARQUICO

#parameters1 = {'n_clusters': [topeCentros], 'affinity':('euclidean', 'l1', 'l2')}
#for i in range (2,topeCentros+1):
#    
#    model = AgglomerativeClustering(n_clusters = i)
#    
#    pca = PCA(n_components = 2) 
#    suscritas = pca.fit_transform(suscritas) 
#    suscritas = pd.DataFrame(suscritas) 
#    suscritas.columns = ['P1', 'P2'] 
#    
#    
#    #plt.figure(figsize =(8, 8)) 
#    #plt.title('Visualising the data') 
#    #Dendrogram = shc.dendrogram((shc.linkage(suscritas, method ='ward'))) 
#    
#    
#    t1_start = perf_counter()
#    model.fit(suscritas)
#    
#    t1_stop = perf_counter()
#    print("Elapsed time: ", t1_stop-t1_start)
#    
#    plt.figure(figsize =(6, 6))
#    title = 'k = ' + str(i)
#    plt.title(title) 
#    plt.scatter(suscritas['P1'], suscritas['P2'],  
#               c = model.fit_predict(suscritas), cmap ='rainbow') 
#    plt.show()
#    
#    #encontrar el mejor estimador:
#    print(model.get_params())
#    
#    print("The average silhouette_score is :", silhouette_score(suscritas, model.labels_), 'for i = ', i)
#
