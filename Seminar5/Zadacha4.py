*** Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
*** Входные и выходные данные хранятся в отдельных текстовых файлах.
def coding(txt):
    count = 1
    res = ''
    l = len(txt)
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
        
    file = open("coding.txt", "w")
    file.write(res)
    file.close()
    return res

def decoding(str):
    number = ''
    res = ''
    for i in range(len(str)):
        if not str[i].isalpha():
            number += str[i]
        else:
            res = res + str[i] * int(number)
            number = ''
    file = open("decoding.txt", "w")
    file.write(res)
    file.close()
    return res

with open(r"input.txt", "r") as file:
    s = file.read()
print(f"Кодирование: {coding(s)}")
print(f"Декодирование: {decoding(coding(s))}")
