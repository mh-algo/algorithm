import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
	a,n=map(int,input().split())
	change=[]
	while a:
		change.append(a%n)    # 회문 여부만 조사할 것이므로 저장 순서는 신경쓰지 않았음
		a//=n
	if change[:]==change[::-1]:
		print(1)
	else: print(0)
