import sys
from collections import deque
#from pprint import pprint
def move(n, apple, rotation):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1     # 뱀의 머리
    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # 오른쪽, 아래, 왼쪽, 위
    head = tail = (0,0)
    idx = 0
    while True:
        #pprint(board)
        y, x = head
        if rotation and board[y][x] == rotation[0][0] + 1:
            sec, c = rotation.popleft()
            if c == 'D':    # 오른쪽
                idx += 1
                if idx > 3:
                    idx = 0
            else:   # 왼쪽
                idx -= 1
                if idx < 0:
                    idx = 3

        ny, nx = y + direct[idx][0], x + direct[idx][1]
        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] > 0:       # 몸과 부딫힐 경우
                return board[y][x]
            board[ny][nx] = board[y][x] + 1      # 뱀의 꼬리에서 머리까지 숫자 1씩 증가
            head = (ny, nx)
            if (ny+1,nx+1) in apple:        # 사과가 존재할 경우
                apple.remove((ny+1,nx+1))
            else:   # 사과가 없는 경우
                ty, tx = tail
                for dy, dx in direct:
                    nty, ntx = ty + dy, tx + dx
                    if 0 <= nty < n and 0 <= ntx < n:
                        if board[nty][ntx] == board[ty][tx] + 1:    # 꼬리와 이어져 있는 몸통 찾기
                            tail = (nty, ntx)
                            board[ty][tx] = 0   # 꼬리 제거
                            break
        else:       # 벽과 부딫힐 경우
            return board[y][x]


input = sys.stdin.readline
n = int(input())
k = int(input())
apple = set()
for _ in range(k):
    apple.add(tuple(map(int,input().split())))
l = int(input())
rotation = deque()
for _ in range(l):
    x,c = input().split()
    rotation.append((int(x),c))

print(move(n, apple, rotation))
