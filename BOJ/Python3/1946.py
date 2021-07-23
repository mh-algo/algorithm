import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	for _ in range(n):
		arr.append(tuple(map(int,input().split())))
	arr.sort()        # 서류 심사 순위대로 정렬
	cnt=0
	b=100001
	for i in range(n):
		if b>arr[i][1]:     # 면접 순위가 높을 경우 변수에 대입
			b=arr[i][1]       # 서류 심사 순위대로 정렬되어있으므로 면접 순위가 변수 b보다 낮을 경우 뽑히지 못한다
			cnt+=1
	print(cnt)
