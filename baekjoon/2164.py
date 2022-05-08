'''
번호 : 2164
타이틀 : 배열 합치기
문제 타입 : 큐
https://www.acmicpc.net/problem/2164

내가 푼 방식 : 리스트
정답 : 덱 
시간 초과 발생 이유 : 
1. 리스트에서는 하나의 요소가 삭제되면, 그 뒤 요소들이 한칸씩 당겨지게 됨. 시간 복잡도 약 O(N)이 됨
2. 덱은 하나의 요소가 삭제되도, 다른 요소는 제어할 필요가 없기 때문에 O(1)이 됨.
'''

import sys
from collections import deque 

sys.stdin=open("2164.txt","r")
input=sys.stdin.readline

n = int(input())
queue = deque()

for i in range(1,n+1):
  queue.append(i)

while(len(queue) > 1):
  
  queue.popleft()
  queue.append(queue.popleft())
  
  '''
  #내가 푼 방법 - 시간 초과
  queue.pop(0)
  i = queue[0]
  queue.pop(0)
  queue.append(i)
  '''

print("{}".format(queue[0]))
