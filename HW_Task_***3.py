'''
*** (3) Напишите программу, которая принимает на вход две строки и определяет, являются ли они анаграммами.
Знаки препинания, пробелы и регистр при этом игнорируются.
Пример ввода:
- Цари, вино и сало.
- Лисица и ворона.
Пример вывода:
- YES
'''

def str_to_list(string: str):
    return sorted(x for x in string if string.isalnum())

def is_anagram(first: str, second: str) -> bool:
    """ Проверяет утверждение: "Переданные строки являются анаграммами".
    Как работает:
    1. Преобразуем строки в списки и сортируем по алфавиту.
    2. Инициализируем флаг утверждением: "Длина списка1 равна длине списка2".
    3. Если утверждение п. 2 Истинно, тогда поэлементно сравниваем отсортированные на п. 1 списки.
    4. Если очередная пара элементов не прошла проверку на равенство, инвертируем флаг в Ложь и прерываем цикл.
    5. Возвращаем значение флага.
    :param first: Первая строка для сравнения, <class 'str'>
    :param second: Вторая строка для сравнения, <class 'str'>
    :return: Истинность утверждения: "Переданные строки являются анаграммами"; <class 'bool'>
    """
    first, second = str_to_list(first), str_to_list(second)
    first_length = len(first)
    flag = first_length == len(second)
    if flag:
        for index in range(first_length):
            if first[index].upper() != second[index].upper():
                flag = not flag
                break
    return flag

def main() -> None:
    """ Главная функция.
    :return: None
    """
    check = is_anagram(first=input('Введите первую строку (выражение)\n>>> '),
                       second=input('Введите вторую строку (выражение)\n>>> '))

    print(f'Это {"" if check else "не "}анаграммы!')

if __name__ == '__main__':
    main()