from tkinter import *
from gui.formula_model import FormulaModel
from gui.formula_creation import FormulaCreationDialogue
import reverse_polish_notation_converter as rpn

class FormulaMainView(LabelFrame):

    def __init__(self, parent, text=''):  # gui parent not class parent
        super(FormulaMainView, self).__init__(parent, text=text)
        self.formula_text = None
        self.variables = None
        self.formula = None
        self.formula_save_subscribers = []
        self.formula_delete_subscribers = []

        btn_create_formula = Button(self, text="Create", width=25, relief=RAISED, bg="gray50",      # formula creation button
                                    command=self._on_create_formula)
        btn_create_formula.pack()

        btn_save_formula = Button(self, text="Save", width=25, relief=RAISED, bg="gray50",      # formula save button
                                  command=self._on_save_formula)
        btn_save_formula.pack()

        btn_delete_formula = Button(self, text="Delete", width=25, relief=RAISED, bg="gray50",      # formula delete button
                                    command=self._on_delete_formula)
        btn_delete_formula.pack()

        self.text_formula = Text(self, width=50, height=10, bg="grey50")        # textbox for the formula once submitted
        self.text_formula.tag_configure("bold", font="Helvetica 12 bold")       # visual customisation
        self.text_formula.tag_configure("normal", font="Helvetica 12")      # visual customisation
        self.text_formula.insert(END, 'Formula:', "bold")       # creates a simple text template
        self.text_formula.config(state=DISABLED)        # prevents users from editing from the main view
        self.text_formula.pack()

        # self.variables_frame = LabelFrame(self, text='Variables')     # old variables box
        # self.variables_frame.pack()

        # left = Label(self, text="Please enter values for variables below")        # old variables box
        # left.pack()

        self.variables_text = Text(self, width=50, height=10, bg="grey50")      # current variables box
        self.variables_text.insert(END, 'Enter variables and values:')      # prompt for users to edit and assign variables values
        self.variables_text.pack()

        self.btn_eval = Button(self, relief=RAISED, text='Evaluate Formula', command=self._on_evaluate)     # initiates the _on_evaluate function to start a pipeline to evaluate and return answer
        self.btn_eval.pack()

        self.answer_text = Text(self, width=50, height=10, bg="grey50")     # answer display box
        self.answer_text.tag_configure("bold", font="Helvetica 12 bold")
        self.answer_text.tag_configure("normal", font="Helvetica 12")
        self.answer_text.insert(END, 'Answer: \n \n', "bold")
        self.answer_text.config(state=DISABLED)     # prevents user editting once it is created
        self.answer_text.pack()

        self.rpn_text = Text(self, width=50, height=10, bg="grey50")        # rpn text box, allows users to see the rpn
        self.rpn_text.tag_configure("bold", font="Helvetica 12 bold")
        self.rpn_text.tag_configure("normal", font="Helvetica 12")
        self.rpn_text.insert(END, 'RPN:', "bold")
        self.rpn_text.config(state=DISABLED)        # disables to prevent editing by users
        self.rpn_text.pack()

    def subscribe_to_formula_save(self, subscriber):        # subscriber method, to save formula
        self.formula_save_subscribers.append(subscriber)

    def subscribe_to_formula_delete(self, subscribers):     # subscriber method to delete formula
        self.formula_delete_subscribers.append(subscribers)

    def add_new_formula(self, formula_text):        # the function that sets up formula text to be added stuff to
        if formula_text == 'clear':
            self.formula_text = None
            self.variables = None
            self.formula = None
            self._update_answer_textbox("")
            self._show_formula("")
            return

        self.formula_text = formula_text        # assignment for class
        self.formula = FormulaModel(formula_text)       # self.formula becomes an object for FormulaModel, OOP
        self._update_rpn_textbox(self.formula.get_rpn())        # gets rpn and pipelines the editing of the textbox to display rpn
        self.variables = self.formula.get_vars()        # grabs the list of variables that is in the formula
        self._show_formula(formula_text)        # uses a private function to show the formula on main view

    def _show_formula(self, formula):       # displays formula in main view

        self.text_formula.config(state=NORMAL)      # enables textbox editing
        self.text_formula.delete('1.0', END)
        self.text_formula.insert(END, 'Formula:' + '\n\n', "bold")
        self.text_formula.insert(END, '\t' + formula + '\n\n', "normal")        # change textbox to contain answer
        self.text_formula.config(state=DISABLED)        # restrict editing to prevent users from altering answer

    def _get_user_values(self):     # get user values for variables

        variables_text = self.variables_text.get("1.0", END)
        variables_text = variables_text.replace(' ', '')
        variables_list = variables_text.split('\n')

        # Remove '' items that are resulted from extra \n values in the string
        # variables_list = [item for item in variables_list if item != '']
        # one liner
        cleared_list = []       # creates empty list
        for item in variables_list:
            if item != '':      # looks for seperation
                cleared_list.append(item)       # append the cleared list to have the line of assignment
        variables_list = cleared_list       # passing the cleared list into variables list

        ## Put the variables and their assigned values in a dictionary format
        variables_dict = {}
        for variable in variables_list:
            var = variable.split('=')
            if len(var) < 2:
                self._update_answer_textbox('Wrong variable provided')
                return False

            else:
                try:
                    variables_dict[var[0]] = float(var[1])
                except ValueError:  # youtube --> works with numbers not strings so try except both tutorial
                    variables_dict[var[0]] = var[1]

        # https://stackoverflow.com/questions/9623114/check-if-two-unordered-lists-are-equal
        if set(self.variables) != set(variables_dict.keys()):       # comparison to check if variables match the dictionary set
            self._update_answer_textbox('Wrong set of variables are provided or this function is not implemented')      # error message if they do not match
            return False

        return variables_dict

    def _on_evaluate(self):     # evaluate trigger function
        values = self._get_user_values()        # grab values and pass into variable
        if values:      # simple true or false comparison
            answer = str(self.formula.evaluate(values))     # evaluates and assigns result into answer
            self._update_answer_textbox(answer)     # calls for function to update the answer textbox

    def _update_answer_textbox(self, answer):       # answer textbox update function
        self.answer_text.config(state=NORMAL)       # enables editing
        self.answer_text.delete('1.0', END)     # clears textbox from char1 to the end
        self.answer_text.insert(END, 'Answer:' + '\n\n', "bold")        # creates heading
        self.answer_text.insert(END, '\t' + answer + '\n\n', "normal")      # inserts answer into the textbox
        self.answer_text.config(state=DISABLED)     # disables editing of textbox

    def _update_rpn_textbox(self, rpn_text):        # rpn textbox update
        show_text = [str(item) for item in rpn_text]        # gets the components of the rpn as a list
        # return
        show_text = ' '.join(show_text)     # joins the text from showtext list into a string
        self.rpn_text.config(state=NORMAL)      # enables textbox editing
        self.rpn_text.delete('1.0', END)        # clears from char1 to end
        self.rpn_text.insert(END, 'RPN:' + '\n\n', "bold")      # format title
        self.rpn_text.insert(END, '\t' + show_text + '\n\n', "normal")      # insert text
        self.rpn_text.config(state=DISABLED)        # lock editing

    def _on_create_formula(self):       # private function for the formula on create button trigger
        formula_text = FormulaCreationDialogue(self).show()     # triggers the freezing of the parent window
        if formula_text is not None:        # checks if data type is not None
            self.add_new_formula(formula_text)      # adds the formula into formula textbox

    def _on_save_formula(self):     # private function for the formula on save button trigger
        for subscriber in self.formula_save_subscribers:        # uses the number of subscribers as a length for loop
            subscriber(self.formula_text)       # formula text is subscribed as save

    def _on_delete_formula(self):
        # print('delete')
        for subscriber in self.formula_delete_subscribers:      # uses the number of subcribers as a length for the loop
            subscriber(self.formula_text)       # formula text is deleted


if __name__ == '__main__':
    window = Tk()
    formainv = FormulaMainView(window)
    formainv.add_new_formula('Integrate(A)')
    formainv.pack()
    window.mainloop()
