import sys
def find_road(map_arr, n, l):
    road = 0
    for i in range(n):
        chk = [1]
        for j in range(1,n):
            if map_arr[i][j] == map_arr[i][j-1]:
                chk.append(chk[j-1]+1)
            elif map_arr[i][j]+1 == map_arr[i][j-1]:
                if chk[j-1] >= 0:
                    chk.append(-l+1)
                else:
                    break
            elif map_arr[i][j] == map_arr[i][j-1]+1:
                if chk[j-1] >= l:
                    chk.append(1)
                else:
                    break
            else:
                break
        if len(chk) == n and chk[-1] >= 0:
            road += 1
            #print(i)
            #print(map_arr[i])
            #print(chk)
    return road

input = sys.stdin.readline
n, l = map(int, input().split())
map_arr = [[a for a in map(int, input().split())] for _ in range(n)]
road = find_road(map_arr,n,l)
tmp = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        tmp[i].append(map_arr[j][i])
road += find_road(tmp,n,l)
print(road)