'''
Задача No19. Решение в группах
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]

Примечание: Пользователь может вводить значения списка или список задан изначально.
'''
k = int(input('Введите целое число, на которое нужно сдвинуть последовательность вправо: '))
integers = list()
for _ in range(5):
    n = int(input('Введите целое число: '))
    integers.append(n)
print(f'Input: {integers} k = {k}')

lenght = len(integers)
k = k % lenght
print(f'Output: {integers[-k:] + integers[:-k]}')