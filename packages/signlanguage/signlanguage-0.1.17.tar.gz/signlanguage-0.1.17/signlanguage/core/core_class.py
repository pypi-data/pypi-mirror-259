from sklearn.cluster                                    import KMeans
from signlanguage.interfaces.interfaces_model           import IKmeans, INeural
import numpy                                            as np
import time

RANGE_THRESHOLD_POOL = 0.01
RANGE_THRESHOLD_CLASS = 0.5

## core dispertion - single core
class CorePool(IKmeans):
    def __init__(self, n_clusters=4, init='k-means++'):
        #core attr
        self.kmeans = KMeans(n_clusters=n_clusters, init=init, n_init='auto')
        self.cluster_centers_ = None

    def fit(self, X):
        try:
            self.kmeans.fit(X)
            self.cluster_centers_ = self.kmeans.cluster_centers_
        except Exception as e:
            print("Error Ocurrido [Core - Kmeans model], Mensaje: {0}".format(str(e)))

    def predict(self, X):
        try:
            distances = self.kmeans.transform(X)
            closest_cluster_distance = np.min(distances, axis=1)
            if (closest_cluster_distance[0] <= RANGE_THRESHOLD_POOL):
                return 1
            return 0
        except Exception as e:
            print("Error Ocurrido [Core - Kmeans model - Predict], Mensaje: {0}".format(str(e)))
            return None
    
    def predict_cluster(self, X):
        return self.kmeans.predict(X)
    
    def predict_min(self, X):
        try:
            cluster_asignado = self.kmeans.predict(X)
            distancia_al_centroide = np.linalg.norm(X - self.cluster_centers_[cluster_asignado])
            if (distancia_al_centroide <= RANGE_THRESHOLD_POOL):
                return 1
            return 0
        except Exception as e:
            print("Error Ocurrido [Core - Kmeans model - PredictV2], Mensaje: {0}".format(str(e)))
            return None
        
    async def predict_min_async(self, X):
        try:
            cluster_asignado = self.kmeans.predict(X)
            distancia_al_centroide = np.linalg.norm(X - self.cluster_centers_[cluster_asignado])
            if (distancia_al_centroide <= RANGE_THRESHOLD_POOL):
                return 1
            return 0
        except Exception as e:
            print("Error Ocurrido [Core - Kmeans model - PredictV2], Mensaje: {0}".format(str(e)))
            return None
