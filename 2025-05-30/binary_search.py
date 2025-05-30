#유형별 문제 풀이 - binary search
# 이진 탐색
finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) -1
    while current_min <= current_max:
        current_guess = (current_min + current_max) // 2
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
    return False
"""
이진 탐색은 반드시 정렬이 된 상태에서만 유효
중간값과 비교해서 범위를 절반씩 줄여나가는 구조
시간복잡도 O(logN)
"""