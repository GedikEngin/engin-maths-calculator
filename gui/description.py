from tkinter import *

class Description(Frame):

    def __init__(self, parent):

        super(Description, self).__init__(parent)

        self.sv_item_desc = StringVar()
        self.text_item_desc = Text(self, width=50, height=10, bg="grey50")
        self.text_item_desc.tag_configure("bold", font="Helvetica 12 bold")
        self.text_item_desc.tag_configure("normal", font="Helvetica 12")

        self.text_item_desc.insert(END, 'Enter item description')
        self.text_item_desc.config(state=DISABLED)
        self.text_item_desc.grid(row=1, column=0, padx=0, pady=0)

    def update_text(self, desc, title='', append=False):
        self.text_item_desc.config(state=NORMAL)
        if not append:
            self.text_item_desc.delete('1.0', END)

        self.text_item_desc.insert(END, title+'\n', "bold")

        self.text_item_desc.insert(END, desc + '\n\n\n', "normal")

        self.text_item_desc.config(state=DISABLED)

if __name__ == '__main__':
    window = Tk()
    descv = Description(window)
    descv.pack()
    window.mainloop()