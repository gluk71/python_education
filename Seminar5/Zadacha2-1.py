# вариант человек против человека:
from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
knft = int(input("Введите количество конфет на столе: "))
flg = randint(0,2) # флаг очередности
if flg:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while knft > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        knft -= k
        flg = False
        p_print(player1, k, counter1, knft)
    else:
        k = input_dat(player2)
        counter2 += k
        knft -= k
        flg = True
        p_print(player2, k, counter2, knft)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
