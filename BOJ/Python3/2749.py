n=int(input())
p=1000000

# 정사각 행렬의 곱
def square_matrix_mul(a,b):
	size=len(a)
	arr=[[0]*size for _ in range(size)]
	for i in range(size):
		for j in range(size):
			for k in range(size):
				arr[i][j]+=a[i][k]*b[k][j]
			arr[i][j]%=p
	return arr

def matrix_pow(arr,n):
	if n==1:
		return arr
	else:
		tmp=matrix_pow(arr,n//2)
		mul=square_matrix_mul(tmp,tmp)
		if n%2==0:
			return mul
		else:
			return square_matrix_mul(mul,arr)

def fibo(n):
	arr=[[1,1],[1,0]]
	if n==0:
		return 0
	ret=matrix_pow(arr,n)
	return ret[0][1]

print(fibo(n))
