import keyboard
# Создать список (автосалон), состоящий из словарей (машина). Словари должны содержать как минимум 5 полей
# (например, номер, модель, год выпуска, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# cars = [{"id":123456, "model":"Mercedes-Benz", "year": 2019, ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех машинах;
# – вывода информации о машине по введенному с клавиатуры номеру;
# – вывода количества машин, моложе введённого года;
# – обновлении всей информации о машине по введенному номеру;
# – удалении машины по номеру.
# Провести тестирование функций.

cars = [{"id": 1, "model": "Mercedes-Benz", "year": 2019, "color": "yellow"},
        {"id": 2, "model": "Audi", "year": 2010, "color": "red"},
        {"id": 3, "model": "BMW", "year": 2020, "color": "black"},
        {"id": 4, "model": "Ford", "year": 2013, "color": "yellow"},
        {"id": 5, "model": "Citroen", "year": 2015, "color": "white"},
        {"id": 6, "model": "Jeep", "year": 2009, "color": "black"},
        {"id": 7, "model": "Lada", "year": 2007, "color": "grey"},
        {"id": 8, "model": "Hyundai", "year": 2021, "color": "black"},
        {"id": 9, "model": "Ferrari", "year": 1999, "color": "red"},
        {"id": 10, "model": "Chevrolet", "year": 2018, "color": "white"}]


def prt():
    print("id\tmodel\t\t\t year\t color\n------------------------------------------")
    for i in range(10):
        print(cars[i].get("id"), "\t", end = "")
        if len(cars[i].get("model")) > 10:
            print(cars[i].get("model"), "\t", cars[i].get("year"), "\t",
                  cars[i].get("color"))
        elif len(cars[i].get("model")) > 6:
            print(cars[i].get("model"), "\t\t", cars[i].get("year"), "\t",
                  cars[i].get("color"))
        else:
            print(cars[i].get("model"), "\t\t\t", cars[i].get("year"), "\t",
                  cars[i].get("color"))



while True:
    print("1 – вывода информации о всех машинах\n",
          "2 – вывода информации о машине по введенному с клавиатуры номеру\n",
          "3 – вывода количества машин, моложе введённого года\n",
          "4 – обновлении всей информации о машине по введенному номеру\n",
          "5 – удалении машины по номеру\n", "Номер действия: ", end = "")
    num = int(input())
    if num == 1:
        prt()
        keyboard.wait("enter")

