## rpn testing

if __name__ == '__main__':

    s = "(3 * (6 + 2) - 4) / (3 + 7)"

    rpn_ans = "3 6 2 + * 4 - 3 7 + /  "
    answer = "(3 * (6 + 2) - 4) / (3 + 7)"
    operators = ['*', '+', '/', '-']
    brackets = ['(', ')']

    stack = []
    rpn = ""

    for ch in s:
        if ch == ' ':
            continue
        print(ch, '=================================')
        if ch in operators or ch == '(':
            stack.append(ch)
        elif ch == ')':
            op = stack.pop()
            while op != '(':
                rpn += op
                print('1', rpn)
                op = stack.pop()
            if stack:
                op = stack.pop()
                rpn += op
        else:
            rpn += ch
            print('2', rpn)
        print('stack', stack)

    print(rpn)
