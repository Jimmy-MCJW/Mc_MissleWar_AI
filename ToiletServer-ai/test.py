import sqlite3 
CONN=sqlite3.connect('log.db')
def DB_Initlize():
    create_database='''CREATE TABLE IF NOT EXISTS log(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    action TEXT,
    time TIME NOT NULL
    )'''
    CONN.execute(create_database)
    CONN.commit()