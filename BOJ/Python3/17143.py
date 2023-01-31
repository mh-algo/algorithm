def eating_shark(shark, r,c,s,d,z):
    # 같은 좌표에 상어가 존재하지 않을 경우
    if (r,c) not in shark:
        shark[(r,c)] = (s,d,z)
    # 같은 좌표에 상어가 존재할 경우
    else:
        # 크기가 큰 상어를 저장
        if shark[(r,c)][2] < z:
            shark[(r,c)] = (s,d,z)
    return shark

def move_shark(shark):
    new_shark = dict()
    for (r,c),(s,d,z) in shark.items():
        direction = direct[d]
        # 상어가 이동하지 않는 경우
        if not s:
            new_shark = eating_shark(new_shark, r, c, s, d, z)
        s_tmp = s
        while s_tmp:
            # 상어가 상하로 이동
            if d <= 2:
                if 1 <= r+s_tmp*direction <= R:
                    r += s_tmp*direction
                    s_tmp = 0
                else:
                    # 위
                    if direction < 0:
                        s_tmp += 1-r
                        r = 1
                        direction = 1
                    # 아래
                    else:
                        s_tmp -= R-r
                        r = R
                        direction = -1
                # 상어의 이동이 종료 되었을 경우
                if s_tmp == 0:
                    # 상어가 물의 최상단에 존재할 경우 위를 바라보도록 변경
                    if r == 1:
                        direction = -1
                    # 상어가 물의 최하단에 존재할 경우 아래를 바라보도록 변경
                    elif r == R:
                        direction = 1
                    # 상어가 위를 바라볼 경우
                    if direction < 0:
                        d = 1
                    # 상어가 아래를 바라볼 경우
                    else:
                        d = 2
                    new_shark = eating_shark(new_shark, r, c, s, d, z)
            # 상어가 좌우로 이동
            else:
                if 1 <= c+s_tmp*direction <= C:
                    c += s_tmp*direction
                    s_tmp = 0
                else:
                    # 왼쪽
                    if direction < 0:
                        s_tmp += 1-c
                        c = 1
                        direction = 1
                    # 오른쪽
                    else:
                        s_tmp -= C-c
                        c = C
                        direction = -1
                    # 상어의 이동이 종료 되었을 경우
                if s_tmp == 0:
                    # 상어가 물의 최좌측에 존재할 경우 왼쪽을 바라보도록 변경
                    if c == 1:
                        direction = -1
                    # 상어가 물의 최우측에 존재할 경우 오른쪽을 바라보도록 변경
                    elif c == C:
                        direction = 1
                    # 상어가 왼쪽을 바라볼 경우
                    if direction < 0:
                        d = 4
                    # 상어가 오른쪽을 바라볼 경우
                    else:
                        d = 3
                    new_shark = eating_shark(new_shark, r, c, s, d, z)
    return new_shark

def fishing(shark, fishing_man):
    fishing_man += 1
    # 낚시꾼과 같은 열에 존재하는 상어 리스트
    shark_exist = list(filter(lambda x: x[1] == fishing_man, shark.keys()))
    # 상어가 존재하지 않은 경우
    if not shark_exist:
        return shark, 0
    shark_exist.sort()      # 열 번호가 가장 낮은 상어 순으로 정렬
    catch_shark = shark_exist[0]
    shark_size = shark[catch_shark][2]
    del shark[catch_shark]      # 잡은 상어 제거
    return shark, shark_size

import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
shark = {(r,c):(s,d,z) for r,c,s,d,z in list(map(int, input().split()) for _ in range(M))}
direct = [0,-1,1,1,-1]
catch_shark = 0
for i in range(C):
    shark, shark_size= fishing(shark, i)
    catch_shark += shark_size
    shark = move_shark(shark)
print(catch_shark)
