import sys
from collections import deque
direct = [(0,1), (0,-1), (1,0), (-1,0)]
def bfs(y,x):
    q = deque()
    chk[y][x] = True
    q.append((y,x))
    share = [(y,x)]
    population = country[y][x]
    while q:
        y, x = q.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n:
                if not chk[ny][nx] and l <= abs(country[ny][nx]-country[y][x]) <= r:
                    chk[ny][nx] = True
                    population += country[ny][nx]
                    share.append((ny,nx))
                    q.append((ny,nx))
    if len(share) > 1:
        for y, x in share:
            tmp[y][x] = population // len(share)
        return 1
    else:
        return 0

input = sys.stdin.readline
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    tmp = [row[:] for row in country]
    chk = [[False for _ in range(n)] for _ in range(n)]
    loop = 0
    for i in range(n):
        for j in range(n):
            ret = bfs(i,j)
            loop = max(loop,ret)
    country = tmp
    if not loop:
        print(cnt)
        break
    cnt += 1