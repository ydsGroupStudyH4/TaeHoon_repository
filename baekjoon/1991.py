'''
번호 : 1991
타이틀 : 트리 순회
문제 타입 : 트리
https://www.acmicpc.net/problem/1991
'''

import sys

sys.stdin=open("1991.txt","r")
input=sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
  root, left, right = list(map(str,input().split()))
  tree[root] = [left, right]

# 전위 (preorder)
def pre_sol(root):
  if root != ".":
    print(root, end="")
    pre_sol(tree[root][0]) # left
    pre_sol(tree[root][1]) # right

# 중위 (inorder)
def in_sol(root):
  if root != ".":
    in_sol(tree[root][0]) # left
    print(root, end="")
    in_sol(tree[root][1]) # right

# 후위 (postorder)
def post_sol(root):
  if root != ".":
    post_sol(tree[root][0]) # left
    post_sol(tree[root][1]) # right
    print(root, end="")
  
pre_sol('A')
print("")
in_sol('A')
print("")
post_sol('A')
print("")