
#----------------------------------------------Задание 1 и Задание 6-------------------------------------------------
# Дана пицца 8 кусочков. Доступны команды:
# 1. print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# написать программу, симулующую поедание кусочков пиццы (По желанию можно анимацию убывание кусочков пиццы добавить)

# P.S. Я немного увлекся, и сделал 3 команды в первом задании
# Потом унифицировал код для 1-го и 6-го задания
# В основной программе можно выбрать количество кусочков на пицце, заменив параметр parts
# он передается во все функции (где нужен)
# Задание очень классное, помогло вспомнить функции и познакомиться с черепашкой по-ближе. Спасибо!

from turtle import *

def draw_pizza(radius, parts):
    """Рисуем пиццу"""
    circle(radius)
    left(90)
    forward(radius)
    left(180 - 180 / parts * 2)
    for i in range(parts - 1):
        forward(radius)
        back(radius)
        right((180 / parts) * 2)


def take_choose():
    """Взять, или не взять? Вот в чем вопрос"""
    choice = input("Взять кусочек? да/нет ")
    if choice != 'да' and choice != 'нет':
        raise ValueError('Ответ только да или нет!')
    return choice


def take_pizza(trig, parts):
    """Берем кусок"""
    pencolor("white")
    if trig == parts - 1:
        pendown()
    else:
        penup()
    forward(radius)
    left(90)
    pendown()
    pensize(2)
    circle(radius, 180 / parts * 2)
    left(90)
    pensize(1)
    if trig == 0:
        penup()
    forward(radius)
    left(180 - 180 / parts)
    """Берем кусочек в сторону, чтобы красиво было :)"""
    if trig == 0:
        pendown()
    forward(radius/2)
    right(180 / parts)
    pencolor("black")
    color('red')
    begin_fill()
    draw_part_again() # Замена строк на функцию — экономия 5-ти строк кода
    end_fill()


def eat_choose(choice):
    """Есть или не есть? Тоже вопрос"""
    choice = input("Съесть кусочек? да/нет ")
    if choice != 'да' and choice != 'нет':
        raise ValueError('Ответ только да или нет!')
    return choice


def eat_pizza():
    """Едим кусочек"""
    color('white')
    left(180 - 180 / parts * 2)
    begin_fill()
    draw_part_again()
    end_fill()


def take_back(parts):
    """Если не есть, то кладем на место"""
    eat_pizza()
    right(180 / parts)
    forward(radius / 2)
    left(180 - 180 / parts)
    color('black')
    draw_part_again()
    left(180 - 180 / parts * 2)

def draw_part_again():
    """рисуем кусочек снова"""
    forward(radius)
    left(90)
    circle(radius, 180 / parts * 2)
    left(90)
    forward(radius)


def go_back(parts):
    """Возвращаемся на исходную (в центр)"""
    right(180 / parts)
    forward(radius/2)
    left(180 - 180 / parts * 3)


radius = 100
parts = 8 #Поменять параметр для выбора количества кусочков
draw_pizza(radius, parts) #вызов функции рисования
trig = 0 #Триггер подсчета съеденных кусочков
while trig < parts: # Пока съели не 8 кусочков
    choice = take_choose()
    if choice == 'да': # Если не берем кусок, тогда завершаем программу
        take_pizza(trig, parts)
        while choice: # Тут просто цикл для поедания пиццы
            choice = eat_choose(choice)
            if choice == 'да': # Если едим, то едим и на исходную. Триггер +1
                eat_pizza()
                go_back(parts)
                trig += 1
                break
            else: #Если не едим, кладем назад и на исходную
                take_back(parts)
                break
    else: # Если в руке нет кусочка, и брать не хочешь, спрашиваем еще раз
        again = input("Введите 'нет', чтобы завершить программу\n"
                      "введите 'да', чтобы продолжить\n")
        if again == "да": # Если да, то в цикл
            continue
        else: # если нет, то выход из программы
            exit()

#----------------------------------------------Задание 2-------------------------------------------------
#Выведите столбец чисел от 1 до 100, используя цикл while

i = 1
while i <= 100:
    print(i)
    i += 1

#----------------------------------------------Задание 3-------------------------------------------------
#Дано число n. Вывести степени этого числа с 1 по 10

n = int(input("Введите число: "))
for i in range(1, 11):
    print(n**i)


#---------------------------------------------- Залание 4. Черепаха 1-------------------------------------------------
# написать программу для черепашки
from turtle import *
import time
n = 200
pensize(2)
for i in range(11):
    forward(n)
    right(180 - 360/22)
time.sleep(5)



#---------------------------------------------- Залание 5. Черепаха 2-------------------------------------------------
# написать программу для черепашки
from turtle import *
from math import *
import time

side, times = int(input("Введите сторону изначального квадрата: ")), int(input("Введите количество квадратов: "))
increase = 20 # изменить для увеличения отступа квадрата
if  side <= 0 :
    raise ValueError("Размер изначального квадрата должна быть > 0")
if  times <= 0 :
    raise ValueError("Количество квадратов должно быть > 0")
for i in range(times):
    for j in range(4):
        forward(side)
        left(90)
    right(135)
    penup()
    forward(increase/2 * sqrt(2))
    side += increase
    pendown()
    left(135)
time.sleep(5)


#---------------------------------------------- Залание 7-------------------------------------------------
#Выведите столбец чисел от start (определяется пользователем) до end,
# используя цикл while. Найти произведение чисел

#P. S. Предусмотрел ввод отрицательных чисел, и если будет такое, то значения меняются, а 0 пропускается из-за произведения
# Если переборщил с этим, то ладно :)

start, end = int(input("Введите начало: ")), int(input("Введите конец: "))
comp = 1
if start > end:
    start, end = end, start

while start != end + 1:
    if start == 0:
        start += 1
        continue
    print(start)
    comp *= start
    start += 1
print("Произведение = ", comp)