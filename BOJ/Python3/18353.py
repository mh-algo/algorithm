import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

d=[1]*n
for i in range(n):
	for j in range(i+1,n):
    # 앞쪽에 있는 숫자가 뒤쪽에 있는 숫자보다 큰 경우
		if arr[i]>arr[j]:
			d[j]=max(d[j],d[i]+1)
print(n-max(d))
