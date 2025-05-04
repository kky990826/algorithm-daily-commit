#코딩 기초 트레이닝
# 수열과 구간 쿼리
def solution(arr, queries):
    for q in queries:
        q1, q2, q3 = q
        for i in range(q1, q2+1):
            if i % q3 == 0:
                arr[i] += 1
    return arr
print(solution([0,1,2,4,3], [[0,4,1],[0,3,2],[0,3,3]]))
