# 해시값이 같은 원소를 연결 리스트로 관리하는 Hash Table
# 체인법(chaining)이란 해시값이 같은 데이터를 체인 모양의 연결 리스트로 연결하는 방법을 말하며, 오픈 해시법이라고 부른다.
# 체인법은 연결리스트를 사용하여 구현한다.
from __future__ import annotations
from typing import Any,Type
import hashlib

class Node:
    """해시를 구성하는 노드"""
    def __init__(self,key:Any,value:Any,next:Node) -> None:
        """초기화"""
        self.key = key # 키 
        self.value = value # 값
        self.next = next # 뒤쪽 노드를 참조

class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    def __init__(self,capacity:int)->None:
        """초기화"""
        self.capacity = capacity # 테이블의 크기 (버켓 또는 Slot의 개수)
        self.table = [None] * self.capacity # 리스트형 테이블 생성

    def hash_value(self,key:Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int): # Key값이 int인 경우
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity) # key값이 문자형인 경우
    
    def search(self,key:Any)->Any:
        """Key가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key) # Key의 Hash값 도출
        p = self.table[hash]

        while p is not None: # p가 비어있지 않다면
            if p.key == key: # 검색 성공
                return p.value
            p = p.next
        
        return None # 검색 실패 # p가 비어있다면
    
    def add(self,key:Any, value:Any)->bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key) # 추가하는 key의 해시값
        p = self.table[hash] # 추가하려는 해시값의 노드에 주목

        while p is not None: # p가 비어 있지않다면,
            if p.key == key:
                return False # 해당하는 Key가 이미 있으므로 False
            p = p.next # 뒤쪽 노드 주목

        temp = Node(key,value, self.table[hash]) # next의 인자로 self.table[hash]를 넣어, 이미 연결되어있는 Node들을 신규 추가 노드 뒤에다가 연결
        self.table[hash] = temp # 노드 추가
        return True

    def remove(self,key:Any)->bool:
        """해당 Key값이 존재하면 삭제"""
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None # 바로 앞의 노드를 주목

        while p is not None: # 지금 주목한 노드가 None이 아니면
            if p.key == key:
                if pp is None: # 삭제할 노드가 맨 앞에 있다면
                    self.table[hash] = p.next
                else: # 삭제할 노드가 3개의 노드 중에서 가운데에 있을 경우
                    pp.next = p.next # 1번째 노드를 3번째 노드에 연결하여 삭제할 노드(중간에 있는)를 삭제
                return True # Key 삭제 성공
            pp = p
            p = p.next
        return False # 해당 해시값의 연결 노드들을 다 순환하고 난 뒤에 # 해당 Key를 못찾을 때