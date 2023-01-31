import sys
from collections import deque
def find_same_num(circle):
    circle_avg = 0  # 원판 평균
    delete_num = set()  # 인접하면서 수가 같은 경우의 원판 좌표를 담는 set
    for i in range(n):
        for j in range(m):
            circle_avg += circle[i][j]
            tmp = circle[i][j]
            if tmp:
                for dy, dx in direct:   # (i,j)에서 인접하는 수 비교
                    ny, nx = i+dy, j+dx
                    if ny >= 0 and nx < m:
                        if tmp == circle[ny][nx]:   # 인접한 수가 같은 경우
                            delete_num.add((i,j))
                            delete_num.add((ny,nx))
    # 인접하면서 수가 같은 경우를 모두 제거
    for y,x in delete_num:
        circle[y][x] = 0
    # 인접하면서 수가 같은 경우가 존재하지 않을 경우
    if not delete_num:
        # 원판에 0을 제외한 모든 수의 개수
        cnt_num = sum(len(list(filter(lambda x: x != 0, circle[i]))) for i in range(n))
        if cnt_num:
            circle_avg /= cnt_num
        for i in range(n):
            for j in range(m):
                if circle[i][j] > 0:    # 평균보다 클 경우
                    if circle[i][j] > circle_avg:
                        circle[i][j] -= 1
                    elif circle[i][j] < circle_avg:     # 평균보다 작을 경우
                        circle[i][j] += 1
    return circle

def rotation(circle, info):
    for x,d,k in info:
        tmp = x
        # x의 배수의 원판을 k만큼 돌리기
        while tmp <= n:
            if d:
                circle[tmp-1].rotate(-k)
            else:
                circle[tmp-1].rotate(k)
            tmp += x
        circle = find_same_num(circle)
    return sum(sum(filter(lambda x:x>0,circle[i])) for i in range(n))

input = sys.stdin.readline
n,m,t = map(int,input().split())
circle = [deque(map(int,input().split())) for _ in range(n)]
info = [tuple(map(int,input().split())) for _ in range(t)]
direct = [(0,-1), (0,1), (-1,0)]
print(rotation(circle, info))