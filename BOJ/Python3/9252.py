# 기존 LCS 알고리즘에 문자열 저장 기능 추가
a=input()
b=input()
dp=[[(0,'')]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
	for j in range(1,len(b)+1):
    # 문자가 같을 경우 길이와 문자를 더해준다
		if a[i-1]==b[j-1]:
			dp[i][j]=(dp[i-1][j-1][0]+1,dp[i-1][j-1][1]+a[i-1])
    # 다를 경우 값이 더 큰 경우를 대입한다
		else:
			if dp[i-1][j][0]>dp[i][j-1][0]:
				dp[i][j]=dp[i-1][j]
			else:
				dp[i][j]=dp[i][j-1]
for x in dp[len(a)][len(b)]:
	print(x)
