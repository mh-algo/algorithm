import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

def binary_search(lis,x):
	start,end=0,len(lis)
	while start<=end:
		mid=(start+end)//2
		if lis[mid]<x:
			start=mid+1
		else:
			end=mid-1
	return start

def LIS():
	lis=[]
	trace=[-1]*n
	for i in range(n):
		if not lis or lis[-1]<arr[i]:
			lis.append(arr[i])
			trace[i]=len(lis)-1
		else:
			index=binary_search(lis,arr[i])
			lis[index]=arr[i]
			trace[i]=index
	#print(lis)
	print(trace)
	index=len(lis)-1
	ret=[]
	for i in range(n-1,-1,-1):
		if trace[i]==index:
			ret.append(arr[i])
			index-=1
	return ret[::-1]

print(LIS())
