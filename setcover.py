#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   setcover.py
@Time    :   2019/10/28 23:35:31
@Author  :   Qi Yang
@Version :   1.0
@Describtion:   None
'''

# here put the import lib
import numpy as np


class Setcover(object):
    def __init__(self,num):
        self.fullset = list(np.arange(1,num)) 
        self.subset = [[1,2,3,4],[1,2,5,7],[3,4,6,8],[5,6],[7],[8]]
        self.weight = np.array([4,2.2,2.2,4,4,4])
        self.remain = self.fullset.copy()

    def greedy(self):
        select = []
        cum_weight = 0
        while (self.remain!=[]):
            aver_weight = np.zeros(self.weight.shape)
            for i,si in enumerate(self.subset):
                j = self.joint(si,self.remain)
                if j == 0 :
                    aver_weight[i] = np.max(self.weight)
                else:
                    aver_weight[i] = self.weight[i] / j
            select_subset = self.subset[np.argmin(aver_weight)]
            weight = self.weight[np.argmin(aver_weight)]
            select.append(select_subset)
            cum_weight += weight
            
            for i in select_subset:
                if i in self.remain:
                    self.remain.remove(i)
        return select,cum_weight

    @staticmethod
    def joint(subset,remain):
        s = 0
        for i in subset:
            for j in remain:
                if i == j :
                    s += 1
        return s


if __name__ == "__main__":
    a = Setcover(9)
    print("Fullset is "+str(a.fullset))
    select , weight = a.greedy()
    print("Select subset is "+str(select))
    print("Total weight is "+str(weight))

