# 모든 자리의 숫자 합이 3의 배수일 경우 3의 배수이므로
# 뒷자리가 0이고 모든 자리의 숫자 합이 3의 배수이면 30의 배수이다.
n=list(map(int,list(input())))
n.sort(reverse=True)
t=0
if n[-1]!=0:
	print(-1)
else:
	for i in n:
		t+=i
	if t%3==0:
		for x in n:
			print(x,end='')
	else: print(-1)
