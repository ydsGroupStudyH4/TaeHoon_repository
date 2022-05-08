'''
번호 : 4344
타이틀 : 평균은 넘겠지
문제 타입 : 모름
https://www.acmicpc.net/problem/4344
'''
## 풀이순서
# 1.리스트 안 평균을 구한다
# 2.리스트 안 값이 평균을 넘으면 카운트 +1 한다
# 3.카운트 / 리스트 길이 를 통해 값을 출력한다

import sys

sys.stdin=open("4344.txt","r")
input=sys.stdin.readline

c = int(input())

for i in range(c):
  input_list = list(map(int, input().split()))
  n = input_list[0]
  n_list = input_list[1:]
  #1
  avg = sum(n_list) / len(n_list)
  #2
  count_student = 0
  for j in n_list:
    if avg < j :
      count_student += 1
  #3
  print(f'{count_student/n*100:0.3f}%' )