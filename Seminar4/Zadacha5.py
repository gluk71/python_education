/* Даны два файла, в каждом из которых находится запись многочлена.
/* Задача - сформировать файл, содержащий сумму многочленов.

def qmn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if qmn(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1 # степень
    ii = l-1 # индекс
    while ii >= 0:
        if qmn(st[ii]) != -1 and qmn(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1     
    return lst

with open('input_1.txt', 'r') as data:
    str_1 = data.readlines()
with open('input_2.txt', 'r') as data:
    str_2 = data.readlines()
print(f"Первый многочлен {str_1}")
print(f"Второй многочлен {str_2}")
l1 = calc_mn(str_1)
l2 = calc_mn(str_2)
ll = len(l1)
if len(l1) > len(l2):
    ll = len(l2)
lst_new = [l1[i] + l2[i] for i in range(ll)]
if len(l1) > len(l2):
    mm = len(l1)
    for i in range(ll,mm):
        lst_new.append(l1[i])
else:
    mm = len(l2)
    for i in range(ll,mm):
        lst_new.append(l2[i])
write_file("result.txt", create_str(lst_new))
with open('result.txt', 'r') as data:
    result = data.readlines()
print(f"Результирующий многочлен {result}")
