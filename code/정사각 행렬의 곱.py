# 정사각 행렬의 곱
# a,b는 행렬을 저장한 배열
def square_matrix_mul(a,b):
	size=len(a)
	arr=[[0]*size for _ in range(size)]
	for i in range(size):
		for j in range(size):
			for k in range(size):
				arr[i][j]+=a[i][k]*b[k][j]
	return arr
