import sys
input = sys.stdin.readline
direct = [(0,0), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
size = 4
max_value = 0
def move_fish(fish_location,sea,shark):
    for a in sorted(fish_location.keys()):
        y,x = fish_location[a]
        if sea[y][x] == 0:
            print(sea)
            print(fish_location)
        print(sea[y][x],y,x)
        b = sea[y][x][1]
        for i in range(8):
            b += i
            if b > 8:
                b = 1
            dy, dx = direct[b]
            ny, nx = y + dy, x + dx
            if 0 <= ny < size and 0 <= nx < size and sea[ny][nx] != shark:
                if sea[ny][nx]:
                    other_fish = sea[ny][nx][0]
                    sea[y][x][1] = b
                    sea[y][x], sea[ny][nx] = sea[ny][nx], sea[y][x]
                    fish_location[a], fish_location[other_fish] = fish_location[other_fish], fish_location[a]
                    break
                else:
                    sea[y][x][1] = b
                    sea[y][x], sea[ny][nx] = sea[ny][nx], sea[y][x]
                    fish_location[a] = (ny, nx)
                    break

def move_shark(fish_location,sea,y=0,x=0,value=0):
    if not value:
        print('#####################')
        value += sea[y][x][0]
        del fish_location[sea[y][x][0]]
        sea[y][x][0] = -1
    shark = sea[y][x]
    #print(sea)
    move_fish(fish_location,sea,shark)

    b = shark[1]
    dy, dx = direct[b]
    flag = False
    sea[y][x] = [0,0]
    #print(sea)
    for i in range(1,4):
        ny, nx = y+dy*i, x+dx*i
        if 0 <= ny < size and 0 <= nx < size and sea[ny][nx]!=[0,0]:
            new_sea = [[r[:] for r in row] for row in sea]
            new_fish_location = dict(fish_location)
            fish_num = new_sea[ny][nx][0]
            del new_fish_location[fish_num]
            new_sea[ny][nx][0] = -1
            move_shark(new_fish_location,new_sea,ny,nx,value+fish_num)
            flag = True
    if not flag:
        global max_value
        max_value = max(max_value, value)

sea = [[] for _ in range(4)]
fish_location = dict()
for i in range(4):
    row = list(map(int,input().split()))
    for j in range(0,8,2):
        sea[i].append([row[j],row[j+1]])
        fish_location[row[j]] = (i,j//2)
move_shark(fish_location,sea)
print(max_value)