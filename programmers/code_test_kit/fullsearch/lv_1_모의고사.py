def solution(answers):
    ## 풀이 순서
    # 1. p1,p2,p3 수포자 1,2,3을 각각 최소 단위의 리스트로 생성
    # 2. 시험 문제는 최대 10000개니까 p1,p2,p3가 각각 10000이 될수 있도록 곱해준다
    # 3. 맞춘 갯수는 score 딕셔너리에 저장 { '수포자' : '점수' }
    # 4. 가장 많이 맞춘 사람을 answer에 저장
    # 5. 가장 많이 맞춘 갯수가 또 존재하면 또 answer에 저장
    
    answer = []
    
    # 1, 2
    p1 = [1,2,3,4,5] * 2000
    p2 = [2,1,2,3,2,4,2,5] * 1250
    p3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    # 3
    score = {1:0,2:0,3:0} 
    
    # 4
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            score[1] += 1
        if answers[i] == p2[i]:
            score[2] += 1
        if answers[i] == p3[i]:
            score[3] += 1
           
    # 5
    answer.append(max(score, key = score.get))
    max_value = score[max(score, key = score.get)]
    score[max(score, key = score.get)] = -1   
    for i in range(1,4):
        if max_value == score[i]:
            answer.append(max(score, key = score.get))
            score[i] = -1
            
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.18ms, 10.3MB)
테스트 2 〉	통과 (0.17ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.4MB)
테스트 4 〉	통과 (0.17ms, 10.4MB)
테스트 5 〉	통과 (0.18ms, 10.1MB)
테스트 6 〉	통과 (0.19ms, 10.4MB)
테스트 7 〉	통과 (1.22ms, 10.4MB)
테스트 8 〉	통과 (0.56ms, 10.3MB)
테스트 9 〉	통과 (2.03ms, 10.4MB)
테스트 10 〉	통과 (1.09ms, 10.3MB)
테스트 11 〉	통과 (2.20ms, 10.4MB)
테스트 12 〉	통과 (2.06ms, 10.3MB)
테스트 13 〉	통과 (0.29ms, 10.4MB)
테스트 14 〉	통과 (2.29ms, 10.4MB)
'''