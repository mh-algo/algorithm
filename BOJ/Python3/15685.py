size = 101
def combine_dragon(board1, board2):
    return [list(map(lambda x: True if x[0] or x[1] else False, zip(board1[k], board2[k]))) for k in range(size)]

'''
드래곤 커브의 다음 세대 방향은 이전 세대 방향에 역순으로 1을 더한 값이다.
ex) d2 = [0,1,2,1]인 경우 d3 = [0,1,2,1, 2,3,2,1]  (여기서 dn은 direct의 index)
'''
def dragon_curve(start):
    direct = [(0,1), (-1,0), (0,-1), (1,0)]
    board = [[False for _ in range(size)] for _ in range(size)]
    x,y,d,g = start
    board[y][x] = True
    location = [d]
    dy, dx = direct[d]
    y += dy; x += dx
    board[y][x] = True
    for _ in range(g):
        for d in location[::-1]:
            d = (d+1)%4
            dy, dx = direct[d]
            y += dy; x += dx
            board[y][x] = True
            location.append(d)
    return board

def cnt_square(dragon_data):
    cnt = 0
    for i in range(size):
        for j in range(size):
            if dragon_data[i][j] and 0 <= i+1 < size and 0 <= j+1 < size:
                if dragon_data[i+1][j] and dragon_data[i][j+1] and dragon_data[i+1][j+1]:
                    cnt += 1
    return cnt

import sys
input = sys.stdin.readline
n = int(input())
info = [list(map(int,input().split())) for _ in range(n)]
dragon_data = [[False for _ in range(size)] for _ in range(size)]
for i in range(n):
    board = dragon_curve(info[i])
    dragon_data = combine_dragon(dragon_data, board)
print(cnt_square((dragon_data)))