from collections import deque

n,m=map(int,input().split())
board=[]
r,b=tuple(),tuple()
for i in range(n):
  board.append(list(' '.join(input()).split()))
  for j in range(m):
    if board[i][j]=='R':
      r=(i,j)
    if board[i][j]=='B':
      b=(i,j)

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def move(x,y,dx,dy):
  cnt=0
  while board[x+dx][y+dy]!='#' and board[x][y]!='O':  # 벽이나 구멍을 만나기 전까지 이동
    x+=dx
    y+=dy
    cnt+=1
  return x,y,cnt

def bfs(r,b):
  ra,rb=r
  ba,bb=b
  queue=deque()
  queue.append((ra,rb,ba,bb,0))
  visit=[[[[0 for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
  while queue:
    rx,ry,bx,by,cnt=queue.popleft()
    if cnt+1>10:      # 이동 횟수가 10을 초과할 경우
      return -1
    for i in range(4):
      nrx,nry,rcnt=move(rx,ry,dx[i],dy[i])
      nbx,nby,bcnt=move(bx,by,dx[i],dy[i])
      if board[nbx][nby]!='O':
        if board[nrx][nry]=='O':    # 빨간 구슬이 구멍에 들어간 경우
          return cnt+1
        if nrx==nbx and nry==nby: # 빨간 구슬과 파란 구슬이 겹친 경우
          if rcnt>bcnt:           # 더 많이 이동한 구슬을 한칸 뒤로 이동 시킴
            nrx-=dx[i]
            nry-=dy[i]
          if rcnt<bcnt:
            nbx-=dx[i]
            nby-=dy[i]
        if visit[nrx][nry][nbx][nby]==0:
          visit[nrx][nry][nbx][nby]=1
          queue.append((nrx,nry,nbx,nby,cnt+1))
  return -1

print(bfs(r,b))
