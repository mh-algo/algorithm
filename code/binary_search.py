# 이진 탐색
# 찾는 숫자가 존재할 경우 1 반환, 그렇지 않은 경우 0 반환하는 함수
def binary_search(arr,x):
	start,end=0,len(arr)-1
	while start<=end:
		mid=(start+end)//2
    # 찾으려는 값이 더 큰 경우
		if arr[mid]<x:
			start=mid+1
    # 찾으려는 값이 더 작은 경우
		elif arr[mid]>x:
			end=mid-1
    # 찾으려는 값이 존재할 경우
		else:
			return 1
  # 찾으려는 값이 존재하지 않을 경우
	return 0
