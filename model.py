
# module

def _module_id(name): # aux function
    """
    Check the database to see if a module exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the module
    """
    pass

def add_new_module(name, desc):
    """
    check if the module already exists or not
    if module does not exist, simply add the module name and description into the database
    if module does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: Module added to the DB, False: Module already exists
    """
    return True


def remove_existing_module(name):
    '''
    get id
    uses id to get all child chapters --> initiates deleting from chapters simultaneously
    in a for loop calls the deletion of the corresponding chapters
    when for loop is completed, deletes the parent module
    :return:
    '''
    pass

def update_existing_module(old_name, new_name, new_desc):
    '''
    see if the new name is the same as the old name
    if it isnt, search database to see if new name exists within the database
    if it doesnt:
        find old name and old name and desc
        delete the old desc
        amend the new name into old name
    if it exists:
        return false, as you cannot change a new name into an existing one

    :param name:
    :param desc:
    :return: if new name exists, return false, if doesnt return true
    '''
    pass

def fetch_all_module_chapters(name):
    '''
    get the id of the module using the name param. that is passed through
    if the module exists:
        search the database and find all the chapters that are associated with the chapter id
    if the module doesnt exist:
        return a warning
    :return:
    '''
    pass

# chapter

def chapter_id(name):
    """
    Check the database to see if a chapter exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the chapter
    """
    pass

def add_new_chapter(name, desc):
    """
    check if the chapter already exists or not
    if chapter does not exist, simply add the chapter name and description into the database
    if chapter does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: chapter added to the DB, False: chapter already exists
    """
    pass

def remove_existing_chapter(name):
    '''
    get id
    uses id to get all child subchapters --> initiates deleting from subchapters simultaneously
    in a for loop calls the deletion of the corresponding subchapters
    when for loop is completed, deletes the parent chapter
    :return:
    '''
    pass

def update_existing_chapter(old_name, new_name, new_desc):
    '''
    see if the new name is the same as the old name
    if it isnt, search database to see if new name exists within the database
    if it doesnt:
        find old name and old name and desc
        delete the old desc
        amend the new name into old name
    if it exists:
        return false, as you cannot change a new name into an existing one

    :param name:
    :param desc:
    :return: if new name exists, return false, if doesnt return true
    '''
    pass

def fetch_all_chapter_subchapter(name):
    '''
    get the id of the chapter using the name param. that is passed through
    if the chapter exists:
        search the database and find all the subchapters that are associated with the subchapter id
    if the chapter doesnt exist:
        return a warning
    :return:
    '''
    pass

# subchapter

def subchapter_id(name):
    """
        Check the database to see if a subchapter exists and returns its id in such case. Otherwise returns None
        :param name:
        :return: None: if module does not exists, str: the id of the subchapter
        """
    pass

def add_new_subchapter(name, desc):
    """
    check if the subchapter already exists or not
    if subchapter does not exist, simply add the subchapter name and description into the database
    if subchapter does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: subchapter added to the DB, False: subchapter already exists
    """
    pass

def remove_existing_subchapter(name):
    '''
    get id
    uses id to get all child formula --> initiates deleting from formula simultaneously
    in a for loop calls the deletion of the corresponding formula
    when for loop is completed, deletes the parent subchapter
    :return:
    '''
    pass

def update_existing_subchapter(old_name, new_name, new_desc):
    '''
    see if the new name is the same as the old name
    if it isnt, search database to see if new name exists within the database
    if it doesnt:
        find old name and old name and desc
        delete the old desc
        amend the new name into old name
    if it exists:
        return false, as you cannot change a new name into an existing one

    :param name:
    :param desc:
    :return: if new name exists, return false, if doesnt return true
    '''
    pass

def fetch_all_subchapter_formula(name):
    '''
    get the id of the subchapter using the name param. that is passed through
    if the subchapter exists:
        search the database and find all the subchapters that are associated with the subchapter id
    if the subchapter doesnt exist:
        return a warning
    :return:
    '''
    pass

# todo populate rest of the stories
