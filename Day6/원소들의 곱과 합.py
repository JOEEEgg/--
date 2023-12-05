from functools import reduce

def solution(num_list):
    list_mul = reduce(lambda x, y: x * y, num_list)  # Calculate the product using reduce

    list_sum = sum(num_list)  # Calculate the sum using sum function
    list_sum_mul = list_sum**2  # Square the sum

    if list_mul < list_sum_mul:
        return 1
    else:
        return 0

result = solution([3, 4, 5, 2, 1])
print("result ==", result)

# 다른 사람 풀이
def solution(num_list):
    mul = 1 
    for n in num_list:
        mul *= n
    return int(mul < sum(num_list) ** 2)