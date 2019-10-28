import numpy as np
import matplotlib.pyplot as plt 

def greedy(m,t):
	mlist=[]
	mt=[]
	for i in range(0,m):
		mlist.append([])
		mt.append(0)
	
	for i,timei in enumerate(t):
		j=np.argmin(mt)
		mt[j]+=timei
		mlist[j].append(i+1)
	a=sum(t)/m
	b=max(t)
	T=(a,b,np.max(mt))
	# x=np.arange(m)
	# plt.bar(x,,width=0.8,bottom=sum(mt[j]))
	# plt.show()
	return mlist,mt,T


if __name__ == "__main__":
	m=4
	n=21
	t=[]
	for k in range(n-1):
		t.append(1)
	t.append(5)
	print(greedy(m,t))
	
			