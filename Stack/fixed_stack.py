from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""
    class Empty(Exception):
        """비어있는 FixedStack에 팝 또는 피크할 때 내보내는 예외 처리"""
        pass
    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int=256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity #스택 본체
        self.capacity = capacity # 스택의 크기
        self.ptr = 0 # 스택 포인터
    
    def __len__(self) -> int:
        """스택에 쌓여있는 데이터의 개수"""
        return self.ptr 
    
    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        """스택이 차있는지 판단"""
        return self.ptr >= self.capacity
    
    def push(self, value:Any) -> None:
        """스택에 value를 푸시(데이터를 넣음)"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에서 데이터 팝"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self) -> None:
        """스택을 비움"""
        self.ptr = 0 # 스택에서 푸시나 팝은 스택 포인터로 이루어지기에 ptr만 0으로 초기화하면 clear가 됩니다.
        # 하지만 나는 self.stk을 다 None으로 만들어줘야된다고생각했엇다...
    
    def find(self,value:Any) -> Any:
        """스택에서 Value를 찾아 인덱스를 반환 없으면 -1"""
        for i in range(self.ptr - 1 , -1, 1):
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self,value:Any) -> int:
        """스택에 있는 value 반환"""
        c = 0 
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contain__(self, value:Any) -> bool:
        """스택에 value가 있는지 없는지 판단"""
        return self.count(value) > 0
    
    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기순으로 출력)"""
        if self.is_empty():
            print('스택이 비어있습니다.')
        else:
            print(self.stk[:self.ptr])

if __name__ == '__main__':

    fixedstack = FixedStack()