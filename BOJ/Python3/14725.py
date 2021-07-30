import sys
input=sys.stdin.readline

class Node:
    def __init__(self,key,cnt=0):
        self.key=key        # 현재 노드 데이터
        self.children={}    # 다음 노드
        self.cnt=cnt        # 트리 차수(높이)

class Tree:
    def __init__(self):
        self.head=Node(None)

    def insert(self,arr):
        curr_node=self.head
        for i in range(len(arr)):
            if arr[i] not in curr_node.children:          # 단어에 대한 노드가 존재하지 않은 경우 노드 생성 후 삽입
                curr_node.children[arr[i]]=Node(arr[i])
            curr_node=curr_node.children[arr[i]]          # 다음 노드로 이동
            curr_node.cnt=i+1           # 노드에 트리 차수 저장

def tree_print(node):
    curr_node=node
    sort_children=sorted(curr_node.children.items(),key=lambda x:x[0])      # 사전 순서가 앞서는 노드가 먼저 출력되어야 하므로 정렬
    for w,next_node in sort_children:
        print('--'*curr_node.cnt+w)
        tree_print(next_node)

tree=Tree()
n=int(input())
for _ in range(n):
	k=input().split()
	tree.insert(k[1:])	# 트리에 숫자를 제외한 배열 삽입
tree_print(tree.head)
