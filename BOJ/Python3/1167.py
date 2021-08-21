from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
# 트리 생성
tree={}
for _ in range(n):
	arr=list(map(int,input().split()))
	tree[arr[0]]=[]
	for i in range(1,len(arr),2):
		if arr[i]==-1:
			break
		tree[arr[0]].append((arr[i],arr[i+1]))

dist=[-1]*(n+1)    # 정점별로 거리를 저장하기 위한 배열
# 루트가 x인 트리에서 루트부터 정점까지의 거리를 구하는 함수
def dfs(x,length=0):
	for v,l in tree[x]:
		if dist[v]==-1:
			dist[v]=length+l
			dfs(v,length+l)

dist[1]=0    # 정점 거리 0으로 초기화
dfs(1)    # 루트가 1일 경우 각 정점까지의 거리를 구함

start=dist.index(max(dist))    # 루트에서 가장 멀리 있는 정점을 루트로 잡음
dist=[-1]*(n+1)    # 재탐색을 위해서 배열 초기화
dist[start]=0    # 정점 거리 0으로 초기화
dfs(start)    # 루트를 start로 잡고 재탐색

print(max(dist))

'''
풀이법
1. 루트에서 가장 먼 정점을 구한다.
2. 그 정점을 루트로 잡고 다시 가장 먼 정점을 구한다.
3. 이 때 구한 가장 먼 정점까지의 거리가 답이다.

증명 참조: https://koosaga.com/14
'''
