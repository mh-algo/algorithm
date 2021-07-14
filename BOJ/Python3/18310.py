n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[(n-1)//2])      # 값이 가장 작을 경우는 중앙값에 해당하는 집
