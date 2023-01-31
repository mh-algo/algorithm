import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for a in arr:
    a -= b
    cnt += 1
    if a > 0:
        cnt += a//c
        if a % c:
            cnt += 1
print(cnt)