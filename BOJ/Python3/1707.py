import sys
from collections import deque

def bfs(t,colors):
  color=colors[t]
  queue=deque()
  queue.append((t,color))
  while queue:
    a,color=queue.popleft()
    color=(color+1)%2
    for i in graph[a]:
      if colors[i]==-1:
        colors[i]=color
        queue.append((i,color))
      elif colors[i]!=color:        # 색이 맞지 않는 경우 False 반환
        return False
  return True

k=int(input())
for _ in range(k):
  v,e=map(int,input().split())
  graph={num+1:set() for num in range(v)}
  colors=[-1 for _ in range(v+1)]
  for _ in range(e):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)
  chk=True
  for i in range(v):
    if colors[i+1]==-1:     # 탐색을 안한 경우만 탐색
      chk=bfs(i+1,colors)
      if chk==False: break
  if chk: print('YES')
  else: print('NO')
