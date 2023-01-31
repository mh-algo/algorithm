import sys
def roll_dice(dice, order):
    move = [
        (0,1,2,3,4,5,6),        # 기존 주사위 눈
        (0,4,2,1,6,5,3),        # 동
        (0,3,2,6,1,5,4),        # 서
        (0,5,1,3,4,6,2),        # 북
        (0,2,6,3,4,1,5)         # 남
    ]
    tmp = [0 for _ in range(7)]
    for i in range(7):
        tmp[i] = dice[move[order][i]]
    return tmp

def map_func(board, order, start):
    x, y = start
    n, m = len(board), len(board[0])
    direct = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]  # 동, 서, 북, 남
    dice = [0 for _ in range(7)]
    for d in order:
        nx, ny = x + direct[d][0], y + direct[d][1]
        if 0 <= nx < n and 0 <= ny < m:
            dice = roll_dice(dice, d)
            x, y = nx, ny
            if board[x][y]:
                dice[6] = board[x][y]
                board[x][y] = 0
            else:
                board[x][y] = dice[6]
            print(dice[1])

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [[a for a in map(int, input().split())] for _ in range(n)]
order = list(map(int, input().split()))
map_func(board, order, (x,y))