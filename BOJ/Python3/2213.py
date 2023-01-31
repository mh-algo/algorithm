import sys

def dfs(tree, check, w, dp, n=1):
    check[n] = True
    children = [next_node for next_node in tree[n] if not check[next_node]]
    not_pick, pick = 0, w[n]

    if not children:
        dp[n][0], dp[n][1] = not_pick, pick
    else:
        for child in children:
            dfs(tree, check, w, dp, child)
            child_not_pick, child_pick = dp[child][0], dp[child][1]
            not_pick += max(child_not_pick, child_pick)
            pick += child_not_pick
        dp[n][0], dp[n][1] = not_pick, pick

def trail(tree, check, pick_arr, pick_chk, n=1):
    check[n] = True
    children = [next_node for next_node in tree[n] if not check[next_node]]
    if pick_chk:
        pick_arr.append(n)
    for child in children:
        child_not_pick, child_pick = dp[child][0], dp[child][1]
        # pick o
        if pick_chk:
            trail(tree, check, pick_arr, 0, child)
        # pick x
        else:
            if child_not_pick < child_pick:
                trail(tree, check, pick_arr, 1, child)
            else:
                trail(tree, check, pick_arr, 0, child)

n = int(sys.stdin.readline())
w = [0] + list(map(int, sys.stdin.readline().split()))

tree = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]
dp = [[0,0] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(tree, check, w, dp)

check = [False for _ in range(n+1)]
pick_arr = []
pick_chk = 0
if dp[1][0] < dp[1][1]:
    pick_chk = 1
trail(tree, check, pick_arr, pick_chk)

print(max(dp[1]))
pick_arr.sort()
for i in pick_arr:
    print(i, end=' ')