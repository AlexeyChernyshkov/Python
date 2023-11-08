# ---------------------Задание 1---------------------------
# Написать регулярное выражение для поиска в строке серии и номера паспорта
# Допускается только запись паспорта из предложенных ниже:
# 00 00 000000
# или 00 00 000 000
# или 00-00-000-000
# или 00-00-000000
# на месте 0 может стоять любая цифра
# Программа должны вывести кол-во валидных значений и показать их в консоле

import re

test_string = "000000 00 00 000000 00 00 0000 00 00 00 000 000 00-00-000-000 00-00-000000"
reg_ex = r"(\d{2}\s*-?\d{2}\s*-?\d{3}\s*-?\d{3})"

passport = re.findall(reg_ex, test_string)

print(len(passport))
for i in passport:
    print(i)


# ---------------------Задание 2---------------------------
# написать регулярное выражение для определения номера автомобиля.
# Допускается только такая запись номера автомобиля А000АА
# А-любая буква(латиница)
# 0-любая цифра
#
# Программа должны вывести кол-во валидных значений и показать их в консоле

import re

test_string = "А000АА АА000А ААА000 000ААА 0А0А0А В902ЫФ"
reg_ex = r"[А-ЯЁ]{1}\d{3}[А-ЯЁ]{2}"

car_num = re.findall(reg_ex, test_string)

print(len(car_num))
for i in car_num:
    print(i)


# ---------------------Задание 3---------------------------
# Написать регулярное выражение для определения валидных логинов.
# Валидными считаются те логины, которые удовлетворяют следующим условиям:
# ●	содержится минимум 1 букву латинского алфавита и не содержится буквы других алфавитов
# ●	содержит  минимум 2 цифры
# ●	в конце имени обязательно нужно указывать “login”
# примеры валидных значений
# 	n12login
# 	name22login
# 	2name2login
# и т.д.
#
# Программа должны вывести кол-во валидных значений и показать их в консоле

import re

test_string = "n12login name22login 2name2login 2name2logi name2login 12login"
reg_ex = r"^(?=.*?\d.*\d)(?=.*[a-zA-Z]).+$"
counter = 0
split_string = test_string.split() #делю строку на подстроки
# print(split_string)

for i in split_string:
    if i[len(i)-5:len(i)] == "login" and re.findall(reg_ex, i[:len(i)-5]): #проверяю ,что окончание login и проверяю строку без него
        print(*re.findall(reg_ex, i))
        counter += 1

print("Прошло проверку:", counter)


# ---------------------Задание 4. Черепашка 1---------------------------
from turtle import *
import time

def draw_square(a):
    for j in range(4):
        forward(a)
        right(90)

def go_back(a, n):
    backward(a * n)
    right(90)
    forward(a)
    left(90)

a = 20
n = 3

for i in range(n):
    for j in range(n):
        draw_square(a)
        forward(a)
    go_back(a, n)

time.sleep(5)

# ---------------------Задание 5---------------------------
import random

def rand_generator(a):
    b = [random.randint(1, 100) for _ in range(a)]
    return b

n = 10

print(rand_generator(n))


# ---------------------Задание 6. Черепашка 2---------------------------
from turtle import *
import time

def draw_triangle(a):
    for j in range(3):
        forward(a)
        left(120)

a = 50
for i in range(4):
    draw_triangle(a)
    forward(a)
    right(90)

time.sleep(3)

# ---------------------Задание 7. Черепашка 3---------------------------

from turtle import *
import time

def draw_hexagon(a):
    for j in range(6):
        forward(a)
        left(60)

a = 50
draw_hexagon(a)
forward(a*2)
draw_hexagon(a)
right(180)
draw_hexagon(a)

time.sleep(3)


















