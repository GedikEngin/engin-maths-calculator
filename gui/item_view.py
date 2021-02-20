from tkinter import *


class AddNewItemDialogue(Toplevel):

    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        # adding module
        self.sv_item_name = StringVar()
        entry_item_name = Entry(self, width=50, textvariable=self.sv_item_name)
        entry_item_name.grid(row=0, column=0, padx=2, pady=5)

        btn_submit_module = Button(self, text="Submit", width=50, relief=RAISED, bg="gray50", command=self.on_okay)
        btn_submit_module.grid(row=2, column=0, padx=2, pady=5)

        self.sv_item_desc = StringVar()
        self.text_item_desc = Text(self, width=50, height=10, bg="grey50")
        self.text_item_desc.insert(END, 'Enter item description')
        self.text_item_desc.grid(row=1, column=0, padx=0, pady=0)

        # init variables
        self.return_variable = None



        # todo format the gui to have description box, on submit, print out name and description

    def on_okay(self):
        name = self.sv_item_name.get()
        desc = self.text_item_desc.get("1.0", END)
        if desc == 'Enter item description\n':
            desc = ''

        self.return_variable = (name, desc)
        # self.sv_item_desc.get()) # todo solve, how to get data from a textbox

        print(self.return_variable)
        self.destroy()

    def show(self):

        self.wm_deiconify() # they freeze and stop the code
        self.grab_set() # they freeze and stop the code
        self.wait_window() # it blocks the code, prevents the code from moving onto the next line

        # after return goes here
        # todo get the text from the description box (!!!! YOU MIGHT HAVE TO DEFINE STRING VARIABLE, SIMILAR TO THE ENTRIES!!!!)

        return self.return_variable


class HPSListbox(LabelFrame): # footnote change in design chapter

    def __init__(self, higher_gui, *args, **kwargs):
        super().__init__(higher_gui, *args, **kwargs)
        self.listbox = None
        self._make_gui()

        self._new_item_callbacks = []
        self._remove_item_callbacks = []
        self._update_item_callbacks = []
        self._select_item_callbacks = []

        self.list_of_parents = []


    def clear_list(self):
        self.listbox.delete(0, END)

    def select_item_by_name(self, name):
        idx = self._get_item_index(name)
        if idx:
            self.listbox.selection_clear(0, END)
            self.listbox.select_set(idx)

    def delete_item_by_name(self, name):
        idx = self._get_item_index(name)
        self.listbox.delete(idx)

    def has_item(self, name):
        contains = name in self.listbox.get(0, END)
        return contains

    def add_new_item(self, name):
        self._add_items_to_list(name)

    def get_selected_item(self):

        selection = self.listbox.curselection()
        if selection:
            selection_name = self.listbox.get(selection[0])
        else:
            selection_name = None
        return selection_name

    def update_list_of_parents(self, list_of_parents):
        self.list_of_parents = list_of_parents

    def subscribe_to_new_item_event(self, command):
        self._new_item_callbacks.append(command)

    def subscribe_to_removed_item_event(self, command):
        self._remove_item_callbacks.append(command)

    def subscribe_to_update_item_event(self, command):
        self._update_item_callbacks.append(command)

    def subscribe_to_select_item_event(self, command):
        self._select_item_callbacks.append(command)

    def _make_gui(self):

        # window background color
        self.configure(bg='grey25')

        # listbox

        self.listbox = Listbox(self, height=8,
                                 bg="gray",
                                 activestyle='dotbox',
                                 font="Helvetica",
                                 fg="white",
                                 selectmode = SINGLE,
                                 exportselection=False,
                               )
        self.listbox.bind('<<ListboxSelect>>', self._onselect)
        self.listbox.grid(row=0, column=0, columnspan=3, stick='nwse')

        # buttons

        btn_add_module = Button(self, text="+", width=16, relief=RAISED, command=self._on_add_button_pressed)
        btn_add_module.grid(row=1, column=0, padx=2, pady=5)

        btn_remove_module = Button(self, text="-", width=16, relief=RAISED, command=self._on_remove_button_pressed)
        btn_remove_module.grid(row=1, column=1, padx=2, pady=5)

        btn_edit_module = Button(self, text="~", width=16, relief=RAISED, command=self._on_edit_button_pressed)
        btn_edit_module.grid(row=1, column=2, padx=2, pady=5)

    # on trigger
    def _on_edit_button_pressed(self):
        new_item_name_and_description = AddNewItemDialogue(self).show()
        print(new_item_name_and_description)
        if new_item_name_and_description:
            new_name = new_item_name_and_description[0]
            new_desc = new_item_name_and_description[1]

            idx = self.listbox.curselection()
            old_name = self.listbox.get(idx)

            if new_name:
                # First remove the existing selected item
                if idx:
                    self._remove_items_from_list(idx)
                # Then add the edited name to the list box
                self._add_items_to_list(new_name)
                # Notify the controller about the change
            else:
                new_name = None

            if new_desc == 'Enter item description':
                new_desc = None

            for command in self._update_item_callbacks:
                # command
                command(old_name, new_name, new_desc)
                # self.subscribe_to_update_item_event(command)

    def _on_add_button_pressed(self):
        new_item_name_and_description = AddNewItemDialogue(self).show()
        if new_item_name_and_description:
            self._add_items_to_list(new_item_name_and_description[0])
            for command in self._new_item_callbacks:
                # command
                command(new_item_name_and_description[0], new_item_name_and_description[1])

            # todo send a signal to the controller that new item is added so it updates the database (with navid)
            # todo receive the description of the item as well ^^^

    def _on_remove_button_pressed(self):
        idx = self.listbox.curselection()
        if idx:

            name = self.listbox.get(idx)

            self._remove_items_from_list(idx)
            for subscribed_functions in self._remove_item_callbacks:

                subscribed_functions(name)

    def _onselect(self, e):
        idx = self.listbox.curselection()
        if idx:
            name = self.listbox.get(idx)
            for command in self._select_item_callbacks:
                command(name)


    # actions

    def _add_items_to_list(self, item: str):
        # todo when a new item is added read all the items from the listbox sort them alphabetically and add them to the list automatically (with navid)
        self.listbox.insert(END, item)


    def _remove_items_from_list(self, idx):
        self.listbox.delete(idx)
        
    def _get_item_index(self, name):
        for i,  lb_entry in enumerate(self.listbox.get(0, END)):
            if name == lb_entry:
                return i
        return None


def add_item_test(mod: HPSListbox):
    mod._add_items_to_list("alpha")
    mod._add_items_to_list("bravo")
    mod._add_items_to_list("charlie")
    print(mod._get_item_index('bravo'))

def delete_item_test(mod: HPSListbox):
    # mod._remove_items_from_list(0)
    pass

def clear_item_test(mod: HPSListbox):
    mod.clear_list()

if __name__ == '__main__':
    window = Tk()
    mv = HPSListbox(window)
    mv.pack()

    # add_item_test(mv)
    # delete_item_test(mv)
    # clear_item_test(mv)
    window.mainloop()

