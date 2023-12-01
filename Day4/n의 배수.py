# def solution(num, n):
#     answer = 0
#     if num % n == 0:
#         answer = 1
#     else :
#         answer = 0
#     return answer

# print(solution(96, 2))

#####################
#1 다른 사람의 풀이

# def solution(num, n):
#     return int(not(num % n))

#2 다른 사람의 풀이

def solution(num, n):
    return int(num % n == 0)

print(solution(98, 2))