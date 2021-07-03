from collections import deque

dx=[2,1,-1,-2,-2,-1,1,2]
dy=[1,2,2,1,-1,-2,-2,-1]

def bfs(chess,start,stop):
  l=len(chess)
  queue=deque()
  queue.append(start)
  while queue:
    x,y=queue.popleft()
    if (x,y)==stop:
      return
    for i in range(8):
      nx=dx[i]+x
      ny=dy[i]+y
      if nx>=l or nx<0 or ny>=l or ny<0:
        continue
      if chess[ny][nx]==0:
        chess[ny][nx]=chess[y][x]+1
        queue.append((nx,ny))

test=int(input())
for i in range(test):
  l=int(input())
  chess=[[0 for _ in range(l)] for _ in range(l)]
  start=tuple(map(int,input().split()))
  stop=tuple(map(int,input().split()))
  bfs(chess,start,stop)
  x,y=stop
  print(chess[y][x])
