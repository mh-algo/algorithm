from collections import deque

m,n,h=map(int,input().split()) # m=가로, n=세로, h=높이
box=[[] for _ in range(h)]
for i in range(h):
  for j in range(n):
    box[i].append(list(map(int,input().split())))

dx=[1,0,-1,0,0,0]              # x=가로, y=높이, z=세로
dy=[0,0,0,0,1,-1]
dz=[0,-1,0,1,0,0]

ripe=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

def bfs():
  cnt=0
  queue=deque()
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if box[i][j][k]==1:     # 토마토가 익어있는 경우 queue에 push
          queue.append((k,i,j))
  while queue:
    x,y,z=queue.popleft()
    for i in range(6):
      nx=dx[i]+x
      ny=dy[i]+y
      nz=dz[i]+z
      if nx>=m or nx<0 or ny>=h or ny<0 or nz>=n or nz<0:
        continue
      if ripe[ny][nz][nx]==0 and box[ny][nz][nx]==0:
        queue.append((nx,ny,nz))
        ripe[ny][nz][nx]=ripe[y][z][x]+1
        cnt=max(cnt,ripe[ny][nz][nx])
  return cnt

cnt=bfs()
ans=True
for i in range(h):
  for j in range(n):
    for k in range(m):
      if ripe[i][j][k]==0 and box[i][j][k]==0:    # 익지 않은 토마토가 존재할 경우
        ans=False
if ans:print(cnt)
else:print(-1)
