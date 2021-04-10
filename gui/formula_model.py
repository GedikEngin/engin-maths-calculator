import numpy as np
from gui import stack
from maths.formula import poly_integration


class FormulaModel:
    list_of_functions = {
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
        'blnkrt(': '**(1/'
    }

    main_operators = ['*', '+', '/', '-', '^']
    single_operand_operators = ['cos', 'arccos', 'sqrt']
    reserved = main_operators + ['(', ')']
    reserved_variable_names = ['A', 'B']  # Todo extend to full letters

    def __init__(self, formula_text):
        self.formula_text = formula_text
        self.vars = None
        self.formula = None

        self.convert_formula()
        # self.convert_formula_one()
        items, self.vars = self._itemise(self.formula_text)
        self.rpn = self.string_to_rpn(items)
        print(self.rpn, '\n', self.vars)
        # self.extract_vars()

    def get_rpn(self):
        return self.rpn

    def convert_formula(self):
        operators = self.list_of_functions.keys()
        self.formula = self.formula_text.replace(' ', '')
        for op in operators:
            self.formula = self.formula.replace(op, self.list_of_functions[op])

    def evaluate(self, vars):

        for key in vars:
            if key == 'A':
                A = vars[key]
            elif key == 'B':
                B = vars[key]
            elif key == 'C':
                C = vars[key]
            elif key == 'D':
                D = vars[key]
            elif key == 'E':
                E = vars[key]
            elif key == 'F':
                F = vars[key]
            elif key == 'G':
                G = vars[key]
            elif key == 'H':
                H = vars[key]
            elif key == 'I':
                I = vars[key]
            elif key == 'J':
                J = vars[key]

        res = eval(self.formula)
        return res

    # def extract_vars(self):
    #     operators = self.list_of_functions.keys() # can be replaced with values to get the 'values'
    #
    #     text = self.formula_text
    #     for op in operators:
    #         text = text.replace(op, '')
    #
    #     for rm in self.reserved:
    #         text = text.replace(rm, '')
    #
    #     text = sorted(set(text))
    #     self.vars = tuple(text)
    #
    #     return self.vars

    def string_to_rpn(self, items):
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

        print('rpn:', rpn)
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

        ## Find which items are reserved  variables and which ones are numeric.
        # if it is numeric, replace the string with the numeric in the list
        variables = []
        for i, item in enumerate(items):
            if item in self.reserved_variable_names:
                variables.append(item)
            else:
                try:
                    numeric = float(item)
                    items[i] = numeric

                except:
                    pass

        return items, variables


if __name__ == '__main__':
    # f1 = FormulaModel('Integrate(A)')
    # f1.evaluate({'A': '2*x^2'})

    f2 = FormulaModel('sqrt(A)')
    # f2.evaluate({'A': 2})
