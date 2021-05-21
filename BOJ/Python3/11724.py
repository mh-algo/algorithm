from collections import deque
import sys

n,m=map(int,sys.stdin.readline().rsplit())
arr=[[] for x in range(n+1)]
for i in range(m):
  a,b=map(int,sys.stdin.readline().rsplit())
  arr[a].append(b)
  arr[b].append(a)
visit=[False]*(n+1)       # 방문 여부 기록을 위한 list

def bfs(x):
  queue=deque()
  queue.append(x)
  visit[x]=True
  while queue:
    t=queue.popleft()
    for i in arr[t]:
      if not visit[i]:
        queue.append(i)
        visit[i]=True
  return 1

count=0
for i in range(1,n+1):
  if not visit[i]:    # 방문 기록이 없는 경우에만 탐색 실행
    count+=bfs(i)
print(count)
