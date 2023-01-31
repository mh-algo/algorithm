import sys
from collections import deque
def shark_hunt(sea, shark):
    d = [(0,1), (0,-1), (1,0), (-1,0)]
    n = len(sea)
    shark_size = 2
    eat_fish = 0
    sec = 0
    while True:
        y, x = shark
        sea[y][x] = 0
        chk = [[False for _ in range(n)] for _ in range(n)]
        q = deque()
        q.append((shark, 0))
        chk[y][x] = True
        fish = []
        while q:
            (y, x), cnt = q.popleft()
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if 0 <= ny < n and 0 <= nx < n:
                    if not chk[ny][nx] and sea[ny][nx] <= shark_size:
                        chk[ny][nx] = True
                        if sea[ny][nx] and sea[ny][nx] < shark_size:
                            if fish and fish[0][1] != cnt+1:
                                break
                            fish.append(((ny,nx), cnt+1))
                        q.append(((ny,nx), cnt+1))
        if not fish:
            return sec
        fish.sort()
        shark, cnt = fish[0]
        sec += cnt
        eat_fish += 1
        if eat_fish == shark_size:
            shark_size += 1
            eat_fish = 0

input = sys.stdin.readline
n = int(input())
sea = []
shark = tuple()
for i in range(n):
    sea.append(list(map(int,input().split())))
    for j in range(n):
        if sea[i][j] == 9:
            shark = (i,j)
print(shark_hunt(sea, shark))