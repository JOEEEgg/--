def solution(my_string, k):
    answer = ''

    for i in range(k + 1):
        answer = my_string * i
    return answer

print(solution("string", 5))

# 왜이리 어렵게 생각했을까?? 너무 쉽네
# def solution(my_string, k):
#     return my_string*k