#코딩 기초 트레이닝
# l로 만들기
def solution(myString):
    result = ''
    for ch in myString:
        if ch < 'l':
            result += 'l'
        else:
            result += ch
    return result