max_value = 0
log = []
def game(user, location=set(), i=0):
    if i == 10:
        global max_value
        max_value = max(max_value, sum(map(lambda x:x[2],user)))
        return
    for j in range(4):
        y,x,score = user[j]
        if y == -1 and x == -1:
            continue
        ny, nx = y, x+dice[i]
        tmp = user[j]
        if nx < len(board[ny]):
            # 중복루트 처리
            if board[ny][nx] == 40:
                if (0,20) in location or (1,7) in location or (3,7) in location or (2,6) in location:
                    return
            if ny > 0:
                if board[ny][nx] == 25:
                    if (1,4) in location or (3,4) in location or (2,3) in location:
                        return
                elif board[ny][nx] == 30:
                    if (1,5) in location or (3,5) in location or (2,4) in location:
                        return
                elif board[ny][nx] == 35:
                    if (1,6) in location or (3,6) in location or (2,5) in location:
                        return
            if y == 0 and nx % 5 == 0 and nx != 20:     # 파란색 화살표를 따라 진입할 경우
                ny, nx = nx//5, 0
            if (ny,nx) not in location:
                if (y,x) != (0,0):
                    location.remove((y,x))
                location.add((ny, nx))
                user[j] = (ny, nx, score+board[ny][nx])
                log.append((i,user[j]))
                game(user, location, i+1)
                location.add((y, x))
                location.remove((ny, nx))
                log.pop()
                user[j] = tmp
        # 도착지점에 도착
        else:
            if (y,x) != (0,0):
                location.remove((y, x))
            user[j]= (-1, -1, score)
            log.append((i,user[j]))
            game(user, location, i+1)
            location.add((y, x))
            log.pop()
            user[j] = tmp

import sys
dice = list(map(int,sys.stdin.readline().split()))
board = [
    [i*2 for i in range(21)],
    [10,13,16,19,25,30,35,40],
    [20,22,24,25,30,35,40],
    [30,28,27,26,25,30,35,40]
]
user = [(0,0,0) for _ in range(4)]
visit = [[False for _ in range(len(board[i]))] for i in range(len(board))]
game(user)
print(max_value)