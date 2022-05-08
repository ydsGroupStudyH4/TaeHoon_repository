'''
번호 : 9934
타이틀 : 완전 이진 트리
문제 타입 : 트리 구조, BFS
https://www.acmicpc.net/problem/9934
'''

import sys

sys.stdin=open("9934.txt","r")
input=sys.stdin.readline

k = int(input())
tree = list(map(str, input().split()))
ans = [[]for _ in range(k)] # k : 3 일떄, [ [], [], [] ] 같이 나옴

def sol(arr, depth):
  mid = len(arr) // 2
  ans[depth].append(arr[mid])
  if len(arr) == 1 :
    return
  sol(arr[:mid],depth+1)
  sol(arr[mid+1:],depth+1)

sol(tree,0)
for i in range(k):
  print(*ans[i]) # *붙이면 [] 모양 사라짐