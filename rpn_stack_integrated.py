import stack

if __name__ == '__main__':

    # key lists
    operators = ['*', '+', '/', '-']
    brackets = ['(', ')']

    # different stack creations
    main_stack = stack.Stack()
    operator_stack = stack.Stack()

    # strings

    formula = "(3 * (6 + 2) - 4) / (3 + 7)" # answer is "3 6 2 + * 4 - 3 7 + /  "
    rpn = ''

    # main run

    for characters in formula:
        if characters == ' ': # checks if the formula string has spaces separating characters,
            continue # error handling to prevent breaks
        print(characters, '-----')

        if characters in operators or characters == '(': # checks if the character from formula is an operator or bracket opening
            main_stack.push_stack(characters) # pushes character into main stack

        elif characters == ')':
            operator_stack.push_stack(main_stack.pop_stack())

            while operator_stack.get_stack_top_element() != '(':
                rpn += operator_stack.get_stack_top_element()
                print('1', rpn)
                operator_stack.push_stack(main_stack.pop_stack())

            if main_stack:
                operator_stack.push_stack(main_stack.pop_stack())
                rpn += operator_stack.get_stack_top_element()

        else:
            rpn += characters
            print('2', rpn)

        print('main stack', main_stack.get_stack_elements())

    print('final rpn', rpn)