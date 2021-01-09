## init database

import sqlite3
conn = sqlite3.connect('Mathematics_database.db')

c = conn.cursor()
try:
    c.execute('''CREATE TABLE IF NOT EXISTS modules
                (id INTEGER PRIMARY KEY,
                 name VARCHAR(25),
                 desc VARCHAR(255)
                 )''')

    c.execute('''CREATE TABLE IF NOT EXISTS chapters
                (id INTEGER PRIMARY KEY,
                name VARCHAR(25),
                desc VARCHAR(255),
                module_id INTEGER
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS subchapters
                (id INTEGER PRIMARY KEY,
                name VARCHAR(25),
                desc VARCHAR(255),
                chapter_id INTEGER,
                module_id INTEGER
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS formulas
                (id INTEGER PRIMARY KEY,
                name VARCHAR(25),
                desc VARCHAR(255),
                formula VARCHAR(511),
                subchapter_id INTEGER,
                chapter_id INTEGER,
                module_id INTEGER
                )''')
except:
    pass

# todo


# module

def get_module_id(name):  # aux function
    """
    Check the database to see if a module exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the module
    """
    c.execute('''
        SELECT id
        FROM modules
        WHERE name = ?
        ''', (name,))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None


def get_module_desc(name):  # aux function

    c.execute('''
        SELECT desc
        FROM modules
        WHERE name = ?
        ''', (name,))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None

def get_all_module_names():
    c.execute('''
            SELECT name
            FROM modules
            ''')
    return [b[0] for b in c.fetchall()]


def add_new_module(name, desc):
    """
    check if the module already exists or not
    if module does not exist, simply add the module name and description into the database
    if module does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: Module added to the DB, False: Module already exists
    """

    if get_module_id(name):
        return False
    c.execute("INSERT INTO modules (name, desc) VALUES (?, ?)", (name, desc))
    conn.commit()
    return True


def remove_existing_module(name):
    '''
    get id
    uses id to get all child chapters --> initiates deleting from chapters simultaneously
    in a for loop calls the deletion of the corresponding chapters
    when for loop is completed, deletes the parent module
    :return:
    '''

    mod_id = get_module_id(name)
    if not mod_id:
        return False

    c.execute("DELETE "
              "FROM modules WHERE name=?", (name,))

    c.execute("DELETE "
              "FROM chapters WHERE module_id = ?", (mod_id,))

    c.execute("DELETE "
              "FROM subchapters WHERE module_id = ?", (mod_id,))

    conn.commit()


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


def fetch_all_module_chapters(mod_name):
    '''
    get the id of the module using the name param. that is passed through
    if the module exists:
        search the database and find all the chapters that are associated with the chapter id
    if the module doesnt exist:
        return a warning
    :return:
    '''

    mod_id = get_module_id(mod_name)

    if not mod_id:
        return []

    c.execute('SELECT name FROM chapters WHERE module_id = ?', (mod_id,))
    chapters = c.fetchall()
    print(chapters)
    return [b[0] for b in chapters]



# chapter
def get_chapter_id(mod_name, chap_name):
    """
    Check the database to see if a chapter exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the chapter
    """
    mod_id = get_module_id(mod_name)
    c.execute('''
        SELECT id
        FROM chapters
        WHERE name = ?
        AND module_id = ?
        ''', (chap_name, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None


def get_all_chapter_names():
    c.execute('''
            SELECT name
            FROM chapters
            ''')
    return [b[0] for b in c.fetchall()]

def add_new_chapter(chap_name, desc, mod_name):
    """
    check if the chapter already exists or not
    if chapter does not exist, simply add the chapter name and description into the database
    if chapter does exists, return popup?

    :param chap_name:
    :param desc:
    :return: bool -> True: chapter added to the DB, False: chapter already exists
    """
    if get_chapter_id(mod_name, chap_name):
        return False

    mod_id = get_module_id(mod_name)
    c.execute("INSERT INTO chapters (name, desc, module_id) VALUES (?, ?, ?)", (chap_name, desc, mod_id))
    conn.commit()
    return True

def remove_existing_chapter(name, module_name):
    '''
    get id
    uses id to get all child subchapters --> initiates deleting from subchapters simultaneously
    in a for loop calls the deletion of the corresponding subchapters
    when for loop is completed, deletes the parent chapter
    :return:
    '''
    chap_id = get_chapter_id(module_name, name)
    module_id = get_module_id(module_name)
    if not chap_id:
        return False
    c.execute("DELETE "
              "FROM chapters WHERE name=? and module_id = ?", (name, module_id))

    c.execute("DELETE "
              "FROM subchapters WHERE chapter_id = ?", (chap_id,))
    conn.commit()
    # todo remove all the linked subchapters

def get_chapter_desc(mod_name, chap_name):

    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT desc
        FROM chapters
        WHERE name = ?
        AND module_id = ?
        ''', (chap_name, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None


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

def fetch_all_chapter_subchapter(mod_name, chap_name):
    '''
    get the id of the chapter using the name param. that is passed through
    if the chapter exists:
        search the database and find all the subchapters that are associated with the subchapter id
    if the chapter doesnt exist:
        return a warning
    :return:
    '''

    chap_id = get_chapter_id(mod_name, chap_name)

    if not chap_id:
        return []

    c.execute('SELECT name FROM subchapters WHERE chapter_id = ?', (chap_id,))
    subchapter = c.fetchall()
    print(subchapter)
    return [b[0] for b in subchapter]


# subchapter

def get_subchapter_id(mod_name, chap_name, subchap_name):
    """
    Check the database to see if a chapter exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the chapter
    """

    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT id
        FROM subchapters
        WHERE name = ?
        AND chapter_id = ?
        AND module_id = ?
        ''', (subchap_name, chap_id, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None


def get_subchapter_desc(mod_name, chap_name, subchap_name):

    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT desc
        FROM subchapters
        WHERE name = ?
        AND chapter_id = ?
        AND module_id = ?
        ''', (subchap_name, chap_id, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None



def get_all_subchapter_names():
    c.execute('''
            SELECT name
            FROM subchapters
            ''')
    return [b[0] for b in c.fetchall()]

def add_new_subchapter(mod_name, chap_name, subchap_name, desc):
    """
    check if the chapter already exists or not
    if chapter does not exist, simply add the chapter name and description into the database
    if chapter does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: chapter added to the DB, False: chapter already exists
    """
    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)
    sub_chap_id = get_subchapter_id(mod_name, chap_name, subchap_name)
    if sub_chap_id:
        return False
    c.execute("INSERT INTO subchapters (name, desc, chapter_id, module_id) VALUES (?, ?, ?, ?)",
              (subchap_name, desc, chap_id, mod_id))
    conn.commit()
    return True

def remove_existing_subchapter(mod_name, chapter_name, subchapter_name):
    '''
    get id
    uses id to get all child subchapters --> initiates deleting from subchapters simultaneously
    in a for loop calls the deletion of the corresponding subchapters
    when for loop is completed, deletes the parent chapter
    :return:
    '''
    mod_id = get_module_id(mod_name)
    chap_id = get_chapter_id(mod_name, chapter_name)
    subchapter_id = get_subchapter_id(mod_name, chapter_name, subchapter_name)
    if not subchapter_id:
        return False
    c.execute("DELETE "
              "FROM subchapters WHERE"
              "name = ?"
              "module_id = ?"
              "chapter_id = ?", (subchapter_name, mod_id, chap_id))
    c.execute("DELETE"
              "FROM formulas"
              "WHERE subchapter_id = ?", (subchapter_id))


    conn.commit()
    # todo remove all the linked subchapters

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

def fetch_all_subchapter_formula(mod_name, chap_name, subchap_name, formula_name):
    '''
    get the id of the subchapter using the name param. that is passed through
    if the subchapter exists:
        search the database and find all the subchapters that are associated with the subchapter id
    if the subchapter doesnt exist:
        return a warning
    :return:
    '''

    subchap_id = get_subchapter_id(mod_name, chap_name, subchap_name)

    if not subchap_id:
        return []

    c.execute('SELECT name'
              'FROM formulas'
              'WHERE subchapter_id = ?',
              (subchap_id))





# formula

def get_formula_id(mod_name, chap_name, subchap_name, formula_name):
    """
    Check the database to see if a chapter exists and returns its id in such case. Otherwise returns None
    :param name:
    :return: None: if module does not exists, str: the id of the chapter
    """

    subchap_id = get_subchapter_id(mod_name, chap_name, subchap_name)
    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT id
        FROM formulas
        WHERE name = ?
        AND subchapter_id = ?
        AND chapter_id = ?
        AND module_id = ?
        ''', (formula_name, subchap_id, chap_id, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None


def get_formula_desc(mod_name, chap_name, subchap_name, formula_name):

    subchap_id = get_subchapter_id(mod_name, chap_name,subchap_name)
    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT desc
        FROM formulas
        WHERE name = ?
        AND subchapter_id = ?
        AND chapter_id = ?
        AND module_id = ?
        ''', (formula_name, subchap_id, chap_id, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None

def get_formula_text(mod_name, chap_name, subchap_name, formula_name):

    subchap_id = get_subchapter_id(mod_name, chap_name,subchap_name)
    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)

    c.execute('''
        SELECT formula
        FROM formulas
        WHERE name = ?
        AND subchapter_id = ?
        AND chapter_id = ?
        AND module_id = ?
        ''', (formula_name, subchap_id, chap_id, mod_id))

    data = c.fetchall()
    if data:
        return data[0][0]
    else:
        return None



def get_all_formula_names():
    c.execute('''
            SELECT name
            FROM formulas
            ''')
    return [b[0] for b in c.fetchall()]

def add_new_formula(mod_name, chap_name, subchap_name, formula_name, desc):
    """
    check if the chapter already exists or not
    if chapter does not exist, simply add the chapter name and description into the database
    if chapter does exists, return popup?

    :param name:
    :param desc:
    :return: bool -> True: chapter added to the DB, False: chapter already exists
    """
    formula = '' # the actual formula text will be added by the formula widget
    formula_id = get_formula_id(mod_name, chap_name, subchap_name, formula_name)
    chap_id = get_chapter_id(mod_name, chap_name)
    mod_id = get_module_id(mod_name)
    subchap_id = get_subchapter_id(mod_name, chap_name, subchap_name)
    if formula_id:
        return False
    c.execute("INSERT INTO formulas (name, desc, formula, chapter_id, module_id, subchapter_id) VALUES (?, ?, ?, ?, ?, ?)",
              (formula_name, desc, formula, chap_id, mod_id, subchap_id)) # formula text will be received later
    conn.commit()
    return True

def remove_existing_formula(mod_name, chap_name, subchap_name, formula_name):
    '''
    get id
    uses id to get all child subchapters --> initiates deleting from subchapters simultaneously
    in a for loop calls the deletion of the corresponding subchapters
    when for loop is completed, deletes the parent chapter
    :return:
    '''

    mod_id = get_module_id(mod_name)
    chap_id = get_chapter_id(mod_name, chap_name)
    subchap_id = get_subchapter_id(mod_name, chap_name, subchap_name)
    formula_id = get_formula_id(mod_name, chap_name, subchap_name, formula_name)

    if not formula_id:
        return False
    c.execute("DELETE"
              "FROM formulas"
              "WHERE name = ?"
              "AND module_id = ?"
              "AND chapter_id = ?"
              "AND subchapter_id = ?",
              (formula_name, mod_id, chap_id, subchap_id))

    conn.commit()
    # todo remove all the linked subchapters

def add_formula_text(mod_name, chap_name, subchap_name, formula_name, formula_text):

    formula_id = get_formula_id(mod_name, chap_name, subchap_name, formula_name)

    if not formula_id:
        return False
    c.execute("UPDATE formulas"
              "SET formula = ?"
              "WHERE id = ?",
              (formula_text, formula_id))

    conn.commit()




if __name__ == '__main__':
    remove_existing_module('test')