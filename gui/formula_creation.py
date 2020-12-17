from tkinter import *

class FormulaCreationFrame(Frame):

    def __init__(self, parent):

        super(FormulaCreationFrame, self).__init__(parent)

        # desc
        self.text_item_desc = Text(self, width=50, height=25, bg="grey50")
        self.text_item_desc.grid(row=0, column=0, padx=2, pady=5)

        # button
        photo = PhotoImage(file=r"C:\Users\enggd\PycharmProjects\nea-calculator\icons\square_root_2_blank.png")

        btn_0 = Button(self, relief=RAISED, image=photo, command=lambda: self.update_text("sqrt"))
        btn_0.image = photo
        btn_0.grid(row=1, column=0, padx=2, pady=5)

        # btn_1 = Button(self, text="1", width=50, relief=RAISED, bg="gray50")
        # btn_1.grid(row=2, column=0, padx=2, pady=5)

    def update_text(self, btn_text):
        print(btn_text)


if __name__ == '__main__':
    window = Tk()
    createv = FormulaCreationFrame(window)
    createv.pack()
    window.mainloop()