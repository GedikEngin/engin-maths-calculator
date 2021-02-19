import numpy as np
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
        # 'ln': 'np.log',
        # 'Integrate': 'poly_integration',
        # 'sum5':
    }

    removables = '()[]{} '

    def __init__(self, formula_text):
        self.formula_text = formula_text
        self.vars = None
        self.formula = None

        self.convert_formula()
        self.extract_vars()

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



    def extract_vars(self):
        operators = self.list_of_functions.keys() # can be replaced with values to get the 'values'

        text = self.formula_text
        for op in operators:
            text = text.replace(op, '')

        for rm in self.removables:
            text = text.replace(rm, '')

        text = sorted(set(text))
        self.vars = tuple(text)

        return self.vars



if __name__ == '__main__':
    f1 = FormulaModel('Integrate(A)')
    f1.evaluate({'A': '2*x^2'})

    f2 = FormulaModel('sqrt(A)')
    f2.evaluate({'A': 2})
