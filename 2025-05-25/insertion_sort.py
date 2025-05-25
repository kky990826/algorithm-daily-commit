#유형별 문제 풀이 - 삽입 정렬
# 삽입 정렬 구현
def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i):
            if array[i - j] < array[i - j - 1]:
                array[i - j], array[i - j - 1] = array[i - j - 1], array[i - j]
            else:
                break
    return array
"""
뒤에서부터 추가되는 숫자를, 기존에 정렬된 부분과 비교해 적절한 위치에 '삽입'하는 방식.
[1,4,5,2,6]라는 배열이 있을때 i의 범위는 1부터 len(array) 이 되어야함(애초에 비교 시작을 두번째 숫자부터 시작하기 때문)
안쪽 반복문(j)은 i보다 앞에 있는 요소들과 역순으로 비교
현재 값을 앞쪽 정렬된 부분과 비교하며, 더 큰 값은 한 칸씩 뒤로 밀고,
최종적으로 알맞은 위치에 현재 값을 삽입한다.
버블 정렬이 큰 값을 뒤로 보내는 방식이라면, 삽입 정렬은 **작은 값을 앞쪽으로 끼워 넣는 방식**이다.
"""