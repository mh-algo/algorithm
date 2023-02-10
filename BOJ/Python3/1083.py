import sys
input = sys.stdin.readline

def sort_func(arr, n, s):
    idx = 0
    while s > 0 and idx < n:
        idx_range = idx
        if idx+s < n:
            idx_range += s
        else:
            idx_range = n-1
        max_value = arr[idx]
        change_idx = 0
        for i in range(idx, idx_range+1):
            if max_value < arr[i]:
                max_value = arr[i]
                change_idx = i
        for i in range(change_idx, idx, -1):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            s -= 1
        idx += 1
    return arr

n = int(input())
arr = list(map(int,input().split()))
s = int(input())
for a in sort_func(arr,n,s):
    print(a,end=' ')