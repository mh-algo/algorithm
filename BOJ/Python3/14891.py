import sys
from collections import deque
def rotation_func(state, rotation):
    for n, d in rotation:
        chk = [False for _ in range(4)]
        q = deque()
        q.append((n-1, d))
        chk[n-1] = True
        while q:
            num, direct = q.pop()
            # 오른쪽
            if num + 1 < 4 and not chk[num+1] and state[num][2] != state[num+1][-2]:
                chk[num+1] = True
                q.append((num+1, -direct))
            # 왼쪽
            if num - 1 >= 0 and not chk[num-1] and state[num][-2] != state[num-1][2]:
                chk[num-1] = True
                q.append((num-1, -direct))
            # 회전
            if direct == 1:
                tmp = state[num].pop()
                state[num].appendleft(tmp)
            else:
                tmp = state[num].popleft()
                state[num].append(tmp)

input = sys.stdin.readline
state = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
rotation = [tuple(map(int, input().split())) for _ in range(k)]
rotation_func(state, rotation)
score = 0
for i in range(4):
    score += state[i][0]*2**i
print(score)