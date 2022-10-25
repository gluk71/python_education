/* Задана натуральная степень k. 
/* Сформировать случайным образом список коэффициентов (значения от -100 до 100) многочлена и записать в файл многочлен степени k. 
/* k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
/* Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

import random

def write_file(fname):
    with open('output.txt', 'w') as data:
        data.write(fname)

def rnd():
    return random.randint(-100,101)


def create_mnc(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

def create_str(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koeff = create_mnc(k)
write_file(create_str(koeff))
