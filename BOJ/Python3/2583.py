from collections import deque

m,n,k=map(int,input().split())
arr=[]
for i in range(k):
  arr.append(list(map(int,input().split())))
paper=[[0]*n for _ in range(m)]
cnt=0
for i in arr:           # 좌표로 이루어진 직사각형 그리기
  x1,y1,x2,y2=i
  for j in range(x1,x2):
    for k in range(y1,y2):
      paper[k][j]=1
visit=[[0]*n for _ in range(m)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(a,b):                 # 나머지 영역의 넓이를 반환하는 함수
  global visit
  queue=deque()
  queue.append((b,a))
  visit[b][a]=1
  area=1
  while queue:
    y,x=queue.popleft()
    for i in range(4):
      ny=dy[i]+y
      nx=dx[i]+x
      if ny>=m or ny<0 or nx>=n or nx<0:
        continue
      if visit[ny][nx]==0 and paper[ny][nx]==0:
        queue.append((ny,nx))
        visit[ny][nx]=1
        area+=1
  return area

area=[]
for i in range(m):
  for j in range(n):
    if visit[i][j]==0 and paper[i][j]==0:
      area.append(bfs(j,i))
print(len(area))
for i in sorted(area):
  print(i,end=' ')
