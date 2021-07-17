import heapq
n=int(input())
card=[]
ans=0
for _ in range(n):
  heapq.heappush(card,int(input()))     # 가장 작은 두 카드를 합친 경우가 효율적이므로 우선순위 큐를 사용
while len(card)!=1:
  pair=0
  pair+=heapq.heappop(card)
  pair+=heapq.heappop(card)
  heapq.heappush(card,pair)
  ans+=pair
print(ans)
