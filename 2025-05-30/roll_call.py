#유형별 문제 풀이 - dict
# 출석 체크
def get_absent_student(all_array, present_array):
    s = set(all_array)
    for i in present_array:
        s.discard(i)
    return list(s)
