import sys

def dfs(tree, check, n=1):
    check[n] = True
    children = [next_node for next_node in tree[n] if not check[next_node]]
    not_pick, pick = 0, 1
    for child in children:
        child_not_pick, child_pick = dfs(tree, check, child)
        not_pick += child_pick
        pick += min(child_not_pick, child_pick)
    return not_pick, pick

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

print(min(dfs(tree, check)))