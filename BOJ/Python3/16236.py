from collections import deque
import heapq

n=int(input())
sea=[]
start=tuple()
for i in range(n):
  sea.append(list(map(int,input().split())))
  for j in range(n):
    if sea[i][j]==9:
      start=(i,j)
      sea[i][j]=0       # 상어가 물고기로 인식되는 경우를 방지하기 위해 0으로 수정

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def bfs(start,shark):
  a,b=start
  queue=deque()
  queue.append((a,b))
  visit=[[0 for _ in range(n)] for _ in range(n)]
  visit[a][b]=1
  fish=[]
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if nx>=n or nx<0 or ny>=n or ny<0:
        continue
      if sea[nx][ny]>shark:
        continue
      if visit[nx][ny]==0:
        visit[nx][ny]=visit[x][y]+1
        queue.append((nx,ny))
        if sea[nx][ny]!=0 and sea[nx][ny]<shark:
          heapq.heappush(fish,(visit[nx][ny]-1,nx,ny))        # 거리가 가까움 -> 가장 위에 있음 -> 가장 왼쪽에 있음
  if fish:                                                    # 순으로 물고기를 잡아먹으므로 우선순위 큐를 이용
    return heapq.heappop(fish)     # 거리가 가장 가깝고, 가장 위에 있으며, 가장 왼쪽에 있는 물고기의 좌표를 반환
  else: return 0

def shark_eat(start):
  shark=2
  eat=0
  a,b=start
  cnt=0
  while 1:
    fish=bfs(start,shark)
    if fish==0:     # 더 이상 잡아먹을 물고기가 없을 경우 break
      break
    c,x,y=fish
    sea[x][y]=0     # 잡아먹은 경우 0 대입
    start=(x,y)     # 상어 시작 위치 재설정
    cnt+=c          # 걸린 시간 누적
    eat+=1          # 잡아먹은 물고기 수
    if eat==shark:   # 상어가 커졌을 경우
      eat=0
      shark+=1
  return cnt        # 걸린 시간 반환

print(shark_eat(start))
