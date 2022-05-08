def solution(array, commands):
    answer = []
    
    for n in range(0,len(commands)):
        i = commands[n][0]
        j = commands[n][1]
        k = commands[n][2]
        
        x = sorted(array[i-1:j])
        
        answer.append(x[k-1])

    return answer

'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
'''