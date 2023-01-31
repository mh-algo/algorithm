import sys
sys.setrecursionlimit(10**6)

def dfs(tree, check, w, n=1):
    check[n] = True
    children = [next_node for next_node in tree[n] if not check[next_node]]
    not_pick, pick = 0, w[n]
    for child in children:
        child_not_pick, child_pick = dfs(tree, check, w, child)
        not_pick += max(child_not_pick, child_pick)
        pick += child_not_pick
    return not_pick, pick

n = int(sys.stdin.readline())
w = [0] + list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
print(max(dfs(tree, check, w)))