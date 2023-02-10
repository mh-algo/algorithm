import sys
input = sys.stdin.readline
m, n = map(int,input().split())
chk = [False, False] + [True for _ in range(n)]
for i in range(2,n+1):
    if chk[i]:
        if i >= m:
            print(i)
        for j in range(i*2,n+1,i):
            chk[j] = False