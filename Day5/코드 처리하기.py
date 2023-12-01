# 1이면 mode를 바꾼다
# mode가 0이고 code[idx] idx가 짝수이면 ret 맨뒤에 code[idx]를 추가
# mode가 1이고 code[idx] idx가 홀수이면 ret 맨뒤에 code[idx]를 추가
# code[idx] = "1"이면 mode 변경
def solution(code):
    answer = ''
    mode = 0
    for idx, word in enumerate(code):
        if word.isalpha():
            if mode == 0 and idx % 2 == 0:
                answer += word
            elif mode == 1 and idx % 2 == 1:
                answer += word

        else:
            if mode == 0:
                mode = 1
            else:
                mode = 0
    if len(answer) == 0:
        return 'EMPTY'
    else:
        return answer

# 다른 사람 풀이1

# def solution(code):
#     return "".join(code.split("1"))[::2] or "EMPTY"

# 다른 사람 풀이2

# def solution(code):
#     answer = ''

#     mode = 0
#     for i in range(len(code)):
#         if code[i] == '1':
#             mode ^= 1
#         else:
#             if i % 2 == mode:
#                 answer += code[i]

#     return answer if answer else 'EMPTY'