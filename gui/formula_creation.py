from tkinter import *

class FormulaCreationFrame(Frame):

    def __init__(self, parent):

        super(FormulaCreationFrame, self).__init__(parent)

        # desc
        self.text_item_desc = Text(self, width=50, height=25, bg="grey50")
        self.text_item_desc.grid(row=0, column=0, padx=2, pady=5, columnspan = 6)

        # buttons
        addition = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\addition.png")
        btn_addition = Button(self, relief=RAISED, image=addition, command=lambda: self.update_text("+"))
        btn_addition.image = addition
        btn_addition.grid(row=1, column=0, padx=2, pady=5)

        arc_cos = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\arc_cos.png")
        btn_arc_cos = Button(self, relief=RAISED, image=arc_cos, command=lambda: self.update_text("cos-1()"))
        btn_arc_cos.image = arc_cos
        btn_arc_cos.grid(row=1, column=1, padx=2, pady=5)


        arc_sin = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\arc_sin.png")
        btn_arc_sin = Button(self, relief=RAISED, image=arc_sin, command=lambda: self.update_text("sin-1()"))
        btn_arc_sin.image = arc_sin
        btn_arc_sin.grid(row=1, column=2, padx=2, pady=5)

        arc_tan = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\arc_tan.png")
        btn_ar_tan = Button(self, relief=RAISED, image=arc_tan, command=lambda: self.update_text("tan-1()"))
        btn_ar_tan.image = arc_tan
        btn_ar_tan.grid(row=1, column=3, padx=2, pady=5)

        blank_base_log = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\blank_base_log.png")
        btn_blank_base_log = Button(self, relief=RAISED, image=blank_base_log, command=lambda: self.update_text("log[]()"))
        btn_blank_base_log.image = blank_base_log
        btn_blank_base_log.grid(row=1, column=4, padx=2, pady=5)

        blank_power = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\blank_power.png")
        btn_blank_power = Button(self, relief=RAISED, image=blank_power, command=lambda: self.update_text("x^()"))
        btn_blank_power.image = blank_power
        btn_blank_power.grid(row=1, column=5, padx=2, pady=5)

        blank_root = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\blank_root.png")
        btn_blank_root = Button(self, relief=RAISED, image=blank_root, command=lambda: self.update_text("[]rt()"))
        btn_blank_root.image = blank_root
        btn_blank_root.grid(row=2, column=0, padx=2, pady=5)

        cos = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\cos.png")
        btn_cos = Button(self, relief=RAISED, image=cos, command=lambda: self.update_text("cos()"))
        btn_cos.image = cos
        btn_cos.grid(row=2, column=1, padx=2, pady=5)

        division = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\division.png")
        btn_divison = Button(self, relief=RAISED, image=division, command=lambda: self.update_text("/"))
        btn_divison.image = division
        btn_divison.grid(row=2, column=2, padx=2, pady=5)

        e_to_the_power = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\e_to_the_power.png")
        btn_e_to_the_power = Button(self, relief=RAISED, image=e_to_the_power, command=lambda: self.update_text("e^()"))
        btn_e_to_the_power.image = e_to_the_power
        btn_e_to_the_power.grid(row=2, column=3, padx=2, pady=5)

        fraction = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\fraction.png")
        btn_fraction = Button(self, relief=RAISED, image=fraction, command=lambda: self.update_text("()/()"))
        btn_fraction.image = fraction
        btn_fraction.grid(row=2, column=4, padx=2, pady=5)

        left_bracket = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\left_bracket.png")
        btn_left_bracket = Button(self, relief=RAISED, image=left_bracket, command=lambda: self.update_text("("))
        btn_left_bracket.image = left_bracket
        btn_left_bracket.grid(row=2, column=5, padx=2, pady=5)

        multiplication = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\multiplication.png")
        btn_multiplication = Button(self, relief=RAISED, image=multiplication, command=lambda: self.update_text("*"))
        btn_multiplication.image = multiplication
        btn_multiplication.grid(row=3, column=0, padx=2, pady=5)

        natural_log = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\natural_log.png")
        btn_natural_log = Button(self, relief=RAISED, image=natural_log, command=lambda: self.update_text("ln()"))
        btn_natural_log.image = natural_log
        btn_natural_log.grid(row=3, column=1, padx=2, pady=5)

        right_bracket = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\right_bracket.png")
        btn_right_bracket = Button(self, relief=RAISED, image=right_bracket, command=lambda: self.update_text(")"))
        btn_right_bracket.image = right_bracket
        btn_right_bracket.grid(row=3, column=2, padx=2, pady=5)

        sin = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\sin.png")
        btn_sin = Button(self, relief=RAISED, image=sin, command=lambda: self.update_text("sin()"))
        btn_sin.image = sin
        btn_sin.grid(row=3, column=3, padx=2, pady=5)

        square_root = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\square_root.png")
        btn_square_root = Button(self, relief=RAISED, image=square_root, command=lambda: self.update_text("sqrt()"))
        btn_square_root.image = square_root
        btn_square_root.grid(row=3, column=4, padx=2, pady=5)

        squaring = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\squaring.png")
        btn_squaring = Button(self, relief=RAISED, image=squaring, command=lambda: self.update_text("^2"))
        btn_squaring.image = squaring
        btn_squaring.grid(row=3, column=5, padx=2, pady=5)

        subtraction = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\subtraction.png")
        btn_subtraction = Button(self, relief=RAISED, image=subtraction, command=lambda: self.update_text("-"))
        btn_subtraction.image = subtraction
        btn_subtraction.grid(row=4, column=0, padx=2, pady=5)

        tan = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\tan.png")
        btn_tan = Button(self, relief=RAISED, image=tan, command=lambda: self.update_text("tan(tan"))
        btn_tan.image = tan
        btn_tan.grid(row=4, column=1, padx=2, pady=5)

        variable_a = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\variable_a.png")
        btn_variable_a = Button(self, relief=RAISED, image=variable_a, command=lambda: self.update_text("A"))
        btn_variable_a.image = variable_a
        btn_variable_a.grid(row=4, column=2, padx=2, pady=5)

        variable_b = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\variable_b.png")
        btn_variable_b = Button(self, relief=RAISED, image=variable_b, command=lambda: self.update_text("B"))
        btn_variable_b.image = variable_b
        btn_variable_b.grid(row=4, column=3, padx=2, pady=5)

        variable_c = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\variable_c.png")
        btn_variable_c = Button(self, relief=RAISED, image=variable_c, command=lambda: self.update_text("C"))
        btn_variable_c.image = variable_c
        btn_variable_c.grid(row=4, column=4, padx=2, pady=5)

        variable_d = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\variable_d.png")
        btn_variable_d = Button(self, relief=RAISED, image=variable_d, command=lambda: self.update_text("D"))
        btn_variable_d.image = variable_d
        btn_variable_d.grid(row=4, column=5, padx=2, pady=5)



    def update_text(self, btn_text):
        print(btn_text)
        self.text_item_desc.insert(END, btn_text)


if __name__ == '__main__':
    window = Tk()
    createv = FormulaCreationFrame(window)
    createv.pack()
    window.mainloop()