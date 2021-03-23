from tkinter import *


class FormulaCreationDialogue(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.return_variable = None

        # formula
        self.text_item_desc = Text(self, width=80, height=15, bg="grey50")
        self.text_item_desc.grid(row=0, column=0, padx=2, pady=5, columnspan=7)

        # buttons

        btn_help = Button(self, relief=RAISED, text='Help', command=self.help_box, width=5)
        btn_help.grid(row=6, column=0, padx=2, pady=5, columnspan=3)

        btn_clear = Button(self, relief=RAISED, text='Clear', width=5)
        btn_clear.grid(row=6, column=3, padx=2, pady=5)

        btn_submit = Button(self, relief=RAISED, text='Submit', command=self.on_submit, width=5)
        btn_submit.grid(row=6, column=4, padx=2, pady=5, columnspan=3)

        # icon buttons
        ## used

        blank_power = PhotoImage(file=r"gui/icons/blank_power.png")
        btn_blank_power = Button(self, relief=RAISED, image=blank_power, command=lambda: self.update_text(
            "()^()"))  # todo redraw the icon to represent the change
        btn_blank_power.image = blank_power
        btn_blank_power.grid(row=1, column=0, padx=2, pady=5)

        square_root = PhotoImage(file=r"gui/icons/square_root.png")
        btn_square_root = Button(self, relief=RAISED, image=square_root, command=lambda: self.update_text("sqrt()"))
        btn_square_root.image = square_root
        btn_square_root.grid(row=1, column=1, padx=2, pady=5)

        blank_root = PhotoImage(file=r"gui/icons/blank_root.png")
        btn_blank_root = Button(self, relief=RAISED, image=blank_root, command=lambda: self.update_text("()blnkrt()"))
        btn_blank_root.image = blank_root
        btn_blank_root.grid(row=1, column=2, padx=2, pady=5)

        left_bracket = PhotoImage(file=r"gui/icons/left_bracket.png")
        btn_left_bracket = Button(self, relief=RAISED, image=left_bracket, command=lambda: self.update_text("("))
        btn_left_bracket.image = left_bracket
        btn_left_bracket.grid(row=2, column=1, padx=2, pady=5)

        right_bracket = PhotoImage(file=r"gui/icons/right_bracket.png")
        btn_right_bracket = Button(self, relief=RAISED, image=right_bracket, command=lambda: self.update_text(")"))
        btn_right_bracket.image = right_bracket
        btn_right_bracket.grid(row=2, column=2, padx=2, pady=5)

        multiplication = PhotoImage(file=r"gui/icons/multiplication.png")
        btn_multiplication = Button(self, relief=RAISED, image=multiplication, command=lambda: self.update_text("*"))
        btn_multiplication.image = multiplication
        btn_multiplication.grid(row=3, column=2, padx=2, pady=5)

        sin = PhotoImage(file=r"gui/icons/sin.png")
        btn_sin = Button(self, relief=RAISED, image=sin, command=lambda: self.update_text("sine()"))
        btn_sin.image = sin
        btn_sin.grid(row=4, column=0, padx=2, pady=5)

        cos = PhotoImage(file=r"gui/icons/cos.png")
        btn_cos = Button(self, relief=RAISED, image=cos, command=lambda: self.update_text("cosine()"))
        btn_cos.image = cos
        btn_cos.grid(row=4, column=1, padx=2, pady=5)

        tan = PhotoImage(file=r"gui/icons/tan.png")
        btn_tan = Button(self, relief=RAISED, image=tan, command=lambda: self.update_text("tan(tanget"))
        btn_tan.image = tan
        btn_tan.grid(row=4, column=2, padx=2, pady=5)

        variable_a = PhotoImage(file=r"gui/icons/variable_a.png")
        btn_variable_a = Button(self, relief=RAISED, image=variable_a, command=lambda: self.update_text("A"))
        btn_variable_a.image = variable_a
        btn_variable_a.grid(row=1, column=3, padx=2, pady=5)

        variable_b = PhotoImage(file=r"gui/icons/variable_b.png")
        btn_variable_b = Button(self, relief=RAISED, image=variable_b, command=lambda: self.update_text("B"))
        btn_variable_b.image = variable_b
        btn_variable_b.grid(row=1, column=4, padx=2, pady=5)

        variable_c = PhotoImage(file=r"gui/icons/variable_c.png")
        btn_variable_c = Button(self, relief=RAISED, image=variable_c, command=lambda: self.update_text("C"))
        btn_variable_c.image = variable_c
        btn_variable_c.grid(row=2, column=3, padx=2, pady=5)

        variable_d = PhotoImage(file=r"gui/icons/variable_d.png")
        btn_variable_d = Button(self, relief=RAISED, image=variable_d, command=lambda: self.update_text("D"))
        btn_variable_d.image = variable_d
        btn_variable_d.grid(row=2, column=4, padx=2, pady=5)

        variable_e = PhotoImage(file=r"gui/icons/variable_e.png")
        btn_variable_e = Button(self, relief=RAISED, image=variable_e, command=lambda: self.update_text("E"))
        btn_variable_e.image = variable_e
        btn_variable_e.grid(row=3, column=3, padx=2, pady=5)

        division = PhotoImage(file=r"gui/icons/division.png")
        btn_divison = Button(self, relief=RAISED, image=division, command=lambda: self.update_text("/"))
        btn_divison.image = division
        btn_divison.grid(row=3, column=1, padx=2, pady=5)

        arc_sin = PhotoImage(file=r"gui/icons/arc_sin.png")
        btn_arc_sin = Button(self, relief=RAISED, image=arc_sin, command=lambda: self.update_text("arcsin()"))
        btn_arc_sin.image = arc_sin
        btn_arc_sin.grid(row=5, column=0, padx=2, pady=5)

        arc_cos = PhotoImage(file=r"gui/icons/arc_cos.png")
        btn_arc_cos = Button(self, relief=RAISED, image=arc_cos, command=lambda: self.update_text("arccos()"))
        btn_arc_cos.image = arc_cos
        btn_arc_cos.grid(row=5, column=1, padx=2, pady=5)

        arc_tan = PhotoImage(file=r"gui/icons/arc_tan.png")
        btn_arc_tan = Button(self, relief=RAISED, image=arc_tan, command=lambda: self.update_text("arctan()"))
        btn_arc_tan.image = arc_tan
        btn_arc_tan.grid(row=5, column=2, padx=2, pady=5)

        variable_f = PhotoImage(file=r"gui/icons/variable_f.png")
        btn_variable_f = Button(self, relief=RAISED, image=variable_f, command=lambda: self.update_text("F"))
        btn_variable_f.image = variable_f
        btn_variable_f.grid(row=3, column=4, padx=2, pady=5)

        variable_g = PhotoImage(file=r"gui/icons/variable_g.png")
        btn_variable_g = Button(self, relief=RAISED, image=variable_g, command=lambda: self.update_text("G"))
        btn_variable_g.image = variable_g
        btn_variable_g.grid(row=4, column=3, padx=2, pady=5)

        variable_h = PhotoImage(file=r"gui/icons/variable_h.png")
        btn_variable_h = Button(self, relief=RAISED, image=variable_h, command=lambda: self.update_text("H"))
        btn_variable_h.image = variable_h
        btn_variable_h.grid(row=4, column=4, padx=2, pady=5)

        variable_i = PhotoImage(file=r"gui/icons/variable_i.png")
        btn_variable_i = Button(self, relief=RAISED, image=variable_i, command=lambda: self.update_text("I"))
        btn_variable_i.image = variable_i
        btn_variable_i.grid(row=5, column=3, padx=2, pady=5)

        variable_j = PhotoImage(file=r"gui/icons/variable_j.png")
        btn_variable_j = Button(self, relief=RAISED, image=variable_j, command=lambda: self.update_text("J"))
        btn_variable_j.image = variable_j
        btn_variable_j.grid(row=5, column=4, padx=2, pady=5)

        subtraction = PhotoImage(file=r"gui/icons/subtraction.png")
        btn_subtraction = Button(self, relief=RAISED, image=subtraction, command=lambda: self.update_text("-"))
        btn_subtraction.image = subtraction
        btn_subtraction.grid(row=3, column=0, padx=2, pady=5)

        num0 = PhotoImage(file=r"gui/icons/num0.png")
        btn_num0 = Button(self, relief=RAISED, image=num0, command=lambda: self.update_text("0"))
        btn_num0.image = num0
        btn_num0.grid(row=1, column=5, padx=2, pady=5)

        num1 = PhotoImage(file=r"gui/icons/num1.png")
        btn_num1 = Button(self, relief=RAISED, image=num1, command=lambda: self.update_text("1"))
        btn_num1.image = num1
        btn_num1.grid(row=1, column=6, padx=2, pady=5)

        num2 = PhotoImage(file=r"gui/icons/num2.png")
        btn_num2 = Button(self, relief=RAISED, image=num2, command=lambda: self.update_text("2"))
        btn_num2.image = num2
        btn_num2.grid(row=2, column=5, padx=2, pady=5)

        num3 = PhotoImage(file=r"gui/icons/num3.png")
        btn_num3 = Button(self, relief=RAISED, image=num3, command=lambda: self.update_text("3"))
        btn_num3.image = num3
        btn_num3.grid(row=2, column=6, padx=2, pady=5)

        num4 = PhotoImage(file=r"gui/icons/num4.png")
        btn_num4 = Button(self, relief=RAISED, image=num4, command=lambda: self.update_text("4"))
        btn_num4.image = num4
        btn_num4.grid(row=3, column=5, padx=2, pady=5)

        num5 = PhotoImage(file=r"gui/icons/num5.png")
        btn_num5 = Button(self, relief=RAISED, image=num5, command=lambda: self.update_text("5"))
        btn_num5.image = num5
        btn_num5.grid(row=3, column=6, padx=2, pady=5)

        num6 = PhotoImage(file=r"gui/icons/num6.png")
        btn_num6 = Button(self, relief=RAISED, image=num6, command=lambda: self.update_text("6"))
        btn_num6.image = num6
        btn_num6.grid(row=4, column=6, padx=2, pady=5)

        num7 = PhotoImage(file=r"gui/icons/num7.png")
        btn_num7 = Button(self, relief=RAISED, image=num7, command=lambda: self.update_text("7"))
        btn_num7.image = num7
        btn_num7.grid(row=4, column=5, padx=2, pady=5)

        num8 = PhotoImage(file=r"gui/icons/num8.png")
        btn_num8 = Button(self, relief=RAISED, image=num8, command=lambda: self.update_text("8"))
        btn_num8.image = num8
        btn_num8.grid(row=5, column=5, padx=2, pady=5)

        num9 = PhotoImage(file=r"gui/icons/num9.png")
        btn_num9 = Button(self, relief=RAISED, image=num9, command=lambda: self.update_text("9"))
        btn_num9.image = num9
        btn_num9.grid(row=5, column=6, padx=2, pady=5)

        addition = PhotoImage(file=r"gui/icons/addition.png")
        btn_addition = Button(self, relief=RAISED, image=addition, command=lambda: self.update_text("+"))
        btn_addition.image = addition
        btn_addition.grid(row=2, column=0, padx=2, pady=5)

        ## unused

        # e_to_the_power = PhotoImage(file=r"gui\icons\e_to_the_power.png")
        # btn_e_to_the_power = Button(self, relief=RAISED, image=e_to_the_power, command=lambda: self.update_text("e^()"))
        # btn_e_to_the_power.image = e_to_the_power
        # btn_e_to_the_power.grid(row=1, column=2, padx=2, pady=5)
        #
        # natural_log = PhotoImage(file=r"gui\icons\natural_log.png")
        # btn_natural_log = Button(self, relief=RAISED, image=natural_log, command=lambda: self.update_text("ln()"))
        # btn_natural_log.image = natural_log
        # btn_natural_log.grid(row=1, column=3, padx=2, pady=5)
        #
        # blank_base_log = PhotoImage(file=r"gui\icons\blank_base_log.png")
        # btn_blank_base_log = Button(self, relief=RAISED, image=blank_base_log, command=lambda: self.update_text("log[]()"))
        # btn_blank_base_log.image = blank_base_log
        # btn_blank_base_log.grid(row=1, column=4, padx=2, pady=5)
        #
        # cube_root = PhotoImage(file=r"gui\icons\cube_root.png")
        # btn_cube_root = Button(self, relief=RAISED, image=cube_root, command=lambda: self.update_text("cube_root()"))
        # btn_cube_root.image = cube_root
        # btn_cube_root.grid(row=1, column=6, padx=2, pady=5)
        #
        # fraction = PhotoImage(file=r"gui\icons\fraction.png")
        # btn_fraction = Button(self, relief=RAISED, image=fraction, command=lambda: self.update_text("()/()"))
        # btn_fraction.image = fraction
        # btn_fraction.grid(row=2, column=3, padx=2, pady=5)
        #
        # array5 = PhotoImage(file=r"gui\icons\array5.png")
        # btn_array5 = Button(self, relief=RAISED, image=array5, command=lambda: self.update_text("sum5()"))
        # btn_array5.image = array5
        # btn_array5.grid(row=2, column=4, padx=2, pady=5)
        #
        # array10 = PhotoImage(file=r"gui\icons\array10.png")
        # btn_array10 = Button(self, relief=RAISED, image=array10, command=lambda: self.update_text("sum10()"))
        # btn_array10.image = array10
        # btn_array10.grid(row=3, column=3, padx=2, pady=5)
        #
        # array15 = PhotoImage(file=r"gui\icons\array15.png")
        # btn_array15 = Button(self, relief=RAISED, image=array15, command=lambda: self.update_text("sum15()"))
        # btn_array15.image = array15
        # btn_array15.grid(row=3, column=4, padx=2, pady=5)
        #
        # squaring = PhotoImage(file=r"gui\icons\squaring.png")
        # btn_squaring = Button(self, relief=RAISED, image=squaring, command=lambda: self.update_text("^2"))
        # btn_squaring.image = squaring
        # btn_squaring.grid(row=1, column=0, padx=2, pady=5)

    def update_text(self, btn_text):
        print(btn_text)
        # idx = self.text_item_desc.curselection()
        self.text_item_desc.insert(END, btn_text)

    def help_box(self):
        help_box = Toplevel()

        text_item_desc = Text(help_box, width=50, height=10, bg="grey50")
        text_item_desc.insert(END, 'Enter item description')
        text_item_desc.pack()

    def on_submit(self):
        self.return_variable = self.text_item_desc.get("1.0", END).replace('\n', '')
        self.destroy()

    def show(self):
        self.wm_deiconify()  # they freeze and stop the code
        self.grab_set()  # they freeze and stop the code
        self.wait_window()  # it blocks the code, prevents the code from moving onto the next lin
        return self.return_variable


if __name__ == '__main__':
    window = Tk()
    createv = FormulaCreationDialogue(window)
    new_item_name_and_description = FormulaCreationDialogue(window).show()

    window.mainloop()
