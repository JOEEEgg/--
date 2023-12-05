# num_list의 홀수만 순서대로 이어 붙인 수와 
# 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 0
    even = ""
    odd = ""
    for n in num_list:
        if n % 2 == 0:
            n = str(n)
            even += n
        else:
            n = str(n)
            odd += n
    answer = int(even) + int(odd)
    return answer

result = [3,4,5,2,1]
print(solution(result))