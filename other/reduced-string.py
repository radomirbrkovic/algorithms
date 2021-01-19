# Super Reduced String https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)  if len(stack) > 0 else "Empty String"               



print superReducedString("aaabccddd")
print superReducedString("aa")
print superReducedString("baab")