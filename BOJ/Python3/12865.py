n,k=map(int,input().split())
obj=[]
for _ in range(n):
	obj.append(tuple(map(int,input().split())))
obj.sort()

def max_value(arr):
	bag=[[0]*(k+1) for _ in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,k+1):
			w=arr[i-1][0]
			if w<=j:
				bag[i][j]=max(bag[i-1][j],bag[i-1][j-w]+arr[i-1][1])
			else:
				bag[i][j]=bag[i-1][j]
	return bag[n][k]

print(max_value(obj))


# 배낭 문제(knapsack problem)
# 아래 원리를 이용해서 해결
# https://cjwoov.tistory.com/57
