def recur(n:int) ->int:
    """순수한 재귀 함수 recur의 구현"""
    if n>0:
        recur(n-1)
        print(n)
        recur(n-2)

x = int(input('값을 입력: '))
recur(x)
