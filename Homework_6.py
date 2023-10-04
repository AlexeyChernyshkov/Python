#----------------------------------------------1-------------------------------------------------
from turtle import *
import time
import sys
import os
def draw_pizza(radius):
    '''Рисуем пиццу'''
    circle(radius)
    #pensize(2)
    left(90)
    forward(radius)
    left(135)
    for i in range(7):
        forward(radius)
        back(radius)
        right(45)


def take_choose():
    '''Взять, или не взять? Вот в чем вопрос'''
    choice = input("Взять кусочек? да/нет")
    if choice != 'да' and choice != 'нет':
        raise ValueError('Ответ только да или нет!')
    return choice


def take_pizza(trig):
    '''Берем кусок'''
    pencolor("white")
    penup()
    forward(radius)
    left(90)
    pendown()
    pensize(2)
    circle(radius, 45)
    left(90)
    pensize(1)
    if trig == 0:
        penup()
    forward(radius)
    left(157.5)
    '''Берем кусочек в сторону, чтобы красиво было :)'''
    if trig == 0:
        pendown()
    forward(radius/2)
    right(22.5)
    pencolor("black")
    color('red')
    begin_fill()
    draw_part_again() # Замена строк на функцию — экономия 5-ти строк кода
    end_fill()


def eat_choose(choice):
    '''Есть или не есть? Тоже вопрос'''
    choice = input("Съесть кусочек? да/нет")
    if choice != 'да' and choice != 'нет':
        raise ValueError('Ответ только да или нет!')
    return choice


def eat_pizza():
    '''Едим кусочек'''
    color('white')
    left(135)
    begin_fill()
    draw_part_again() # Замена строк на функцию — экономия 1-ой строки кода
    end_fill()


def take_back():
    '''Если не есть, то кладем на место'''
    eat_pizza()
    right(22.5)
    forward(radius / 2)
    left(157.5)
    color('black')
    draw_part_again() # Замена строк на функцию — экономия 1-ой строки кода
    left(135)

def draw_part_again():
    '''рисуем кусочек снова'''
    forward(radius)
    left(90)
    circle(radius, 45)
    left(90)
    forward(radius)


def go_back():
    '''Возвращаемся на исходную (в центр)'''
    right(22.5)
    forward(radius/2)
    left(112.5)


radius = 100
draw_pizza(radius) #вызов функции рисования
trig = 0 #Триггер подсчета съеденных кусочков
while trig < 8: # Пока съели не 8 кусочков
    choice = take_choose()
    if choice == 'да': # Если не берем кусок, тогда завершаем программу
        take_pizza(trig)
        while choice: # Тут просто цикл для поедания пиццы
            choice = eat_choose(choice)
            if choice == 'да': # Если едим, то едим и на исходную. Триггер +1
                eat_pizza()
                go_back()
                trig += 1
                break
            else: #Если не едим, кладем назад и на исходную
                take_back()
                break
    else: # Если не берем кусок, тогда завершаем программу
        print("Куска нет в руке\n"
              "Нажми Enter и введи 'да' чтобы попробовать еще раз\n"
              "Нажми Enter дважды, чтобы завершить\n")
        os.system("Pause")
        #sys.exit()


#----------------------------------------------2-------------------------------------------------






