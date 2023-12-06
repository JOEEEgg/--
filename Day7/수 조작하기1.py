# control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, 
# control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
# w : n + 1
# s : n - 1
# d : n + 10
# a : n - 10
def solution(n, control):
    answer = n
    num_dict = {'w': 1, 's':-1, 'd':10, 'a':-10}
    
    for i in control:
        answer += num_dict[i]
    return answer

print(solution(0, "wsdawsdassw"))


# 다른 사람 풀이
def solution(n, control):
    answer = 0
    for i in control:
        if i == 'w':
            n += 1
        elif i == 's':
            n -= 1
        elif i == 'd':
            n += 10
        elif i == 'a':
            n -= 10
    answer = n
    return answer
