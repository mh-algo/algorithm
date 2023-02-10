import sys
input = sys.stdin.readline
n,m = map(int,input().split())
poket = {input().strip():i+1 for i in range(n)}
poket_sort = sorted(poket.items(), key = lambda x:x[1])
for _ in range(m):
    p = input().strip()
    if poket.get(p):
        print(poket[p])
    else:
        print(poket_sort[int(p)-1][0])