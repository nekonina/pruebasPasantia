from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
import pandas as pd
from time import perf_counter 
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import homogeneity_score, completeness_score
import math

suscritas = pd.read_csv('250TriviasAlm.csv')
suscritas1 = pd.read_csv('250TriviasAlmScalada.csv')
topeCentros = round(math.sqrt(suscritas.shape[0]/2))
parameters1 = {'init':('k-means++', 'random'), 'n_init':list(range(10,16)), 'n_clusters': list(range(3,topeCentros)), 'max_iter':list(range(200,600, 50))}
kmean = KMeans()

estimador = GridSearchCV(kmean, parameters1)

t1_start = perf_counter()

estimador.fit(suscritas1)

t1_stop = perf_counter()
print("Elapsed time: ", t1_stop-t1_start)

#encontrar el mejor estimador:
print(estimador.best_estimator_)

print("The average silhouette_score is :", silhouette_score(suscritas1, estimador.best_estimator_.labels_))

#con los centros del mejor estimador, 
#predecir a que centro pertenece c/instancia y devolverlo como un dataframe


#cluster_labels = estimador.best_estimator_.predict(predic).tolist()



#obtener los centros de los mejores estimadores:
#print(estimador.best_estimator_.cluster_centers_)


#
##metodo1 para extracion del centro con mayor cantidad de instancias
#t1_start = perf_counter()
#
#cuenta = df['in'].value_counts()
#valorMasGrande = max(df['in'].value_counts())
#elegido = cuenta[cuenta == max(cuenta)].index[0]
#
#t1_stop = perf_counter()
#print("Elapsed time with series:", t1_stop-t1_start)
#
#
# #metodo2 para extracion del centro con mayor cantidad de instancias
#t1_start = perf_counter()
#   
#cuenta1 = df.groupby('in')
#valorMasGrande = df.groupby('in').size().max()
#elegido1 = cuenta1.size()[cuenta1.size() == valorMasGrande].index[0]
#
#t1_stop = perf_counter()
#print("Elapsed time with DF:", t1_stop-t1_start)
#
#
##METODO 1 PARA ACCESAR A LOS ELEMENTOS DE UN DETERMINADO CENTRO
#t1_start = perf_counter()
#for i in range(valorMasGrande):
#    instancia = cuenta1.groups[elegido1][i]
#    print(iris.data[instancia])
#    
#t1_stop = perf_counter()
#print("Elapsed time acceso METODO 1:", t1_stop-t1_start)


#METODO 2 PARA ACCESAR A LOS ELEMENTOS DE UN DETERMINADO CENTRO
