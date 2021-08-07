from collections import deque
import sys
input=sys.stdin.readline

tree={}
n=int(input())
for _ in range(n-1):
    key,child,weight=map(int,input().split())
    if key not in tree:
        tree[key]=[]
    tree[key].append((child,weight))
    if child==n:
        break

arr=[]
def bfs(key,weight=0):
	if key not in tree:           # 트리의 마지막 노드일 경우 0 반환
		return 0
	queue=deque()
	queue.append((-1,key,weight))
	max_weight=[0]*(len(tree[key]))
	while queue:
		n,k,w=queue.popleft()
		nn=n
    # 루트 노드를 기준으로 간선별로 가중치를 계산한다
		if k in tree:
			for nk,nw in tree[k]:
				if n==-1:           # n이 -1일 경우(루트 노드일 경우)
					nn+=1             # nn을 1 증가시킨다(간선별로 구분하기 위함)
				queue.append((nn,nk,w+nw))  # queue.append((간선 구분, 노드 번호, 누적 가중치))
				max_weight[nn]=max(max_weight[nn],w+nw) # 최대 누적 가중치를 저장한다
	max_weight.sort(reverse=True)
	if len(max_weight)>=2:    # 간선별로 저장된 최대 누적 가중치 중 가장 큰 2개를 더한다
		return max_weight[0]+max_weight[1]
	return max_weight[0]
	

ans=0
for i in range(1,n+1):
	ans=max(ans,bfs(i))
print(ans)



'''
python3로 채점하면 시간 초과가 뜬다.
이 방법보다 더 효율적인 방법으로 풀어야 할 듯 싶다.

효율적인 방법을 찾아본 결과 아래 방법대로 하면 쉽게 해결될 듯 싶다.
https://kyun2da.github.io/2021/05/04/tree's_diameter/
'''
