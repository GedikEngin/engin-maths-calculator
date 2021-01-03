from tkinter import *

class FormulaMainView(Frame):

    def __init__(self, parent): # gui parent not class parent
        super(FormulaMainView, self).__init__(parent)
        self.formula = None
        self.variables = None

        self.text_formula = Text(self, width=50, height=10, bg="grey50")
        self.text_formula.insert(END, 'Enter item description')
        self.text_formula.pack()


        # self.variables_frame = LabelFrame(self, text='Variables')
        # self.variables_frame.pack()

        left = Label(self, text="Please enter values for variables below")
        left.pack()

        self.variables_text = Text(self, width=50, height=10, bg="grey50")
        self.variables_text.insert(END, 'Enter item description')
        self.variables_text.pack()

        self.btn_eval = Button(self, relief=RAISED, text='Evaluate Formula', command=self.evaluate)
        self.btn_eval.pack()

    def add_new_formula(self, formula, variables):
        self.formula = formula
        self.variables = variables
        self._set_formula(formula)


    def _set_formula(self, formula):
        # todo gets the text of formula e.g. (SQRT(A)) and displays it in the text box
        pass


    def evaluate(self):

        variables_text = self.variables_text.get("1.0", END)
        variables_text = variables_text.replace(' ', '')
        variables_list = variables_text.split('\n')

        # Remove '' items that are resulted from extra \n values in the string
        # variables_list = [item for item in variables_list if item != '']
        # one liner
        cleared_list = []
        for item in variables_list:
            if item != '':
                cleared_list.append(item)
        variables_list = cleared_list

        ## Put the variables and their assigned values in a dictionary format
        print(variables_list)
        variables_dict = {}
        for variable in variables_list:
            var = variable.split('=')
            if len(var) < 2:
                print('Wrong variable provided')
            else:
                variables_dict[var[0]] = var[1]

        # https://stackoverflow.com/questions/9623114/check-if-two-unordered-lists-are-equal
        if set(self.variables) != set(variables_dict.keys()):
            print(' Wrong set of variables are provided')
        else:
            print(variables_dict)

        ### todo let the FC know that user has providded values for evaluation

if __name__ == '__main__':
    window = Tk()
    formainv = FormulaMainView(window)
    formainv.add_new_formula("sqrt(A)", ['A'])
    formainv.pack()
    window.mainloop()

    # todo formula view and formula creation directly communicate
