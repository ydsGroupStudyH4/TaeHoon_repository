def solution(progresses, speeds):
    answer = []
    ans_list = []

    # 1. progresses와 speeds를 이용하여 예상작업기간(ans_list) 측정
    # [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1] ---> [5, 10, 1, 1, 20, 1]
    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] == 0 :
            ans_list.append(int((100 - progresses[i])/speeds[i]))
        else:
            ans_list.append(int((100 - progresses[i])/speeds[i] + 1))

    # 2. 예상작업기간 리스트 안에서 max값을 하나씩 찾으면서, 새로운 max값을 찾으면 그 길이를 answer에 추가
    # [5, 10, 1, 1, 20, 1] ---> [5], [10,1,1] 의 길이를 answer에 추가
    max_value = ans_list[0]
    for j in range(len(ans_list)) :
        if max_value < ans_list[j]:
            answer.append(len(ans_list[ans_list.index(max_value):ans_list.index(ans_list[j])]))
            max_value = ans_list[j]
    # 3. 남은 부분 처리
    # [5, 10, 1, 1, 20, 1] 중 [20, 1]은 #2에서 추가안하고 마지막에 따로 추가
    answer.append(len(ans_list[ans_list.index(max_value):]))
            
            
    return answer