#유형별 문제 풀이 - recursive
# 회문 검사
def is_palindrome(string):  # for문을 이용해서 풀이
    n = len(string)
    for i in range(n):
        if string[i] != string[n -1 - i]:
            return False
    return True

def is_palindrome2(string): # 재귀를 이용해서 풀이
    if string[0] != string[-1]:
        return False
    if len(string) <= 1:
        return True
    return is_palindrome2(string[1:-1])