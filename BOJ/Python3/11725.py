from collections import deque
import sys

input=sys.stdin.readline
n=int(input())
arr={i:set() for i in range(1,n+1)}
for _ in range(n-1):
  a,b=map(int,input().split())
  arr[a].add(b)
  arr[b].add(a)

def bfs(start):
  visit=[0 for _ in range(n+1)]
  queue=deque()
  queue.append(start)
  visit[start]=1
  while queue:
    a=queue.popleft()
    for x in arr[a]:
      if not visit[x]:
        queue.append(x)
        visit[x]=a        # 방문 후 부모 노드의 번호를 저장
  return visit

ans=bfs(1)
for i in ans[2:]:
  print(i)
