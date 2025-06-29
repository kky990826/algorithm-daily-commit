from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string):
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append("(")
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) !=0:
        return False
    else:
        return True

def separate_to_u_v(string):
    left = right = 0
    for i, ch in enumerate(string):
        if ch == "(": left += 1
        else:         right += 1
        if left == right:
            return string[:i+1], string[i+1:]
    return string, ""

def reverse_parenthesis(string):
    reversed_string = ""
    for char in string:
        if char == "(":
            reversed_string += ")"
        elif char == ")":
            reversed_string += "("
    return reversed_string

def change_to_correct_parenthesis(balanced_parentheses_string):
    if balanced_parentheses_string == "":
        return ""
    u, v = separate_to_u_v(balanced_parentheses_string)
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if (is_correct_parenthesis(balanced_parentheses_string)):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))