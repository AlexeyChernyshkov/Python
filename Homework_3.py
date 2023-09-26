'''
#----------------------------Задача 1-----------------------------#
# Дано: температура в цельсиях(число) и давление в паскалях (число).
# Написать замерзнет вода или нет.
# Вода замерзает при выполнения двух условий:
# 	1. давление в 10^5 Паскаль
# 	2. температура меньше либо равно 0 градусов по цельсию

temp_C, press_Pa = int(input("Температура, цельсий: ")), int(input("Давление, паскаль: "))
if temp_C <= 0 and press_Pa % 9999 > 0:
    print("YES")
else:
    print("NO")






#----------------------------Задача 2-----------------------------#
# Начальник составляет график смены, кто работает а кто нет, он вправе выбрать кого-то одного из рабочих или сразу двоих,
# используя два параметра employee1 и employee2.
# В каждый параметр он может написать “работает” или “не работает” (только эти варианты)
# Напишите программу, которая в зависимости от выбора начальника выводит информацию  о количестве работников на смене

employee1, employee2 = input("Первый: "), input("Второй: ")
if employee1 == "работает":
    if employee2 == "работает":
        print("2")
    elif employee2 == "не работает":
        print("1")
elif employee1 == "не работает":
    if employee2 == "работает":
        print("1")
    elif employee2 == "не работает":
        print("0")



#----------------------------Задача 3-----------------------------#
# Дано два числа. Найдите наибольшее четное число среди них. Если оно не существует, выведите фразу "not found"

num_1, num_2 = int(input("1st:")), int(input("2nd:"))
if num_1 % 2 !=0 and num_2 % 2 != 0:
    print('not found')
elif num_1 % 2 == 0 and num_2 % 2 != 0:
    print(num_1)
elif num_2 % 2 == 0 and num_1 % 2 != 0:
    print(num_2)
elif num_1 % 2 == 0 and num_2 % 2 == 0:
    print(max(num_1, num_2))


#----------------------------Дополнительная задача 1-----------------------------#
# Первый рабочий за один день может сделать на заказ в 100 деталей (максимум). Стоимость одной детали 1 рубль. В день максимум работает по 12 часов
# Второй рабочий за один день может сделать на заказ в 90 деталей (максимум). Стоимость одной детали 1.5 рубля. В день максимум работает по 12 часов
# Если они работают в вместе за один час они могут сделать на заказ 16 деталей. Стоимость одной детали 2 рубля.
# В таком случае смена заканчивается на 2 часа раньше. То есть оба рабочих работают по 10 часов
# Клиент вправе выбрать кого-то одного из рабочих или сразу двоих, используя два параметра employee1 и employee2.
# В каждый параметр он может написать “да” или “нет” (только эти варианты)
# Напишите программу, которая в зависимости от выбора клиента производит расчет

employee1, employee2 = input("да/нет: "), input("да/нет: ")
if (employee1 == 'да' or employee1 == 'нет') and (employee2 == 'да' or employee2 == 'нет'):
    if employee1 == employee2:
        if employee1 == 'нет':
            print('Выходной')
        elif employee1 == 'да':
            print(f'Рассчет: { 10 * 16 * 2} рублей')
    else:
        if employee1 == 'да':
            print(f'Рассчет работы первого: {100 * 1} рублей')
        elif employee1 == 'нет':
            print(f'Рассчет работы второго: {90 * 1.5} рублей')
else:
    print('да или нет')

'''
#----------------------------Дополнительная задача 2-----------------------------#
#Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
# Дан число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
# Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).


side, trig, counter = int(input("11 - север, 12 - запад, 13 - юг, 14 - восток ")), "да", 0
if side == 11:
    print("Начальное направление: север")
elif side == 12:
    print("Начальное направление: запад")
elif side == 13:
    print("Начальное направление: юг")
elif side == 14:
    print("Начальное направление: восток")
else:
    print("Неверно задано начальное положение")
while trig != 'нет':
    move = int(input("Выберите направление движения: "))
    if move == 0:
        print("Иду прямо...")
    elif move == 1:
        print("Поворачиваюсь налево...")
        counter += 1
    elif move == -1:
        print("Поворачиваюсь направо...")
        counter -= 1
    else:
        print("Можно вводить только -1, 0, 1")
    if counter > 0:
        while counter > 4:
            counter -= 4
    else:
        while counter < -4:
            counter += 4

    trig = input("Продолжаем? да/нет ")
side += counter
if side > 14:
    side -= 4
print(side)

