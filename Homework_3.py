'''
#----------------------------Задача 1-----------------------------#
# Дано: температура в цельсиях(число) и давление в паскалях (число).
# Написать замерзнет вода или нет.
# Вода замерзает при выполнения двух условий:
# 	1. давление в 10^5 Паскаль
# 	2. температура меньше либо равно 0 градусов по цельсию

temp_C, press_Pa = int(input("Температура, цельсий: ")), int(input("Давление, паскаль: "))
if temp_C <= 0 and press_Pa == 10 ** 5:
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

#----------------------------Дополнительная задача 2-----------------------------#
#Робот может перемещаться в четырех направлениях («11» — север, «12» — запад, «13» — юг, «14» — восток)
# и принимать три цифровые команды: 0 — продолжать движение, 1 — поворот налево, –1 — поворот направо.
# Дан число (11, 12, 13 или 14) — исходное направление робота и целое число N (0, 1 или -1) — посланная ему команда.
# Вывести направление робота после выполнения полученной команды (то есть север, запад, юг или восток).


#Сделал задачу таким образом, чтобы можно было продолжать вводить направления движения, пока на вопрос "Продолжить?" не будет введено "нет".
# Использовал словарь ключ:значение


choice, trig, counter = int(input("11 - север, 12 - запад, 13 - юг, 14 - восток ")), "да", 0
side = {'11':'север', '12':'запад', '13':'юг', '14':'восток'}
if side.get(str(choice)) != None:
    print(f"Начальное значение: {side.get(str(choice))}")
else:
    print("Значение задано неверно!")
    exit()
while trig != 'нет':  # пока не будет введено "нет" на вопрос "Продолжаем?" — цикл продолжается
    move = input("Выберите направление движения: ")
    if move == '0':
        print("Иду прямо...")
    elif move == '1':
        print("Поворачиваюсь налево...")
        counter += 1
    elif move == '-1':
        print("Поворачиваюсь направо...")
        counter -= 1
    else:
        print("Можно вводить только -1, 0, 1")
    if counter > 0:
        while counter > 4:
            counter -= 4   # уменьшаем значение счетчика до границ 1 - 4, если надо
    else:
        while counter < -4:
            counter += 4  # увеличиваем значение счетчика до границ 1 - 4, если надо
    trig = input("Продолжаем? да/нет ")  # Ответ пользователя
choice += counter
if choice > 14:
    choice -= 4  #уменьшаем значение выбора (оно же значение нынешнего положения) до границ 11 - 14, если надо
elif choice < 11:
    choice += 4 #увеличиваем значение выбора (оно же значение нынешнего положения) до границ 11 - 14, если надо
print(f"Конечная точка: {side.get(str(choice))}")

'''
# ----------------------------Дополнительная задача 2-----------------------------#
# Даны два прямоугольника, стороны которых параллельны или перпендикулярны осям координат.
# Известны координаты левого нижнего угла каждого из них и длины их сторон.
# Один из прямоугольников назовем первым, другой — вторым.
# а) Определить, принадлежат ли все точки первого прямоугольника второму.
# б) Определить, принадлежат ли все точки одного из прямоугольников другому.
# в) Определить, пересекаются ли эти прямоугольники.


left_1 = [int(input("x кордината первого прямоугольника ")), int(input("y кордината первого прямоугольника "))]
w_h_1 = [int(input("ширина_1 ")), int(input("высота_1 "))]
left_2 = [int(input("x кордината второго прямоугольника ")), int(input("y кордината второго прямоугольника "))]
w_h_2 = [int(input("ширина_2 ")), int(input("высота_2 "))]

right_1 = [left_1[0] + w_h_1[0], left_1[1] + w_h_1[1]]  # Правый верхний угол перовго прямоугольника
right_2 = [left_2[0] + w_h_2[0], left_2[1] + w_h_2[1]]  # Правый верхний угол второго прямоугольника

# Просто вывод для проверки
# print(left_1, w_h_1)
# print(left_2, w_h_2)
# print(right_1, right_2)

print("-------------------------а-------------------------")

if left_2[0] <= left_1[0] and left_2[1] <= left_1[1]:
    if right_2[0] >= right_1[0] and right_2[1] >= right_1[1]:
        print("Да, первый принадлежит второму")
    else:
        print("Нет, первый не принадлежит второму")
else:
    print("Нет, первый не принадлежит второму")

print("-------------------------б-------------------------")

if left_2[0] == left_1[0] and left_2[1] == left_1[1] and right_2[0] == right_1[0] and right_2[1] == right_1[1]:
    print("Прямоугольники совпадают")
elif left_2[0] <= left_1[0] and left_2[1] <= left_1[1] and right_2[0] >= right_1[0] and right_2[1] >= right_1[1]:
    print("Да, первый принадлежит второму")
elif left_1[0] <= left_2[0] and left_1[1] <= left_2[1] and right_1[0] >= right_2[0] and right_1[1] >= right_2[1]:
    print("Да, второй принадлежит первому")
else:
    print("Не принадлежат")


print("-------------------------в-------------------------")


if (right_1[0] < left_2[0] or right_1[1] < left_2[1]) or (right_2[0] < left_1[0] or right_2[1] < left_1[1]):
    print("Не пересекаются")
else:
    print("Пересекаются")





