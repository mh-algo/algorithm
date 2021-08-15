# LCS 풀이 
a=input()
b=input()
c=input()
dp=[[[0]*(len(a)+1) for _ in range(len(b)+1)] for _ in range(len(c)+1)]
for i in range(1,len(c)+1):
	for j in range(1,len(b)+1):
		for k in range(1,len(a)+1):
			if c[i-1]==b[j-1] and c[i-1]==a[k-1]:
				dp[i][j][k]=dp[i-1][j-1][k-1]+1
			else:
				dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[len(c)][len(b)][len(a)])
