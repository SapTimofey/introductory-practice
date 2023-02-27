# Написать функцию one_list(arr), которая получает список из произвольного количества элементов и 
# объединяет их в один список. Если какой-либо из является в свою очередь списком, 
# то отдельные объекты в массиве будут сглажены так, чтобы результатом был одноуровневый список.
#
# Пример:
# one_list([[1,2],[3,4,5],[6,[7],[[8]]]]) ==> [1,2,3,4,5,6,7,8]


import traceback


def one_list(arr):
    list1 = []
    for i in arr:
        if type(i) == int:
            list1.append(i)
        else:
            list1.extend(i)
    for i in list1:
        if type(i) != int:
            list1 = one_list(list1)
    return list1


# Тесты
try:
	assert one_list([1,2,3]) == [1,2,3]
	assert one_list([[1,2],[3,4,5],[6,[7],[[8]]]]) == [1,2,3,4,5,6,7,8]
	assert one_list([[0,2,[0,[4,5]]],[[]],0]) == [0,2,0,4,5,0]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")