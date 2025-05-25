#유형별 문제 풀이 - 버블 정렬
# 버블 정렬 구현
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
"""
앞의 숫자와 뒤의 숫자를 비교해가면서 자리를 바꿔가면서 정렬해나가는 방식
[1,4,5,2,6]라는 배열이 있을때 i의 범위는 len(array) -1 이 되어야지 0부터 4번째 index까지 비교를 해나갈 수 있음
j는 비교하는 횟수를 의미, len(array) -1 - i 가 되어야 각 index마다 비교 횟수를 카운트할 수 있다
각 단계마다 인접한 두 값을 비교하고, 앞의 값이 크면 서로 교환.
이 과정을 반복하면서 큰 값이 점점 뒤로 "밀려나서" 정렬됨.
즉, 배열의 **뒤에서부터 정렬이 완료**된다.
"""