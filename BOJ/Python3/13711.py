n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# 수열 a를 기준으로 우선순위를 정함
rank=[0]*(n+1)
for i in range(n):
	rank[a[i]]=i+1

arr=[]
# 배열 rank를 기준으로 이분 탐색하는 함수
def binary_search(target):
	start,end=0,len(arr)-1
	while start<=end:
		mid=(start+end)//2
    # target의 우선순위가 더 클 경우
		if rank[arr[mid]]<rank[target]:
			start=mid+1
    # target의 우선순위가 더 작을 경우
		else:
			end=mid-1
	return start

for x in b:
	if not arr or rank[arr[-1]]<rank[x]:
		arr.append(x)
	else:
		arr[binary_search(x)]=x
print(len(arr))   # LCS의 크기 == 배열 arr의 크기
