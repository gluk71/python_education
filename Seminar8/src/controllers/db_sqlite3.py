import sqlite3
import os

conn = None
db_file_name = './database/db.sqlite3'

def init():
    global conn
    if os.path.isfile(db_file_name):
        try:
            print('Database file exist')
            conn = sqlite3.connect(db_file_name)
        except:
            print('Error connecting to SQLite database')
    else:
        conn = sqlite3.connect(db_file_name)
    