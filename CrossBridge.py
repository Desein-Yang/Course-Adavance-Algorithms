# Q1
# four people want to cross bridge 
def max(a,b):
	if (a>b):return a 
	else:b
	
def min(a,b):
	if (a<b):return a
	else:b

def method_1(cost,n):
	return 2*cost[0]+cost[n-1]+cost[n-2]

def method_2(cost,n):
	return 2*cost[1]+cost[0]+cost[n-1]

def sumcost(cost):
	n=len(cost)
	if (n==1):
		sum=cost[0]
	elif(n==2):
		sum=max(cost[0],cost[1])
	elif(n>=3):
		sum=sumcost(cost[0:n-2])+min(method_1(cost,n),method_2(cost,n))
	return sum


if __name__ == '__main__':
	cost=[2,5,7,11,15]
	sum=sumcost(cost)
	print(sum)
