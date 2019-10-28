#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   fuzzycmeans.py
@Time    :   2019/10/24 10:52:31
@Author  :   Qi Yang
@Version :   1.0
@Describtion:   None
'''

# here put the import lib

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.linalg import norm
import kmeans
from matplotlib.pyplot import scatter,plot

from scipy.spatial.distance import cdist




class fuzzy_cmeans(object):
    def __init__(self,m,clusters):
        self.m=m
        self.k=clusters
        self.epsilon=1
        self.episode=1000
        self.centers=[]
        self.u= None
    
    def new_center(self,point,u):
        um = u ** self.m
        return (point.T @ um / np.sum(um, axis=0)).T

    def update_u(self,point,centers):
        power = float(2 / (self.m - 1))     
        temp = cdist(point, centers) ** power
        denominator_ = temp.reshape((point.shape[0], 1, -1)).repeat(temp.shape[-1], axis=1)
        denominator_ = temp[:, :, np.newaxis] / denominator_
        return 1 / denominator_.sum(2)

    @staticmethod
    def dist(p1,p2):
        return np.sqrt(np.power(p1[0]-p2[0],2)+np.power(p1[1]-p2[1],2))
    
    def Jfunc(self,point,center,u):
        dist_sum=0
        for j,cj in enumerate(center):
            for i,si in enumerate(point):
                dist_sum += np.power(u[i][j],self.m) * np.power(self.dist(si,cj),2)
        return dist_sum


    def fit(self,point):
        n=len(point)

        # initilize centers
        for i in range(self.k):
            self.centers.append(point[random.randint(0,n)])
        
        # initialize u matrix of membership grade
        self.u = np.zeros((n,self.k),dtype = float)
        for i in range(n):
            self.u[i][random.randint(0,self.k)] = 1 # set one in every column
        assert np.sum(self.u,axis=1).all() == 1.

        u=self.u.copy()
        centers=self.centers.copy()
        iter_times = 0
        dist_sum=[]
        dist_sum.append(self.Jfunc(point,centers,u))
        while iter_times < self.episode:

            centers=self.new_center(point,u)
            u=self.update_u(point,centers)
            iter_times += 1
            dist_sum.append(self.Jfunc(point,centers,u))

            if (norm(u - self.u) < self.epsilon) or (dist_sum[iter_times-1]-dist_sum[iter_times]<self.epsilon) :
                break
            if iter_times%100==0:
                print("is running",str(iter_times),"times")
        self.centers=centers
        self.u=u
        return dist_sum

def run(m,point):
    fcm = fuzzy_cmeans(clusters=2,m=m)
    fcm_distance = fcm.fit(point)
    fcm_centers = fcm.centers
    x=[]
    for i in range(len(fcm_distance)-1):
        x.append(i)

    y1=point.copy()
    y2=point.copy()

    for i in range(len(point)):
        y1[i][1]=fcm.u[i][0]
        y2[i][1]=fcm.u[i][1]
    
    line1=0.01
    line3=0.05
    plt.figure(figsize=(25,5))
    plt.subplot(131)
    plt.scatter(point[:,0], point[:,1],linewidths=line1,c='black')
    plt.scatter(fcm_centers[:1,0], fcm_centers[:1,1],marker='^',c='#F4A460')
    plt.scatter(y1[:,0],y1[:,1],c='#F4A460',linewidths=line3)
    plt.legend(('points','centers','membership grade'))
    plt.title('u of No.1 center')


    plt.subplot(132)
    plt.scatter(point[:,0], point[:,1],linewidths=line1,c='black')
    plt.scatter(fcm_centers[1:,0], fcm_centers[1:,1],marker='^',c='#00CED1')
    plt.scatter(y2[:,0],y2[:,1],c='#00CED1',linewidths=line3)
    plt.legend(('points','centers','membership grade'))
    plt.title('u of No.2 center')


    plt.subplot(133)
    plt.plot(x,fcm_distance[1:],c='black')   
    plt.title('Cumulative distance')
    name='fig'+str(m)

    plt.savefig(name)
    plt.show()




n_samples = 50
#centerbox= [(-5,0),(5,0)]
#point,_ = make_blobs(n_samples=100, n_features=2, cluster_std=1.6,center_box=centerbox, shuffle=False, random_state=42)
point=np.zeros((n_samples,2))
for i in range(25):
    point[i][0]=random.randint(0,45)
    point[-i][0]=random.randint(55,100)

run(2,point)
run(3,point)
run(4,point)
run(5,point)
run(10,point)
run(100,point)


kmeans.run(2,point)



    
