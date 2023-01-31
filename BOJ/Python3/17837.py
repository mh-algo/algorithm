import sys
from collections import deque
direct = [tuple(), (0,1), (0,-1), (-1,0), (1,0)]
def white_red_block(i):
    tmp = deque()       # 다음칸으로 옮길 체스말들
    num = -1
    y, x, d = chess_pieces[i]
    dy, dx = direct[d]
    ny, nx = y + dy, x + dx
    while num != i:     # i번 체스말이 나올때까지 반복(i번 체스말과 그 위에 쌓인 체스말들 옮기기)
        num = board_state[y-1][x-1].pop()
        # 하얀색(정순)
        if board[ny-1][nx-1] == 0:
            tmp.appendleft(num)
        # 빨간색(역순)
        else:
            tmp.append(num)
        num_y, num_x, num_d = chess_pieces[num]
        chess_pieces[num] = (ny, nx, num_d)     # 체스말의 좌표를 옮겨질 위치로 제지정
    board_state[ny-1][nx-1].extend(list(tmp))   # 옮겨진 체스말 위치 업데이트

def blue_block(i):
    tmp = deque()
    num = -1
    y, x, d = chess_pieces[i]
    # 반대 방향으로 변경
    if d == 1 or d == 3:
        chess_pieces[i] = (y,x,d+1)
    else:
        chess_pieces[i] = (y,x,d-1)
    y, x, d = chess_pieces[i]
    dy, dx = direct[d]
    ny, nx = y + dy, x + dx
    # 체스판을 벗어나거나 이동할 칸이 파란색 칸이 아닐 경우 체스말 옮김
    if 0 <= ny-1 < n and 0 <= nx-1 < n and board[ny-1][nx-1] != 2:
        while num != i:     # i번 체스말이 나올때까지 반복(i번 체스말과 그 위에 쌓인 체스말들 옮기기)
            num = board_state[y-1][x-1].pop()
            # 다음에 이동할 칸이 빨간색
            if board[ny-1][nx-1] == 1:
                tmp.append(num)
            # 다음에 이동할 칸이 하얀색
            else:
                tmp.appendleft(num)
            num_y, num_x, num_d = chess_pieces[num]
            chess_pieces[num] = (ny,nx,num_d)       # 체스말의 좌표를 옮겨질 위치로 제지정
        board_state[ny-1][nx-1].extend(list(tmp))   # 옮겨진 체스말 위치 업데이트

def move_pieces(chess_pieces, board_state):
    for i in range(k):
        y,x,d = chess_pieces[i]
        dy, dx = direct[d]
        ny, nx = y+dy, x+dx
        # 체스판을 벗어나지 않을 경우
        if 0 <= ny-1 < n and 0 <= nx-1 < n:
            if board[ny-1][nx-1] == 2:
                blue_block(i)
            else:
                white_red_block(i)
        # 체스판을 벗어날 경우
        else:
            blue_block(i)
        if complete(board_state):
            return True
    return False

def complete(board_state):
    for row in board_state:
        for col in row:
            if len(col) >= 4:
                return True
    return False

input = sys.stdin.readline
n, k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]  # 체스판 블록 정보
chess_pieces = []   # 체스말의 좌표를 체스 번호순으로 저장
board_state = [[deque() for _ in range(n)] for _ in range(n)]   # 체스판에 놓여진 말 표시(체스말의 좌표에 쌓여진 순으로 체스말의 번호를 저장)
for i in range(k):
    chess_pieces.append(tuple(map(int,input().split())))
    y,x,d = chess_pieces[-1]
    board_state[y-1][x-1].append(i)
success = False
for i in range(1000):
    if move_pieces(chess_pieces, board_state):
        success = True
        print(i+1)
        break
if not success:
    print(-1)