# Найти сумму чисел списка стоящих на нечетной позиции

import Func_list_generation as lg
numbers_list = lg.list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_elem = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'сумма чисел, стоящих на нечётных позициях: \n{odd_elem} равна {sum_odd}.')
