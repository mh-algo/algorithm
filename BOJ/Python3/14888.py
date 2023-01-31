import sys
from collections import deque
def calc(value, i, idx):
    v = value
    if i == 0:
        v += arr[idx]
    elif i == 1:
        v -= arr[idx]
    elif i == 2:
        v *= arr[idx]
    else:
        if v > 0:
            v //= arr[idx]
        else:
            v = -(abs(v) // arr[idx])
    return v

def bfs(arr, operator):
    max_value = -float('inf')
    min_value = float('inf')
    q = deque()
    for i in range(4):
        q.append((arr[0],operator[:], 1))
    while q:
        value, oper, idx = q.popleft()
        if idx == n:
            max_value = max(max_value, value)
            min_value = min(min_value, value)
        for i in range(4):
            if oper[i]:
                op = oper[:]
                op[i] -= 1
                v = calc(value, i, idx)
                q.append((v, op, idx+1))
    return max_value, min_value

input = sys.stdin.readline
n = int(input())
arr = [a for a in map(int, input().split())]
operator = list(map(int, input().split()))
max_value, min_value = bfs(arr, operator)
print(max_value)
print(min_value)