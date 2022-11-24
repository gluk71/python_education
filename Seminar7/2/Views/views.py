import os
from Models.model import *

def screen_cleaner():
    os.system('cls')
    
def show_records():
    reading_csv()
    
def create_record():
    fName = input("Введите имя: ")
    lName = input("Введите фамилию: ")
    phone1 = input("Номер телефона: ")
    phone2 = input("Номер телефона2: ")
    descr = input("Описание: ")
    writing_scv(fName, lName, phone1, phone2, descr)
