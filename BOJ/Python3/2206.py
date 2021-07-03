from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
  graph.append(list(map(int,' '.join(input()).split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs():
  visit=[[[0,0] for _ in range(m)] for _ in range(n)]     #[0,0]=[벽을 부수기 전 이동한 칸의 개수, 벽을 부순 후 이동한 칸의 개수]
  queue=deque()
  queue.append((0,0,0))
  visit[0][0][0]=1
  while queue:
    x,y,w=queue.popleft()
    if y==n-1 and x==m-1:
      return visit[y][x][w]
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if nx>=m or nx<0 or ny>=n or ny<0:
        continue 
      if graph[ny][nx]==1 and w==0:           # 벽이 존재해 벽을 1번 부술 경우
        visit[ny][nx][1]=visit[y][x][0]+1
        queue.append((nx,ny,1))
      elif graph[ny][nx]==0 and visit[ny][nx][w]==0:    # 가로막은 벽이 존재하지 않는 경우
        visit[ny][nx][w]=visit[y][x][w]+1
        queue.append((nx,ny,w))
  return -1

print(bfs())
