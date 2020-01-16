from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
import pandas as pd
from time import perf_counter 

iris = datasets.load_iris()

parameters1 = {'init':('k-means++', 'random'), 'n_init':list(range(10,21)), 'n_clusters': list(range(3,11)), 'max_iter':list(range(200,1100, 100))}
kmean = KMeans()
estimador = GridSearchCV(kmean, parameters1)
estimador.fit(iris.data)

#encontrar el mejor estimador:
print(estimador.best_estimator_)

#obtener los centros de los mejores estimadores:
print(estimador.best_estimator_.cluster_centers_)

#con los centros del mejor estimador, 
#predecir a que centro pertenece c/instancia y devolverlo como un dataframe
df = pd.DataFrame(estimador.best_estimator_.predict(iris.data).tolist(), columns = ['in'])

#metodo1 para extracion del centro con mayor cantidad de instancias
t1_start = perf_counter()

cuenta = df['in'].value_counts()
valorMasGrande = max(df['in'].value_counts())
elegido = cuenta[cuenta == max(cuenta)].index[0]

t1_stop = perf_counter()
print("Elapsed time with series:", t1_stop-t1_start)


 #metodo2 para extracion del centro con mayor cantidad de instancias
t1_start = perf_counter()
   
cuenta1 = df.groupby('in')
valorMasGrande = df.groupby('in').size().max()
elegido1 = cuenta1.size()[cuenta1.size() == valorMasGrande].index[0]

t1_stop = perf_counter()
print("Elapsed time with DF:", t1_stop-t1_start)


#METODO 1 PARA ACCESAR A LOS ELEMENTOS DE UN DETERMINADO CENTRO
t1_start = perf_counter()
for i in range(valorMasGrande):
    instancia = cuenta1.groups[elegido1][i]
    print(iris.data[instancia])
    
t1_stop = perf_counter()
print("Elapsed time acceso METODO 1:", t1_stop-t1_start)


#METODO 2 PARA ACCESAR A LOS ELEMENTOS DE UN DETERMINADO CENTRO
t1_start = perf_counter()
for i in range(valorMasGrande):
    instancia = cuenta1.get_group(elegido1).iloc[i].name
    print(iris.data[instancia])
    
t1_stop = perf_counter()
print("Elapsed time acceso METODO 2:", t1_stop-t1_start)