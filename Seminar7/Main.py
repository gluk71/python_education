import os
import json

def creating_scv():
    file = 'phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')
        
info = []       
def writing_scv():
    file = 'phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_json():
    data = json.dumps(info, indent=4)
    with open("phonebook.json", "a") as file:
        json.dump(data,file)
    print(data)


def get_info():
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    phone_number = ''
    valid =False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    description = input('Введите описание: ')
    info.append(description)
    return info


def main():
    get_info()
    file_extension = os.path.splitext("phonebook.csv")
     
    if (file_extension[1] == '.csv'):
        writing_scv()
    else:
        writing_json() 
        
if __name__ == "__main__":
    main()
