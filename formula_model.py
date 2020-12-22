import numpy as np


class FormulaModel:
    list_of_functions = {
        'sqrt': 'np.sqrt()',
        'ln': 'np.log()',
        'cos': 'np.cos()',
        '+': '+',
        '*': '*'
    }


    removables = '()[]{} '

    def __init__(self, formula_text):
        self.formula_text = formula_text
        self.vars = None

        print(self.formula_text)
        self.extract_vars()
        self.convert_formula()

    def convert_formula(self):
        operators = self.list_of_functions.keys()
        self.formula = self.formula_text.replace(' ', '')

        for op in operators:
            self.formula = self.formula.replace(op, self.list_of_functions[op])

    def evaluate(self, vars):
        print(vars)
        for k in vars.keys():
            cmd = k+'='+vars[k]
            print(cmd)
            exec(cmd)

       eval(self.formula)



    def extract_vars(self):
        operators = self.list_of_functions.keys() # can be replaced with values to get the 'values'

        text = self.formula_text
        for op in operators:
            text = text.replace(op, '')

        for rm in self.removables:
            text = text.replace(rm, '')

        text = sorted(set(text))
        self.vars = tuple(text)



if __name__ == '__main__':
    f1 = FormulaModel('sqrt(A+b+C) * A')
    f1.evaluate({'A': '9', 'b': '4', 'C':'2'})


