#-----------------------------Задание 1----------------------------
# Дано:
# 3 стороны треугольника
# Проверить существует ли треугольник

sides = [int(input("Введите сторону ")) for i in range(3)]

for i in range(len(sides)):
    if sides[i] <= 0:
        raise ValueError("Сторона не может быть отрицательной")
sides.sort()

if sides[0] + sides[1] > sides[2]:
    print("Треугольник существует")
else:
    print("Треугольник не существует")









