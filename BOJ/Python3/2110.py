import sys
input=sys.stdin.readline

arr=[]
n,c=map(int,input().split())
for _ in range(n):
	arr.append(int(input()))
arr.sort()

def binary_search(arr):
	start=1             # 두 공유기의 최소 거리를 1로 생각함
	end=arr[-1]-arr[0]  # 두 공유기의 최대 거리
	distance=0
	while start<=end:
		mid=(start+end)//2    # 두 공유기 사이의 거리
		install=arr[0]    # 공유기를 설치한 집
		cnt=1   # 설치한 공유기 개수
		for i in range(1,n):
			if arr[i]-install>=mid:     # 두 공유기 간의 거리가 mid 보다 클 경우
				install=arr[i]            # 공유기를 설치함
				cnt+=1                # 공유기를 설치했으므로 1 증가
		if cnt>=c:
			start=mid+1            # 설치한 공유기 수가 c보다 같거나 많을 경우
			distance=mid           # 두 공유기간의 거리 저장
		else:              # 공유기를 c만큼 설치하지 못할 경우
			end=mid-1
	return distance

print(binary_search(arr))
