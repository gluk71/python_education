from Controllers.controllers import *
from Views.views import *

def main():
    screen_cleaner()
    default_page()
    choise = input("\nВаш выбор: ")
    
    if choise == '1':
        show_records()

    elif choise == '2':
        create_record()

    elif choise == '3':
        raise SystemExit

if __name__ == "__main__":
    main()