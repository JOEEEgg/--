def solution(a, b, flag):
    answer = 0

    if flag == True:
        answer = a + b
    else:
        answer = a - b
    
    return answer

print(solution(-4, 7, False)) 


# 다른 사람 풀이


# def solution(a, b, flag):
#     if flag: return a+b
#     return a-b