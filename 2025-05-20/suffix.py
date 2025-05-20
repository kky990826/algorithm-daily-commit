#코딩 기초 트레이닝
# 꼬리 문자열
def solution(str_list, ex):
    result = [s for s in str_list if ex not in s]
    return "".join(result)