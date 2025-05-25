#유형별 문제 풀이 - 선택 정렬
# 선택 정렬 구현
def selection_sort(array):
    for i in range(len(array)-1):
        min_idx = i
        for j in range(len(array)-1-i):
            if array[min_idx] > array[i + j]:
                min_idx = i + j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
"""
배열에서 가장 작은 수를 앞으로 끌어다 정렬해나가는 방식
[1,4,5,2,6]라는 배열이 있을때 i의 범위는 len(array) -1 이 되어야지 0부터 4번째 index까지 비교를 해나갈 수 있음
이때 가장 앞의 숫자가 작다고 인덱스를 초기화를 시켜놓고 뒤의 숫자들과 비교해야함  
j는 비교하는 횟수를 의미, len(array) -1 - i 가 되어야 각 index마다 비교 횟수를 카운트할 수 있다
이 과정을 반복하면서 **앞에서부터 차례로 정렬**되어 간다.
"""