#유형별 문제 풀이 - recursive
# 카운트 다운
def count_down(number):
    if number < 0:  # 반드시 탈출 조건을 명시해줘야함
        return
    print(number)
    count_down(number -1)
count_down(60)
