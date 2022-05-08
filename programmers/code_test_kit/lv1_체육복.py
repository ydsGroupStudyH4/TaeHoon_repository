def solution(n, lost, reserve):
    ## 풀이 순서
    # 1. 전체 학생수 만큼 now_list 모든 요소가 1로 확장 ( 1은 현재 체육복 가진순 )
    # 2. 여벌있는 학생들은 +1
    # 3. 잃어버린 학생들은 -1
    # 4. 인덱스 0과 5의 에러 방지를 위한 양 끝에 -1 추가
    # 5. 체육복이 0인 학생들 기준으로 양쪽 여벌 확인 및 빌려주기
    # 6. 체육수업 들을 수 있는 학생 수 계산
    
    # 1
    answer = 0    
    now_list = [1,] * n 
    
    # 2
    for i in reserve:
        now_list[i-1] += 1        
    
    # 3
    for j in lost:
        now_list[j-1] -= 1
    
    # 4
    now_list.insert(0,-1)
    now_list.append(-1)
    
    # 5
    for k in range(n):
        if now_list[k] == 0:
            if(now_list[k-1] > 1):
                now_list[k-1] -= 1
                now_list[k] += 1
            elif(now_list[k+1] > 1):
                now_list[k+1] -= 1
                now_list[k] += 1
    
    # 6
    answer = n - now_list.count(0)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10MB)
테스트 3 〉	통과 (0.01ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 9.98MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.02ms, 10.4MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.4MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''