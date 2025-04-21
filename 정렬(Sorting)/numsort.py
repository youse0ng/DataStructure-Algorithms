import sys

N = int(sys.stdin.readline())
not_sorted = list()
for _ in range(N):
    not_sorted.append(int(sys.stdin.readline()))

def heapify_down(a,left,right):
    temp = a[left] # 루트 노드
    parent = left

    while parent < (right + 1) // 2:
        cl = parent * 2 + 1
        cr = cl + 1
        child = cr if cr <= right and a[cr] > a[cl] else cl # 자식 노드 중에 큰 노드 선택
        if temp > a[child]: # 부모 노드가 더 크면 break
            break
        a[parent] = a[child] # 자식과 부모 노드 교환
        parent = child 
    a[parent] = temp # whild문을 지나면, a[child] = temp

n = len(not_sorted)
for i in range((n-1)//2,-1,-1):
    heapify_down(not_sorted,i,n-1) # maxHeap을 마치고

for i in range(n-1,0,-1): # Heap 정렬
    not_sorted[i],not_sorted[0] = not_sorted[0],not_sorted[i] # a[0] 과 마지막 원소 교체체
    heapify_down(not_sorted,0,i-1) # 다시 힙정렬

for i in not_sorted:
    print(i)