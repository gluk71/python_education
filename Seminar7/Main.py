from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv
from File_writing import writing_json

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

path = 'Phonebook.json'
valid = exists(path)
if not valid:
    creating()

write_scv()
write_json()
