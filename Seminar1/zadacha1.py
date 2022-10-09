def InputNum(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
    return number

def checkNum(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("В неделе 7 дней")


num = InputNum("Введите число: ")
checkNum(num)
