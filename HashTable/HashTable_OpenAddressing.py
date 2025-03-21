# 해시 충돌이 발생할 때 해결하는 또 다른 방법으로 오픈 주소법이 존재
# 충돌이 발생했을 시에 재해시를 수행하여 빈 버킷을 찾는 방법을 말하며 닫힌 해시법이라고도 불린다.#
# Line Probing을 통한 Open Addressing Hash Table을 구현할 예정이다.
# Line Probing이란 해시 충돌이 발생했을 경우에, Key + 1을 수행하여 다시 재해시를 하는 방법으로
# 빈 Slot(bucket)을 찾는 과정이다.
#   0    1    2     3    4   5  6   7     8   9    10  11  12
# [None, 14, None, 29, None, 5, 6, 18, 34, None, 75, 37, 51]
# 다음과 같이 HashTable이 존재할 때, key 5를 삭제한다고 했을 경우, 5만 삭제하면 되는 것이 아니다.
# 만약 18을 검색할 경우 5가 삭제되어 HashTable 5의 자리가 비어있어, 18이 존재함에도 18을 검색할 수 없게 된다.
# 따라서 이러한 오류를 방지하기 위한 버킷에 속성이 필요하다.
## '데이터가 저장되어 있음', '비어있음', '삭제 완료'과 같은 속성이 필요하다.
### 삭제완료: 해시값이 같은 데이터가 다른 버킷에 저장되어 있음.
### 비어 있음: 해시값이 같은 데이터가 존재하지 않음.

from __future__ import annotations
from typing import Any,Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0 #데이터를 저장
    EMPTY = 1 # 비어있음
    DELETED = 2 # 삭제 완료

class Bucket:
    """해시를 구성하는 버킷"""
    def __init__(self,key:Any=None, value:Any=None, stat:Status=Status.EMPTY)->None:
        """초기화"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set(self,key:Any,value:Any,stat=Status)->None:
        """모든 필드에 값을 설정"""
        self.key = key
        self.value = value
        self.stat = stat
    
    def set_status(self,stat:Status) -> None:
        """속성을 설정"""
        self.stat = stat

class OpenHash:
    """오픈 주소법으로 구현하는 해시 클래스"""
    def __init__(self,capacity:int)->None:
        """초기화"""
        self.capacity = capacity # 해시 테이블 크기
        self.table = [Bucket()]*self.capacity # 해시 테이블

    def hash_value(self,key:Any)-> int:
        """해시값을 구함"""
        if isinstance(key,int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capacity)
    
    def rehash_value(self,key:Any)->int:
        """재해시값을 구함"""
        return (self.hash_value(key)+1)%self.capacity # 만약 13크기의 해시테이블이 있다면 13번째 해시테이블이 차있어 +1을 하여 1로 갈 수 있도록 % self.capacity진행하였다.

    def search_node(self,key:Any)->Any:
        """키가 Key인 버킷을 검색"""
        hash = self.hash_value(key) # 검색하는 키의 해시값
        p = self.table[hash]

        for _ in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash) # Deleted +1해서 해당 bucket 찾는다?
            p = self.table[hash]
        return None
    
    def search(self,key:Any) ->Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value # 검색 성공
        else: 
            return None # 검색 실패

    def add(self,key:Any, value:Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        if self.search(key) is not None:
            return False # 이미 등록된 키

        hash = self.hash_value(key) # 추가하는 키의 해시값
        p = self.table[hash] # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key,value,Status.OCCUPIED)
                return True
            hash = self.rehash_value(key)
            p = self.table[hash]
        return False # 해시 테이블이 가득 참

    def remove(self,key:Any) -> int:
        """키가 key인 원소를 삭제"""
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) ->None:
        """해시테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ',end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('--미등록--')
            elif self.table[i].stat == Status.DELETED:
                print('--삭제 완료--')