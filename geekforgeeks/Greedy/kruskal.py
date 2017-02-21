#kruskal algorithm MST
from collections import defaultdict

d = []

def addedge(x,y,value):
	d.append([x,y,value])

def findparent(element):
	if parent[element] == element:
		return element
	else: 
		return findparent(parent[element])


def union(x,y):
	i = findparent(x)
	j = findparent(y)

	if rank[i] > rank[j]:
		parent[j] = i

	elif rank[i] < rank[j]:
		parent[i] = j
	
	else:
		parent[i] = j
		rank[j] = rank[j] + 1
	

def kruskal(m):
	
	count = 0
	
	while(m):
		x,y,val = d[count]
		i = findparent(x)
		j = findparent(y)
		if i!=j:
			mst.append(d[count])
			union(x,y)
		count = count + 1
		m = m - 1


addedge(0,1,10)
addedge(0,2,6)
addedge(0,3,5)
addedge(1,3,15)
addedge(2,3,4)

d = sorted(d,key = lambda item : item[2])
n = len(d)
mst = []
parent = [-1]*n
for x in range(n):
	parent[x] = x
rank = [0]*n
kruskal(n)
print mst