# 세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
# 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
# 세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
def solution(a, b, c):
    answer = 0
    
    if  a == b == c:
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
    elif (a == b) or (a == c) or (c == b) :
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2 ) 
    else:
        answer = a + b + c    
    return answer

print(solution(3,5,3))

# 다른사람 풀이

def solution(a, b, c):
    answer=a+b+c
    if a==b or b==c or a==c: answer*=a**2+b**2+c**2
    if a==b==c:answer*=a**3+b**3+c**3
    return answer