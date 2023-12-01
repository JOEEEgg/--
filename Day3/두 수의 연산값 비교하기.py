def solution(a, b):
    answer = 0
    
    num1 = int(str(a)+str(b))
    num2 = 2 * a * b
    
    if num1 > num2:
        answer = num1
    elif num1 < num2:
        answer = num2
    else:
         answer = num1   
    return answer

print(solution(91, 2))



# 내 거지같은 풀이 (틀림)
# def solution(a, b):
#     answer = ''
#     a, b = str(a), str(b)
#     if ((a+b) < 2 * (int(a * b))):
#         answer = 2 * (int(a * b))
#     elif((a+b) == 2 * (int(a * b))):
#         answer (a+b)
#     return answer

# print(solution(2, 91))
