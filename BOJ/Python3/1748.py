n=input()
num=int(n)
ans=0
for i in range(len(n)):
  p=pow(10,i)*9
  if num-p<0:
    ans+=num*(i+1)
  else: ans+=p*(i+1)
  num-=p
print(ans)
