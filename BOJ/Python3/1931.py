import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
  arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x:(x[1],x[0]))            # 회의가 먼저 끝나는 순으로 정렬, 같을 경우 먼저 시작하는 순으로 정렬
a,b=arr[0]
cnt=1
for x,y in arr[1:]:
  if b<=x:        # 현재 회의 끝나는 시간이랑 다음 회의 시작하는 시간이 겹치지 않을 경우(같을 경우는 회의 진행할 수 있다고 판단)
    cnt+=1
    a,b=x,y
print(cnt)
