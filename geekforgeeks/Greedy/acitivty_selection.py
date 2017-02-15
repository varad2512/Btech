#activity selection

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]

n = 6
index = 0
prev = 0
while(n>0):
	if start[index] >= prev:
		print index
		prev = end[index]
	index = index + 1
	n = n - 1