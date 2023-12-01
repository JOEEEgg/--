# n이 홀수면 n보다 작은 홀수를 모두 더한 값이 result
# n이 짝수면 n보다 작은 짝수의 제곱을 더한 값이 result

# range(start, stop, step)
#내 풀이
# n이 4라면
def solution(n):
    a = 0
    if (n%2 == 1):
        for i in range(n,0,-2):
            a += i # a = a + i
    else:
        for i in range(n,0,-2):
            a += (i**2) # a = a + (i**2)
    return a