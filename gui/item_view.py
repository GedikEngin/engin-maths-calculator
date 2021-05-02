from tkinter import *


class AddNewItemDialogue(Toplevel):  # inherit from tkinter class, TopLevel

    def __init__(self, parent):  # constructor with the parent being passed through
        Toplevel.__init__(self, parent)  # subclassing

        # adding modules/chapters/subchapters/formula entity
        self.sv_item_name = StringVar()
        entry_item_name = Entry(self, width=50, textvariable=self.sv_item_name)  # name entry box
        entry_item_name.grid(row=0, column=0, padx=2, pady=5)

        btn_submit_module = Button(self, text="Submit", width=50, relief=RAISED, bg="gray50",
                                   command=self.on_okay)  # submission button with function attachment
        btn_submit_module.grid(row=2, column=0, padx=2, pady=5)

        self.sv_item_desc = StringVar()  # description entry box
        self.text_item_desc = Text(self, width=50, height=10, bg="grey50")
        self.text_item_desc.insert(END, 'Enter item description')  # user prompt
        self.text_item_desc.grid(row=1, column=0, padx=0, pady=0)

        # init variables
        self.return_variable = None  # construction of variable

    def on_okay(self):
        name = self.sv_item_name.get()  # name assignment from name component of box entity
        desc = self.text_item_desc.get("1.0", END)  # grabs entry in textbox from char1 to end
        if desc == 'Enter item description\n':  # checks if description exists
            desc = ''  # else empty string

        self.return_variable = (name, desc)
        # self.sv_item_desc.get())

        print(self.return_variable)
        self.destroy()  # destroys box

    def show(self):
        self.wm_deiconify()  # freeze and stop the code
        self.grab_set()  # freeze and stop the code
        self.wait_window()  # it blocks the code, prevents the code from moving onto the next line

        return self.return_variable


class HPSListbox(LabelFrame):  # inherit from tkinter class

    def __init__(self, higher_gui, *args, **kwargs):
        super().__init__(higher_gui, *args, **kwargs)
        self.listbox = None
        self._make_gui()

        self._new_item_callbacks = []  # empty list for new items
        self._remove_item_callbacks = []  # empty list for items to be removed
        self._update_item_callbacks = []  # empty list for items to be updated
        self._select_item_callbacks = []  # empty list for items to be selected

        self.list_of_parents = []  # empty list for parents to be recorded

    def clear_list(self):  # clears list
        self.listbox.delete(0, END)  # select and deletes all characters

    def select_item_by_name(self, name):  # allows us to grab the item
        idx = self._get_item_index(name)  # gets index using name in listbox
        if idx:
            self.listbox.selection_clear(0, END)  # clears selection from start to end for listbox
            self.listbox.select_set(idx)  # gets listbox idx

    def delete_item_by_name(self, name):  # uses items name and idx to delete from listbox
        idx = self._get_item_index(name)
        self.listbox.delete(idx)

    def has_item(self, name):  # checks if item is in listbox
        contains = name in self.listbox.get(0, END)
        return contains

    def add_new_item(self, name):  # method to add items to listbox
        self._add_items_to_list(name)

    def get_selected_item(self):  # accessor method

        selection = self.listbox.curselection()  # uses user cursor selection
        if selection:  # if selection exists
            selection_name = self.listbox.get(selection[
                                                  0])  # returns the item selected by user, first item selected is 0
            # and it is configured so only 1 item can be selected at a time
        else:
            selection_name = None  # if selection does not exist
        return selection_name  # return none type

    def update_list_of_parents(self, list_of_parents):  # update the list of parent for object
        self.list_of_parents = list_of_parents

    def subscribe_to_new_item_event(self, command):  # subscriber method for the new items being added
        self._new_item_callbacks.append(command)

    def subscribe_to_removed_item_event(self, command):  # subscriber method for items that are being removed
        self._remove_item_callbacks.append(command)

    def subscribe_to_update_item_event(self, command):  # subscriber method for items being updated
        self._update_item_callbacks.append(command)

    def subscribe_to_select_item_event(self, command):  # subscriber method for items being selected
        self._select_item_callbacks.append(command)

    def _make_gui(self):  # creates main gui

        # window background color
        self.configure(bg='grey25')

        # listbox configuration

        self.listbox = Listbox(self, height=8,
                               bg="gray",
                               activestyle='dotbox',
                               font="Helvetica",
                               fg="white",
                               selectmode=SINGLE,
                               exportselection=False,
                               )
        self.listbox.bind('<<ListboxSelect>>', self._onselect)
        self.listbox.grid(row=0, column=0, columnspan=3, stick='nwse')

        # buttons

        btn_add_module = Button(self, text="+", width=16, relief=RAISED,
                                command=self._on_add_button_pressed)  # adding button, trigger for adding box pop up
        btn_add_module.grid(row=1, column=0, padx=2, pady=5)  # location and sizing

        btn_remove_module = Button(self, text="-", width=16, relief=RAISED,
                                   command=self._on_remove_button_pressed)  # removing button, trigger for deletion
        btn_remove_module.grid(row=1, column=1, padx=2, pady=5)  # location and sizing

        btn_edit_module = Button(self, text="~", width=16, relief=RAISED,
                                 command=self._on_edit_button_pressed)  # edit button, trigger for edit box pop up
        btn_edit_module.grid(row=1, column=2, padx=2, pady=5)  # location and sizing

    # on trigger
    def _on_edit_button_pressed(self):  # edit trigger
        new_item_name_and_description = AddNewItemDialogue(
            self).show()  # uses same window from adding, which passes information in the format (name, desc)
        # print(new_item_name_and_description)
        if new_item_name_and_description:  # new_item_name_and_description == (name, desc)
            new_name = new_item_name_and_description[0]  # new name is item[0]
            new_desc = new_item_name_and_description[1]  # new desc is item[1]

            idx = self.listbox.curselection()  # retrieved index from cursor selection
            old_name = self.listbox.get(idx)  # assigns it into old name, grabs name using idx

            if new_name:  # if new name exists
                # First remove the existing selected item
                if idx:
                    self._remove_items_from_list(idx)
                # Then add the edited name to the list box
                self._add_items_to_list(new_name)
                # Notify the controller about the change
            else:
                new_name = None  # no change

            if new_desc == 'Enter item description':
                new_desc = None  # no change

            for command in self._update_item_callbacks:  # sets up execution chain
                # command
                command(old_name, new_name, new_desc)  # updated values
                # self.subscribe_to_update_item_event(command)

    def _on_add_button_pressed(self):  # receives trigger from button that it is linked to
        new_item_name_and_description = AddNewItemDialogue(self).show()  # grabs information from box
        if new_item_name_and_description:  # checks if data exists
            self._add_items_to_list(
                new_item_name_and_description[0])  # adds items to the list, uses name item[0] to add to listbox
            for command in self._new_item_callbacks:
                # command
                command(new_item_name_and_description[0],
                        new_item_name_and_description[1])  # uses item[0]{name} and item[1]{desc}

    def _on_remove_button_pressed(self):  # deletion function
        idx = self.listbox.curselection()  # grabs index of selected item
        if idx:     # if idx exists

            name = self.listbox.get(idx)        # gets name using idx

            self._remove_items_from_list(idx)       # removes the item from listbox via idx
            for subscribed_functions in self._remove_item_callbacks:        # uses the subscription method to remove entity
                subscribed_functions(name)

    def _onselect(self, e):     # when anything is selected
        idx = self.listbox.curselection()       # retrieve idx
        if idx:
            name = self.listbox.get(idx)        # name is retrieved
            for command in self._select_item_callbacks:     # gets item callbacks
                command(name)       # passes name into command

    # actions

    def _add_items_to_list(self, item: str):        # adds item to the list and sets item as a string type
        self.listbox.insert(END, item)      # inserts into textbox from the end

    def _remove_items_from_list(self, idx):     # gets idx passed as a parameter
        self.listbox.delete(idx)        # deletes the item from the listbox with matching idx

    def _get_item_index(self, name):        # getting item index function
        for i, lb_entry in enumerate(self.listbox.get(0, END)):
            if name == lb_entry:
                return i
        return None


# def add_item_test(mod: HPSListbox):     # testing function when there was no proper gui to interact with
#     mod._add_items_to_list("alpha")
#     mod._add_items_to_list("bravo")
#     mod._add_items_to_list("charlie")
#     print(mod._get_item_index('bravo'))
#
#
# def delete_item_test(mod: HPSListbox):      # testing function when there was no proper gui to interact with
#     # mod._remove_items_from_list(0)
#     pass
#
#
# def clear_item_test(mod: HPSListbox):       # testing function when there was no proper gui to interact with
#     mod.clear_list()


if __name__ == '__main__':
    window = Tk()
    mv = HPSListbox(window)
    mv.pack()

    # add_item_test(mv)
    # delete_item_test(mv)
    # clear_item_test(mv)
    window.mainloop()
