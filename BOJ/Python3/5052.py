import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	max_len=0
	for _ in range(n):
		arr.append(input().strip())
	arr.sort()
	chk=False
	for i in range(n-1):
		now_len=len(arr[i])
		if arr[i]==arr[i+1][:now_len]:      # 정렬하게 되면 arr[i]의 전화번호가 arr[i+1]의 전화번호의 앞에 위치한 번호이다.
			chk=True                          # ex. 정렬 전 [911,9762599,91125426] -> 정렬 후 [911,91125426,9762599]
			break
	if chk:
		print('NO')
	else:
		print('YES')

'''
Trie로 풀 수 있다고 하니 공부 후 추가할 예정
참고: https://alpyrithm.tistory.com/72
'''
