#longest subsequence problem dynamic programming
def LIS(arr,n):
	lis = [1]*n
	for i in range(1,n):
		for j in range(0,i):
			if arr[i]>arr[j] and lis[j]+1>lis[i]:
				lis[i] = lis[j]+1
	return max(lis)

input = [1,2,3,4,5,10,2,1]
print LIS(input,len(input))