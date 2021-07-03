import sys
import heapq

V,E=map(int,sys.stdin.readline().split())    # V=정점의 개수, E=간선의 개수
K=int(input())   # K=시작 정점의 번호
graph=[[] for _ in range(V+1)]
for _ in range(E):
  u,v,w=map(int,sys.stdin.readline().split())
  graph[u].append((v,w))

def dijkstra(start):
  distance=[float('inf') for _ in range(V+1)]
  distance[start]=0
  queue=[]
  heapq.heappush(queue,(0,start))
  while queue:
    w,v=heapq.heappop(queue)
    if distance[v]<w:  # 쓸모없는 계산 방지
      continue
    for nv,nw in graph[v]:
      next=distance[v]+nw
      if distance[nv]>next:
        distance[nv]=next
        heapq.heappush(queue,(next,nv))
  return distance

distance=dijkstra(K)
for i in distance[1:]:
  if i==float('inf'):print('INF')
  else:print(i)
