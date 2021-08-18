import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

dict={}
for x in a:
	if x not in dict:
		dict[x]=1
	else:
		dict[x]+=1

for x in b:
	if x not in dict:
		print(0,end=' ')
	else:
		print(dict[x],end=' ')
