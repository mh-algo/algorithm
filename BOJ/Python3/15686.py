'''
치킨집을 가지고 dfs 돌리기
'''
min_value = float('inf')
def dfs(pick_chicken=[], idx=0, cnt=0):
    if cnt == m:
        global min_value
        value = 0
        for hy, hx in house:
            v = float('inf')
            for cy, cx in pick_chicken:
                v = min(v, abs(hy-cy) + abs(hx-cx))
            value += v
        min_value = min(min_value, value)
        return

    for i in range(idx, len(chicken)):
        pick_chicken.append(chicken[i])
        dfs(pick_chicken, i+1, cnt+1)
        pick_chicken.pop()

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
chicken = []
house = []
for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] == 2:
            chicken.append((i,j))
        elif city[j] == 1:
            house.append((i,j))
dfs()
print(min_value)