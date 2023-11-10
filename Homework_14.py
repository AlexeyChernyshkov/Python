"""
# ---------------------Задание 1---------------------------
# написать функцию is_positive(num), которая возвращает True в случае, если num положительное, и False во всех остальных случаях.
# Дан список чисел (только целые числа).
# Напечатать 0 и отрицательные числа в списке применив, функцию is_positive


def is_positive(num):
    if num > 0:
        return True
    else:
        return False

num_list = [12, -2, 0, 32, -5, -12, 15]

for i in num_list:
    if is_positive(i) == False:
        print(i)
"""

# ---------------------Задание 2---------------------------
# написать функцию num_to_name_week(num_day_week), которая возвращает имя дня недели(строка)
# ПРимер
# num_to_name_week(1) -> ‘Понедельник’

def num_to_name_week(num_day_week):
    week_days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}
    return week_days.get(num_day_week)

n = int(input("Введите поряковый номер дня недели "))

if 1 <= n <= 7:
    print(num_to_name_week(n))
else:
    print("Необходимо ввести от 1 до 7")



# ---------------------Задание 3---------------------------
# написать функцию для вычисления периметра n-угольника
# (проверку на существование фигуры прописать отдельную(ые) функцию(и)),
# применить эту функцию(и) для вычисления периметра n-угольника

def equilateral_perimeter(n, a):
    return n * a

def non_equilateral_perimeter(a):
    p = 0
    for i in a:
        p += i
    return p



def check(n, a):



choice = input("n-угольник равносторонний? да/нет\n")

if choice == "да":
    n = int(input("Введите количество сторон:\n"))
    a = int(input("Введите длину сторон: \n"))
    print(f"Периметр равен: {equilateral_perimeter(n, a)}")
if choice == "нет":
    n = int(input("Введите количество сторон:\n"))
    a = [int(input("Значение стороны:\n")) for _ in range(n)]
    print(f"Периметр равен: {non_equilateral_perimeter(a)}")





