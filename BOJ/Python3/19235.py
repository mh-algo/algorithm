import sys
from collections import deque
block_type = [(0,), ((0,0),(0,0)), ((0,0), (0,1)), ((0,0), (1,0))]
row = 6; col = 4
# 블록을 보드에 놓을 경우
# (빨간색 보드를 기준으로 나온 블록의 좌표를 초록색/파란색 보드의 0행이나 1행의 좌표로 변경 후 진행)
def put_block(t, block, board):
    (ax,ay),(bx,by) = block     # 넘겨 받은 좌표는 (t1[0],y+t1[1]),(t2[0],y+t2[1]) (여기서 (t1,t2) = block_type[t])
                                # 위의 좌표는 초록색/파란색 보드의 0행이나 1행의 좌표로 변경된 후의 좌표
    # 블록이 쌓이게 되는 위치에 블록을 위치
    # 1x1 블록은 1, 1x2 블록은 2, 2x1 블록은 3과 -3으로 표시(2x1 블록의 경우 블록의 경계를 구별하기 위해 3,-3으로 표현)
    if t == 2:
        nax,nbx = ax,bx
        while nax+1 < row and nbx+1 < row and not board[nax+1][ay] and not board[nbx+1][by]:
            nax += 1; nbx += 1
        board[nax][ay], board[nbx][by] = 2, 2
    elif t == 3:
        nbx = bx
        while nbx+1 < row and not board[nbx+1][by]:
            nbx += 1
        board[nbx-1][by], board[nbx][by] = 3, -3
    else:
        nax = ax
        while nax+1 < row and not board[nax+1][ay]:
            nax += 1
        board[nax][ay] = 1

def fill_empty_area(board):
    # 더 이상 내려올 수 없을 때까지 반복 진행
    # 보드의 맨 아래부터 빈 공간이 있는지 확인 후 빈 공간이 존재하고 바로 위에 블록이 존재할 경우 블록을 한칸 내리는 방식으로 진행
    while True:
        move = False
        for i in range(row-1,0,-1):
            for j in range(col):
                # 보드에 빈 공간이 존재하고
                if board[i][j] == 0:
                    # 바로 위에 블록이 존재할 경우
                    if board[i-1][j] != 0:
                        # 블럭이 1x2가 아닌 경우
                        if board[i-1][j] != 2:
                            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                            move = True
                        else:
                            # 블럭이 1x2이고 1x2의 블록이 내려올 수 있는 경우
                            if j+1 < col and board[i][j+1] == 0 and board[i-1][j+1] == 2:
                                board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                                board[i][j+1], board[i-1][j+1] = board[i-1][j+1], board[i][j+1]
                                move = True
        # 더 이상 내려올 수 없을 경우
        if not move:
            break

# 행이 블록으로 채워졌을 경우 행 제거 진행
def del_line(board):
    score = 0
    # 더 이상 지워질 행이 존재하지 않을 때까지 반복 진행
    while True:
        chk = False
        for i in range(row):
            # 행이 블록으로 채워졌을 경우
            if 0 not in board[i]:
                for j in range(col):
                    # 행을 지웠을 때 2x1 블록이 지워질 경우 1x1 블록으로 변경
                    if board[i][j] == 3:
                        board[i+1][j] = 1
                    elif board[i][j] == -3:
                        board[i-1][j] = 1
                del board[i]
                board.appendleft([0,0,0,0])
                score += 1
                chk = True
        # 더 이상 지워질 행이 존재하지 않는 경우
        if not chk:
            return score
        fill_empty_area(board)  # 행을 지운 후 내려올 수 있는 블록 내리기

# 블록이 넘쳤을 경우 넘친 블록이 존재하는 열의 개수 반환
def chk_overflow(board):
    cnt = 0
    for i in range(2):
        if sum(board[i]) != 0:
            cnt += 1
    return cnt

# 블록이 넘쳤을 경우 넘친 열의 개수만큼 라인 제거
def overflow_del_line(board, cnt):
    for _ in range(cnt):
        for j in range(col):
            # 행을 지웠을 때 2x1 블록이 지워질 경우 1x1 블록으로 변경
            if board[-1][j] == -3:
                board[-2][j] = 1
        board.pop()
        board.appendleft([0,0,0,0])

# 초록색/파란색 보드
def color_board(block_info, board):
    t,x,y = block_info
    score = 0
    put_block(t, list(map(lambda x:(x[0],x[1]+y), block_type[t])), board)
    score += del_line(board)
    cnt = chk_overflow(board)
    if cnt:     # 블록이 넘쳤을 경우
        overflow_del_line(board, cnt)
    return score

# 블록의 좌표를 파란색 보드에 맞게 수정
def change_block_to_blue(block_info):
    t,x,y = block_info
    if t == 2:
        return (3,y,3-x)
    elif t == 3:
        return (2,y,3-x-1)
    else:
        return (t,y,3-x)

# 보드 안에 존재하는 블록 count
def count_block(board):
    return sum(1 if board[i][j] != 0 else 0 for i in range(row) for j in range(col))

def domino_game():
    green = deque([0 for _ in range(4)] for _ in range(6))
    blue = deque([0 for _ in range(4)] for _ in range(6))
    score = 0
    cnt = 0
    for block_info in block_list:
        score += color_board(block_info, green)
        block_info = change_block_to_blue(block_info)
        score += color_board(block_info, blue)
    cnt += count_block(green)
    cnt += count_block(blue)
    return score, cnt

input = sys.stdin.readline
n = int(input())
block_list = [list(map(int,input().split())) for _ in range(n)]
score, cnt = domino_game()
print(score)
print(cnt)