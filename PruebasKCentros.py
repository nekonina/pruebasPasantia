from sklearn import svm, datasets
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
import pandas as pd
from time import perf_counter 
from sklearn.metrics import silhouette_score
from sklearn.metrics.cluster import homogeneity_score, completeness_score
import math
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

suscritas = pd.read_csv('250TriviasAlm.csv')
suscritas1 = pd.read_csv('250TriviasAlmScalada.csv')
topeCentros = round(math.sqrt(suscritas.shape[0]/2))
parameters = {'init':('k-means++', 'random'), 'n_init':list(range(10,16)), 'n_clusters': list(range(3,topeCentros)), 'max_iter':list(range(200,600, 50))}
kmean = KMeans()

pca = PCA(.95)
pca.fit(suscritas1)
susc = pca.transform(suscritas1)

estimador = GridSearchCV(kmean, parameters1)

t1_start = perf_counter()

estimador.fit(susc)

t1_stop = perf_counter()
print("Elapsed time: ", t1_stop-t1_start)

#encontrar el mejor estimador:
print(estimador.best_estimator_)

print("The average silhouette_score is :", silhouette_score(susc, estimador.best_estimator_.labels_))


# CORRER LOS CASOS SIN PASAR LA DATA POR EL PCA

#t1_start = perf_counter()
#
#estimador.fit(suscritas)
#
#t1_stop = perf_counter()
#print("Elapsed time: ", t1_stop-t1_start)
#
##encontrar el mejor estimador:
#print(estimador.best_estimator_)
#
#print("The average silhouette_score is :", silhouette_score(suscritas, estimador.best_estimator_.labels_))
#

#PROBANDO EL CLUSTER GERARQUICO

parameters = {'n_clusters':list(range(2,topeCentros)), 'affinity':('euclidean', 'l1', 'l2'), 'linkage': ('ward', 'complete', 'average', 'single')}

