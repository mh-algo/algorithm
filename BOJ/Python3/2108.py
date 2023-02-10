import sys
input = sys.stdin.readline
n = int(input())
arr = []
cnt = dict()
for _ in range(n):
    a = int(input())
    arr.append(a)
    if cnt.get(a):
        cnt[a] += 1
    else:
        cnt[a] = 1
arr.sort()
print(round(sum(arr)/n))
print(arr[n//2])
tmp = sorted(list(cnt.items()), key = lambda x: (-x[1],x[0]))
if n > 1 and tmp[0][1] == tmp[1][1]:
    print(tmp[1][0])
else:
    print(tmp[0][0])
print(abs(arr[0]-arr[-1]))