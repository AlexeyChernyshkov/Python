# ---------------------Задание 1---------------------------
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.


strin = "sdhfjlsdashhhhajhsdklshdk"
res_str = strin[:strin.find("h")] + strin[strin.rfind("h")+1:]
print(res_str)

# ---------------------Задание 2---------------------------
# Посчитайте кол-во чисел в произвольной строке (число - это набор цифр, перед число и после числа ставятся пробелы)

strin = "hg 123 fh s2h sa 123 432 sh sa1"

res_str = strin.split(" ")
count = 0
for i in res_str:
    if i.isdigit():
        count +=1
print(count)


# ---------------------Задание 3---------------------------
# Посчитайте кол-во букв в произвольной строке

strin = "hg 123 fh s2h sa 123 432 sh sa1"

count = 0
for i in strin:
    if i.isalpha():
        count +=1
print(count)


# ---------------------Задание 4---------------------------
# Пользователь вводит положительное целое число.
# Зашифровать каждую цифру серией из букв (конкретный принцип составления серии букв разработать самостоятельно).

digit = 1234567890
code_digits = {0:"a", 1:"b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}

code_string = ''.join(code_digits.get(int(_)) for _ in str(digit))
print(code_string)


# ---------------------Задание 5---------------------------
# есть словарь для шифрования, а также произвольная строка
#  Реализовать интерфейс для  шифрования и дешифрования

strin = "He22o Wo33d11"
code_str = {"1": "!", "2": "@", "3": "#"}

for i in code_str:  # Шифрование
    strin = strin.replace(i, code_str[i])

print(strin)

for i in strin:     # Расшифровка
    if i in code_str.values():
        index = list(code_str.values()).index(i)
        keys = list(code_str.keys())
        strin = strin.replace(i, keys[index])

print(strin)


# ---------------------Задание 6---------------------------
# Дана произвольная многострочная строка.
# ●	Сначала выведите третий символ этой строки.
# ●	Во второй строке выведите предпоследний символ этой строки.
# ●	В третьей строке выведите первые пять символов этой строки.
# ●	В четвертой строке выведите всю строку, кроме последних двух символов.
# ●	В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# ●	В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# ●	В седьмой строке выведите все символы в обратном порядке.
# ●	В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# ●	В девятой строке выведите длину данной строки.

strin = """Сначала выведите третий символ этой строки.
Во второй строке выведите предпоследний символ этой строки.
В третьей строке выведите первые пять символов этой строки.
В четвертой строке выведите всю строку, кроме последних двух символов.
В пятой строке выведите все символы с четными индексами.
В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
В седьмой строке выведите все символы в обратном порядке.
В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
В девятой строке выведите длину данной строки."""

s = strin.split("\n")
for i in range(len(s)):
    if i == 0:
        print(s[i][2:3])
    elif i == 1:
        print(s[i][len(s[i])-2:len(s[i])-3:-1])
    elif i == 2:
        print(s[i][:5])
    elif i == 3:
        print(s[i][:len(s[i])-2])
    elif i == 4:
        print(s[i][::2])
    elif i == 5:
        print(s[i][1::2])
    elif i == 6:
        print(s[i][::-1])
    elif i == 7:
        print(s[i][::-2])
    elif i == 8:
        print(len(s[i]))

# ---------------------Задание 7---------------------------
# Создайте словарь всех покупателей и стоимости покупок (для каждого покупателя: стоимость покупки). найти для такого словаря:
# ●	максимальную стоимость покупки и кто совершил эту покупку
# ●	кол-во сделанных продаж


buys = {"Коля": 200, "Дима": 500, "Вася": 500, "Саша": 400, "Саша2": 500}

buyers = list(buys.keys())

names = [n for n in buys if buys.get(n) == max(buys.values())]  #Имена с максимальной покупкой (на случай нескольких вариантов)
for n in names:
    print(f"{n}: {buys.get(n)} рублей")

print(f"Количество покупок: {len(buyers)}")








