from gui.item_view import *
from gui.description import *
from gui.formula_main_view import *
import model

window = Tk()
global mv, chv, subchv, descv, formv, feditv  # global variables, model view, chapter view, subchapter view, description view, formula main view, formula edit view


# init functions

def _make_widgets():
    global mv, chv, subchv, descv, formv, feditv  # GUI Frames, global variables
    mv = HPSListbox(window, text='Modules')  # create modules listbox (components on left hand side)
    mv.grid(row=0, column=0)
    mv.subscribe_to_new_item_event(_on_module_new_item)  # subscription for new items being added
    mv.subscribe_to_removed_item_event(_on_module_removed_item)  # subscriptions for items being removed
    mv.subscribe_to_select_item_event(_on_module_selected_item)  # subscriptions for items being selected
    mv.subscribe_to_update_item_event(_on_module_updated_item)  # subscriptions for items being updated

    chv = HPSListbox(window, text='Chapters')  # repeat of module view
    chv.grid(row=1, column=0)
    chv.subscribe_to_new_item_event(_on_chapter_new_item)
    chv.subscribe_to_removed_item_event(_on_chapter_removed_item)
    chv.subscribe_to_select_item_event(_on_chapter_selected_item)
    chv.subscribe_to_update_item_event(_on_chapter_updated_item)

    subchv = HPSListbox(window, text='Subchapters')  # repeat of module view
    subchv.grid(row=2, column=0)
    subchv.subscribe_to_new_item_event(_on_subchapter_new_item)
    subchv.subscribe_to_removed_item_event(_on_subchapter_removed_item)
    subchv.subscribe_to_select_item_event(_on_subchapter_selected_item)
    subchv.subscribe_to_update_item_event(_on_subchapter_updated_item)

    formv = HPSListbox(window, text='Formulas')  # repeat of module view
    formv.grid(row=3, column=0)
    formv.subscribe_to_new_item_event(_on_formula_new_item)
    formv.subscribe_to_removed_item_event(_on_formula_removed_item)
    formv.subscribe_to_select_item_event(_on_formula_selected_item)
    formv.subscribe_to_update_item_event(_on_formula_updated_item)

    descv = Description(window, text='Description')  # frame for description box (central part of main window)
    descv.grid(row=0, column=1, rowspan=4)  # location

    feditv = FormulaMainView(window, text='Formula Control')  # control box at the top segment of the far right column
    feditv.grid(row=0, column=2, rowspan=4)
    feditv.subscribe_to_formula_save(_on_save_formula)


def _load_modules():  # retrieving all modules at the start
    module_names = model.get_all_module_names()  # assigns all the modules in a list to module_names
    for mod in module_names:
        if not mv.has_item(mod):  # comparison to check for existence
            mv.add_new_item(mod)  # adds the module into listbox


def _load_chapters():
    chapter_names = model.get_all_chapter_names()  # retrieving all chapters at the start
    _load_specific_chapters(chapter_names)  # loads specific chapters


def _load_specific_chapters(chapter_names):  # loads chapters that are linked to module selectiom
    chv.clear_list()  # primes listbox to be altered
    for chap in chapter_names:
        if not chv.has_item(chap):  # checks for existence
            chv.add_new_item(chap)  # adds to listbox


def _load_subchapters():
    subchapter_names = model.get_all_subchapter_names()  # retrieves all subchapters at the start
    _load_specific_subchapters(subchapter_names)  # loads specific subchapters


def _load_specific_subchapters(subchapter_names):  # loads subchapters that are linked to chapter selection
    subchv.clear_list()  # primes listbox to be altered
    for subchap in subchapter_names:
        if not subchv.has_item(subchap):  # checks for existence
            subchv.add_new_item(subchap)  # adds to listbox


def _load_formulas():
    formula_names = model.get_all_formula_names()  # retrieving all formulas at the start
    _load_specific_formulas(formula_names)  # loads specific modules


def _load_specific_formulas(formula_names):  # loads chapters that are linked to subchapter selection
    formv.clear_list()  # primes listbox to be altered
    for form in formula_names:
        if not formv.has_item(form):  # checks for existence
            formv.add_new_item(form)  # adds to listbox


# Module View
def _on_module_new_item(name, desc):
    print('NEA: Controller received module name and desc', name, desc)
    if model.add_new_module(name, desc):
        # clear sub/chapters listbox
        chv.clear_list()
        subchv.clear_list()
        mv.select_item_by_name(name)
        pass
    else:
        mv.delete_item_by_name(name)
        print('An error is present: \n Check if the module is already present within the database')
        print('The added item has been deleted')

    # story:
    # when new item is added the item name and description is saved into the database
    # it is selected and then the description is displayed in the description box
    # blank chapters and subchapters boxes appear that are linked to the new item


def _on_module_removed_item(name):
    print('Controller is deleting module name', name)
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

    # story:
    # when the module is selected, we get the list of all chapter items to populate the chapter list box
    # the chapter list box is populated with the retrieved items
    # the description box is populated with the selected item
    # the first chapter is auto selected
    # {for chapters} ^^ the controller also retrieves the linked subchapters


def _on_module_updated_item(old_name, new_name, new_desc):  # received from update box
    print('Controller received subchapter name and desc', old_name, new_name, new_desc)
    mod_name = old_name  # replacements sent to the model
    if mod_name is None:  # checks if it is selected
        print('NEA: There is no module selection, please select a module before editing.')
    model.update_modules_name_and_desc(old_name, new_name, new_desc)  # updates via model


# Chapter View
# repeat of module system above

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


def _on_chapter_removed_item(name):
    mod_name = mv.get_selected_item()
    if mod_name is None:
        print('NEA: There is no mod selection, please select a mod before adding a chapter.')
        return
    print('Controller is deleting module name', name)
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
    print('Controller received subchapter name and desc', old_name, new_name, new_desc)
    chap_name = old_name
    mod_name = mv.get_selected_item()
    if mod_name is None or chap_name is None:
        print('NEA: There is no chapter selection, please select a module before editing a formula.')
    model.update_chapters_name_and_desc(mod_name, old_name, new_name, new_desc)


# Sub chapter View
# repeat of module system above

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
    model.remove_existing_subchapter(name, chap_name)


def _on_subchapter_selected_item(subchap_name):
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    if mod_name is None or chap_name is None:
        descv.update_text('NEA: There is no mod or chapter selection, please select a mod before viewing a chapter.',
                          'ERROR')
        return

    desc = model.get_subchapter_desc(mod_name, chap_name, subchap_name)
    if desc is None:
        desc = 'Error: Could not find description'

    descv.update_text(desc, subchap_name)

    formula = model.fetch_all_subchapter_formula(mod_name, chap_name, subchap_name)
    _load_specific_formulas(formula)


def _on_subchapter_updated_item(old_name, new_name, new_desc):
    print('Controller received subchapter name and desc', old_name, new_name, new_desc)
    subchap_name = old_name
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    if mod_name is None or chap_name is None or subchap_name is None:
        print('NEA: There is no subchapter selection, please select a chapter before editing a subchapter.')
    model.update_subchapters_name_and_desc(mod_name, chap_name, old_name, new_name, new_desc)


# formula
# repeat of module system above

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

    if model.add_new_formula(mod_name, chap_name, subchap_name, name, desc):
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
    mod_name = mv.get_selected_item()  # focuses on getting a module to link to
    if mod_name is None:
        print('NEA: There is no module selection, please select a module before adding a subchapter.')
        return

    chap_name = chv.get_selected_item()  # focuses on getting a chapter to link to
    if chap_name is None:
        print('NEA: There is no chapter selection, please select a chapter before adding a subchapter.')
        return

    subchap_name = subchv.get_selected_item()  # focuses on getting a subchapter to link to
    if subchap_name is None:
        print('No subchap selection, please select')

    formula_name = formv.get_selected_item()  # focuses on getting a formula to link to
    if subchap_name is None:
        print('No formula selection, please select')

    model.add_formula_text(mod_name, chap_name, subchap_name, formula_name,
                           formula_text)  # commits to database into formula table in the formulatext field


def _on_formula_updated_item(old_name, new_name, new_desc):
    print('Controller received module name and desc', old_name, new_name, new_desc)
    formula_name = old_name
    mod_name = mv.get_selected_item()
    chap_name = chv.get_selected_item()
    subchap_name = subchv.get_selected_item()
    if formula_name is None or mod_name is None or chap_name is None or subchap_name is None:  # repeat of function
        # above, just uses higher level conditions
        print('NEA: There is no formula selection, please select a subchapter before editing a formula.')
    model.update_formula_name_and_desc(mod_name, chap_name, subchap_name, old_name, new_name,
                                       new_desc)  # over write and update old formula text


if __name__ == '__main__':
    _make_widgets()
    _load_modules()
    _load_chapters()
    _load_subchapters()
    _load_formulas()
    window.mainloop()
