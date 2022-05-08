'''
번호 : 1920
타이틀 : 수 찾기
문제 타입 : 해시
https://www.acmicpc.net/problem/1920
'''

import sys

sys.stdin=open("1920.txt","r")
input=sys.stdin.readline

n = int(input())
key_list = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

pool ={}
for p in key_list:
  pool[p] = 1 # { 4:1, 1:1, 5:1, 2:1, 3:1 }처럼 나옴 { key:value }

for i in target_list:
  if i in pool:
    print("1")
  else:
    print("0")


      