# Написать функцию change_cent, которая принимает количество американской валюты в центах и возвращает список из четырех значений, 
# который показывает наименьшее количество монет, используемых для составления этой суммы. 
# Рассматриваются только монетные номиналы: Pennie (1 цент), Nickel (5 центов), Dime (10 центов) and Quarter (25 центов).
# Возвращаемый список должен быть формата [кол-во Pennie, кол-во Nickel, кол-во Dime, кол-во Quarter]
# Если в функцию передается вещественное число, его значение сперва должно быть округлено в меньшую сторону
# 
# Пример
# change_cent(56) ==> [1,1,0,2] --> 1 * 1 + 1 * 5 + 0 * 10 + 2 * 25


import traceback


def change_cent(money):
    money = int(money)
    list1 = []
    list2 = [25, 10, 5, 1]
    a = 0
    for i in range(4):
        while money - list2[i] >= 0:
            a += 1
            money -= list2[i]
        list1.append(a)
        a = 0
    list1.reverse()
    return list1


# Тесты
try:
    assert change_cent(29) == [4,0,0,1]  
    assert change_cent(91) == [1,1,1,3]  
    assert change_cent(0) == [0,0,0,0]     
    # assert change_cent(127) == [2,1,2,4]
    assert change_cent(127) == [2,0,0,5]
    assert change_cent(3.9) == [3,0,0,0]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
