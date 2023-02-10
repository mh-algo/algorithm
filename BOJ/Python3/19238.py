import sys
from collections import deque
input = sys.stdin.readline
direct = [(-1,0), (0,-1), (0,1), (1,0)]

def bfs(start, dest, road):
    visit = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append(start)
    y, x = start
    visit[y-1][x-1] = 0
    arrive = []
    if (y,x) in dest:   # 출발지와 도착지가 같은 경우
        dest.remove(start)
        return start, 0
    while q:
        y,x = q.popleft()
        for dy, dx in direct:
            ny, nx = y+dy, x+dx
            if 0 <= ny-1 < n and 0 <= nx-1 < n:
                if not road[ny-1][nx-1] and not visit[ny-1][nx-1] != -1:    # 벽이 없고 아직 방문하지 않은 경우
                    visit[ny-1][nx-1] = visit[y-1][x-1] + 1
                    if (ny,nx) in dest:     # 방문한 곳이 목적지에 해당할 경우
                        cnt = visit[ny-1][nx-1]
                        arrive.append((cnt,(ny,nx)))
                    q.append((ny,nx))
    if arrive:  # 최단거리, 행 번호, 열 번호 순으로 정렬
        cnt, taxi = sorted(arrive)[0]
        dest.remove(taxi)
        return taxi, cnt
    return -1,-1

def start_taxi(gas, road, taxi, people, dest):
    while people:   # 모든 승객을 이동시킬때까지 반복
        taxi, cnt = bfs(taxi, people, road)     # 택시 -> 사람
        gas -= cnt
        if cnt < 0 or gas < 0:  # 방문할 수 없는 장소거나 도중에 연료가 바닥날 경우
            return -1
        taxi, cnt = bfs(taxi, {dest[taxi]}, road)   # 사람 -> 목적지
        gas -= cnt
        if cnt < 0 or gas < 0:
            return -1
        gas += cnt*2
    return gas

n,m,gas = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(n)]
taxi = tuple(map(int,input().split()))
people = set()
dest = dict()
for i in range(m):
    py, px, dy, dx = map(int, input().split())
    people.add((py, px))
    dest[(py, px)] = (dy, dx)
print(start_taxi(gas, road, taxi, people, dest))