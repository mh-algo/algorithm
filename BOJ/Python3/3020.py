import sys
input=sys.stdin.readline

n,h=map(int,input().split())
first,second=[0],[0]    # 배열의 index와 장애물의 개수를 맞추기 위해 [0]으로 초기화

for i in range(n):
    # 종유석일 경우
    if i%2:
        second.append(h-int(input()))   # 종유석은 거꾸로 달려있으므로 종유석이 없는 빈 공간을 저장하기 위해서 높이에서 뺌
    # 석순일 경우
    else:
        first.append(int(input()))

# 이분 탐색을 위해 정렬
first.sort()
second.sort()

# 이분 탐색 함수
# x보다 작은 길이의 개수를 반환하는 함수
def search(arr,x):
    start,end=0,n//2
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<x:
            start=mid+1
        elif arr[mid]>=x:
            end=mid-1
    return start-1

wall,cnt=n,1  # 장애물의 최솟값과 개수
for i in range(1,h+1):
    tmp=n//2-search(first,i)+search(second,i)  # 아래 추가 설명 참조
    # 장애물의 최솟값이 존재할 경우
    if wall>tmp:
        wall=tmp
        cnt=1
    # 장애물의 개수가 같은 경우
    elif wall==tmp:
        cnt+=1
print(wall,cnt)


### 추가 설명 ###
'''
    n//2-search(first,i)  -> 석순 개수
    search(second,i)-> 종유석 개수
    
    높이가 i일 경우 석순의 개수는 n//2의 값, 즉 석순의 총 개수에 i보다 작은 높이의 석순을 빼는 것이다.
    (석순의 총 개수) - (i보다 작은 높이의 석순) = (파괴하는 석순의 수)
    
    높이가 i일 경우 종유석의 개수는 종유석 아래의 빈 공간의 높이가 i보다 작은 경우의 개수이다.
    왜냐하면 빈 공간의 높이가 i보다 작은 경우는 반대로 말했을 경우 높이가 i 일 경우에는 종유석과 만난다는 뜻이기 때문이다.
'''
