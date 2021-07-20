from collections import deque
import sys

input=sys.stdin.readline
n,m=map(int,input().split())
distance=[[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
	a,b=map(int,input().split())
	distance[a][b]=1
	distance[b][a]=1
for k in range(1,n+1):    # 플로이드 와샬 알고리즘 사용
	distance[k][k]=0
	for a in range(1,n+1):
		for b in range(1,n+1):
			distance[a][b]=min(distance[a][b],distance[a][k]+distance[k][b])
total,idx=float('inf'),0
for i in range(n):
	t=sum(distance[i][1:])
	if t<total:
		total=t
		idx=i
print(idx)
