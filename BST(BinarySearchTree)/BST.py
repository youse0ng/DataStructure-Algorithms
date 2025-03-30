from __future__ import annotations
from typing import Any,Type

class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key:Any, value:Any, left:Node=None, right:Node =None):
        self.key = key # 키 
        self.value = value # 값
        self.left = left # 왼쪽 포인터
        self.right = right # 오른쪽 포인터

class BinarySearchTree:
    """이진 검색 트리"""
    def __init__(self):
        """초기화"""
        self.root = None # 루트 노드
    
    # Search의 Pseudo Code
    # 루트에 주목, 주목하는 노드를 p라고 한다.
    # p가 None이면, 검색을 실패하고 종료
    # 검색하는 key와 주목 노드p의 키를 비교
    # - 검색하는 key < 주목 노드 p의 키이면, 주목노드의 왼쪽 서브 트리로 이동
    # - 검색하는 key > 주목 노드 p의 키이면, 주목노드의 오른쪽 서브 트리로 이동
    # - 검색하는 key == 주목 노드 p의 키이면, 검색 성공 종료
    def search(self,key:Any) -> Any:
        """키가 key인 노드를 검색"""
        p = self.root # 시작 루트 노드에 주목
        while True:
            if p is None:
                return None
            if key == p.key: # 검색 성공
                return p.value # p.value 반환
            elif key < p.key: # key가 주목 노드의 키보다 낮으면
                p = p.left # 왼쪽 서브트리로 이동
            else: # key가 주목 노드의 키보다 크다면
                p = p.right # 오른쪽 서브트리로 이동

    # add(삽입)의 Pseudo Code
    # 루트에 주목, 주목하는 노드를 node라고 함
    # 삽입하는 key와 주목 노드 node의 키 비교
    # - key == node의 키: 삽입에 실패하고 종료
    # - key < node의 키: 왼쪽 서브 노드로 이동, 만약 노드가 존재하지 않으면 삽입하고 노드가 존재하면 key값을 다시 비교
    # - key > node의 키: 오른쪽 서브 노드로 이동, 만약 노드가 존재하지 않으면 삽입, 노드가 존재하면 key값을 다시 비교
    def add(self,key:Any,value:Any)-> bool:
        """키가 key이고 값이 value인 노드를 삽입"""

        def add_node(node:Node, key:Any, value:Any)-> None:
            """node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드 삽입"""
            if key == node.key: # key가 이진 검색 트리에 이미 존재
                return False
            elif key < node.key: # 왼쪽 노드 접근
                if node.left is None: # 왼쪽 노드가 없다면
                    node.left = Node(key,value,None,None) # 삽입
                else: # 왼쪽 노드가 있다면
                    add_node(node.left,key,value) # 재귀 함수로 왼쪽 트리로 더 들어간다
            else: # 오른쪽 노드 접근
                if node.right is None: # 노드가 없다면 삽입
                    node.right = Node(key,value,None,None)
                else: # 아니면 또 다시 재귀함수로 탐색
                    add_node(node.right,key,value)
            return True
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)
        
    # 노드를 삭제할 경우 생각해야할 3가지 경우
    # 1. 자식 노드가 없는 노드를 삭제하는 경우
    # 2. 자식 노드가 1개인 노드를 삭제하는 경우
    # 3. 자식 노드가 2개인 노드를 삭제하는 경우
    ## 1. 부모 노드의 삭제할 노드의 참조를 지움 (Parent.left = None or Parent.right = None)
    ## 2. 삭제할 노드가 부모 노드의 왼쪽 자식인 경우, 부모 노드의 왼쪽 포인터를 삭제할 노드의 자식을 가르키도록 
    ## 2. 삭제할 노드가 부모 노드의 오른쪽 자식인 경우, 부모 노드의 오른쪽 포인터를 삭제할 노드의 자식을 가르키도록
    ## 3. 삭제할 노드의 왼쪽 서브트리에서 가장 큰 노드를 찾아서 삭제할 노드에 삽입
    ## 3.1. 옮긴 노드에 자식이 없으면, 1.을 수행
    ## 3.2. 옮긴 노드에 자식이 1개만 있으면, 2.를 수행
    ## 어렵다..
    def remove(self,key:Any) ->bool:
        """키가 key인 노드를 삭제"""
        p = self.root # 스캔 중인 노드
        parent = None # 스캔 중인 노드의 부모노드
        is_left_child = True # p는 parent의 왼쪽 자식 노드인지 확인

        while True # 삭제할 키 검색. 검색에 성공하면, p는 발견한 노드를 참조하고, parent는 발견한 노드의 부모 노드를 참조
            if p is None: # 아무 것도 없으면 삭제할 것도 없음
                return False
            if key == p.key: # key와 노드 p의 키가 같으면
                break
            else:
                parent = p # 가지를 내려가기 전에 부모를 설정
                if key < p.key: # key 쪽이 작으면
                    is_left_child = True
                    p = p.left # 왼쪽 서브트리에서 검색
                else: # key 쪽이 더 크면
                    is_left_child = False
                    p = p.right

        ## 자식 노드가 없는 노드를 삭제하는 경우와 자식 노드가 1개인 노드를 삭제하는 경우
        if p.left is None: # p에 왼쪽 자식이 없으면, (이때, p는 위 while문을 통해 내가 삭제하고자 하는 노드임)
            if p is self.root: # p가 왼쪽 자식이 없고 root노드라면, root노드를 p.right로 연결해서 삭제, 오른쪽도 None이어도 삭제가능 
                self.root = p.right
            elif is_left_child: # p가 루트 노드가 아닌 parent의 왼쪽 자식일 때,
                parent.left = p.right # 부모의 왼쪽 포인터가 오른쪽 자식을 가리켜 
            else: 
                parent.right = p.right # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None: # p에 오른쪽 자식이 없으면, 
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴

        else: ## 자식 노드가 2개 있는 경우,
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None: # 가장 큰 노드를 left를 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key # left의 키를 p로 이동
            p.value = left.value # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True
    def dump(self) -> None:
        """덤프(모든 노드의 키의 오름차순으로 출력)"""
        def print_subtree(node:Node):
            """노드를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력"""
            if  node is not None:
                print_subtree(node.left) # 왼쪽 서브트리는 주목한 노드보다 값이 낮다.
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None: # 맨 왼쪽 노드 (가장 작은 값)
            p = p.left
        return p.key
    
    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key