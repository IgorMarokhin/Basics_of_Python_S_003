'''
Задача No23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
больших предыдущего (элемента с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)

Примечание: Пользователь может вводить значения списка или список задан изначально.
'''
list_1 = [0, -1, 5, 2, 3]
print(f'Input: {list_1}')

count = 0
index = 0
while index < len(list_1) - 1:
    index += 1
    if list_1[index - 1] < list_1[index]:
        count += 1
print(f'Output: {count}')