#------------------Задание 1--------------------------
# Найдите количество различных элементов данного массива
n = [4, -17, 3, -5, 16, 0, 36.2, 34, -2, -76, 4, 0, -2, 8, 81, 100, 25, 0, 0, 0, 0]
print(len(set(n)))

#------------------Задание 2--------------------------
# Найти наиболее часто встречающийся элемент в массиве целых чисел.

n = [4, -17, 3, -5, 16, 0, -5, -5, -5, -5, -5, -5, 36, 34, -2, -76, 4, 0, 0, 0, -2, 8, 81, 100, 25, 0, 0, 0]
count = 0
digits = []
for i in range(len(n)):
    if n.count(n[i]) > count and n[i] not in digits: #Если встречается чаще предыдущего
        count = n.count(n[i])
        digits.clear()
        digits.append(n[i])
    elif n.count(n[i]) == count and n[i] not in digits: #Если число встречается столько же раз, сколько предыдущее
        count = n.count(n[i])
        digits.append(n[i])

res = ', '.join(str(i) for i in digits)
print(f"{res} : {count} раз")

#------------------Задание 3--------------------------
# В данном массиве найти два наименьших элемента.

n = [0, 4, -17, 3, -4, 16, 6.2, 36, 34, -2, -7, 4, 0, -2, 8, 81, 100, 25]

print("min 1: ", min(set(n)))
n.remove(min(set(n)))
print("min 2: ", min(set(n)))


#------------------Задание 4--------------------------
# В данном массиве найдите наибольшую серию подряд идущих элементов, расположенных по возрастанию.

n = [0, 4, -17, 3, -4, 16, 6.2, 36, 34, -2, -7, 4, 0, -2, 9, 8, 81, 100, 250]
arr = [[n[0]]]
for i in range(1, len(n)):
    if n[i - 1] > n[i]:
        arr.append([])
    arr[-1].append(n[i])

print(max(arr, key = len))


#------------------Задание 5--------------------------
# Поменять местами наибольший и наименьший элементы массива
n = [0, -84, -17, 3, -4, 16, 6.2, 36, 34, -2, -7, 4, 0, -2, 9, 8, 81, 100, 250]

n[n.index(max(n))], n[n.index(min(n))] = min(n), max(n)

print(n)


#------------------Задание 6--------------------------
# напечатать прямоугольник (заданы длина, ширина и символ) при помощи цикла for

h, l, symbol = 6, 7, "*"
a = []
for i in range(h):
    a.append([])
    for j in range(l):
        a[i].append(symbol)

for row in a:
    print()
    for element in row:
        print(element, end=' ')

#------------------Задание 7--------------------------
# напечатать прямоугольник (заданы длина, ширина и символ) при помощи цикла for

h, l, symbol = 6, 7, "*"
a = []
for i in range(h):
    a.append([])
    for j in range(l):
        if i != 0 and i != h-1:
            if j == 0 or j == l-1:
                a[i].append(symbol)
            else:
                a[i].append(" ")
        else:
            a[i].append(symbol)

for row in a:
    print()
    for element in row:
        print(element, end=' ')




#------------------Задание 8--------------------------
# напечатать квадрат (заданы длина и символ) при помощи цикла for по образцу
# усложнение (рассматривать как отдельную задачу): программа не должна дважды проходить по уже пройденным элементам матрицы

# Если при выводе массива проход тоже считается, тогда это не усложненная версия задачи

l, symbol = 11, "*"
if l % 2 == 0:
    l += 1

a = []
for i in range(l):
    a.append([])
    for j in range(l):
        if i != 0 and i != l-1 and j != 0 and j != l-1:
            if (i % 2 != 0 and j % 2 != 0) or (i % 2 == 0 and j % 2 == 0):
                a[i].append(''.join(symbol))
            else:
                a[i].append(''.join(" "))
        else:
            a[i].append(''.join(symbol))

print('\n'.join(map(' '.join, a)))



#------------------Задание 9--------------------------
# напечатать ромб (заданы длина, ширина и символ)  при помощи цикла for

h, symbol = 20, "*"
if h % 2 == 0:
    h += 1

a = []
for i in range(h):
    a.append([])
    for j in range(h):
        if i <= int(h / 2) and int(h / 2) - i <= j <= int(h / 2) + i:
            a[i].append(symbol)
        elif i > int(h / 2) and a[int(h/2)-(i-int(h/2))][j] == "*": #тут проверяем такую же строку но в верхней части ромба (последнюю с первой и так далее)
            a[i].append(symbol)
        else:
            a[i].append(" ")

for row in a:
    print()
    for element in row:
        print(element, end=' ')



#------------------Задание 10--------------------------
#напечатать полый ромб (заданы длина, ширина и символ) при помощи цикла for

h, symbol = 7, "*"
if h % 2 == 0:
    h += 1

a = []
for i in range(h):
    a.append([])
    for j in range(h):
        if i <= int(h / 2) and (j == int(h / 2) - i or j == int(h / 2) + i):
            a[i].append(symbol)
        elif i > int(h / 2) and a[int(h/2)-(i-int(h/2))][j] == "*": #тут проверяем такую же строку но в верхней части ромба (последнюю с первой и так далее)
            a[i].append(symbol)
        else:
            a[i].append(" ")

for row in a:
    print()
    for element in row:
        print(element, end=' ')







