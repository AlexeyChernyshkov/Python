"""
# # ------------------------Задача 1--------------------------#
# Ферзю задаются координаты в формате 4 4.
# Показать при помощи консоли список, куда ферзь может ходить из заданной позиции


def go_check(x1, y1, x2, y2):
    if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) or ((x1 - x2) ** 2 == (y1 - y2) ** 2):
        return True
    else:
        return False


def create_desk():
    desk = []
    for i in range(8):
        desk.append([])
        for j in range(8):
            if i == coord[0] - 1 and j == coord[1] - 1:
                desk[i].append("♕")
            elif go_check(coord[0] - 1, coord[1] - 1, i, j):
                desk[i].append("*")
            elif (i - j) % 2 == 0:
                desk[i].append("▢")
            else:
                desk[i].append("■")

    for i in desk:
        print(*i, sep=", ")



coord = [int(input("Введите положение по вертикали ")), int(input("Введите положение по горизонтали "))]

check_start = lambda a: a[0] in range(1, 9) and a[1] in range(1, 9)
if not check_start(coord):
    raise ValueError("Стартовые позиции от 1 до 8")

create_desk()

# # ------------------------Задача 2--------------------------#
# Дана произвольная строка создать строку, в которой содержаться только цифры из исходной строки

def find_digit():
    res = ""
    for i in s:
        if i.isdigit():
            res += i
    return res


s = list(str(input("Введите строку:\n")))

print(find_digit())


# # ------------------------Задача 3--------------------------#
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Необходимо создать новый список чисел, которые будут составлять 70% от исходного числа.
# Для создания такого списка использовать функцию map().
# Необходимо посчитать разницу между суммами исходного списка и преобразованного

import random

a = []
gen_int = lambda: random.randint(10, 200)
for i in range(5):
    a.append(gen_int())
a.sort(reverse = True)

find_percents = lambda x: x * 0.7
b = list(map(round, list(map(find_percents, a))))   # Окргуление списка b

print(f"Первый список {a} сумма {sum(a)}")
print(f"Второй список {b} сумма {sum(b)}")
print(f"Разница сумм: {sum(a) - sum(b)}")


# # ------------------------Задача 4--------------------------#
# Дан список чисел (можно создать любым способом, но приветствуется через лямбду функцию и random).
# Создать новый список при помощи filter(), отобрать значения по маске 3*3? , где * - любое кол-во цифр, ? - одна цифра
# Вычислить при помощи reduce() произведение нового списка

import random
import re
import functools

# a = [333, 343434, 3333, 34, 322223, 343433, 3, 233334,  333332]

# Если нужен точный список для проверки, раскомментить строку выше, и закомментить 4 строки ниже
# Можно увеличить количество генерируемых элементов и разброс
a = []
gen_int = lambda: random.randint(0, 4000)
for i in range(100):
    a.append(gen_int())

a = list(map(str, a))

reg_ex = re.compile("^[3]{1}[0-9]*[3]{1}[0-9]{1}$")
find_num = list(filter(reg_ex.match, a))
if find_num:
    print(find_num)

try:
    find_num = list(map(int, find_num))
    comp = functools.reduce(lambda x, y: x * y, find_num)
    print(comp)
except TypeError:
    print("Нет нужных данных (список пуст)")


"""
# # ------------------------Задача 5--------------------------#
# Дана строка, состоящая из символов A, B и C.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
import re

string = "AABAAAAABCABAAABC"

count = count_max = 1
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        count += 1
    else:
        if count_max < count:
            count_max = count
        count = 1
if count_max < count:
    count_max = count

print(count_max)

# reg_ex = r"(.)\1"
#
# final = re.sub(reg_ex, '. .', string)
# print(final)
# print (len(max(re.sub(reg_ex, '. .', string).split(), key=len))-1)




"""

# # ------------------------Задача 6--------------------------#
# Дана строка, состоящая из символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.


string = "XZYXXZZYYZXYZXYYXYZXZZYXYZYZXXYXZZYZXYYZX"

final = lambda x: x.split("XZZY")

res = len(max(final(string), key=len))

print(res)

"""

