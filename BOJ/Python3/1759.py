from itertools import combinations
import sys
input=sys.stdin.readline
l,c=map(int,input().split())
arr=input().split()
arr.sort()
combi=list(combinations(arr,l))
alpha='aeiou'
for s in combi:
	cnt=0
	for a in s:
		if a in alpha:          # 모음 개수 count
			cnt+=1
	if cnt>=1 and l-cnt>=2:       # 모음이 1개 이상이고, 자음이 2개 이상인 경우
		print(''.join(s))
