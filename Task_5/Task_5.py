# Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, 
# затем вводится ровно N целых чисел. 
# Какое наименьшее число переменных нужно для решения этой задачи?

N = int(input("Введите кол-во чисел N: "))
sum = 0
for i in range(N):
    number = int(input("Введите числа: "))
    sum += number
print(sum)
