from gui import stack

main_operators = ['*', '+', '/', '-', '^']
single_operand_operators = ['cos', 'arccos', 'sqrt']
reserved = main_operators + ['(', ')']
reserved_variable_names = ['A', 'B', 'C', 'D']


def itemise(formula):
    items = []
    item = ''
    for char in formula:
        if char == ' ':
            continue

        if char in reserved:
            if item != '':
                items.append(item)
            items.append(char)
            item = ''
        else:
            item += char

    if item != '':
        items.append(item)

    ## Find which items are reserved  variables and which ones are numeric.
    # if it is numeric, replace the string with the numeric in the list
    variables = []
    for i, item in enumerate(items):
        if item in reserved_variable_names:
            variables.append(item)
        else:
            try:
                numeric = float(item)
                items[i] = numeric
            except:
                pass

    return items, variables

def string_to_rpn(items):
    main_stack = stack.StackClass()
    main_operators = ['*', '+', '/', '-', '^', 'cos', 'arccos', 'log', 'sqrt']
    rpn = []

    for item in items:
        if item == '(':
            main_stack.push_stack(item)
        elif item in main_operators:
            if main_stack.get_stack_top_element() in single_operand_operators:
                op = main_stack.pop_stack()
                rpn.append(op)

            main_stack.push_stack(item)
        elif item == ')':
            op = main_stack.pop_stack()
            if op:
                while op != '(':
                    rpn.append(op)
                    op = main_stack.pop_stack()
                if op == '(':
                    continue
                if main_stack:
                    op = main_stack.pop_stack()
                    rpn.append(op)

        else:
            rpn.append(item)

    if main_stack.get_stack_top_element():
        rpn.append(main_stack.pop_stack())

    print('rpn:', rpn)
    return rpn, variables


def eval_rpn(vars_vals, ops, rpn):
    pass


if __name__ == '__main__':
    # https: // www.mathblog.dk / tools / infix - postfix - converter /

    # formula = '((((arccos(A+D)*(cos(B)+25))-C)/((35)+(75))'  # A D + arccos B cos 25 + * C - 35 75 + /
    formula = 'sqrt(A)'

    items, variables = itemise(formula)
    rpn = string_to_rpn(items)
    print(items)
    print(variables)
    print(rpn)
    # vars_vals = {'A':1, 'B': 2, 'C':3}