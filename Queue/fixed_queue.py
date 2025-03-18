# 링버퍼로 큐 구현하기

from typing import Any

class FixedQueue:
    class Empty(Exception):
        """비어있는 Fixed Queue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass
    
    class Full(Exception):
        """가득 차 있는 Fixed Queue에서 인큐할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self,capacity:int) -> None:
        """큐 초기화"""
        self.no = 0 # 현재 데이터 개수
        self.front = 0 # 맨 앞 원소 커서
        self.rear = 0 # 맨 뒤 원소 커서
        self.capacity = capacity # 큐의 크기
        self.que = [None] * capacity # 큐의 본체
        
    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.capacity <= self.no

    def enque(self, x: Any) -> None:
        """데이터 x를 큐에 인큐"""         
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1 # 그 다음 인큐할 때 rear가 증가해야 입력이 가능하니, rear를 +1 해줌
        self.no += 1
        if self.rear == self.capacity: # 크기가 12인 queue에 11인 rear에 원소가 추가되면 12가 된다. 하지만 que[12]는 존재하지 않으니 다시 rear를 0으로
            self.rear = 0 
    
    def deque(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            return FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity: # 만약 크기가 12인 queue에 11번째의 데이터를 디큐하면 이제 다시 인덱스를 0으로 할당해야한다.
            self.front = 0
        return x
    
    def peek(self) -> Any:
        """큐에서 데이터를 피크(맨 앞 데이터를 들여다봄)"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self,value:Any) -> int:
        """큐에서 value를 찾아 인덱스를 반환, 없으면 -1 반환"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self,value:Any) -> int:
        """큐에 있는 value개수 반환"""
        c = 0 
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c
    
    def __contains__(self,value:Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐에 있는 모든 데이터를 지움"""
        self.no = self.front = self.rear = 0
        
    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 맨 끝 순으로 출력"""
        if is_empty():
            print('큐가 비어있습니다.')
        else:
            for i in range(self.no):
                idx = (i + self.front) % self.capacity
                print(self.que[idx], end='')
            print()
            
from enum import Enum

if __name__ == '__main__':
    Menu = Enum('Menu', ['인큐','디큐','피크','검색','덤프','종료'])
    
    def select_menu() -> Menu:
        """메뉴 선택"""        
        s = [f'({m.value}){m.name}' for i in Menu]
        while True:
            print(*s, sep =' ',end='')
            n = int(input(': '))
            if 1 <= n <= len(Menu):
                return Menu(n)
            
    q = FixedQueue(64)
    
    while True:
        print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
        menu = select_menu()
        
        if menu == Menu.인큐:
            x = int(input('인큐할 데이터를 입력하세요.: '))
            try:
                q.enque(x)
            except FixedQueue.Full:
                print('큐가 가득 찼습니다.')
                
        elif menu == Menu.디큐:
            try:
                x = q.deque()
                print(f'디큐한 데이터는 {x}입니다.')
            except FixedQueue.Empty:
                print('큐가 비어 있습니다.')
        
        elif menu == Menu.피크:
            try:
                x = q.peek()
                print(f'피크한 데이터는 {x}입니다.')
            except FixedQueue.Empty:
                print('큐가 비어 있습니다.')
            
        elif menu == Menu.검색:
            x = int(input("검색할 값을 입력하시오: "))
            if x in q:
                print(f"{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.")
            else:
                print(f'{x}는 Queue에서 찾을 수 없습니다.')
                
        elif menu == Menu.덤프:
            q.dump()
        
        else:
            break