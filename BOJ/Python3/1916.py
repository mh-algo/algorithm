import sys
import heapq

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
  a,b,d=map(int,sys.stdin.readline().split())
  graph[a].append((d,b))
start,stop=map(int,input().split())

def dijkstra(start):
  cost=[float('inf') for _ in range(n+1)]
  queue=[]
  cost[start]=0
  heapq.heappush(queue,(0,start))
  while queue:
    d,b=heapq.heappop(queue)
    if cost[b]<d:
      continue
    for nd,nb in graph[b]:
      next_cost=cost[b]+nd
      if next_cost<cost[nb]:
        cost[nb]=next_cost
        heapq.heappush(queue,(next_cost,nb))
  return cost

cost=dijkstra(start)
print(cost[stop])
