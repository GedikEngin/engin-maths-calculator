import numpy as np
from gui import stack
from maths.formula import poly_integration


class FormulaModel:
    list_of_functions = {   # list of functions that are being displayed in the GUI via dictionary
        'sqrt': 'np.sqrt',
        '+': '+',
        '*': '*',
        '^': '**',
        'sine(': 'np.sin(',
        'cosine(': 'np.cos(',
        'tangent(': 'np.tan(',
        'arcsin(': 'np.arcsin(',
        'arccos(': 'np.arccos(',
        'arctan(': 'np.arctan(',
        '/': '/',
        '-': '-',
        'ln': 'np.log(',
        'root': 'root'
    }

    main_operators = ['*', '+', '/', '-', '^', 'root']  # basic staple operators/operators that require 2 inputs
    single_operand_operators = ['cosine', 'arccos', 'sine', 'arcsin', 'tangent', 'arctan', 'blnkrt', 'sqrt', 'ln']  # operations that require one variable input
    reserved = main_operators + ['(', ')']  # type of brackets the rpn converter and evaluator will recognise
    reserved_variable_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']    # the variable names that will be recognised explicitly by the system

    def __init__(self, formula_text): # constructor method
        self.formula_text = formula_text
        self.vars = None
        self.formula = None

        self.convert_formula()  # first phase of the conversion
        # self.convert_formula_one()
        items, self.vars = self._itemise(self.formula_text)  # assigns the
        self.rpn = self.string_to_rpn(items)
        print(self.rpn, '\n', self.vars)
        # self.extract_vars()

    def get_vars(self):  # accessor method for variables
        return self.vars

    def get_rpn(self):   # accessor method for the rpn
        return self.rpn

    def convert_formula(self):
        operators = self.list_of_functions.keys()       # gets the list of functions and assigns into local variable
        self.formula = self.formula_text.replace(' ', '')       # string handling
        for op in operators:
            self.formula = self.formula.replace(op, self.list_of_functions[op])     # replaces the dictionary keys into formula

    def evaluate(self, vars):   # function to evaluate rpn

        answer = "Not possible to calculate"    # default answer
        vars_stack = stack.StackClass()  # assigning vars_stack to become a stack object
        for item in self.rpn:

            if item in self.main_operators:     # checking for main operators and removing from stack
                v1 = vars_stack.pop_stack()     # v1 is the item popped from stack
                v2 = vars_stack.pop_stack()     # v2 is the item popped from the stack

                answer = self.evaluate_normal_operator(item, v1, v2)        # answer is updated to the result from evaluate_normal_operator
                vars_stack.push_stack(answer)       # answer is pushed into the variables stack as it may be needed to calculate more items (rpn style)
            elif item in self.single_operand_operators:     # else if to check if the operator requires a single variable passed into it
                v1 = vars_stack.pop_stack()     # remove from stack
                answer = self.evaluate_single_oprand_operator(item, v1)     # evaluate answer
                vars_stack.push_stack(answer)    # push answer into stack to be used again

            elif type(item) is int or type(item) is float:      # checks if the next element in the stack is a float or int
                vars_stack.push_stack(item)     # and if so pushes it into the stack to be used

            elif item in vars.keys():       # check if the next element is a variable
                vars_stack.push_stack(float(vars[item]))        # turn into a string and push it into stack

            else:

                print("eval formula: the item is not recognised in the rpn {}".format(item))        # error message for admin/su

        return vars_stack.pop_stack()       # return the popped item

    def evaluate_normal_operator(self, operator, v1, v2):       # receive the operator and variables
        if operator == '*':
            return v1 * v2

        elif operator == '/':
            if v1 == 0:
                return 0
            elif v2 == 0:
                return
            return v1/v2

        elif operator == '+':
            return v1 + v2

        elif operator == '-':
            return v1-v2

        elif operator == 'root':
            return v1**(1/v2)       # uses fractional powers to evaluate roots

        else:
            print("formula_model: the normal operator not recognised")      # error message if it doesnt recognise normal operator

    def evaluate_single_oprand_operator(self, operator, v):
        if operator == "cosine":
            return np.cos(v)        # use numpy to evaluate

        elif operator == "sine":
            return np.sin(v)        # use numpy to evaluate

        elif operator == 'tangent':
            return np.tan(v)        # use numpy to evaluate

        elif operator == 'arccos':
            return np.arccos(v)     # use numpy to evaluate

        elif operator == 'arcsin':
            return np.arcsin(v)     # use numpy to evaluate

        elif operator == 'arctan':
            return np.arctan(v)     # use numpy to evaluate

        elif operator == 'ln':
            return np.log(v)        # use numpy to evaluate

        else:
            print("formula_model: the single operand operator not recognised")      # error message if it doesnt recognise single operand operator

    def string_to_rpn(self, items):     # function that focuses on converting the string received by formula submission into rpn
        main_stack = stack.StackClass()
        main_operators = self.main_operators + self.single_operand_operators
        rpn = []

        for item in items:
            if item == '(':
                main_stack.push_stack(item)
            elif item in main_operators:
                if main_stack.get_stack_top_element() in self.single_operand_operators:
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

        # print('rpn:', rpn)
        return rpn

    def _itemise(self, formula):
        items = []
        item = ''
        for char in formula:
            if char == ' ':
                continue

            if char in self.reserved:
                if item != '':
                    items.append(item)
                items.append(char)
                item = ''
            else:
                item += char

        if item != '':
            items.append(item)

        variables = []
        for i, item in enumerate(items):        # reiterates elements in items and checks if they are reserved
            if item in self.reserved_variable_names:
                variables.append(item)
            else:
                try:
                    numeric = float(item)       # converts item into a float
                    items[i] = numeric

                except:     # error handling to avoid any abnormalities
                    pass

        return items, variables


if __name__ == '__main__':
    # f1 = FormulaModel('Integrate(A)')
    # f1.evaluate({'A': '2*x^2'})

    f2 = FormulaModel('sqrt(A)')
    # f2.evaluate({'A': 2})
