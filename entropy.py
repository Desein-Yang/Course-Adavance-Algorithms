import numpy as np

class Person(object):
    def __init__(self,region,height):
        self.height = height
        self.region = region

    @staticmethod
    def prob(personlist,height,region):
        '''p(x,y)  p(x>height,y) p(x<height,y)'''
        prob = [0,0]
        
        for i in personlist:
            if i.region == region and i.height >= height:
                prob[0] += 1
            elif i.region == region and i.height < height:
                prob[1] += 1
        n = len(personlist)
        prob[0] = prob[0] / n 
        prob[1] = prob[1] / n
        return prob

    @staticmethod
    def condprob(personlist,height,region):
        '''p(y|x)'''
        prob = [0,0]
        num = [0,0]
        for i in personlist:
            if i.height >= height:
                num[0] += 1
                if i.region == region:
                    prob[0] += 1
            if i.height < height:
                num[1] += 1
                if i.region == region:
                    prob[1] += 1
        if num[0]!=0:
            prob[0]=prob[0]/num[0]
        else:
            prob[0]=0
        if num[1]!=0:
            prob[1]=prob[1]/num[1]
        else:
            prob[1]=0

        return prob

    @staticmethod
    def condentropy(personlist,height):
        '''H(Y|X)'''
        H = 0
        region = ['Europe','Asia','America']
        for i in region:
            prob = Person.prob(personlist,height,i)
            condprob = Person.condprob(personlist,height,i)
            if condprob[0]!=0 and condprob[1]!=0:
                H +=  prob[0]*np.log2(condprob[0])+prob[1]*np.log2(condprob[1])
            elif condprob [0]== 0 and condprob[1] != 0:
                H += prob[1]*np.log2(condprob[1])
            elif condprob [0]!= 0 and condprob[1] == 0:
                H += prob[0]*np.log2(condprob[0])
            else:
                H += 0
        H = 0 - H
        return H

    @staticmethod
    def infogain(personlist,condent):
        ig = 0
        prob =[0,0,0]
        H = 0
        n = len(personlist)
        region = ['Europe','Asia','America']
        for i in personlist:
            prob[region.index(i.region)] += 1/n
        for j in prob:    
            H -= j * np.log2(j)
        ig = H - condent
    
        return ig,H
            

if __name__ == "__main__":
    
    #height = [180,183,176,168,174,170,180,179,175]
    region = ['Europe','Europe','Europe','Asia','Asia','Asia','America','America','America']
    height = [73,75,70,60,65,59,78,80,75]
    personlist = []
    for i in range(9):
        p = Person(region[i],height[i])
        personlist.append(p)

    for i in height:
        IG,H = Person.infogain(personlist,Person.condentropy(personlist,i))   
        print ("information gain = "+str(IG)+" when weight =" + str(i))
    print("entropy =" +str(H))




    

        

    

    

    


            


