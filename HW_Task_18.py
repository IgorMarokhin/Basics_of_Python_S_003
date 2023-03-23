'''
Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5
'''

list_integers = list()
N = int(input('Введите количество элементов списка А: '))
for _ in range(N):
    integer = int(input('Введите целое число: '))
    list_integers.append(integer)
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - list_integers[0])
index = 0
for i in range(1, N):
    count = abs(X - list_integers[i])
    if count < min:
        min = count
        index = i
print(f'n = {N}')
print(f'Введенный пользователем список: {list_integers}')
print(f'x = {X}')
print(f'Число {list_integers[index]} в списке A наиболее близко по величине к числу {X}.')