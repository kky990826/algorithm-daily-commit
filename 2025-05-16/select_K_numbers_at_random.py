#코딩 기초 트레이닝
# 무작위로 K개의 수 뽑기
def solution(arr, k):
    result = []
    seen = set()

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
        if len(result) == k:
            break

    while len(result) < k:
        result.append(-1)

    return result
