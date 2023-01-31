import copy
import sys

block = []
n = int(sys.stdin.readline())

for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))

direct = [0, 1, 2, 3]    # 왼쪽, 오른쪽, 위, 아래
max_block = 0    # 가장 큰 블록

def func(array, direction, cnt = 0):
    arr = copy.deepcopy(array)
    arr_tmp = [[0 for _ in range(n)] for _ in range(n)]
    check = [[0 for _ in range(n)] for _ in range(n)]
    max_value = 0

    for i in range(n):
        for j in range(n - 1):
            # 왼쪽으로 모든 숫자 밀기(숫자 합치기 x)
            if direction == 0:
                if arr[i][j] == 0:
                    for k in range(j+1, n):
                        if arr[i][k] != 0:
                            arr[i][k], arr[i][j] = arr[i][j], arr[i][k]
                            break

            # 위로 모든 숫자 밀기(숫자 합치기 x)
            elif direction == 2:
                if arr[j][i] == 0:
                    for k in range(j+1, n):
                        if arr[k][i] != 0:
                            arr[k][i], arr[j][i] = arr[j][i], arr[k][i]
                            break

        k = 0
        for j in range(n):
            # 왼쪽으로 모든 숫자 밀기(숫자 합치기 o)
            if direction == 0:
                if arr[i][j] != 0 and check[i][j] == 0:
                    if j + 1 < n and arr[i][j] == arr[i][j+1]:
                        check[i][j] = 1
                        check[i][j + 1] = 1
                        arr_tmp[i][k] = arr[i][j] + arr[i][j+1]
                    else:
                        check[i][j] = 1
                        arr_tmp[i][k] = arr[i][j]
                    max_value = max(max_value, arr_tmp[i][k])
                    k += 1

            # 위로 모든 숫자 밀기(숫자 합치기 o)
            elif direction == 2:
                if arr[j][i] != 0 and check[j][i] == 0:
                    if j + 1 < n and arr[j][i] == arr[j+1][i]:
                        check[j][i] = 1
                        check[j+1][i] = 1
                        arr_tmp[k][i] = arr[j][i] + arr[j+1][i]
                    else:
                        check[j][i] = 1
                        arr_tmp[k][i] = arr[j][i]
                    max_value = max(max_value, arr_tmp[k][i])
                    k += 1

    for i in range(n):
        for j in range(n-1, 0, -1):
            # 오른쪽으로 모든 숫자 밀기(숫자 합치기 x)
            if direction == 1:
                if arr[i][j] == 0:
                    for k in range(j-1, -1, -1):
                        if arr[i][k] != 0:
                            arr[i][k], arr[i][j] = arr[i][j], arr[i][k]
                            break

            # 아래로 모든 숫자 밀기(숫자 합치기 x)
            elif direction == 3:
                if arr[j][i] == 0:
                    for k in range(j-1, -1, -1):
                        if arr[k][i] != 0:
                            arr[k][i], arr[j][i] = arr[j][i], arr[k][i]
                            break

        k = n-1
        for j in range(n-1, -1, -1):
            # 오른쪽으로 모든 숫자 밀기(숫자 합치기 o)
            if direction == 1:
                if arr[i][j] != 0 and check[i][j] == 0:
                    if j - 1 >= 0 and arr[i][j] == arr[i][j-1]:
                        check[i][j] = 1
                        check[i][j-1] = 1
                        arr_tmp[i][k] = arr[i][j] + arr[i][j-1]
                    else:
                        check[i][j] = 1
                        arr_tmp[i][k] = arr[i][j]
                    max_value = max(max_value, arr_tmp[i][k])
                    k -= 1

            # 아래로 모든 숫자 밀기(숫자 합치기 o)
            elif direction == 3:
                if arr[j][i] != 0 and check[j][i] == 0:
                    if j - 1 >= 0 and arr[j][i] == arr[j-1][i]:
                        check[j][i] = 1
                        check[j-1][i] = 1
                        arr_tmp[k][i] = arr[j][i] + arr[j-1][i]
                    else:
                        check[j][i] = 1
                        arr_tmp[k][i] = arr[j][i]
                    max_value = max(max_value, arr_tmp[k][i])
                    k -= 1
    #print(arr)
    #print(arr_tmp)
    #print(max_value)
    cnt += 1
    #print(cnt)
    global max_block

    # 이동 횟수가 5일 경우 최댓값 갱신
    if cnt == 5:
        max_block = max(max_block, max_value)

    # 프루닝
    if max_value > max_block / pow(2, 5 - cnt):
        for d in direct:
            func(arr_tmp, d, cnt)

for d in direct:
    func(block, d)

print(max_block)