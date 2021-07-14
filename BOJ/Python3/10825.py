import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for _ in range(n):
  student=input().split()
  kor,eng,math=map(int,student[1:])
  arr.append((kor,eng,math,student[0]))
arr.sort(key=lambda x:(-x[0],x[1],-x[2],x[3]))
for x in arr:
  print(x[3])
