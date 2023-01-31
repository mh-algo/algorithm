import sys
input = sys.stdin.readline
n = int(input())
arr = [[a for a in map(int, input().split())] for _ in range(n)]
tmp = [0 for _ in range(n+1)]
for i in range(n-1,-1,-1):
    t, p = arr[i]
    tmp[i] = tmp[i+1]
    if i+t <= n:
        tmp[i] = max(tmp[i], tmp[i+t]+p)
print(tmp[0])