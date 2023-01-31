import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [[a for a in map(int, input().split())] for _ in range(n)]
team = list(combinations(range(n),n//2))
value_dict = dict()
for t in team:
    value = 0
    for i in range(n//2):
        for j in range(i+1,n//2):
            a, b = t[i], t[j]
            value += arr[a][b]
            value += arr[b][a]
    value_dict[t] = value
min_result = float('inf')
tmp = [i for i in range(n)]
for t1, v in value_dict.items():
    t2 = tuple(filter(lambda x: x not in t1, tmp))
    min_result = min(min_result, abs(value_dict[t1]-value_dict[t2]))
print(min_result)