def execute_ladder(ladder, size):
    n, h = size
    for j in range(1,n+1):
        locate = j
        for i in range(1,h+1):
            if (i,locate) in ladder:
                l, r = ladder[(i,locate)]
                if l:
                    locate -= l
                if r:
                    locate += r
        if locate != j:
            return -1

def ret_cnt(ladder, size):
    n, h = size
    min_cnt = float('inf')
    if execute_ladder(ladder, size) != -1:
        return 0
    for i in range(1,h+1):
        for j in range(1,n):
            if (i,j) not in ladder and (i,j+1) not in ladder:
                ladder[(i,j)] = [0,1]
                ladder[(i,j+1)] = [1,0]
                if execute_ladder(ladder, size) != -1:
                    min_cnt = 1
                for k in range(i,h+1):
                    for l in range(1,n):
                        if (k,l) not in ladder and (k,l+1) not in ladder:
                            ladder[(k,l)] = [0,1]
                            ladder[(k,l+1)] = [1,0]
                            if execute_ladder(ladder, size) != -1:
                                min_cnt = min(min_cnt,2)
                            for a in range(k,h+1):
                                for b in range(1,n):
                                    if (a,b) not in ladder and (a,b+1) not in ladder:
                                        ladder[(a,b)] = [0,1]
                                        ladder[(a,b+1)] = [1,0]
                                        if execute_ladder(ladder, size) != -1:
                                            min_cnt = min(min_cnt, 3)
                                        del ladder[(a,b)]
                                        del ladder[(a,b+1)]
                            del ladder[(k,l)]
                            del ladder[(k,l+1)]
                del ladder[(i,j)]
                del ladder[(i,j+1)]

    if min_cnt > 3:
        return -1
    return min_cnt

import sys
input = sys.stdin.readline
n, m, h = map(int, input().split())
ladder = dict()
for _ in range(m):
    a, b = map(int, input().split())
    ladder[(a,b)] = [0,1]
    ladder[(a,b+1)] = [1,0]
print(ret_cnt(ladder, (n,h)))