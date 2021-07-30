def preorder(tree,key):           # 전위 순회
	if key!='.':
		left,right=tree[key]
		print(key,end='')
		preorder(tree,left)
		preorder(tree,right)

def inorder(tree,key):            # 중위 순회
	if key!='.':
		left,right=tree[key]
		inorder(tree,left)
		print(key,end='')
		inorder(tree,right)

def postorder(tree,key):          # 후위 순회
	if key!='.':
		left,right=tree[key]
		postorder(tree,left)
		postorder(tree,right)
		print(key,end='')

n=int(input())
tree={chr(65+i):tuple() for i in range(n)}
for _ in range(n):
	key,left,right=input().split()
	tree[key]=(left,right)
preorder(tree,'A')
print()
inorder(tree,'A')
print()
postorder(tree,'A')
