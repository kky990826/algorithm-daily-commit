#유형별 문제 풀이 - 스택
# 기온 변화 구하기
def dailyTemperatures(T):
    temperatures = [0] * len(T)
    stack = []
    for current_day, current_temp in enumerate(T):
        while stack and T[stack[-1]] < current_temp:
            previous_day = stack.pop()
            temperatures[previous_day] = current_day - previous_day
        stack.append(current_day)
    return temperatures