def solution(participant, completion):
    ## 풀이 순서
    # 1. completion 과 participant의 길이가 다르므로 completion에 '1' 추가
    # 2. completion, participant 역순 정렬 -> 이유 : '1'를 맨뒤에 보내기 위해
    # 3. 반복문을 이용해 participant와 completion의 같은 인덱스에 값이 다르면 answer에 추가
    
    answer = ''
    
    # 1
    completion.append('1')
    
    # 2
    participant.sort(reverse = True)
    completion.sort(reverse = True)
    
    # 3
    for i in range(len(participant)):   
        if participant[i] != completion[i]:
            answer = participant[i]
            break;
    
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.4MB)
테스트 4 〉	통과 (0.57ms, 10.2MB)
테스트 5 〉	통과 (0.45ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (40.01ms, 18.1MB)
테스트 2 〉	통과 (54.43ms, 22.2MB)
테스트 3 〉	통과 (70.94ms, 24.8MB)
테스트 4 〉	통과 (81.79ms, 26.3MB)
테스트 5 〉	통과 (83.90ms, 26.3MB)
'''