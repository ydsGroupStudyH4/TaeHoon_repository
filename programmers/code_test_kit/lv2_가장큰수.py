def solution(numbers):
    ###풀이 순서
    # 1. numbers의 숫자들을 문자형(str)으로 바꾸고 각각 3을 곱해서 리스트에 정렬한다
    # 1.2 3 곱하는 이유 : numbers의 원소 길이가 1000이므로 원소들을 길이는 맞춰준다
    # 1.3 reverse하는 이유 : 원소들을 큰 숫자로 정렬하기 위함
    ###
    answer = ''
    lists = list(map(str,numbers))  
    lists.sort(key = lambda x: x*3, reverse = True)  
    answer = "".join(lists) 
    return str(int(answer)) 
    ###예시
    # 입력 : 6 10 2 
    # 과정 : list = [6, 10, 2]
    # 과정 : key -> 666 , 101010 , 222 
    # 과정 : sort -> 666 , 222 , 101010   <-- 문자열은 첫번째 인덱스부터 인덱스별로 비교를 한다.
    # 과정 : sort -> 6 , 2 , 10 
    # 출력 : 6210
    ###