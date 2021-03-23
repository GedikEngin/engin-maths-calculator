import stack

def string_to_rpn(formula):
    main_stack = stack.StackClass()
    operators = ['*', '+', '/', '-']
    rpn = ''

    for char in formula:
        if char == '':
            continue
        if char in operators or char == '(':
            main_stack.push_stack(char)
        elif char == ')':
            operator = main_stack.pop_stack()
            while operator != '(':
                rpn += operator
                operator = main_stack.pop_stack()

            if main_stack:
                operator = main_stack.pop_stack()

                if operator:
                    rpn += operator

        else:
            rpn += char

    print('rpn:', rpn)


if __name__ == '__main__':

    formula = '(A*(A+2)-C)/(3+7)'
    string_to_rpn(formula)