def solution(citations):
    ###풀이 순서
    # 1. 역순 정렬을 해서 큰 값이 앞으로 오게한다
    # 2. citations 길이의 역순으로 h-index를 구한다
    # 3. 만약 입력값이 모두 0인 것을 대비해, 반복문을 -1까지 늘려준다
    answer = 0
    citations.sort(reverse = True)
    for i in range(len(citations), -1, -1): # <-- 3
        count = 0
        answer = i
        print(i)
        for j in range(len(citations)):
            if answer <= citations[j]:
                count +=1
            if count >= answer:
                return answer
    return answer