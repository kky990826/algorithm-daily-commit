#유형별 문제 풀이 - 스택
# 괄호 유효성 문제
def isValid(s):
    stack = []

    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack:
                return False
            top = stack.pop()

            # 여는 괄호와 닫는 괄호 짝이 맞는지 확인
            if c == ')' and top != '(':
                return False
            elif c == ']' and top != '[':
                return False
            elif c == '}' and top != '{':
                return False

    # 스택이 비어있으면 모든 괄호가 잘 맞았다는 뜻
    return not stack


