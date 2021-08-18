n,m=map(int,input().split())
arr=list(map(int,input().split()))

def binary_search():
    start,end=max(arr),sum(arr)
    ret=0
    while start<=end:
        mid=(start+end)//2
        lesson=0
        cnt=0
        # lesson의 값이 mid보다 작은 최대의 값이 될 경우 cnt+=1
        for x in arr:
            lesson+=x
            if lesson>mid:
                lesson=x
                cnt+=1
        # cnt가 m보다 작을 경우(mid가 클 수록 cnt의 값이 작으므로 범위의 값을 줄이기 위해 end=mid-1)
        if cnt<m:
            end=mid-1
        # cnt가 m보다 크거나 같을 경우(mid가 작을 수록 cnt의 값이 크므로 범위의 값을 늘리기 위해 start=mid+1)
        else:
            start=mid+1
    return start

print(binary_search())
