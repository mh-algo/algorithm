import sys
input = sys.stdin.readline
direct = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]  # 위, 아래, 왼쪽, 오른쪽

def move_shark(sea, shark, shark_p):
    sea = [[(x,0) for x in sea[i]] for i in range(n)]   # 배열을 (x,0) 형태로 재구성
                                                        # (x,0)에서 x는 상어 번호, 0는 상어가 방문했을 때의 sec
    sec = 1
    while sec <= 1000:
        for i in range(1,m+1):
            if shark[i]:
                y, x, d = shark[i]
                priority = shark_p[i][d]    # 현재 바라보고 있는 방향에 해당하는 방향 우선순위
                my_smell = 0
                flag = False
                for p in priority:
                    dy, dx = direct[p]
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < n and 0 <= nx < n:
                        shark_n, s = sea[ny][nx]
                        if not my_smell and i == shark_n:   # 자신의 냄새가 존재하는 칸의 방향 저장
                            my_smell = p
                        if not shark_n or s-sec < -k:   # 칸이 비어있거나 냄새가 사라진 칸의 경우
                            shark[i] = (ny,nx,p)
                            flag = True
                            break

                # 상어 주변에 비어있는 칸이나 냄새가 사라진 칸이 없을 경우 자신의 냄새가 있는 칸으로 이동
                if not flag:
                    dy, dx = direct[my_smell]
                    ny, nx = y+dy, x+dx
                    shark[i] = (ny,nx,my_smell)

        # 이동한 상어의 정보를 sea에 반영
        for i, shark_data in enumerate(shark):
            if shark_data:
                y, x, d = shark_data
                _, s = sea[y][x]
                if s == sec:  # 낮은 번호를 가진 상어랑 같은 칸에 존재할 경우
                    shark[i] = tuple()  # 상어 정보 제거
                else:
                    sea[y][x] = (i,sec)

        # 남은 상어의 수가 1일 경우
        shark_cnt = len(list(filter(lambda x:len(x),shark)))
        if shark_cnt == 1:
            return sec
        sec += 1

    return -1

n, m, k = map(int,input().split())
sea = []
shark = [[] for _ in range(m+1)]    # index번째 상어의 정보를 (y좌표, x좌표, 방향) 형태로 저장
for i in range(n):
    sea.append(list(map(int,input().split())))
    for j in range(n):
        x = sea[i][j]
        if x:
            shark[x].append(i)
            shark[x].append(j)
for i, d in enumerate(map(int,input().split())):
    shark[i+1].append(d)
shark = list(map(tuple,shark))
shark_p = [[[]] for _ in range(m+1)]    # index번째 상어의 방향 우선순위 저장
for i in range(1,m+1):
    for _ in range(4):
        shark_p[i].append(list(map(int,input().split())))
print(move_shark(sea, shark, shark_p))