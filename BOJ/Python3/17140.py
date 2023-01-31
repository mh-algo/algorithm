import sys
from collections import Counter
def array_sort(arr, R, C):
    if R >= C:
        for i in range(R):
            arr_cnt = Counter(arr[i])
            if 0 in arr_cnt:        # 0인 경우 제거
                del arr_cnt[0]
            # 수의 개수와 수의 크기를 기준으로 정렬
            arr_cnt = sorted(arr_cnt.items(), key=lambda x: (x[1], x[0]))
            j = 0
            for a,b in arr_cnt:
                if j >= 50:     # 배열의 크기가 100을 넘어갈 경우
                    break
                arr[i][j*2], arr[i][j*2+1] = a, b   # 배열에 정렬된 값 저장
                j += 1
            C = max(C,j*2)      # 행 최대 길이 구하기
            if j < C:       # 배열에 값을 저장하고 나머지 부분들은 0으로 초기화
                for k in range(j*2,100):
                    arr[i][k] = 0
    else:
        for i in range(C):
            arr_cnt = Counter([arr[j][i] for j in range(R)])
            if 0 in arr_cnt:
                del arr_cnt[0]
            arr_cnt = sorted(arr_cnt.items(), key=lambda x: (x[1], x[0]))
            j = 0
            for a, b in arr_cnt:
                if j >= 50:
                    break
                arr[j*2][i], arr[j*2+1][i] = a, b
                j += 1
            R = max(R,j*2)
            if j < R:
                for k in range(j * 2, 100):
                    arr[k][i] = 0
    return arr, R, C

input = sys.stdin.readline
r,c,k = map(int, input().split())
arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(3):
    row = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = row[j]
find = False
R,C = 3,3
if arr[r-1][c-1] == k:
    print(0)
else:
    for i in range(100):
        arr,R,C = array_sort(arr,R,C)
        if arr[r-1][c-1] == k:
            find = True
            print(i+1)
            break
    if not find:
        print(-1)