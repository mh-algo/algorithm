n = int(input())
t = 0
find = False
for i in range(1,n):
    if i % 10 == 0:
        t = eval(str(i)+'+'+'+'.join(str(i)))
        if t == n:
            print(i)
            find = True
            break
    else:
        t += 2
        if t == n:
            print(i)
            find = True
            break
if not find:
    print(0)