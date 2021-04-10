from gui import stack


def string_to_rpn(formula):
    main_stack = stack.StackClass()
    main_operators = ['*', '+', '/', '-', '^']
    reserved = main_operators + ['(', ')']
    rpn = ''

    item = ''
    i=0
    for char in formula:
        print("------------------------------------------")
        print(i, ' char: ', char)

        if char == ' ':
            continue
        elif char not in reserved:
            item += char
            if i+1 < len(formula) and formula[i+1] not in reserved:
                continue
        else:
            item = char

        print(i, " item:  ", item)
        item = ''
        i += 1


    #     if item in main_operators or item == '(':
    #         main_stack.push_stack(item)
    #         item = ''
    #     elif item == ')':
    #         operator = main_stack.pop_stack()
    #         if operator:
    #             while operator != '(':
    #                 rpn += ' ' + operator
    #                 operator = main_stack.pop_stack()
    #             if operator == '(':
    #                 continue
    #             if main_stack:
    #                 operator = main_stack.pop_stack()
    #                 rpn += ' ' + operator
    #         item = ''
    #
    #     else:
    #         rpn += ' ' + item
    #
    #     i= i+1
    #
    # print('rpn:', rpn)
    # return rpn

def eval_rpn(vars_vals, ops, rpn):
    pass


if __name__ == '__main__':

    formula = '(((arccos(A)*(cos(B)+25)-C)/((35)+(75))' # A arccos B cos * 25 + C - 35 75 + /

    rpn = string_to_rpn(formula)
    vars_vals = {'A':1, 'B': 2, 'C':3}

