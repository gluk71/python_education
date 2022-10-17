import random

def InputNum(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def four():
	num1 = int(InputNum("Введите индекс 1:...."))
	num2 = int(InputNum("Введите индекс 2:...."))
	mas = [random.randint(-10, 10) for i in range(10)]

	s = mas[num1] * mas[num2]

	print(s)

four()
