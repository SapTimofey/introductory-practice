def func1(a):
    for i in range(2, a // 2):
        if a % 2 == 0:
            return False
    return True


print("Введите число: ")
num = int(input())
if num > 0:
    print(func1(num))


def func2(list):
    a = 0
    b = 0
    sum = 0
    for i in range(0, len(list)):
        if list[i] < 0:
            a = i
            break
    list1 = list[::-1]
    for i in range(0, len(list)):
        if list[i] < 0:
            b = i
            break
    list2 = list[a+1:len(list) - b:]
    for i in range(0, len(list2)):
        sum += list2[i]
    print(list1, list2)
    return sum


list = [1, 2, -3, 4, 5, -1, -1, 2, 3, -3, 4]
print(func2(list))


def func3(list):
    k = 1
    max1 = 0
    for i in range(0, len(list) - 1):
        if list[i] < list[i + 1]:
            k += 1
        else:
            max1 = max(max1, k)
            k = 1
    return max1


list = [1, 2, -3, 4, 5, -1, -1, 2, 3, -3, 4]
print(func3(list))


