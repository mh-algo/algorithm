def count_population(area, s_area):
    p = [0 for _ in range(5)]
    for r in range(1,n+1):
        for c in range(1,n+1):
            p[s_area[r][c]-1] += area[r][c]
    return p

def split_area(area,x,y,d1,d2):
    s_area = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # 좌측 상단, 우측 하단 경계선
    for i in range(d1+1):
        s_area[x+i][y-i] = 5
        s_area[x+d2+i][y+d2-i] = 5
    # 좌측 하단, 우측 상단 경계선
    for i in range(d2+1):
        s_area[x+i][y+i] = 5
        s_area[x+d1+i][y-d1+i] = 5
    # 경계선 내부 채우기
    for r in range(1,n+1):
        row = s_area[r]
        try:
            for c in range(list.index(row,5)+1,n-list.index(row[::-1],5)):
                s_area[r][c] = 5
        except:
            pass
    # 나머지 구간 채우기
    for r in range(1,n+1):
        for c in range(1,n+1):
            if not s_area[r][c]:
                if 1 <= r < x+d1 and 1 <= c <= y:
                    s_area[r][c] = 1
                elif 1 <= r <= x+d2 and y < c <= n:
                    s_area[r][c] = 2
                elif x+d1 <= r <= n and 1 <= c < y-d1+d2:
                    s_area[r][c] = 3
                elif x+d2 < r <= n and y-d1+d2 <= c <= n:
                    s_area[r][c] = 4
    p = count_population(area, s_area)
    return max(p)-min(p)

import sys
input = sys.stdin.readline
n = int(input())
area = [[0 for _ in range(n+1)]]
for _ in range(n):
    area.append([0]+list(map(int, input().split())))
min_p = float('inf')
for x in range(1,n+1):
    for y in range(1,n+1):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                if x+d1+d2 <= n and y-d1 >= 1 and y+d2 <= n:
                    min_p = min(min_p, split_area(area,x,y,d1,d2))
print(min_p)