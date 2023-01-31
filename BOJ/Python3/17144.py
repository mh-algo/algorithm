import sys
from collections import deque
d = [(0,1), (0,-1), (1,0), (-1,0)]
def spread_dust(room, air_cleaner):
    r, c = len(room), len(room[0])
    new_room = [deque([0 for _ in range(c)]) for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if room[y][x]:      # 먼지가 있는 경우
                cnt = 0
                for dy, dx in d:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < r and 0 <= nx < c:
                        if nx != 0 or ny not in air_cleaner:    # 공기 청정기 위치가 아닐 경우
                            new_room[ny][nx] += room[y][x]//5   # 먼지 확산
                            cnt += 1
                new_room[y][x] += room[y][x]-(room[y][x]//5)*cnt    # 먼지가 확산된 양만큼 감소
    return new_room

def rotation_air(room, air_cleaner):
    # 공기청정기 위쪽
    ty = air_cleaner[0]
    for i in range(ty-1,-1,-1):
        room[i][0] = room[i-1][0]
    room[0].popleft()
    room[0].append(0)
    for i in range(ty):
        room[i][-1] = room[i+1][-1]
    room[ty].pop()
    room[ty].appendleft(0)

    # 공기청정기 아랫쪽
    r = len(room)
    by = air_cleaner[1]
    for i in range(by+1,r-1):
        room[i][0] = room[i+1][0]
    room[-1].popleft()
    room[-1].append(0)
    for i in range(r-1,by,-1):
        room[i][-1] = room[i-1][-1]
    room[by].pop()
    room[by].appendleft(0)

    return room

def turn_on(room, air_cleaner,t):
    for _ in range(t):
        room = spread_dust(room, air_cleaner)
        room = rotation_air(room, air_cleaner)
    return room

def calc_dust(room):
    total_dust = 0
    for r in room:
        total_dust += sum(r)
    return total_dust

input = sys.stdin.readline
r, c, t = map(int,input().split())
room = []
air_cleaner = []
for i in range(r):
    room.append(deque(map(int,input().split())))
    for dust in room[i]:
        if dust == -1:
            air_cleaner.append(i)
            room[i][0] = 0
room = turn_on(room, air_cleaner,t)
print(calc_dust(room))