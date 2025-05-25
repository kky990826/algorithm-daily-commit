#유형별 문제 풀이 - 병합 정렬
# 병합 정렬 구현
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1
    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1
    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1
    return result

# 위의 사례는 두개의 array를 단순히 각 요소의 값을 비교해서 새로운 array를 만들어내는 것
# array가 두개가 주어지고 각 array가 이미 오름차순으로 정렬이 되어 있기 때문에 가능한 것임
# 즉 병합 정렬을 완전히 만들기에는 기존 merge 함수만으로는 부족함
# 만약 [1, 4, 5, 2, 6] => 이런 array가 하나만 주어지고 내부적으로 정렬이 안되어 있을때는 어떻게 하는가?
# 분할과 병합의 방식으로 기존 merge 함수를 정렬해나가는 것이 필요

def merge_sort(array):
    if len(array) <= 1:  # 재귀 종료 조건
        return array
    mid = len(array) // 2  # 두개의 array로 분할
    left = merge_sort(array[:mid])  # 분할한 array에서 merge_sort를 호출함으로 다시 분할이 일어남
    right = merge_sort(array[mid:])
    return merge(left, right)  # merge 실시

# 매번 배열을 절반으로 나누기 때문에 O(log2(n))의 단게가 필요 => 분할
# 각 단계마다 전체 데이터를 병합해가는 과정에서  O(n)의 단게가 필요 => 병합
# 따라서 전체 O(nlogn)의 시간 복잡도가 필요함. 우리가 정렬을 말할때 시간 복잡도 NlogN을 말하는 이유가 바로 병합 정렬 때문!

"""
배열을 반으로 계속 나누어 최소 단위(1개 또는 0개 원소)로 쪼갠 뒤,
작은 배열부터 정렬하면서 다시 병합해나가는 방식.

예: [1, 4, 5, 2, 6] 라는 배열이 있을 때
- 배열을 재귀적으로 반으로 나눔: [1, 4], [5, 2, 6] → [1], [4], [5], [2, 6] ...
- 나눌 수 없을 때까지 쪼갠 후, 두 개씩 비교하며 병합하면서 정렬

이 과정을 반복하면서 **작은 정렬된 배열들을 합치며 전체 정렬**을 완성해나간다.
병합 과정에서는 두 배열의 앞쪽 값들을 비교하여 더 작은 값을 차례로 새로운 배열에 추가한다.

결과적으로 정렬은 분할과 병합을 통해 완성되며,
전체 배열이 **뒤에서부터 정렬되는 것이 아니라** 병합을 통해 **전체적으로 균형 있게 정렬**되어 간다.

참고로 파이썬에서 제공하는 sort 메서드는 내부적으로 Timsort를 사용함 
Timsort는 삽입 정렬과 병합 정렬을 혼합하여 만들어냄

삽입 정렬은 내부적으로 새로운 array를 return하지 않는데 반해 병합 정렬은 내부적으로 새로운 array를 return
sorted(arr)를 사용하게 되면 새로운 array를 return하고 arr.sort()를 하게 되면 새로운 array를 return하지 않는다
Timsort를 어떻게 구현하느냐에 따라서 return을 하기도 하지 않기도 한다
"""
