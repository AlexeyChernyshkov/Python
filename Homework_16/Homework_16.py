# # ------------------------Задача 1--------------------------
# Дан текстовый файл.
# Написать функцию, которая будет подсчитывать количество чисел в строке,
# которые отделены пробелами, возвращаемое значение должно быть типа int.
# Применить эту функцию для файла и найти общее кол-во таких чисел
def count_numbers(file):
    a = file.split(" ")
    count = 0
    for i in a:
        if i.isdigit():
            count += 1
    return count


with open("Test_1.txt", "r") as f:
    x = f.readline()
    print(x)
    print(count_numbers(x))

# # ------------------------Задача 2--------------------------
# Дан текстовый файл. Написать функцию, которая составляет шифр для цифр
# (шифр можете придумать свой, вот пример 1 → ! | 2 → @  | 3 → #  |  4 → $  и т.д.),
# возвращаемое значение должно быть типа string.
# Применить эту функция для файла и заменить все цифры на зашифрованные значения





