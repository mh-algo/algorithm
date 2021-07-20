import sys

input=sys.stdin.readline
n=int(input())
m=int(input())
bus=[[float('inf')]*(n+1) for _ in range(n+1)]
for _ in range(m):
	a,b,cost=map(int,input().split())
	bus[a][b]=min(bus[a][b],cost)
for k in range(1,n+1):
	bus[k][k]=0
	for a in range(1,n+1):
		for b in range(1,n+1):
			bus[a][b]=min(bus[a][b],bus[a][k]+bus[k][b])
for arr in bus[1:]:
	for x in arr[1:]:
		if x==float('inf'):
			print(0,end=' ')
		else: print(x,end=' ')
	print()
