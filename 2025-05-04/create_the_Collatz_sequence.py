#코딩 기초 트레이닝
# 콜라츠 수열 만들기
def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 ==0:
           n = n // 2
        else:
            n = 3*n + 1
        answer.append(n)
    return answer
print(solution(10))