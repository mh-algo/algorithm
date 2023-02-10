data = [(0,0),-1]
for i in range(9):
    for j, n in enumerate(map(int,input().split())):
        if n > data[1]:
            data[0] = (i+1,j+1)
            data[1] = n
print(data[1])
y,x = data[0]
print(y,x)