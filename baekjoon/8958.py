'''
번호 : 8958
타이틀 : OX퀴즈
문제 타입 : 구현, 문자열
https://www.acmicpc.net/problem/8958
'''

import sys

sys.stdin=open("8958.txt","r")
input=sys.stdin.readline

c = int(input())

for i in range(c):
  ox_str = str(input())
  temp = 0
  score = 0
  for j in range(len(ox_str)):
    if ox_str[j] == 'O' :
      temp += 1
      score += temp
    elif ox_str[j] == 'X' :
      temp = 0  
      
  print(score)