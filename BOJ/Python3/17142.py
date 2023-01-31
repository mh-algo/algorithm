import sys
from collections import deque
d = [(0,1), (0,-1), (1,0), (-1,0)]
min_time = float('inf')
def complete(time, chk):
    t = -1
    for i in range(n):
        for j in range(n):
            if laboratory[i][j] != 1:
                if not chk[i][j]:
                    return -1
                else:
                    t = max(t, time[i][j])
    return t

def spread_virus(pick_virus):
    time = [[0 for _ in range(n)] for _ in range(n)]
    chk = [[False for _ in range(n)] for _ in range(n)]
    q = deque(zip(pick_virus,[0 for _ in range(m)]))
    for y,x in pick_virus:
        chk[y][x] = True
    while q:
        (y,x),sec = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n:
                if laboratory[ny][nx] != 1 and not chk[ny][nx]:
                    chk[ny][nx] = True
                    if laboratory[ny][nx] != 2:
                        time[ny][nx] = sec+1
                    q.append(((ny,nx),sec+1))
    global min_time
    t = complete(time, chk)
    if t != -1:
        min_time = min(min_time, t)

def put_virus(pick_virus=[],idx=0,cnt=0):
    if cnt == m:
        spread_virus(pick_virus)
    else:
        for i in range(idx,len(virus)):
            pick_virus.append(virus[i])
            put_virus(pick_virus,i+1,cnt+1)
            pick_virus.pop()

input = sys.stdin.readline
n, m = map(int,input().split())
laboratory = []
virus = []
for i in range(n):
    laboratory.append(list(map(int,input().split())))
    for j in range(n):
        if laboratory[i][j] == 2:
            virus.append((i,j))
put_virus()
if min_time == float('inf'):
    min_time = -1
print(min_time)