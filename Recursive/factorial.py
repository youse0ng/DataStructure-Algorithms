# 재귀 함수로 팩토리얼 계산하기

from math import factorial

def factorial_recursive(n:int) -> int:
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

if __name__ == '__main__':
    n = int(input('팩토리얼 계산할 수: '))
    print(factorial_recursive(n))