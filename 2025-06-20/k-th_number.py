#유형별 문제 풀이 - 정렬
# K번째 수

def solution(array, commands):
    answer = []
    for i in commands:
        splited_array = array[i[0]-1:i[1]]
        sorted_array = sorted(splited_array)
        answer.append(sorted_array[i[2]-1])
    return answer
