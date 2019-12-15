#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11930392.py
@Time    :   2019/12/06 16:14:51
@Author  :   Qi Yang
@Version :   1.0
@Describtion:   None
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler

class Kmeans(object):
    def __init__(self,filename,k):
        self.k = k
        self.data = self.preprocess(self.load_data(filename))
        self.datanum = self.data.shape[0]
        self.centers = self.ini_centers_random() 
        self.clusters = np.zeros(self.datanum)

    # import data 
    @staticmethod
    def load_data(filename):
        '''Read and preprocess data from file \n Return ndarray '''
        data_df = pd.read_csv(filename,header=None)
        data = data_df.values
        return data
    
    def preprocess(self,data):
        scaler1 = MinMaxScaler()
        data = scaler1.fit_transform(data)
        scaler2 = StandardScaler()
        data = scaler2.fit_transform(data)
        return data
    # calculate distance
    @staticmethod
    def eudic_dist(s1,s2):
        dist = 0
        for i in range(s1.shape[0]):
            dist += np.power(s1[i]-s2[i],2)
        return np.sqrt(dist)

    # initilization
    def ini_centers_random(self):
        centers=[]
        for i in range(self.k):
            rand_id = np.random.randint(0,self.datanum)
            centers.append(self.data[rand_id])
        return np.array(centers)


    def cal_centers(self,cluster):
        cluster = np.array(cluster)
        centers = np.zeros(cluster.shape[1])
        for sample in cluster:
            centers += sample
        centers = centers / cluster.shape[0]
        dist=[self.eudic_dist(centers,x) for x in cluster]
        return cluster[np.argmin(dist)]
    # kmeans
    def clustering(self):
        # centers,centers_index = self.ini_centers()
        nochange = True
        iter_times = 0
        while(nochange):
            # find cloest centers and classify
            clusters = np.zeros(self.datanum)
            for i,sample in enumerate(self.data):
                dists = np.zeros(self.k)
                for j,center in enumerate(self.centers):
                    dists[j] = self.eudic_dist(sample,center)
                clusters[i] = np.argmin(dists)+1
            clusters = clusters.astype(int)
                

            self.clusters = clusters 

            # update centers
            clusterdata = [[] for _ in range(self.k)]
            new_centers = []
            for i,j in enumerate(clusters):
                clusterdata[j-1].append(self.data[i])
            for clus in clusterdata:
                new_centers.append(self.cal_centers(clus))
            new_centers= np.array(new_centers)
            iter_times += 1
            if (iter_times >10):
                self.centers = self.ini_centers_random()
            if (new_centers == self.centers).all():
                nochange = False
            else:
                self.centers = new_centers
            with open('log.txt','a') as f:
                f.write('Iteration:'+str(iter_times)+'\n'+'K:'+str(self.k)+'\n')
                #f.write(str(self.centers)+'\n')
                f.write(str(self.clusters)+'\n')
                f.write(str(self.evaluate()))
        return self.clusters
    
    def evaluate(self):
        sse = 0
        for i,sample in enumerate(self.data):
            center = self.centers[self.clusters[i]-1] 
            sse += self.eudic_dist(sample,center)
        return sse


def show_k(path,a,b):
    # test what is k
    sse = []
    for k in range(a,b):
        clf = Kmeans(path,k)
        clusters = clf.clustering()
        sse.append (clf.evaluate())
    plt.plot(range(2,9),sse)
    plt.show()
    with open('choose_log.txt','a') as f:
        f.write(str(clusters))
        f.write('\n')
        f.write(str(sse))
    

# predict when k is determined
if __name__ == "__main__":
    path = 'G:\Course Note-Master\Advanced AI-ZhangYu\Assignment4\data.txt'
    # show_k(path,2,9)
    clf = Kmeans(path,5)
    clusters = clf.clustering()
    with open('cluster.txt','a') as f:
        for i in clusters:
            f.write(str(i))
            f.write('\n')
