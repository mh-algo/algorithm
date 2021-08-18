n,m=map(int,input().split())

arr=[]
def solve(x,cnt=0):
	if cnt==m:
		for x in arr:
			print(x,end=' ')
		print()
	for i in range(x,n+1):
		arr.append(i)
		solve(i+1,cnt+1)
		arr.pop()
solve(1)
