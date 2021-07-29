class Node:
    def __init__(self,key,data=None):
        self.key=key          # 알파벳
        self.data=data        # 저장되는 문자열(문자열이 끝나는 경우를 제외하고는 None)
        self.children={}      # 다음 노드를 저장하는 딕셔너리

class Trie:
    def __init__(self):
        self.head=Node(None)        # head를 초기화
		
    def insert(self,string):
        curr_node=self.head         # 현재 노드에 head를 대입
        for s in string:
            if s not in curr_node.children:     # 현재 노드에서 알파벳 s 다음에 올 노드가 없는 경우 노드 생성 후 삽입
                curr_node.children[s]=Node(s)
            curr_node=curr_node.children[s]     # 현재 노드에서 다음 노드로 이동
        curr_node.data=string           # 문자열이 끝났을 경우 현재 노드의 data에 문자열 대입(문자열 끝을 구분하기 위한 목적)

    def search(self,string):
        curr_node=self.head
        for s in string:
            if s not in curr_node.children:			# 다음 노드가 존재하지 않을 경우
                return False
            curr_node=curr_node.children[s]         # 문자열의 알파벳 순서대로 노드 탐색
        if curr_node.data!=None:	# 문자열 탐색이 종료된 후 data에 문자열이 존재할 경우
            return True
        else:			# 문자열이 존재하지 않을 경우
            return False
    
    
    
    
# ex.
trie=Trie()
trie.insert('hello')
trie.insert('hell')
trie.insert('apple')
    
print(trie.search('app'))      # False 출력
print(trie.search('ant'))      # False 출력
print(trie.search('hell'))     # True 출력
print(trie.search('he'))       # False 출력
print(trie.search('hello'))    # True 출력
