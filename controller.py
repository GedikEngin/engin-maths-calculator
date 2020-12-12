from gui.item_view import *
import model

# mv = None
# chv = None
# subch = None

window = Tk()

# init functions
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
    chv.subscribe_to_new_item_event(_on_chapter_new_item)
    chv.subscribe_to_removed_item_event(_on_chapter_removed_item)
    # chv.subscribe_to_update_item_event(_on_chapter_updated_item) # todo attend the lack of the function/holder
    chv.subscribe_to_select_item_event(_on_chapter_selected_item)



    subch = HPSListbox(window)
    subch.grid(row=0, column=2)
    subch.subscribe_to_new_item_event(_on_subchapter_new_item)
    subch.subscribe_to_removed_item_event(_on_subchapter_removed_item)
    # subch.subscribe_to_update_item_event(_on_chapter_updated_item) # todo attend the lack of the function/holder
    # subch.subscribe_to_select_item_event(_on_chapter_selected_item)

def _load_modules():
    module_names = model.get_all_module_names()
    for mod in module_names:
        if not mv.has_item(mod):
            mv.add_new_item(mod)

def _load_chapters():
    chapter_names = model.get_all_chapter_names()
    _load_specific_chapters(chapter_names)


def _load_specific_chapters(chapter_names):
    chv.clear_list()
    for chap in chapter_names:
        if not chv.has_item(chap):
            chv.add_new_item(chap)


def _load_subchapters():
    subchapter_names = model.get_all_subchapter_names()
    _load_specific_subchapters(subchapter_names)

def _load_specific_subchapters(subchapter_names):
    subch.clear_list()
    for subchap in subchapter_names:
        if not subch.has_item(subchap):
            subch.add_new_item(subchap)


# Module View
def _on_module_new_item(name, desc):
    print('NEA: Controller received module name and desc', name, desc)
    if model.add_new_module(name, desc):
        #clear sub/chapters listbox
        chv.clear_list()
        subch.clear_list()
        mv.select_item_by_name(name)
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
    #todo very important, remove all chapters, subchapters and formulas that are linked to the module
    model.remove_existing_module(name)
    chv.clear_list()
    subch.clear_list()

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


def _on_module_selected_item(mod_name):
    print('Controller received module name', mod_name)
    chapters = model.fetch_all_module_chapters(mod_name)
    _load_specific_chapters(chapters)

    # todo
    # story:
    # when the module is selected, we get the list of all chapter items to populate the chapter list box
    # the chapter list box is populated with the retrieved items
    # the description box is populated with the selected item
    # the first chapter is auto selected
    # {for chapters} ^^ the controller also retrieves the linked subchapters

# Chapter View
def _on_chapter_new_item(name, desc):
    print('Controller received chapter name and desc', name, desc)

    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no mod selection, please select a mod before adding a chapter.')
        return

    if model.add_new_chapter(name, desc, mod_name):
        # clear subchapters listbox
        subch.clear_list()
        chv.select_item_by_name(name)
        pass
    else:
        chv.delete_item_by_name(name)
        print('An error is present: \n Check if the chapter is already present within the database')
        print('The added item has been deleted')


def _on_chapter_removed_item(name):
    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no mod selection, please select a mod before adding a chapter.')
        return
    print('Controller is deleting module name', name)
    #todo very important, remove all chapters, subchapters and formulas that are linked to the module
    model.remove_existing_chapter(name, mod_name)

def _on_chapter_selected_item(chap_name):
    print('Controller received module name', chap_name)

    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no mod selection, please select a mod before viewing a chapter.')
        return

    subchapter = model.fetch_all_chapter_subchapter(mod_name, chap_name)
    _load_specific_subchapters(subchapter)



# Sub chapter View
def _on_subchapter_new_item(name, desc):
    print('Controller received chapter name and desc', name, desc)

    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no module selection, please select a module before adding a subchapter.')
        return

    chap_name = chv.get_selected_item()
    if chap_name is None:
        print('NEA: There is no chapter selection, please select a chapter before adding a subchapter.')
        return

    if model.add_new_subchapter(mod_name, chap_name, name, desc):
        pass
    else:
        subch.delete_item_by_name(name)
        print('An error is present: \n Check if the subchapter is already present within the database')
        print('The added item has been deleted')


def _on_subchapter_removed_item(name):
    chap_name = chv.get_selected_item()
    if chap_name is None:
        print('NEA: There is no chapter selection, please select a chapter before adding a subchapter.')
        return
    print('Controller is deleting chapter name', name)
    #todo very important, remove all chapters, subchapters and formulas that are linked to the module
    model.remove_existing_subchapter(name, chap_name)


if __name__ == '__main__':

    _make_widgets()
    _load_modules()
    _load_chapters()
    _load_subchapters()
    window.mainloop()