
def InputNum(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sumNums(number):
    s =0
    for i in range(1,number + 1):
        n=(1 + 1/i) ** i
        s = s + n

    return s

number = InputNum("Введите число:....")

print(f"Сумма цифр = {sumNums(number)}")






