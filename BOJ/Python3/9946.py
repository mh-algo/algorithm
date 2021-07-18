import sys
input=sys.stdin.readline
s1,s2='',''
cnt=0
while 1:
  cnt+=1
  s1=input()
  s2=input()
  A=ord('A')
  z=ord('z')
  arr1=[0 for _ in range(A,z+1)]    # A부터 z까지의 배열 생성
  arr2=[0 for _ in range(A,z+1)]
  if s1=='END\n' and s2=='END\n':
    break
  for i in s1:      # 알파벳의 개수를 배열에 저장
    arr1[ord(i)-A]+=1
  for i in s2:
    arr2[ord(i)-A]+=1
  print('Case {0}: '.format(cnt),end='')
  if arr1==arr2:      # 저장된 배열이 같을 경우 제대로 회수함
    print('same')
  else: print('different')    # 다를 경우 회수 실패
