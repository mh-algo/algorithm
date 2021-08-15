import sys

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())
arr=list(map(int,input().split()))
a.sort()

# 이진 탐색
def binary_search(x):
	start,end=0,len(a)-1
	while start<=end:
		mid=(start+end)//2
		if a[mid]<x:
			start=mid+1
		elif a[mid]>x:
			end=mid-1
    # 해당 숫자를 찾은 경우 1 반환
		else:
			return 1
  # 해당 숫자가 없는 경우 0 반환
	return 0

for x in arr:
	print(binary_search(x))
