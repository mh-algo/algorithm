import sys
sound = sys.stdin.readline().strip()
ducks = []
sample = 'quack'
for c in sound:
    flag = False
    for i, duck in enumerate(ducks):
        if c == sample[len(duck)]:
            duck.append(c)
            if len(duck) == len(sample):
                ducks[i] = []
            flag = True
            break
    if not flag:
        ducks.append([c])
print(-1) if len(list(filter(lambda x:len(x)>0, ducks))) else print(len(ducks))