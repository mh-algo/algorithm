n,k=map(int,input().split())    # n = 물건 개수, k = 가방에 넣을 수 있는 최대 무게
obj=[]
# (물건 무게, 가치)를 obj에 append
for _ in range(n):
	obj.append(tuple(map(int,input().split())))

def knapsack_problem(arr):
	bag=[[0]*(k+1) for _ in range(n+1)]
	for i in range(1,n+1):
		for j in range(1,k+1):
			w=arr[i-1][0]    # 물건의 무게
			v=arr[i-1][1]    # 물건의 가치
			if w<=j:
				bag[i][j]=max(bag[i-1][j],bag[i-1][j-w]+v)
			else:
				bag[i][j]=bag[i-1][j]
	return bag[n][k]

print(knapsack_problem(obj))

'''
n=4, k=7 이고 
obj=[(3,6),(4,8),(5,12),(6,13)] 일 경우

              물건 무게
            │  0 1 2 3 4 5 6 7
          __│__________________________
물건 종류  0 │  0  0  0  0  0  0  0  0
          1 │  0  0  0  6  6  6  6  6
          2 │  0  0  0  6  8  8  8  14
          3 │  0  0  0  6  8  12 12 14
          4 │  0  0  0  6  8  12 13 14
          
배열 bag은 위와 같다
'''
