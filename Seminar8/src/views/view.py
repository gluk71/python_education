from tkinter import filedialog, ttk
from tkinter import *

from controllers import ctrl

main_window = None
main_table = None

def init_main_window():
    
    w = main_window.winfo_screenwidth()
    h = main_window.winfo_screenheight()
    w = w//2 # середина экрана
    h = h//2 
    w = w - 200 # смещение от середины
    h = h - 200

    main_window.title('База "Университет"')
    main_window.geometry((f'1220x800+{w}+{h}'))

def employee():
    main_table = ttk.Treeview(main_window,show='headings',columns=['Фаимлия','Имя','Телефон','Факультет','Предмет'],name='table_main')
    table_main.column('Наименование',width=200,anchor=W)

    # for i in range(10):
    #     main_table.insert('',i,values=(1,2))
    
    main_table.pack(expand=1,side=TOP,fill=BOTH)

    ctrl.employee()

def create_menu():
    myMenu = Menu(main_window)
    main_window.config(menu=myMenu)

    file_menu = Menu(myMenu)
    myMenu.add_cascade(label="Файл",menu=file_menu)
    file_menu.add_command(label="Выход", command=myMenu.quit)

    u_menu = Menu(myMenu)
    myMenu.add_cascade(label="Справочник",menu=u_menu)
    u_menu.add_command(label="Сотрудники", command=employee)
    u_menu.add_command(label="Студенты", command=myMenu.add)
    u_menu.add_command(label="Должности", command=myMenu.add)
    u_menu.add_command(label="Специальности", command=myMenu.add)

def init():

    global main_window

    main_window = Tk()

    init_main_window()
    create_menu()

    main_window.mainloop()