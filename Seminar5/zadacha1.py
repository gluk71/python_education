
# Напишите программу, удаляющую из текста все слова, содержащие "абв".

etner = input("Введите текст через пробел:\n")
print(f"Исходный текст: {enter}")
find_txt = "абв"
lst_txt = [i for i in enter.split() if find_txt not in i]
print(f'Результат: {" ".join(lst_txt)}')
