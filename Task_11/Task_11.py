# Для настольной игры используются карточки с номерами от 1 до N. 
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
# Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.

n = int(input("Введите число n: "))
sum_1 = n
sum_2 = 0
for i in range(1, n):
    sum_1 += i
    sum_2 += int(input("Введите число: "))
print(sum_1 - sum_2)