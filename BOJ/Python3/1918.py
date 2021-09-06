from collections import deque
from string import ascii_uppercase

# 연산자 우선순위를 반환하는 함수
def priority(x):
	if x=='(':
		return 0
	elif x in '+-':
		return 1
	return 2

# 후위표기식을 print 하는 함수
def calc(arr):
	stack=deque()
	for x in arr:
    # x가 문자일 경우
		if x in ascii_uppercase:
			print(x,end='')
		else:
			if x=='(':
				stack.append(x)
      # x가 ')'일 경우 '('가 나올때까지 출력
			elif x==')':
				while 1:
					t=stack.pop()
					if t!='(':
						print(t,end='')
					else:
						break
      # x가 연산자일 경우
			else:
        # stack의 top에 위치한 연산자가 x보다 우선순위가 높을 경우 stack에서 pop한 후 출력
        # 작아질 경우 stack에 push
				while stack and priority(stack[-1])>=priority(x):
					print(stack.pop(),end='')
				stack.append(x)
  # stack에 남은 연산자들 출력
	while stack:
		print(stack.pop(),end='')

a=input()
calc(a)
