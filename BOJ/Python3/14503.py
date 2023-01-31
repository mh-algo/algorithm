def move_robot(room, start):
    direct = [(-1,0), (0,1), (1,0), (0,-1)]
    r, c, d = start
    room[r][c] = -1
    chk = 0
    cnt = 1
    while True:
        d -= 1
        if d < 0:
            d = 3
        dr, dc = direct[d]
        nr, nc = r + dr, c + dc
        if room[nr][nc] == 0:
            r = nr
            c = nc
            room[nr][nc] = -1
            cnt += 1
            chk = 0
        else:
            chk += 1
            if chk == 4:
                back = d-2
                if d < 0:
                    back += 4
                br, bc = direct[back]
                nr, nc = r + br, c + bc
                if room[nr][nc] != 1:
                    r = nr
                    c = nc
                    chk = 0
                else:
                    return cnt

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
start = tuple(map(int, input().split()))
room = [[a for a in map(int,input().split())] for _ in range(n)]
print(move_robot(room, start))