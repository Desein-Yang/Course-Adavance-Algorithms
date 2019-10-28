import numpy as np
from numpy import random
import matplotlib.pyplot as plt




class Point(object):
    def __init__(self,num,pos_x,pos_y):
        self.num=num
        self.pos_x=pos_x
        self.pos_y=pos_y

    def dist(self,p2):
        dist=np.sqrt(np.power(self.pos_x-p2.pos_x,2)+np.power(self.pos_y-p2.pos_y,2))
        return dist

    def maxdist(self,centers):
        templist=[]
        for cen_i in centers:
            templist.append(self.dist(cen_i))
            return np.max(templist)

# virtual center selection algorithm
def vcs(pointlist,centernum):
    search=[]
    r=random.randint(1,2)
    while (pointlist):
        ini=pointlist[random.randint(1,pointnum)-1]
        search.append(ini)
        for p in pointlist:
            dist=p.dist(ini)
            if (dist>=2*r):
                pointlist.remove(p)
        if (len(search)<=centernum):
            return search
            break

def csa(point,centernum):
    search=[]
    ini=point[random.randint(1,pointnum)-1]
    search.append(ini)
    while(point): 
        dist=[]
        for i in point:
            dist.append(i.maxdist(search))
        dist_max=np.argmax(dist)
        search.append(point(dist_max))
        point.remove(point(dist_max))
        if (len(search)<=centernum):
            return search
            break


        
        

if __name__ == "__main__":
    pointlist=[]
    pointnum=10
    centernum=2

    for i in range(0,pointnum):
        x=random.randint(1,19)
        y=random.randint(1,19)
        pointlist.append(Point(i,x,y))

    center=csa(pointlist,centernum)
    for i in center:
        print (i.num,i.pos_x,i.pos_y)
    
    fig, ax = plt.subplots()
    x=[]
    y=[]
    for i in pointlist:
        x.append()
        y.append()
    plt.scatter(x, y)

    plt.show()
