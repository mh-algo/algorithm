def grow_tree(ground, tree, k):
    new_tree = dict()
    dead_tree = dict()
    for (y,x,age),cnt in sorted(tree.items(), key=lambda x:x[0][2]):        # 나이를 기준으로 오름차순 정렬
        g = ground[y-1][x-1] + add_ground[y-1][x-1]*k   # 땅에 있는 양분의 양
        # 최소 나무 한 그루가 먹을 양분이 존재
        if g >= age:
            # 모든 나무가 양분을 섭취
            if g // age >= cnt:
                ground[y-1][x-1] -= age*cnt     # 섭취한 양분을 제거
                age += 1
                if (y,x,age) in new_tree:
                    new_tree[(y,x,age)] += cnt
                else:
                    new_tree[(y,x,age)] = cnt
            # 일부 나무만 양분을 섭취
            else:
                ground[y-1][x-1] -= (g // age) * age        # 섭취한 양분을 제거
                # 양분을 먹지 못해 죽은 나무
                if (y,x,age) in dead_tree:
                    dead_tree[(y,x,age)] += cnt - g // age
                else:
                    dead_tree[(y,x,age)] = cnt - g // age
                cnt = g // age
                age += 1
                # 양분을 먹은 일부 나무
                if (y,x,age) in new_tree:
                    new_tree[(y,x,age)] += cnt
                else:
                    new_tree[(y,x,age)] = cnt
            # 나무가 번식
            if age % 5 == 0:
                for dy, dx in direct:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny-1 < n and 0 <= nx-1 < n:
                        if (ny,nx,1) in new_tree:
                            new_tree[(ny,nx,1)] += cnt
                        else:
                            new_tree[(ny,nx,1)] = cnt
        # 한 그루도 양분을 못먹음
        else:
            if (y,x,age) in dead_tree:
                dead_tree[(y,x,age)] += cnt
            else:
                dead_tree[(y,x,age)] = cnt
    for (y,x,age),cnt in dead_tree.items():
        ground[y-1][x-1] += (age//2) * cnt
    return new_tree, ground

import sys
input = sys.stdin.readline
direct = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
n, m, k = map(int, input().split())
ground = [[5 for _ in range(n)] for _ in range(n)]
add_ground = [list(map(int,input().split())) for _ in range(n)]
tree = {tuple(map(int,input().split())):1 for _ in range(m)}
for i in range(k):
    tree, ground = grow_tree(ground, tree, i)
print(sum(tree.values()))