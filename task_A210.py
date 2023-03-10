# Написать функцию array_of_tiers(n), которая принимает число и возвращает список чисел, 
# последовательно отсеченных по одному разряду.
#
# Пример:
# array_of_tiers(420) ==> [4, 42, 420]
# array_of_tiers(2021) ==> [2, 20, 202, 2021]


import traceback


def array_of_tiers(n):
    list1 = []
    for i in range(len(str(n))):
        list1.append(n // (10 ** i))
    list1.reverse()
    return list1


# Тесты
try:
    assert array_of_tiers(420) == [4, 42, 420]
    assert array_of_tiers(2021) == [2, 20, 202, 2021]
    assert array_of_tiers(80200) == [8, 80, 802, 8020, 80200]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

