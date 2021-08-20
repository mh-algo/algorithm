import sys
input=sys.stdin.readline

n=int(input())    # 수열의 크기
arr=list(map(int,input().split()))    # 수열

# 이진 탐색
def binary_search(lis,x):
	start,end=0,len(lis)
	while start<=end:
		mid=(start+end)//2
		if lis[mid]<x:
			start=mid+1
		else:
			end=mid-1
	return start

# LIS를 찾는 함수
def LIS(arr,n):
	lis=[]    # lis를 구할 때 사용되는 배열
	trace=[-1]*n    # 배열 arr의 숫자가 lis 배열에 대입될 때 index를 저장하는 배열
	for i in range(n):
		# arr[i]의 값이 배열 lis의 마지막 index의 값보다 클 경우
		if not lis or lis[-1]<arr[i]:
			lis.append(arr[i])    # 배열 lis에 추가
			trace[i]=len(lis)-1   # trace에 index를 저장
		# arr[i]의 값이 배열 lis의 마지막 index의 값보다 작을 경우
		else:
			index=binary_search(lis,arr[i])    # 이진 탐색을 통해서 배열 lis에 arr[i]가 저장될 index를 구함
			lis[index]=arr[i]    # 배열 lis[index]의 값 변경
			trace[i]=index    # trace에 index를 저장
	index=len(lis)-1
	ret=[]		# 최종적으로 lis가 저장되는 배열
	for i in range(n-1,-1,-1):    # trace 배열을 역순으로 탐색하기 위함
		# trace 배열 뒤에서부터 배열 lis의 index 순으로 저장
		if trace[i]==index:
			ret.append(arr[i])
			index-=1
	return ret[::-1]

print(*LIS(arr,n))
