def solution(a, b):
    answer = 0

    if (str(a) + str(b) > str(b) + str(a)) :
        answer = str(a) + str(b)
    elif(str(a) + str(b) < str(b) + str(a)):
        answer = str(b) + str(a)
    else:
        answer = (str(a) + str(b))
    return int(answer)

print(type(solution(9, 91)))

##########################################

# def solution(a, b):
#     a, b = str(a), str(b)
#     return int(max(a+b, b+a))