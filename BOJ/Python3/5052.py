import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	max_len=0
	for _ in range(n):
		arr.append(input().strip())
	arr.sort()
	chk=False
	for i in range(n-1):
		now_len=len(arr[i])
		if arr[i]==arr[i+1][:now_len]:      # 정렬하게 되면 arr[i]의 전화번호가 arr[i+1]의 전화번호의 앞에 위치한 번호이다.
			chk=True                          # ex. 정렬 전 [911,9762599,91125426] -> 정렬 후 [911,91125426,9762599]
			break
	if chk:
		print('NO')
	else:
		print('YES')

		
		
'''
아래는 Trie로 푼 경우
'''

import sys
input=sys.stdin.readline

class Node:
	def __init__(self,key,data=None):
		self.key=key
		self.data=data
		self.children={}

class Trie:
	def __init__(self):
		self.head=Node(None)
		
	def insert(self,string):
		curr_node=self.head
		for s in string:
			if s not in curr_node.children:
				curr_node.children[s]=Node(s)
			curr_node=curr_node.children[s]
		curr_node.data=string

	def search(self,string):
		curr_node=self.head
		for s in string:
			curr_node=curr_node.children[s]
		if curr_node.children:
			return False
		else:
			return True

t=int(input())
for _ in range(t):
	n=int(input())
	arr=[]
	trie=Trie()
	for _ in range(n):
		s=input().strip()
		arr.append(s)
		trie.insert(s)
	success=True
	for s in arr:
		success=trie.search(s)
		if not success:
			break
	if success:
		print('YES')
	else:
		print('NO')
