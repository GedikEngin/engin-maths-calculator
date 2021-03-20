# rpn stack integrated
import stack

if __name__ == '__main__':

    # key assignments
    formula = '(3 * (6 + 2) - 4) / (3 + 7)'
    operators = ['*', '+', '/', '-']
    brackets = ['(', ')']
    rpn = ''

    # stack
    main_stack = stack.StackClass()

    # main code
    for char in formula:
        if char == '':
            continue
        print(char, '-=-=-=-')
        if char in operators or char == '(':
            main_stack.push_stack(char)
        elif char == ')':
            operator = main_stack.pop_stack()
            while operator != '(':
                rpn += operator
                print('op in while loop', operator)
                operator = main_stack.pop_stack()

            if main_stack:
                operator = main_stack.pop_stack()

                if operator:
                    rpn += operator

        else:
            rpn += char
            print('final else rpn', rpn)

    print('end -=-=-=-', rpn)
