# s = (){}[] 를 포함한 문자열 ( 1 ~ 10^4 )

def solution(s):
    if len(s) % 2 != 0: return False
    stack = []

    for i in s:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        elif not stack or stack.pop() != i:
            return False

    return not stack

print(solution("({})"))