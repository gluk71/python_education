from User_interface import get_info as gi

info = gi()
def write_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def write_json ():
    file = 'Phonebook.json'
    with open (file, 'a', encoding = 'utf-8') as data:
        //тут пишем что надо
        
