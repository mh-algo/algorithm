n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
arr=[]
def solve(x=0,cnt=0):
	if cnt==m:
		for x in arr:
			print(x,end=' ')
		print()
		return
	for i in range(0,n):
		if a[i] not in arr:
			arr.append(a[i])
			solve(i+1,cnt+1)
			arr.pop()
solve()
