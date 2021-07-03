import sys
import heapq

def dijkstra(graph,time,start):
  queue=[]
  time[start]=0
  heapq.heappush(queue,(0,start))
  while queue:
    t,com=heapq.heappop(queue)
    if time[com]<t:
      continue
    for nt,ncom in graph[com]:
      next_time=time[com]+nt
      if next_time<time[ncom]:
        time[ncom]=next_time
        heapq.heappush(queue,(next_time,ncom))

def hacking_com(time):
  t=0
  cnt=0
  for i in time:
    if i!=float('inf'):
      if t<i:
        t=i
      cnt+=1
  return cnt,t

test=int(sys.stdin.readline().strip())
for _ in range(test):
  n,d,c=map(int,sys.stdin.readline().split())
  graph=[[] for _ in range(n+1)]
  for _ in range(d):
    a,b,s=map(int,sys.stdin.readline().split())
    graph[b].append((s,a))
  time=[float('inf') for _ in range(n+1)]
  dijkstra(graph,time,c)
  cnt,t=hacking_com(time)
  print(cnt,t)
