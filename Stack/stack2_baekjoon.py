class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,x:int):
        self.stack.append(x)

    def pop(self)-> int:
        if not self.__len__(): # 스택에 아무것도 없으면,
            return -1
        else:
            return self.stack.pop()

    def empty(self):
        if not self.__len__():
            return 1
        else:
            return 0

    def __len__(self):
        return len(self.stack)
    
    def get_stack(self):
        return self.stack
    
    def peek(self):
        if self.__len__(): # 4 -> True -> not -> False: 값이 들어있으면, False가 되고, 값이 안들어 있으면, 
            return self.stack[-1]
        else:
            return -1

N = int(input())
a = Stack()
for _ in range(N):
    command = input().split()
    if command[0] == '1':
        a.push(int(command[1]))
    elif command[0] == '2':
        print(a.pop())
    elif command[0] == '3':
        print(a.__len__())
    elif command[0] == '4':
        print(a.empty())
    elif command[0] == '5':
        print(a.peek())
