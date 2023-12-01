# def solution(ineq, eq, n, m):
#     answer = 0

#     if n >= m and (ineq + eq) == (">="):
#         answer = 1
#     elif n <= m and (ineq + eq)  == ("<="):
#         answer = 1
#     elif n > m and (ineq + eq)  == (">!"):
#         answer = 1
#     else:
#         if n < m and (ineq + eq)  == ("<!"):
#             answer = 1
#     return answer

# def solution(ineq, eq, n, m):
#         return int(eval(str(n) + ineq + eq.replace("!", "") + str(m)))

# print(solution(str("<"), str("="), 20, 50))

print(eval('1' + '+' + '2'))
print(eval('1+2'))