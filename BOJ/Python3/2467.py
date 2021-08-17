n=int(input())
arr=list(map(int,input().split()))
arr.sort()

def search():
	start,end=0,n-1
	zero_mix=float('inf')
	a,b=0,0
	while start<end:
		mix=arr[start]+arr[end]
    # 새로 섞은 용액이 0에 가까울 경우
		if abs(zero_mix)>abs(mix):
			zero_mix=mix
			a,b=arr[start],arr[end]
    # 새로 섞은 용액이 0보다 클 경우
		if mix>0:
			end-=1
    # 새로 섞은 용액이 0보다 작을 경우
		else:
			start+=1
	return a,b

a,b=search()
print(a,b)
