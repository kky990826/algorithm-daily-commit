#코딩 기초 트레이닝
# 조건 문자열
def solution(ineq, eq, n, m):
    if ineq == ">" and eq == "=":
        return 1 if n >= m else 0
    elif ineq == "<" and eq == "=":
        return 1 if n <= m else 0
    elif ineq == ">" and eq == "!":
        return 1 if n > m else 0
    elif ineq == "<" and eq == "!":
        return 1 if n < m else 0
    else:
        return 0
