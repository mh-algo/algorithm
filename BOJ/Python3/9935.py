s=input()
w=input()
stack=[]
for a in s:
	stack.append(a)
	if a==w[-1]:              # 단어의 끝과 알파벳이 같은 경우
		if ''.join(stack[-len(w):])==w:   # 단어가 같을 경우
			del stack[-len(w):]     # 단어 제거
if stack:
	print(''.join(stack))
else:
	print('FRULA')
