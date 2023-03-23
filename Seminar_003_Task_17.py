'''
Задача No17. Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''

list_1 = list()
for _ in range(8):
    n = int(input('Введите целое число: '))
    list_1.append(n)
print(f'Input: {list_1}')

list_2 = set(list_1)
print(f'Output: {len(list_2)}')