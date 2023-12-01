def solution(str1, str2):
    answer = ''

    for i in range(len(str1)):
        answer += str1[i] + str2[i]

    return answer

print(solution("aaaaaa", "bbbbbb"))


##########################
# zip함수 : a의 첫번째 인덱스 b의 첫번쨰 인덱스와 같이 일치하는 인덱스 값을 추출
# a = 'aaaaa'
# b = 'bbbbb'

# answer = ''

# for i,j in zip(a, b):
#     answer += i + j
# print(answer)