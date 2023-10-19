'''

#---------------------------------------------- Залание 1-------------------------------------------------
# Вывести на экран фигуру из звездочек:
# *******
# *******
# *******
# *******
# (квадрат из n строк, в каждой строке n звездочек)
# n - гарантируется, что целое число

n = int(input("Введите n: "))

for i in range(n):
    print("*" * n)

#---------------------------------------------- Залание 2-------------------------------------------------
# распечатайте все числа, которые делятся на 3 от start до end(включительно)
# (start, end - могут быть перепутаны), start , end- гарантируется, что целые числа

start, end = int(input("Введите начало: ")), int(input("Введите конец: "))
comp = 1
if start > end:
    start, end = end, start

while start < end + 1:
    if start % 3 == 0:
        print(start)
        start += 3
    else:
        start += 1

#---------------------------------------------- Залание 3. Черепашка 1-------------------------------------------------
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во углов произвольное)

from turtle import *
import time

steps = int(input("Введите количество углов: "))
start, up = 20, 10 #начальный размер и увеличение
colors = {0:"black", 1:"red", 2:"blue", 3:"yellow"} #словарь с цветами для покраски

for i in range(steps):
    color(colors.get(i % 4)) #берем значение цвета из словаря
    left(90)
    forward(start)
    right(90)
    forward(start)
    start += up

time.sleep(5)


#---------------------------------------------- Залание 4. Черепашка 2-------------------------------------------------
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во углов произвольное)

from turtle import *
import time

steps = int(input("Введите количество сторон: "))
start, up = 20, 10 #начальный размер и увеличение
colors = {0:"red", 1:"green", 2:"blue"} #словарь с цветами для покраски

for i in range(steps):
    color(colors.get(i % 3)) #берем значение цвета из словаря
    forward(start)
    left(90)
    start += up

time.sleep(5)


#---------------------------------------------- Залание 5. Черепашка 3-------------------------------------------------
#напишите программу для черепахи, чтобы она рисовала вот так  (кол-во углов произвольное)

from turtle import *
import time

steps = int(input("Введите количество волн: "))
start = 40
colors = {0:"red", 1:"black", 2:"blue"} #словарь с цветами для покраски

for i in range(steps):
    color(colors.get(i % 3)) #берем значение цвета из словаря
    forward(start)
    left(90)
    forward(start)
    right(90)
    forward(start)
    right(90)
    forward(start)
    left(90)

time.sleep(5)


#---------------------------------------------- Залание 6-------------------------------------------------
#Выведите на экран числа 1.2, 1.4, 1.6, ..., 2.8. Для программы необходимо использовать цикл for

from numpy import arange

start, end = 1, 3

for i in arange(start + 0.2, end, 0.2):
    print(f"{i:.1f}")

'''
#---------------------------------------------- Залание 6-------------------------------------------------
# Дано:
# n - кол-во сторон (гарантируется, что число целое)
# a - сторона многоугольника
# is_fill - нужно залить фигуру (гарантируется, что будет использован только логический тип данных)
# нарисовать ПРАВИЛЬНЫЙ многоугольник по заданным характеристикам
#
# УСЛОЖНЕНИЕ(необязательно делать) (добавьте еще одну переменную, хочет ли пользователь, чтобы каждая сторона многоугольника была разного цвета)


def draw(sides, value):
    """Рисуем фигуру"""
    if is_fill:
        fillcolor("yellow")
        begin_fill()
    for i in range(sides):
        if is_diff:
            pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        forward(value)
        left(180 / n * 2)
    if is_fill:
        end_fill()


from turtle import *
import time
from random import *

n, a = int(input("Количество сторон: ")), int(input("Длина сторон: "))
is_fill = True #нужно ли красить
is_diff = True #нужно ли красить разными цветами стороны
colormode(255)

draw(n, a)

time.sleep(5)







