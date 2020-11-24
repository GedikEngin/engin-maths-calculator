from gui.item_view import *
import model

# mv = None
# chv = None
# subch = None

window = Tk()


def _make_widgets():
    global mv, chv, subch
    mv = HPSListbox(window)
    mv.grid(row=0, column=0)
    mv.subscribe_to_new_item_event(_on_module_new_item)
    mv.subscribe_to_removed_item_event(_on_module_removed_item)
    mv.subscribe_to_update_item_event(_on_module_updated_item)
    mv.subscribe_to_select_item_event(_on_module_selected_item)

    chv = HPSListbox(window)
    chv.grid(row=0, column=1)

    subch = HPSListbox(window)
    subch.grid(row=0, column=2)

# Module View
def _on_module_new_item(name, desc):
    print('NEA: Controller received module name and desc', name, desc)
    if model.add_new_module(name, desc):
        #clear sub/chapters listbox
        chv.clear_list()
        subch.clear_list()
        mv.select_item_by_name(name) #todo we have a bug that the first item is not selected
        pass
    else:
        mv.delete_item_by_name(name)
        print('An error is present: \n Check if the module is already present within the database')
        print('The added item has been deleted')

    # todo
    # story:
    # when new item is added the item name and description is saved into the database
    # it is selected and then the description is displayed in the description box
    # blank chapters and subchapters boxes appear that are linked to the new item


def _on_module_removed_item(name):
    print('Controller is deleting module name', name)
    # todo receive signal on removal --> subscribe this function to the modules list
    # story:
    # the item is removed, and all the linked chapters and subchapters and formulas removed
    # every item with a key that is linked to a module key is removed from the database
    # chapters and subchapters get cleared
    # the selection will go to a default, pre-existing item

def _on_module_updated_item(name, desc):
    print('Controller received module name and desc', name, desc)
    # todo
    # story:
    # when updated the items name and description are updated only, all the links remain the same
    # the display in the list box and description will change to match the updated item

def _on_module_selected_item(name, desc):
    print('Controller received module name and desc', name, desc)
    # todo
    # story:
    # when the module is selected, we get the list of all chapter items to populate the chapter list box
    # the chapter list box is populated with the retrieved items
    # the description box is populated with the selected item
    # the first chapter is auto selected
    # ^^ the controller also retrieves the linked subchapters

# Chapter View
def _on_chapter_new_item(name, desc):
    print('Controller received chapter name and desc', name, desc)
    # todo

# Sub chapter View
def _on_subchapter_new_item(name, desc):
    print('Controller received subchapter name and desc', name, desc)
    # todo


if __name__ == '__main__':

    _make_widgets()
    window.mainloop()