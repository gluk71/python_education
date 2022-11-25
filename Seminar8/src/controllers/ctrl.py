from . import db_sqlite3
from views import view

def view_init():
    view.init()

def db_init():
    db_sqlite3.init()

def init():
    db_init()
    view_init()

def employee():
    pass