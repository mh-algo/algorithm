import sys
input = sys.stdin.readline
t = int(input())
arr = [int(input()) for _ in range(t)]
size = max(arr)
chk = [False, False] + [True for _ in range(size)]
for i in range(2,size+1):
    if chk[i]:
        for j in range(i*2,size+1,i):
            chk[j] = False
for a in arr:
    for i in range(a//2,1,-1):
        if chk[i] and chk[a-i]:
            print(f'{i} {a-i}') if i < a-i else print(f'{a-i} {i}')
            break