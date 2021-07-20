from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
glass=[]          # 시험관
virus=[]          # 바이러스의 좌표를 저장할 list
for i in range(n):
	glass.append(list(map(int,input().split())))
	for j in range(n):
		if glass[i][j]:
			virus.append((glass[i][j],i,j))     # 바이러스가 존재할 경우 virus.append((바이러스 종류,x,y))
s,x,y=map(int,input().split())
virus.sort()        # 낮은 숫자의 바이러스가 먼저 오도록 정렬

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(q):
	queue=deque(q)      # 1초 동안 이동할 바이러스의 좌표를 담은 queue
	next_queue=deque()  # 이동한 바이러스의 좌표를 담을 queue
	while queue:
		v,x,y=queue.popleft()
		for i in range(4):
			nx=x+dx[i]
			ny=y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				if not glass[nx][ny]:
					glass[nx][ny]=glass[x][y]           # 시험관이 비었을 경우 증식
					next_queue.append((glass[nx][ny],nx,ny))    # 증식한 바이러스의 좌표를 queue에 저장
	return list(next_queue)

for _ in range(s):        # s번 반복
	virus=bfs(virus)
print(glass[x-1][y-1])
