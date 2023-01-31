import sys
from collections import deque

def move(board, y, x, dy, dx):
    cnt = 0
    while board[y+dy][x+dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        cnt += 1
    return y, x, cnt

def bfs(board, r, b, n, m):
    d = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque()
    q.append((r,b,0))
    visit = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
    while q:
        (ry,rx), (by,bx), cnt = q.popleft()
        if cnt + 1 > 10:
            return -1
        for dy, dx in d:
            nry, nrx, rcnt = move(board, ry, rx, dy, dx)
            nby, nbx, bcnt = move(board, by, bx, dy, dx)
            if board[nby][nbx] != 'O':
                if board[nry][nrx] == 'O':
                    return cnt + 1
                if nry == nby and nrx == nbx:
                    if rcnt > bcnt:
                        nry -= dy
                        nrx -= dx
                    if rcnt < bcnt:
                        nby -= dy
                        nbx -= dx
                if not visit[nry][nrx][nby][nbx]:
                    visit[nry][nrx][nby][nbx] = True
                    q.append(((nry,nrx), (nby,nbx),cnt+1))
    return -1

n, m = map(int, sys.stdin.readline().split())
board = []
r, b = tuple(), tuple()

for i in range(n):
    board.append((' '.join(sys.stdin.readline())).split())
    for j in range(m):
        if board[i][j] == 'R':
            r = (i,j)
        if board[i][j] == 'B':
            b = (i,j)

print(bfs(board,r,b,n,m))