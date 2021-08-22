import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[[0]*(n+1)]
for _ in range(n):
	arr.append([0]+list(map(int,input().split())))
dp=[[0]*(n+1) for _ in range(n+1)]

# 가로 구간 합
for i in range(1,n+1):
	for j in range(1,n+1):
		dp[i][j]=dp[i][j-1]+arr[i][j]

# 세로 구간 합
for j in range(1,n+1):
	for i in range(1,n+1):
		dp[i][j]+=dp[i-1][j]

for _ in range(m):
	x1,y1,x2,y2=map(int,input().split())
	print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]) # 배열의 총 합에서 구하지 않는 부분의 가로, 세로의 합을 빼고 중복으로 빼진 부분을 더해준다.
