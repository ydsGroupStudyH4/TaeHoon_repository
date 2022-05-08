'''
번호 : 11728
타이틀 : 배열 합치기
문제 타입 : 문자열
'''

import sys

sys.stdin=open("11728.txt","r")
input=sys.stdin.readline


a, b = map(int, input().split()) # split : 문자열 나누기
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
answer_list = a_list + b_list
answer = ' '.join(map(str, sorted(answer_list)))
print(answer)


## 내가 만든 코드
# 결과 : 시간초과
# sorted 사용 안함
'''
a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
ab_list = a_list + b_list

for i in range(0, len(ab_list)):
  for j in range(i, len(ab_list)):
    if(ab_list[i] > ab_list[j]):
      c = ab_list[i]
      ab_list[i] = ab_list[j]
      ab_list[j] = c 

print(ab_list) 
'''
    


