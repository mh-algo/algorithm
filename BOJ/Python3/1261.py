import heapq
import sys
input=sys.stdin.readline

arr=[]
m,n=map(int,input().split())
for _ in range(n):
	arr.append(list(map(int,' '.join(input()).split())))   

dx=[1,0,-1,0]
dy=[0,1,0,-1]
# 벽을 간선 간의 거리라고 생각하고 다익스트라 알고리즘을 사용
def dijkstra(start=(0,0)):
	dist=[[float('inf')]*m for _ in range(n)]
	a,b=start
	queue=[]
	heapq.heappush(queue,(arr[a][b],a,b))     # (벽,x좌표,y좌표) 순으로 배열에 저장
	dist[a][b]=0
	while queue:
		d,x,y=heapq.heappop(queue)
		for i in range(4):
			nx=dx[i]+x
			ny=dy[i]+y
			if 0<=nx<n and 0<=ny<m:
				cost=d+arr[nx][ny]
				if dist[nx][ny]>cost:
					dist[nx][ny]=cost
					heapq.heappush(queue,(cost,nx,ny))
	return dist[n-1][m-1]

print(dijkstra())
