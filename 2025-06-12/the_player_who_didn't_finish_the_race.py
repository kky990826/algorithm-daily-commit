#유형별 문제 풀이 - 해시
# 완주하지 못한 선수
def solution(participants, completion):
    s = {}
    for name in participants:
        s[name] = s.get(name, 0) +1 
    for name in completion:
        s[name] -= 1
    for name in s:
        if s[name] > 0:
            return name


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))