from collections import deque

r,c=map(int,input().split())
board=[]
for i in range(r):
  board.append(input())
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visit=[[set() for _ in range(c)] for _ in range(r)]      # 지나온 알파벳을 저장하기 위해 만든 list

def bfs(a=0,b=0):
  queue=deque()
  queue.append((a,b,board[0][0]))
  visit[0][0].add(board[0][0])
  cnt=1
  while queue:
    x,y,alpha=queue.popleft()    # 큐에 저장된 가로, 세로의 값과 지나갔던 알파벳들을 pop
    for i in range(4):
      ny=dy[i]+y
      nx=dx[i]+x
      if ny>=r or ny<0 or nx>=c or nx<0:
        continue
      tmp=alpha+board[ny][nx]
      if board[ny][nx] not in alpha and tmp not in visit[ny][nx]:    # 이미 지나간 알파벳이 아니거나 중복 탐색이 아닌 경우
        queue.append((nx,ny,tmp))
        visit[ny][nx].add(tmp)
        cnt=max(cnt,len(tmp))
  return cnt

print(bfs())
