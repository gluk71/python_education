import csv

fPath = 'c:\\project\\univerdb\\Database\\phonebook.csv'
def writing_scv(fn,ln,p1,p2,ds):
    #file = 'c:\\project\\univerdb\\Database\\phonebook.csv'
    with open (fPath, 'a', encoding = 'utf-8') as data:
        data.write(f'{fn};{ln};{p1};{p2};{ds}\n')

def reading_csv():
    with open('c:\\project\\univerdb\\Database\\phonebook.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print(', '.join(row))
            print('\n')

        
def writing_json():
    data = json.dumps(info, indent=4)
    with open("phonebook.json", "a") as file:
        json.dump(data,file)
    print(data)