'''

#---------------------------------Задача 1------------------------------------------
#даны 3 числа, распечатать в порядке возрастания

digits = [int(input("1st: ")), int(input("2nd: ")), int(input("3rd: "))]

digits.sort()
print(digits)
'''


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


