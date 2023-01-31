import sys
from collections import deque
def bfs(virus, road, size):
    direct = [(1,0),(-1,0),(0,1),(0,-1)]
    n, m = size
    road_set = set(road)
    q = deque()
    for v in virus:
        q.append(v)
    while q:
        y, x = q.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m:
                if (ny,nx) in road_set:
                    q.append((ny,nx))
                    road_set.remove((ny,nx))
    return len(road_set)

input = sys.stdin.readline
n, m = map(int, input().split())
virus = []
road = []
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        if row[j] == 2:
            virus.append((i,j))
        elif row[j] == 0:
            road.append((i,j))
max_value = 0
l = len(road)
road_set = set(road)
for i in range(l):
    road_set.remove(road[i])
    for j in range(i+1,l):
        road_set.remove(road[j])
        for k in range(j+1,l):
            road_set.remove(road[k])
            max_value = max(max_value, bfs(virus, road_set, (n,m)))
            road_set.add(road[k])
        road_set.add(road[j])
    road_set.add(road[i])
print(max_value)