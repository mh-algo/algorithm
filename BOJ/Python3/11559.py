from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(field,visit,a,b):
  queue=deque()
  queue.append((a,b))
  visit[a][b]=1
  cnt=1
  color=field[a][b]
  puyo=[(a,b)]
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=dx[i]+x
      ny=dy[i]+y
      if nx<0 or nx>=6 or ny<0 or ny>=12:
        continue
      if visit[nx][ny]==0 and color==field[nx][ny]:     # 방문하지 않고, 색이 같을 경우
        visit[nx][ny]=1
        cnt+=1
        puyo.append((nx,ny))
        queue.append((nx,ny))
  if cnt>=4:      # 같은 색이 4개 이상 붙어있을 경우
    return puyo
  return -1

field=[['.' for _ in range(12)] for _ in range(6)]        # 뿌요뿌요 필드를 오른쪽으로 90도 돌린 형태로 배열에 저장
for i in range(11,-1,-1):
  line=input()
  for j in range(6):
    if line[j]!='.':
      field[j][i]=line[j]
cnt=0
while True:
  puyo=[]     # 사라진 뿌요들을 담을 list
  visit=[[0 for _ in range(12)] for _ in range(6)]
  for i in range(12):
    for j in range(6):
      if field[j][i]!='.' and visit[j][i]==0:     # 필드에 뿌요가 있고, 방문하지 않은 경우
        remove_puyo=bfs(field,visit,j,i)
        if remove_puyo!=-1:
          for k in remove_puyo:     # 사라진 뿌요들을 puyo에 넣음
            puyo.append(k)
  if puyo!=[]:
    puyo.sort(reverse=True)       # 맨 뒤의 배열에서부터 지워나가기 위해 정렬
    for x,y in puyo:
      del field[x][y]             # 사라진 뿌요를 지우고 필드에 .을 채워줌
      field[x].append('.')
    cnt+=1
  else: break     # 더 이상 사라질 뿌요가 없는 경우 break
print(cnt)
