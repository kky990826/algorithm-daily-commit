#코딩 기초 트레이닝
# 문자열 잘라서 정렬하기
def solution(myString):
    parts = [s.strip() for s in myString.split('x') if s.strip()]
    parts.sort()
    return parts