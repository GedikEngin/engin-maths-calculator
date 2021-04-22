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
        'ln': 'np.log(',
        'root':'root'
    }

    main_operators = ['*', '+', '/', '-', '^', 'root']
    single_operand_operators = ['cosine', 'arccos', 'sine', 'arcsin', 'tangent', 'arctan', 'blnkrt', 'sqrt', 'ln']
    reserved = main_operators + ['(', ')']
    reserved_variable_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

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

    def get_vars(self):
        return self.vars

    def get_rpn(self):
        return self.rpn

    def convert_formula(self):
        operators = self.list_of_functions.keys()
        self.formula = self.formula_text.replace(' ', '')
        for op in operators:
            self.formula = self.formula.replace(op, self.list_of_functions[op])

    def evaluate(self, vars):

        answer = "Not possible to calculate"
        vars_stack = stack.StackClass()
        for item in self.rpn:

            if item in self.main_operators:
                v1 = vars_stack.pop_stack()
                v2 = vars_stack.pop_stack()

                answer = self.evaluate_normal_operator(item, v1, v2)
                vars_stack.push_stack(answer)
            elif item in self.single_operand_operators:
                v1 = vars_stack.pop_stack()

                answer = self.evaluate_single_oprand_operator(item, v1)
                vars_stack.push_stack(answer)
            elif type(item) is int or type(item) is float:
                vars_stack.push_stack(item)
            elif item in vars.keys():
                vars_stack.push_stack(float(vars[item]))
            else:
                # todo show this in the gui
                print("eval formula: the item is not recognised in the rpn {}".format(item))

        return vars_stack.pop_stack()

    def evaluate_normal_operator(self, operator, v1, v2):
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
            return v1**(1/v2)

        else:
            print("fomula_modl: the normal operator not recognised")

    def evaluate_single_oprand_operator(self, operator, v):
        if operator == "cosine":
            return np.cos(v)
        elif operator == "sine":
            return np.sin(v)
        elif operator == 'tangent':
            return np.tan(v)
        elif operator == 'arccos':
            return np.arccos(v)
        elif operator == 'arcsin':
            return np.arcsin(v)
        elif operator == 'arctan':
            return np.arctan(v)
        elif operator == 'ln':
            return np.log(v)
        else:
            print("fomula_modl: the single operand operator not recognised")

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
