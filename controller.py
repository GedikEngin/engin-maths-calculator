from gui.item_view import *
from gui.description import *
from gui.formula_main_view import *
import model

# todo fix appearance globally
# todo formula main view becomes formula edit view

window = Tk()
global mv, chv, subchv, descv, formv, feditv


# init functions

def _make_widgets():
    global mv, chv, subchv, descv, formv, feditv # GUI Frame
    mv = HPSListbox(window, text='Modules') # use hps to get to size and alter frame height
    mv.grid(row=0, column=0)
    mv.subscribe_to_new_item_event(_on_module_new_item)
    mv.subscribe_to_removed_item_event(_on_module_removed_item)
    mv.subscribe_to_select_item_event(_on_module_selected_item)
    mv.subscribe_to_update_item_event(_on_module_updated_item)

    chv = HPSListbox(window, text='Chapters')
    chv.grid(row=1, column=0)
    chv.subscribe_to_new_item_event(_on_chapter_new_item)
    chv.subscribe_to_removed_item_event(_on_chapter_removed_item)
    chv.subscribe_to_select_item_event(_on_chapter_selected_item)
    chv.subscribe_to_update_item_event(_on_chapter_updated_item)

    subchv = HPSListbox(window, text='Subchapters')
    subchv.grid(row=2, column=0)
    subchv.subscribe_to_new_item_event(_on_subchapter_new_item)
    subchv.subscribe_to_removed_item_event(_on_subchapter_removed_item)
    subchv.subscribe_to_select_item_event(_on_subchapter_selected_item)
    subchv.subscribe_to_update_item_event(_on_subchapter_updated_item)

    formv = HPSListbox(window, text='Formulas')
    formv.grid(row=3, column=0)
    formv.subscribe_to_new_item_event(_on_formula_new_item)
    formv.subscribe_to_removed_item_event(_on_formula_removed_item)
    formv.subscribe_to_select_item_event(_on_formula_selected_item)
    formv.subscribe_to_update_item_event(_on_formula_updated_item)

    descv = Description(window, text='Description')
    descv.grid(row=0, column=1, rowspan=4)

    feditv = FormulaMainView(window, text='Formula Control')
    feditv.grid(row=0, column=2, rowspan=4)
    feditv.subscribe_to_formula_save(_on_save_formula)

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
    subchv.clear_list()
    for subchap in subchapter_names:
        if not subchv.has_item(subchap):
            subchv.add_new_item(subchap)


def _load_formulas():
    formula_names = model.get_all_formula_names()
    _load_specific_formulas(formula_names)

def _load_specific_formulas(formula_names):

    formv.clear_list()
    for form in formula_names:
        if not formv.has_item(form):
            formv.add_new_item(form)



# Module View
def _on_module_new_item(name, desc):
    print('NEA: Controller received module name and desc', name, desc)
    if model.add_new_module(name, desc):
        #clear sub/chapters listbox
        chv.clear_list()
        subchv.clear_list()
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
    subchv.clear_list()

    # story:
    # the item is removed, and all the linked chapters and subchapters and formulas removed
    # every item with a key that is linked to a module key is removed from the database
    # chapters and subchapters get cleared
    # the selection will go to a default, pre-existing item


def _on_module_selected_item(mod_name):
    print('Controller received module name', mod_name)
    chapters = model.fetch_all_module_chapters(mod_name)
    _load_specific_chapters(chapters)
    subchv.clear_list()
    formv.clear_list()

    desc = model.get_module_desc(mod_name)
    if desc is None:
        desc = 'Error: Could not find description'

    descv.update_text(desc, mod_name)

    # todo
    # story:
    # when the module is selected, we get the list of all chapter items to populate the chapter list box
    # the chapter list box is populated with the retrieved items
    # the description box is populated with the selected item
    # the first chapter is auto selected
    # {for chapters} ^^ the controller also retrieves the linked subchapters


def _on_module_updated_item(old_name, new_name, new_desc):
    print('Controller received module name and desc', old_name, new_name, new_desc)
    # todo
    # story:
    # when updated the items name and description are updated only, all the links remain the same
    # the display in the list box and description will change to match the updated item

def _on_chapter_new_item(name, desc):
    print('Controller received chapter name and desc', name, desc)

    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no mod selection, please select a mod before adding a chapter.')
        return

    if model.add_new_chapter(name, desc, mod_name):
        # clear subchapters listbox
        subchv.clear_list()
        chv.select_item_by_name(name)
        pass
    else:
        chv.delete_item_by_name(name)
        print('An error is present: \n Check if the chapter is already present within the database')
        print('The added item has been deleted')
# Chapter View


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

    desc = model.get_chapter_desc(mod_name, chap_name)
    if desc is None:
        desc = 'Error: Could not find description'

    descv.update_text(desc, chap_name)

    formv.clear_list()
    subchapter = model.fetch_all_chapter_subchapter(mod_name, chap_name)
    _load_specific_subchapters(subchapter)

def _on_chapter_updated_item(old_name, new_name, new_desc):
    print('Controller received chapter name and desc', old_name, new_name, new_desc)


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
        subchv.delete_item_by_name(name)
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

def _on_subchapter_selected_item(subchap_name):
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    if mod_name is None or chap_name is None:
        descv.update_text('NEA: There is no mod or chapter selection, please select a mod before viewing a chapter.',
                          'ERROR')
        return

    # todo fomula_names = model.fetch_all_subchapter_formula(mod_name, chap_name, name)

    desc = model.get_subchapter_desc(mod_name, chap_name, subchap_name)
    if desc is None:
        desc = 'Error: Could not find description'

    descv.update_text(desc, subchap_name)

    formula = model.fetch_all_subchapter_formula(mod_name, chap_name, subchap_name)
    _load_specific_formulas(formula)

def _on_subchapter_updated_item(old_name, new_name, new_desc):
    print('Controller received module name and desc', old_name, new_name, new_desc)


# formula

def _on_formula_new_item(name, desc):
    print('Controller received chapter name and desc', name, desc)

    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no module selection, please select a module before adding a subchapter.')
        return

    chap_name = chv.get_selected_item()
    if chap_name is None:
        print('NEA: There is no chapter selection, please select a chapter before adding a subchapter.')
        return

    subchap_name = subchv.get_selected_item()
    if subchap_name is None:
        print('No subchap selection, please select')

    if model.add_new_formula(mod_name, chap_name,subchap_name, name, desc):
        pass
    else:
        formv.delete_item_by_name(name)
        print('An error is present: \n Check if the formula is already present within the database')
        print('The added item has been deleted')


def _on_formula_removed_item(name):
    formula_name = formv.get_selected_item()
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    subchap_name = subchv.get_selected_item()
    if formula_name is None or mod_name is None or chap_name is None or subchap_name is None:
        print('NEA: There is no formula selection, please select a subchapter before removing a formula.')
        return
    print('Controller is deleting chapter name', name)
    #todo very important, remove all chapters, subchapters and formulas that are linked to the module
    model.remove_existing_formula(mod_name, chap_name, subchap_name, formula_name)

def _on_formula_selected_item(formula_name):

    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    subchap_name = subchv.get_selected_item()
    if mod_name is None or chap_name is None or subchap_name is None:
        descv.update_text('NEA: There is no mod or chapter selection, please select a mod before viewing a chapter.',
                          'ERROR')
        return

    # todo fomula_names = model.fetch_all_subchapter_formula(mod_name, chap_name, name)
    # update description

    desc = model.get_formula_desc(mod_name, chap_name, subchap_name, formula_name)
    if desc is None:
        desc = 'Error: Could not find the formula'

    descv.update_text(desc, formula_name)
    # update formula_edit_view
    formula_text = model.get_formula_text(mod_name, chap_name, subchap_name, formula_name)
    if formula_text == '':
        formula_text = 'clear'
    feditv.add_new_formula(formula_text)


# formula main view

def _on_save_formula(formula_text):


    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no module selection, please select a module before adding a subchapter.')
        return

    chap_name = chv.get_selected_item()
    if chap_name is None:
        print('NEA: There is no chapter selection, please select a chapter before adding a subchapter.')
        return

    subchap_name = subchv.get_selected_item()
    if subchap_name is None:
        print('No subchap selection, please select')

    formula_name = formv.get_selected_item()
    if subchap_name is None:
        print('No formula selection, please select')

    model.add_formula_text(mod_name, chap_name, subchap_name, formula_name, formula_text)

def _on_formula_updated_item(old_name, new_name, new_desc):
    print('Controller received module name and desc', old_name, new_name, new_desc)
    formula_name = old_name
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    subchap_name = subchv.get_selected_item()
    if formula_name is None or mod_name is None or chap_name is None or subchap_name is None:
        print('NEA: There is no formula selection, please select a subchapter before editing a formula.')
    model.update_formula_name_and_desc(mod_name, chap_name, subchap_name, old_name, new_name, new_desc)



if __name__ == '__main__':

    _make_widgets()
    _load_modules()
    _load_chapters()
    _load_subchapters()
    _load_formulas()
    window.mainloop()