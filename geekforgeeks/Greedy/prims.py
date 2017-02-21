#prims 
import heapq as heap
from collections import defaultdict as d 
#TODO complete code
def addedge(x,y):
	defaultdict[x].append(y,cost))
def prims(n):
	while (l):
		keyy,current = heap.heappop(l)
		mst.append(current)
		neighbours  = defaultdict[current]
		for x in neighbours:
			if x not in mst:
				for key,value in l:
					if value == current:
						if keyy < key:
							l[key] = current
							h.heapify(l)
addedge()
l = []
	for x in range(n):
		l.append((9999,n))
	heap.heapify(l)
mst = []