from tkinter import *
from gui.formula_model import FormulaModel

class FormulaMainView(Frame):

    def __init__(self, parent): # gui parent not class parent
        super(FormulaMainView, self).__init__(parent)
        self.formula_text = None
        self.variables = None
        self.formula = None

        btn_create_formula = Button(self, text="Create", width=25, relief=RAISED, bg="gray50",
                                    command=self._on_create_formula)
        btn_create_formula.pack()

        btn_save_formula = Button(self, text="Save", width=25, relief=RAISED, bg="gray50",
                                    command=self._on_save_formula)
        btn_save_formula.pack()

        btn_delete_formula = Button(self, text="Delete", width=25, relief=RAISED, bg="gray50",
                                    command=self._on_delete_formula)
        btn_delete_formula.pack()

        self.text_formula = Text(self, width=50, height=10, bg="grey50")
        self.text_formula.insert(END, 'Formula:')
        self.text_formula.tag_configure("bold", font="Helvetica 12 bold")
        self.text_formula.tag_configure("normal", font="Helvetica 12")
        self.text_formula.config(state=DISABLED)
        self.text_formula.pack()


        # self.variables_frame = LabelFrame(self, text='Variables')
        # self.variables_frame.pack()

        left = Label(self, text="Please enter values for variables below")
        left.pack()

        self.variables_text = Text(self, width=50, height=10, bg="grey50")
        self.variables_text.insert(END, 'Enter variables and values:')
        self.variables_text.pack()

        self.btn_eval = Button(self, relief=RAISED, text='Evaluate Formula', command=self._on_evaluate)
        self.btn_eval.pack()

        self.answer_text = Text(self, width=50, height=10, bg="grey50")
        self.answer_text.insert(END, 'Answer: \n \n')
        #todo insert disable feature
        # get the answer variable and update the textbox
        self.answer_text.pack()

    def add_new_formula(self, formula_text):
        self.formula_text = formula_text
        self.formula = FormulaModel(formula_text)
        self.variables = self.formula.extract_vars()
        self._show_formula(formula_text)


    def _show_formula(self, formula):
        # todo gets the text of formula e.g. (SQRT(A)) and displays it in the text box
        # todo use the formula parameter passed into the function to display in the gui textbox
        # todo use --> _update_formula_textbox()

        self.text_formula.config(state=NORMAL)
        self.text_formula.delete('1.0', END)
        self.text_formula.insert(END, 'Formula:'+'\n\n', "bold")
        self.text_formula.insert(END, '\t' + formula + '\n\n', "normal")
        self.text_formula.config(state=DISABLED)


    def _get_user_values(self):

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
        variables_dict = {}
        for variable in variables_list:
            var = variable.split('=')
            if len(var) < 2:
                self._update_answer_textbox('Wrong variable provided')
                return False
                # todo set the value of the text box, it is disabled initially, create a function that is dedicatted to updating the textbox
            else:
                try:
                    variables_dict[var[0]] = float(var[1])
                except ValueError: # youtube --> works with numbers not strings so try except both tutorial
                    variables_dict[var[0]] = var[1]

        # https://stackoverflow.com/questions/9623114/check-if-two-unordered-lists-are-equal
        if set(self.variables) != set(variables_dict.keys()):
            self._update_answer_textbox('Wrong set of variables are provided')
            return False


        return variables_dict

    def _on_evaluate(self):
        values = self._get_user_values()
        if values:
            answer = str(self.formula.evaluate(values))
            self._update_answer_textbox(answer)



    def _update_answer_textbox(self, answer):
        self.answer_text.config(state=NORMAL)
        self.answer_text.delete('1.0', END)
        self.answer_text.insert(END, 'Answer:'+'\n\n', "bold")
        self.answer_text.insert(END, '\t' + answer + '\n\n', "normal")
        self.answer_text.config(state=DISABLED)


    def _on_create_formula(self):
        print('create')


    def _on_save_formula(self):
        print('save')


    def _on_delete_formula(self):
        print('delete')


if __name__ == '__main__':
    window = Tk()
    formainv = FormulaMainView(window)
    formainv.add_new_formula('Integrate(A)')
    formainv.pack()
    window.mainloop()

