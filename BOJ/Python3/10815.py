import sys
input=sys.stdin.readline
n=int(input())
card1=set(map(int,input().split()))
m=int(input())
card2=list(map(int,input().split()))
for c in card2:
  chk=0
  if c in card1:
    chk=1
  print(chk,end=' ')
