import sys
input=sys.stdin.readline
a=input().strip()
b=input().strip()
d=[[0]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1,len(a)+1):
	for j in range(1,len(b)+1):
    # 두 문자열의 알파벳이 일치할 경우
		if a[i-1]==b[j-1]:
			d[i][j]=d[i-1][j-1]+1       # 이전 알파벳에 저장된 값 + 1
    # 두 문자열의 알파벳이 일치하지 않을 경우
		else:
			d[i][j]=max(d[i-1][j],d[i][j-1])  # 이전에 저장된 값들 중 가장 큰 값을 저장
print(d[len(a)][len(b)])


'''
최종적으로 저장된 배열 d의 모습은 아래와 같다

      C A P C A K
   ______________
  │ 0 0 0 0 0 0 0 
A │ 0 0 1 1 1 1 1 
C │ 0 1 1 1 2 2 2 
A │ 0 1 2 2 2 3 3 
Y │ 0 1 2 2 2 3 3 
K │ 0 1 2 2 2 3 4 
P │ 0 1 2 3 3 3 4 



LCS 알고리즘에 대한 정보
https://ko.wikipedia.org/wiki/최장_공통_부분_수열
'''
