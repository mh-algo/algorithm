import sys
input=sys.stdin.readline

n=int(input())
arr=[]
for _ in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort()

# 이분 탐색 함수
# 배열 lis에서 x보다 작은 값이 존재하는 index를 반환하는 함수
def binary_search(lis,x):
    start,end=0,len(lis)-1
    while start<end:
        mid=(start+end)//2
        if lis[mid][1]<x:
            start=mid+1
        else:
            end=mid-1
    return start

lis=[]    # LIS 저장할 배열
trace={}  # 배열 arr의 값들이 배열 LIS[index]에 저장될 경우 그 값과 index를 기록하기 위한 dict
          # trace에 {(arr의 데이터):(열 lis의 index)} 형식으로 저장
for i in range(n):
    if not lis or lis[-1][1]<arr[i][1]:
        lis.append(arr[i])
        trace[arr[i]]=len(lis)-1
    else:
        index=binary_search(lis,arr[i][1])
        lis[index]=arr[i]
        trace[arr[i]]=index

print(n-len(lis))
index=len(lis)-1
# arr의 맨 뒤에 위치한 데이터부터 시작
for i in range(n-1,-1,-1):
    # trace에 저장된 index와 현재 index가 같을 경우
    if trace[arr[i]]==index:
        # lis에 해당하므로 trace에서 지운다
        # 이런 방법으로 trace에는 lis에 해당되지 않은 값만 남긴다)
        del(trace[arr[i]])
        index-=1

for a,b in trace.keys():
	print(a)
