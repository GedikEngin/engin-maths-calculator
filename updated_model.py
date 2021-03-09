import sqlite3

conn = sqlite3.connect('secondary_database.db')
conn.execute("PRAGMA foreign_keys = 1")
c = conn.cursor()

try:
    c.execute('''CREATE TABLE IF NOT EXISTS modules
                    (id INTEGER PRIMARY KEY NOT NULL,
                     name VARCHAR(25) NOT NULL,
                     desc VARCHAR(255) NOT NULL
                     )''')
    print('modules created')

    c.execute('''CREATE TABLE IF NOT EXISTS chapters
                    (id INTEGER PRIMARY KEY NOT NULL,
                    name VARCHAR(25) NOT NULL,
                    desc VARCHAR(255) NOT NULL,
                    module_id INTEGER NOT NULL,
                    FOREIGN KEY (module_id) REFERENCES modules (id)
                    )''')

    print('chapters created')

    c.execute('''CREATE TABLE IF NOT EXISTS subchapters
                    (id INTEGER PRIMARY KEY NOT NULL,
                    name VARCHAR(25) NOT NULL,
                    desc VARCHAR(255) NOT NULL,
                    chapter_id INTEGER NOT NULL,
                    FOREIGN KEY (chapter_id) REFERENCES chapters (id)
                    )''')

    print('subchapters created')

    c.execute('''CREATE TABLE IF NOT EXISTS formulas
                    (id INTEGER PRIMARY KEY NOT NULL,
                    name VARCHAR(25) NOT NULL,
                    desc VARCHAR(255) NOT NULL,
                    formula VARCHAR(255) NOT NULL,
                    subchapter_id INTEGER NOT NULL,
                    FOREIGN KEY (subchapter_id) REFERENCES chapters (id)
                    )''')

    print('formulas created')
except:
    pass


conn.commit()
