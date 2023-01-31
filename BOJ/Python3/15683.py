import sys
direct = [(-1,0), (0,1), (1,0), (0,-1)]
cctv_direct = [
    [(0,),(1,),(2,),(3,)],
    [(1,3),(0,2)],
    [(0,1),(1,2),(2,3),(3,0)],
    [(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
    [(0,1,2,3)]
]
min_area = float('inf')
def office_check(office, size, y, x, d):
    n, m = size
    ny, nx = y + direct[d][0], x + direct[d][1]
    while 0 <= ny < n and 0 <= nx < m:
        if office[ny][nx] != 6:
            if office[ny][nx] == 0:
                office[ny][nx] = '#'
            ny += direct[d][0]
            nx += direct[d][1]
        else:
            break

def dfs(office, cctv, size, idx=0):
    if idx == len(cctv):
        global min_area
        cnt = 0
        for row in office:
            cnt += row.count(0)
        min_area = min(min_area, cnt)
        return
    y,x = cctv[idx]
    cctv_n = office[y][x]
    for cctv_d in cctv_direct[cctv_n-1]:
        tmp = [row[:] for row in office]
        for d in cctv_d:
            office_check(tmp, size, y, x, d)
        dfs(tmp, cctv, size, idx+1)

input = sys.stdin.readline
n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if 0 < office[i][j] < 6:
            cctv.append((i,j))
dfs(office, cctv, (n,m))
print(min_area)