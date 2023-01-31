import sys

max_block = 0
def board_rotation(board, n):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[i][j] = board[j][n-1-i]
    return tmp

def board_up(board, n):
    tmp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        flag = 0; target = -1
        for i in range(n):
            if board[i][j] != 0:
                if flag == 1 and tmp[target][j] == board[i][j]:
                    tmp[target][j] *= 2
                    flag = 0
                else:
                    flag = 1; target += 1
                    tmp[target][j] = board[i][j]

        for i in range(target+1, n):
            tmp[i][j] = 0

    return tmp

def max_block_calc(board, n):
    global max_block
    for b in board:
        max_block = max(max_block, max(b))

def dfs(board, n, cnt=0):
    if cnt == 5:
        return
    else:
        tmp = board
        for _ in range(4):
            tmp = board_rotation(tmp, n)
            move_board = board_up(tmp, n)
            max_block_calc(move_board, n)
            dfs(move_board, n, cnt+1)

n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))

dfs(board, n)
print(max_block)