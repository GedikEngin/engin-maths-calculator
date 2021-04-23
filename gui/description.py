from tkinter import *

class Description(LabelFrame): # inherit directly from tkinter

    def __init__(self, parent, text=''):

        super(Description, self).__init__(parent, text=text)   # possibly mention inheritance in design -- gui parent

        self.sv_item_desc = StringVar() # creation and config of text box
        self.text_item_desc = Text(self, width=50, height=58, bg="grey50")  # box config
        self.text_item_desc.tag_configure("bold", font="Helvetica 12 bold")  # title config
        self.text_item_desc.tag_configure("normal", font="Helvetica 12")    # main body config
        self.text_item_desc.config(state=DISABLED) # disables text box to prevent further editing
        self.text_item_desc.grid(row=1, column=0, padx=0, pady=0)   # alignment

    def update_text(self, desc, title='', append=False):   # text updating function
        self.text_item_desc.config(state=NORMAL)    # allows textbox to be edited
        if not append:
            self.text_item_desc.delete('1.0', END)  # deletes everything from first character to the end of the textbox

        self.text_item_desc.insert(END, title+'\n', "bold")  # formatting title line
        self.text_item_desc.insert(END, desc + '\n\n\n', "normal")  # formatted main text
        self.text_item_desc.config(state=DISABLED)  # shuts textbox back

if __name__ == '__main__':#
    window = Tk()
    descv = Description(window)
    descv.pack()
    window.mainloop()