import sys
input=sys.stdin.readline

t=int(input())
for _ in range(t):
	n=int(input())
	sticker=[]
	for _ in range(2):
		sticker.append(list(map(int,input().split())))
	dp=[[0]*n for _ in range(2)]
	for j in range(n):
		for i in range(2):
			if j==0:
				dp[i][j]=sticker[i][j]
				continue
			if i==0:
				dp[i][j]=max(dp[i][j-1],dp[i+1][j-1]+sticker[i][j])
			else:
				dp[i][j]=max(dp[i][j-1],dp[i-1][j-1]+sticker[i][j])
	print(max(dp[0][n-1],dp[1][n-1]))
