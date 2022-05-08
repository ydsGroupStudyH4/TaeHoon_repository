'''
번호 : 9012
타이틀 : 괄호
문제 타입 : 스택
https://www.acmicpc.net/problem/9012
'''

import sys


sys.stdin=open("9012.txt","r")
input=sys.stdin.readline

a = int(input())
for i in range(a):
  b = list(input())
  sum = 0
  
  for j in b:
    if( j == '('):
      sum += 1
    elif(j == ')'):
      sum -= 1
    if(sum < 0):
      print("NO")
      break
        
  if(sum == 0):
    print('YES')
  elif(sum > 0 ):
    print('NO')

