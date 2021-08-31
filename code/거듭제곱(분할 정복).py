# boj 1629 참고

# a^b 계산
def power(a,b):
	if b==1:
		return a
	else:
		x=power(a,b//2)
		if b%2==0:
			return x*x
		else:
			return x*x*a

a,b=map(int,input().split())
print(power(a,b))


'''
a^100을 분할 정복을 이용하여 구하면 아래와 같다.

a^100=a^50*a^50
a^50=a^25*a^25
a^25=a^12*a^12*a
a^12=a^6*a^6
a^6=a^3*a^3
a^3=a*a*a

그냥 구할 경우 100번의 연산이 필요하지만
분할 정복을 이용하여 구하면 6번의 연산으로 구할 수 있다.
'''
