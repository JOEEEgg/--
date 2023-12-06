# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
# num_list = [a, b]
# b > a, b - a를  b < a, 2b
def solution(num_list):
    answer = num_list

    if num_list[-1] > num_list[-2]:
        answer.append(num_list[-1] - num_list[-2]) 
    elif num_list[-1] <= num_list[-2]:
        answer.append(2 * (num_list[-1])) 
    return answer

# 다른 사람의 풀이
def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l