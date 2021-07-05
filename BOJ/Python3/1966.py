from collections import deque

test=int(input())
for _ in range(test):
  n,m=map(int,input().split())
  tmp=list(map(int,input().split()))
  queue=deque()
  for i in range(len(tmp)):       # 일반 문서일 경우=(tmp[i],0), 찾고자 하는 문서일 경우=(tmp[i],1)
    if i==m:
      queue.append((tmp[i],1))
    else: queue.append((tmp[i],0))
  cnt=0
  max_a,max_b=max(queue)
  while queue:
    a,b=queue.popleft()
    if max_a==a:      # a가 queue에서 최댓값일 경우
      cnt+=1
      if b==1:        # a가 최댓값이고 찾고자 하는 문서일 경우
        break
      max_a,max_b=max(queue)   # 최댓값보다 작은 수일 경우 queue에 다시 push
    else: queue.append((a,b))
  print(cnt)
