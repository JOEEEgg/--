def solution(number, n, m):
    answer = 0
    if number % n == 0 and number % m == 0:
        answer = 1
    else :
        answer = 0
    return answer

print(solution(68, 2, 3))

# 다른 사람의 풀이

# def solution(number, n, m):
#     return int(number%n == 0 and number%m == 0)