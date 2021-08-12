n=int(input())
arr=list(map(int,input().split()))
arr.sort()

def binary_search():
    start,end=0,n-1
    a,b=start,end
    mix=arr[start]+arr[end]
    while start<end:
        t=arr[start]+arr[end]
        if abs(mix)>abs(t):
            mix=t
            a,b=start,end
        if t<0:
            start+=1
        else:
            end-=1
    return arr[a],arr[b]

a,b=binary_search()
print(a,b)
