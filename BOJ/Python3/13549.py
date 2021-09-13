from collections import deque

n,k=map(int,input().split())

dx=[-1,1,2]
def search(n):
	queue=deque()
	queue.append(n)
	visit=[float('inf')]*100001    # 최솟값을 저장하는 배열
	visit[n]=0
	while queue:
		x=queue.popleft()
		for i in range(3):
      # 걷는 경우
			if i<2:
				nx=x+dx[i]
      # 순간 이동 하는 경우
			else:
				nx=x*dx[i]
			if nx>=0 and nx<=100000:
        # 이동하는데 1초가 경과되는 경우
				if i<2:
					if visit[nx]>visit[x]+1:
						visit[nx]=visit[x]+1
						queue.append(nx)
        # 이동하는데 0초가 경과되는 경우
				else:
					if visit[nx]>visit[x]:
						visit[nx]=visit[x]
						queue.append(nx)
	return visit[k]

print(search(n))
