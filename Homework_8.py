'''
#---------------------------------------------- Залание 1-------------------------------------------------
# распечатайте все числа (должны быть только положительные), которые делятся на 3 без остатка от start до end(включительно) (start, end - могут быть перепутаны),
# start , end- гарантируется, что целые числа
# Найти в этом списке самое маленькое число, которое делится на три без остатка

start, end = int(input("Введите начало: ")), int(input("Введите конец: "))
flag = True
minimum = 0
if start > end:
    start, end = end, start

while start < end + 1:
    if start % 3 == 0:
        print(start)
        if flag:
            minimum = start
            flag = False
        start += 3
    else:
        start += 1
print("Минимальное число, кратное 3: ", minimum)
'''

n = int(input("Введите кол-во строк: "))

if n % 2 == 0: #Можно было сделать проверку и raise, но решил просто n увеличивать до нечетности
    n += 1
half = (n-1)/2
for i in range(int(half + 1)):
    if i == half:
        print(" * " * n)
    if i < half :
        print(" . " * i, "*", " . " * (int(half) - i), "*", " . " * (int(half) - i), "*", " . " * i)






















