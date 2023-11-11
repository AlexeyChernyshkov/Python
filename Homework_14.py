# ---------------------Задание 1---------------------------
# написать функцию is_positive(num), которая возвращает True в случае, если num положительное, и False во всех остальных случаях.
# Дан список чисел (только целые числа).
# Напечатать 0 и отрицательные числа в списке применив, функцию is_positive


def is_positive(num):
    if num > 0:
        return True
    else:
        return False

num_list = [12, -2, 0, 32, -5, -12, 15]

for i in num_list:
    if is_positive(i) == False:
        print(i)


# ---------------------Задание 2---------------------------
# написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# ПРимер
# num_to_name_week(1) -> ‘Понедельник’

def num_to_name_week(num_day_week):
    week_days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    return week_days.get(num_day_week)

n = int(input("Введите поряковый номер дня недели "))

if 1 <= n <= 7:
    print(num_to_name_week(n))
else:
    print("Необходимо ввести от 1 до 7")



# ---------------------Задание 3---------------------------
# написать функцию для вычисления периметра n-угольника
# (проверку на существование фигуры прописать отдельную(ые) функцию(и)),
# применить эту функцию(и) для вычисления периметра n-угольника



# в задании нет постановки, о каком n-угольнике идет речь, поэтому сделал для обоих вариантов

import random

def equilateral_perimeter(n, a): # Равносторонний
    return n * a

def non_equilateral_perimeter(a): # Неравносторонний
    p = 0
    for i in a:
        p += i
    return p

def check(n):   # сторон должно быть 3 или больше
    return True if n >= 3 else False

n = int(input("Введите количество сторон:\n"))
if check(n):
    choice = input("n-угольник равносторонний? да/нет\n")
    if choice == "да":
        a = random.randint(1, 100)
        print(f"Длина стороны: {a}")
        print(f"Периметр равен: {equilateral_perimeter(n, a)}")
    elif choice == "нет":
        a = [random.randint(1, 100) for _ in range(n)]
        print(f"Длины сторон: {', '.join(str(i) for i in a)}")
        print(f"Периметр равен: {non_equilateral_perimeter(a)}")
    else:
        print("Неверный ввод. Только да/нет")
else:
    print("Не существует")


# ---------------------Задание 4. Черепашка 1---------------------------
from turtle import *
import time
def romb(a): # Рисуем ромб
    for i in range(2):
        forward(a)
        left(360 / 5)
        forward(a)
        left(180 - (360 / 5))

def border(a): # рисуем рамку
    forward(a)
    left(360 / 5)
    forward(a)
    left(360 / 5)
    for i in range(10):
        forward(a)
        left(360 / 10)
    left(360 / 10)
    forward(a)
    left(360 / 5)
    forward(a)

def figure(a): # Рисуем синюю фигуру
    b = a/2
    for i in range(4):
        forward(b)
        left(36)
    left(360 / 10)
    for i in range(4):
        forward(b)
        left(36)

a = 50
speed(10)
color("red")
for _ in range(10):
    romb(a)
    left(360 / 10)
border(a)
color("blue")
for _ in range(10):
    figure(a)
    left(360 / 5)

time.sleep(5)



# ---------------------Задание 5. Черепашка 2---------------------------
# написать ОДНУ функцию для фигур как на картинке.
# и решить задачу с применением этой функции. порядок фигур не важен.
# Также должна быть возможность задавать произвольный размер и цвет через функцию


# Случайно наткнулся на решение в интернете
# Решил изменить так, чтобы нужно было задавать только количество фигур и сторону квадрата (для рассчета площади)
# Все остальное (цвет и координаты перехода) генерируется самостоятельно

from turtle import *
import random
from math import tan, sqrt, pi


def go_position(x, y):
    '''Перемещение к следующей фигуре'''
    penup()
    goto(x, y)
    pendown()
    color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Рандомный генератор цвета
    begin_fill()


def draw_figure(n, l):
    '''Рисование фигуры'''
    angle = 360.0 / n
    for i in range(n):
        forward(l)
        right(angle)
    end_fill()


def calc_s():
    '''Рассчет площади квадрата, для расчета площади фигур'''
    return 4 * side_length ** 2 / (4 * tan(pi / 4))


def calc_side():
    '''Рассчет длины стороны фигуры'''
    return sqrt(4 * square * tan(pi / sides) / sides)


def gen_x_cord(x_cord, n):
    '''Генерация x координат начала рисования фигуры'''
    count = 0
    while n != 1:
        a = x_cord[count]
        if (len(x_cord) - 1) % 4 == 0:
            x_cord.append(a * -1 + (side_length * 1.5))     # Генерируем x координату для нового цикла фигур (1 четверть)
        else:
            x_cord.append(x_cord[count] * -1)   # Генерируем x координату, в зависимости от прошлого значения (2, 3, 4 четверти)
        count += 1
        n -= 1
    return x_cord


def gen_y_cord(x_cord, y_cord):
    '''Генерация y координат начала рисования фигуры'''
    for j in range(1, len(x_cord)):
        if j % 4 == 1 or j % 4 == 2:
            y_cord.append(x_cord[j])    # Если 1 или 2 четверть, то y = x
        else:
            y_cord.append(x_cord[j] * -1)   # Если 3 или 4 четверть, то y = -x
    return y_cord


figure_count = 9  # Меняем количество фигур
side_length = 20  # Устанавливаем размер стороны квадрата, чтобы высчитать площадь для каждой фигуры

x = [0]
y = [0]

speed(10)
colormode(255)

square = calc_s()  # Рассчитываем площадь квадрата
x_cords = gen_x_cord(x, figure_count)  # Генерируем x координату
y_cords = gen_y_cord(x_cords, y)  # Генерируем y координату

for i in range(figure_count):
    sides = i + 3
    side_length = round(calc_side(), 3)  # Рассчитываем длину стороны для каждой фигуры
    go_position(x_cords[i], y_cords[i])  # Переходим к точке начала рисования
    draw_figure(sides, side_length)  # Рисуем фигуру

exitonclick()


# ---------------------Задание 6. Черепашка 3---------------------------
from turtle import *
import time

def snow(n, a):
    for i in range(n):
        forward(a)
        back(a / 4)
        right(45)
        forward(a / 4)
        back(a / 4)
        left(90)
        forward(a / 4)
        back(a / 4)
        right(45)
        back(a * 3 / 4)
        left(360 / n)

count = int(input("количество: "))
a = int(input("размер: "))
pen_color = input("Цвет: ")
color(pen_color)
speed(10)
pensize(5)
snow(count, a)


time.sleep(3)


# # ------------------------Задача 7--------------------------#
# создать генератор даты
# требования к функции :
# функция случайно определять три целых числовых значения
# необходимо сделать проверки для валидности кол-во дней в месяце
# результат функции строка вида 00.00.0000 или 00/00/0000
# 01.01.2000
# 10/10/2000

import re
import random

def generate_date():
    year = random.randint(1000, 9999)
    month = random.randint(1, 12)
    day = day_valid(month, year)
    sep = random.choice(['.', '/'])
    return f"{day}{sep}{month}{sep}{year}"

def day_valid(month, year):
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # Високосный
            return random.randint(1, 29)
        else:   # Не високосный
            return random.randint(1, 28)
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return random.randint(1, 31)
    elif month in (2, 4, 6, 9, 11):
        return random.randint(1, 30)

# создать функции проверки валидности даты
def is_valid_date(date: str):
    l = re.findall(r'\d{1,2}[\./]\d{1,2}[\./]\d{4}', date)
    print(f'date = {date}  l ={l}')
    if l[0] == date:
       return True
    else:
       return False

date = generate_date()
print(is_valid_date(date))




