'''

#---------------------------------Задача 1------------------------------------------
#даны 3 числа, распечатать в порядке возрастания

digits = [int(input("1st: ")), int(input("2nd: ")), int(input("3rd: "))]

digits.sort()
print(digits)



#---------------------------------Задача 2------------------------------------------

# Написать программу для следующей задачи
# работают 3 сотрудника, у них есть оклад в размере 300.
# Если сотрудник выполнит 50 и более продаж, то получит премию в размере 30% от оклада,
# если более 75, то получит премию в размере 65% от оклада,
# а если 100, то - 100% от оклада

workers, summ = [int(input("1st: ")), int(input("2nd: ")), int(input("3rd: "))], []
salary = 300

for i in range(len(workers)):
    if workers[i] >= 0:
        if workers[i] > 50:
            if workers[i] > 75:
                if workers[i] >= 100:
                    summ.append(salary + salary)
                else:
                    summ.append(salary + salary * 0.65)
            else:
                summ.append(salary + salary * 0.3)
        else:
            summ.append(salary)
    else:
        summ.append("Выработка не может быть отрицательной")
for i in range(len(summ)):
    print(f"{i+1}-й работник:", summ[i])



#---------------------------------Задача 3------------------------------------------
# Игра камень ножницы бумага с компьютером
# (камень побеждает ножницы / ножницы побеждает бумагу / бумага побеждает камень)
# Игрок делает ход и затем компьютер делает ход
# Вывести кто победил.

from random import *

count, trig = int(input("Введите кол-во игр: ")), 0

if count <= 0:
    print("Кол-во раундов должно быть > 0")
    exit()

while trig != count:
    user_choice = input("камень, ножницы или бумага? ")
    comp_choice = ['камень', 'ножницы', 'бумага']

    ai = choice(comp_choice)

    print("Ваш выбор: ", user_choice)
    print("Выбор ai: ", ai)

    if user_choice != 'камень' and user_choice != 'ножницы' and user_choice != 'бумага':
        print('Выбор только между камнем, ножницами и бумагой')
    elif user_choice == ai:
        print("Ничья")
    else:
        if user_choice == 'камень' and ai == 'ножницы':
            print("Ты выиграл")
        elif user_choice == 'ножницы' and ai == 'бумага':
            print("Ты выиграл")
        elif user_choice == 'бумага' and ai == 'камень':
            print("Ты выиграл")
        else:
            print("Ты проиграл")
    trig += 1



#---------------------------------Задача 4------------------------------------------

# Пользователь с клавиатуры вводит количество часов. ЧАСЫ МОГУТ БЫТЬ ДРОБНЫМИ
# Если полученное значение находится в диапазоне от 0 до 5 нужно вывести надпись Good Night,
# если в диапазоне от 6 до 13 Good Morning,
# если в диапазоне от 14 до 17 Good Day,
# если в диапазоне от 18 до 0 Good Evening.

hours = float(input("Введите кол-во часов: "))

if hours >= 0 and hours <= 24:
    if (hours >= 0 and hours <= 5) or hours == 24:
        print("Good Night")
    if hours > 5 and hours <= 13:
        print("Good Morning")
    if hours > 13 and hours <= 17:
        print("Good Day")
    if hours > 17 and hours < 24:
        print("Good Evening")
else:
    print("Неверное время")

'''





