
#----------------Задание 1----------------
n = int(input('Введите число: '))
if n > 0:
    print('num>0')
else:
    print('num<0')


#----------------Задание 2----------------
n = int(input('Введите число: '))
if n % 3 == 0:
    print('ok')
else:
    print(':(')


#----------------Задание 3----------------
n = int(input('Введите число: '))
if n >= 1 and n <= 12:
    print('Да')
else:
    print('Нет')


#----------------Задание 4----------------
from turtle import *
from time import *

n = input('Выберите фигуру: ')
if n == 'круг':
    r = int(input('Введите радиус круга: '))
    circle(r)
    sleep(5)
elif n == 'квадрат':
    length = int(input('Введите длину стороны квадрата: '))
    for i in range(4):
        forward(length)
        left(90)
    sleep(5)
elif n == 'прямоугольник':
    length1, length2 = int(input('Введите длину первой стороны прямоугольника: ')), int(input('Введите длину второй стороны прямоугольника: '))
    for i in range(1, 5):
        if i % 2 != 0:
            forward(length1)
            left(90)
        else:
            forward(length2)
            left(90)
    sleep(5)
elif n == 'треугольник':
    length3 = int(input('Введите длину стороны треугольника: '))
    for i in range(3):
        forward(length3)
        left(120)
    sleep(5)
else:
    print('Доступны только: круг, квадрат, прямоугольник, треугольник')


#----------------Задание 5----------------
from turtle import *
from time import *

r, choice = int(input('Введите радиус круга: ')), input('Закрасить круг? да/нет ')
if choice == 'да':
    color('red')
    begin_fill()
    circle(r)
    end_fill()
    sleep(5)
elif choice == 'нет':
    circle(r)
    sleep(5)
else:
    print('Выберите: да/нет')

