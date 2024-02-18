# 스택: 선입후출
# 쌓이는 구조

def stack():
    stack = [] # 빈 리스트 생성

    # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop() # 가장 최근 들어온 7이 삭제
    stack.append(1) 
    stack.append(4)
    stack.pop() # 가장 최근 들어온 4가 삭제

    print(stack) #최하단의 원소부터 출력됨
    print(stack[::-1]) # 최상단의 원소부터 출력됨

stack()

# 큐: 선입선출
# 대기열 구조

from collections import deque

def queue():
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()

    # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
    queue.append(5) #list와 동일하게 작동. 오른쪽에 데이터 삽입
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft() # 왼쪽의 데이터를 삭제함
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print(queue) #먼저 들어온 순서대로 출력
    queue.reverse()
    print(queue) #나중에 들어온 순서대로 출력

queue()