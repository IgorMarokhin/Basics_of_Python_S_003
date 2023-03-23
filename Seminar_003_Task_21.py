'''
Задача No21. Решение в группах
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

Примечание: Список словарей задан изначально. Пользователь его не вводит
'''

dict_1 = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}
list_1 = [0]*len(dict_1)
i = 0
for element in dict_1:
    for key in element.keys():
        list_1[i] = element[key]
        i += 1
print(list_1)
list_1 = [w.strip() for w in list_1]
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)