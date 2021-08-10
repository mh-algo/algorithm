n=int(input())
arr=list(map(int,input().split()))
ans_arr=[]

# 이분 탐색 함수 사용
# 배열에서 target 다음으로 작은 수의 index를 반환하는 함수
def binary_search(arr,target):
	start,end=0,len(arr)-1
	while start<=end:
		mid=(start+end)//2
		if arr[mid]<target:
			start=mid+1
		else:
			end=mid-1
	return start

for x in arr:
  # 배열이 비어있거나 배열의 마지막 숫자보다 x가 작은 경우
	if not ans_arr or ans_arr[-1]<x:
		ans_arr.append(x)
  # 마지막 숫자보다 x가 클 경우
  # 배열 내에 x 다음으로 작은 수가 위치한 index에 x 대입
	else:
		ans_arr[binary_search(ans_arr,x)]=x
print(n-len(ans_arr))
