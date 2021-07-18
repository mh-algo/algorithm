import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))
arr.sort(reverse=True)          # 버틸 수 있는 최대 중량 순으로 정렬
weigh=[arr[x]*(x+1) for x in range(n)]    # 정렬 후 x번째 배열에 위치한 로프는 로프 x+1개를 사용해 무게를 나눌 경우가 가장 효율적이다
print(max(weigh))
