# Balanced bracket https://www.hackerrank.com/challenges/balanced-brackets/problem

tests = [
    '[()][{}()][](){}([{}(())([[{}]])][])[]([][])(){}{{}{[](){}}}()[]({})[{}{{}([{}][])}]',
    '[()][{}[{}[{}]]][]{}[]{}[]{{}({}(){({{}{}[([[]][[]])()]})({}{{}})})}',
    '(])[{{{][)[)])(]){(}))[{(})][[{)(}){[(]})[[{}(])}({)(}[[()}{}}]{}{}}()}{({}](]{{[}}(([{]',
    '){[]()})}}]{}[}}})}{]{](]](()][{))])(}]}))(}[}{{)}{[[}[]'
]

openBracket = ['{', '[', '(']
closeBracket = ['}', ']', ')']

def isBalanced(s):
    stack = []
    for i in s:
        if i in openBracket:
            stack.append(i)
        elif i in closeBracket:
            pos = closeBracket.index(i)

            if  len(stack) > 0 and stack[-1] == openBracket[pos]:
                stack.pop()
            else:
                return 'NO'

    if len(stack) == 0:
        return 'YES'   
    else: 
        return 'NO'                     




for test in tests:
    print isBalanced(test)    