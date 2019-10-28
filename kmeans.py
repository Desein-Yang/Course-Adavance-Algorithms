#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   kmeans.py
@Time    :   2019/10/24 10:52:23
@Author  :   Qi Yang
@Version :   1.0
@Describtion:   None
'''

# here put the import lib

import numpy as np
import time  
import matplotlib.pyplot as plt  
  
  
# calculate Euclidean distance  
def euclDistance(vector1, vector2):  
	return np.sqrt(np.sum(np.power(vector2 - vector1, 2)))  #求这两个矩阵的距离，vector1、2均为矩阵
  
# init centroids with random samples  
#在样本集中随机选取k个样本点作为初始质心
def initCentroids(dataSet, k):  
	numSamples, dim = dataSet.shape   #矩阵的行数、列数 
	centroids = np.zeros((k, dim))  		#感觉要不要你都可以
	for i in range(k):  
		index = int(np.random.uniform(0, numSamples))  #随机产生一个浮点数，然后将其转化为int型
		centroids[i, :] = dataSet[index, :]  
	return centroids  
  
# k-means cluster 
#dataSet为一个矩阵
#k为将dataSet矩阵中的样本分成k个类 
def kmeans(k,dataSet):  
	numSamples = dataSet.shape[0]  #读取矩阵dataSet的第一维度的长度,即获得有多少个样本数据
    # first column stores which cluster this sample belongs to,  
    # second column stores the error between this sample and its centroid  
	clusterAssment = np.mat(np.zeros((numSamples, 2)))  #得到一个N*2的零矩阵
	clusterChanged = True  
  
    ## step 1: init centroids  
	centroids = initCentroids(dataSet, k)  #在样本集中随机选取k个样本点作为初始质心
  
	while clusterChanged:  
		clusterChanged = False  
        ## for each sample  
		for i in range(numSamples):  #range
			minDist  = 100000.0  
			minIndex = 0  
            ## for each centroid  
            ## step 2: find the centroid who is closest  
			#计算每个样本点与质点之间的距离，将其归内到距离最小的那一簇
			for j in range(k):  
				distance = euclDistance(centroids[j, :], dataSet[i, :])  
				if distance < minDist:  
					minDist  = distance  
					minIndex = j  
              
            ## step 3: update its cluster 
			#k个簇里面与第i个样本距离最小的的标号和距离保存在clusterAssment中
			#若所有的样本不在变化，则退出while循环
			if clusterAssment[i, 0] != minIndex:  
				clusterChanged = True  
				clusterAssment[i, :] = minIndex, minDist**2  #两个**表示的是minDist的平方
  
        ## step 4: update centroids  
		for j in range(k):  
			#clusterAssment[:,0].A==j是找出矩阵clusterAssment中第一列元素中等于j的行的下标，返回的是一个以array的列表，第一个array为等于j的下标
			pointsInCluster = dataSet[np.nonzero(clusterAssment[:, 0].A == j)[0]] #将dataSet矩阵中相对应的样本提取出来 
			centroids[j, :] = np.mean(pointsInCluster, axis = 0)  #计算标注为j的所有样本的平均值
  
	print ('Congratulations, cluster complete!')  
	return centroids, clusterAssment[:,0]  
  
# show your cluster only available with 2-D data 
#centroids为k个类别，其中保存着每个类别的质心
#clusterAssment为样本的标记，第一列为此样本的类别号，第二列为到此类别质心的距离 
def run(k,point):
	centers, labels = kmeans(k,point)
	y1=point.copy()
	y2=point.copy()

	for i in range(len(point)):
		y1[i][1]=labels[i]
		y2[i][1]=1-labels[i]

	line1=0.01
	line3=0.05
	
	plt.figure(figsize=(25,5))

	plt.subplot(131)
	plt.scatter(point[:,0], point[:,1],linewidths=line1,c='black')
	plt.scatter(centers[:1,0], centers[:1,1],marker='^',c='#F4A460')
	plt.title('origin points')
	
	plt.subplot(132)
	plt.scatter(centers[:1,0], centers[:1,1],marker='^',c='black')
	plt.scatter(y1[:,0],y1[:,1],c='#F4A460',linewidths=line3)
	plt.legend(('points','centers','membership grade'))
	plt.title('u of No.1 center')
	
	plt.subplot(133)
	plt.scatter(centers[1:,0], centers[1:,1],marker='^',c='black')
	plt.scatter(y2[:,0],y2[:,1],c='#00CED1',linewidths=line3)
	plt.legend(('points','centers','membership grade'))
	plt.title('u of No.2 center')
	plt.savefig('kmeans k2')
	plt.show()






