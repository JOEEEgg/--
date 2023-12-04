# 예) a = 3, d = 4 일 떄 iucluded가 [true, false, false, true, true]이면 result = 37
# [true, false, false, true, true] = 3, 7, 11, 15, 19
# 그래서  result = 37

def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        if included[i]:  # True인 경우에만 계산 수행
            answer += a + d * i

    return answer

# 예시로 주어진 입력값을 사용하여 함수 호출 및 결과 출력
result = solution(3, 4, [True, False, False, True, True])
print("result =", result)
 
 
# 다른 풀이
# def solution(a, d, included):
#     ai = a
#     answer = 0 
#     for i in included:
#         if i == True:
#             answer += ai 
#         ai = ai + d    
#     return answer