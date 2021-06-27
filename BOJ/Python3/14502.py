from collections import deque
n,m=map(int,input().split())
arr=[]
virus=[]    # 바이러스가 위치하는 좌표가 저장될 list
wall=0      # 벽의 개수
for i in range(n):
  arr.append(list(map(int,input().split())))
  for j in range(m):
    if arr[i][j]==2:            # 바이러스가 존재할 경우 좌표를 tuple 형태로 list에 저장
      virus.append((i,j))
    if arr[i][j]==1:            # 벽이 존재하면 벽의 개수를 1 늘림
      wall+=1

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(a,b,c):                 # 벽을 세운뒤 증식한 바이러스의 개수를 반환할 함수
  ay,ax=a               # 새로 세울 3개의 벽의 위치
  by,bx=b
  cy,cx=c
  check=[[0]*m for _ in range(n)]        # 중복 탐색을 막기 위한 list
  virus_cnt=0
  queue=deque()
  for i,j in virus:               # 바이러스 위치를 queue에 저장
    queue.append((i,j))
    virus_cnt+=1
    check[i][j]=2
  if check[ay][ax]==2 or check[by][bx]==2 or check[cy][cx]==2:      # 벽을 세울 위치에 이미 바이러스가 존재할 경우 -1 반환
    return -1
  check[ay][ax]=1           # 새로 벽을 세운 위치 list에 저장
  check[by][bx]=1
  check[cy][cx]=1
  while queue:
    y,x=queue.pop()
    for i in range(4):
      ny=dy[i]+y
      nx=dx[i]+x
      if nx>=m or nx<0 or ny>=n or ny<0:          # 리스트의 범위를 벗어난 경우에 continue
        continue
      if check[ny][nx]==0 and arr[ny][nx]==0:     # 바이러스가 없고 벽이 없는 경우 탐색 계속
        virus_cnt+=1
        check[ny][nx]=2
        queue.append((ny,nx))
  return virus_cnt                # 총 증식한 바이러스 개수 반환

arr_size=n*m
max_size=0
seq_arr=[]

for i in range(n):              # 벽 3개를 세울 수 있는 모든 경우의 수를 list에 저장
  for j in range(m):
    seq_arr.append((i,j))

seq_size=len(seq_arr)

for i in range(seq_size):
  for j in range(i+1,seq_size):
    for k in range(j+1,seq_size):
      cnt=bfs(seq_arr[i],seq_arr[j],seq_arr[k])
      if cnt!=-1:           # 벽을 세울 수 있는 경우
        max_size=max(max_size,arr_size-wall-cnt-3)      # max(max_size, 총 배열 크기-벽의 개수-증식 완료한 바이러스 개수-새로 세운 벽 3개)
print(max_size)
