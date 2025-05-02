#코딩 기초 트레이닝
# 코드 처리하기
def solution(code):
    mode = 0
    ret = ""
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] == "1":
                mode = 1
            elif idx % 2 == 0:
                ret += code[idx]
        else:  # mode == 1
            if code[idx] == "1":
                mode = 0
            elif idx % 2 == 1:
                ret += code[idx]
    return ret if ret else "EMPTY"


