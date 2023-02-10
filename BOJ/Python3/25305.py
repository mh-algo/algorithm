import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = list(map(int,input().split()))
print(sorted(arr)[-k])