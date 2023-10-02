#----------------------------------------------1-------------------------------------------------
from turtle import *
import time

def draw_pizza(radius):
    circle(radius)
    left(90)
    forward(radius)
    left(135)
    for i in range(7):
        forward(radius)
        back(radius)
        right(45)


def eat_pizza(choice):
    color('red')
    begin_fill()
    forward(radius)
    left(90)
    circle(radius, 45)
    left(90)
    forward(radius)
    end_fill()

def choice_1():
    choice = input("Съесть кусочек? да/нет")
    if choice != 'да' and choice != 'нет':
        raise ValueError('Ответ только да или нет!')
    return choice

radius = 100
draw_pizza(radius)
trig = 0
while trig <= 8:
    choice = choice_1()
    while choice != 'нет' and trig <=8:
        eat_pizza(choice)
        trig += 1
# for i in range(7):
#     forward(radius)
#     back(radius)
#     right(45)

# for i in range(8):
#     color('red')
#     begin_fill()
#     forward(radius)
#     left(90)
#     time.sleep(3)
#     circle(radius, 45)
#     left(90)
#     forward(radius)
#     end_fill()
# time.sleep(5)

