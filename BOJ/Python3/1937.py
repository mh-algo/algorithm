from collections import deque
import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
bamboo=[]
for _ in range(n):
  bamboo.append(list(map(int,input().split())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
visit=[[0]*n for _ in range(n)]

def dfs(x,y):
  if visit[x][y]:
    return visit[x][y]        # 이미 데이터가 있는 경우 반환
  visit[x][y]=1
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<n and 0<=ny<n:
      if bamboo[x][y]<bamboo[nx][ny]:
        visit[x][y]=max(visit[x][y],dfs(nx,ny)+1)
  return visit[x][y]

cnt=0
for i in range(n):
  for j in range(n):
    cnt=max(cnt,dfs(i,j))
print(cnt)
