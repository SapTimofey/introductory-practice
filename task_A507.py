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


def prt(num_car):
    if num_car == 0:
        num_car -= 1
        print("id\tmodel\t\t\t year\t color\n------------------------------------------")
        for i in range(len(cars)):
            print(cars[i].get("id"), "\t", end="")
            if len(cars[i].get("model")) > 10:
                print(cars[i].get("model"), "\t", cars[i].get("year"), "\t",
                      cars[i].get("color"))
            elif len(cars[i].get("model")) > 6:
                print(cars[i].get("model"), "\t\t", cars[i].get("year"), "\t",
                      cars[i].get("color"))
            else:
                print(cars[i].get("model"), "\t\t\t", cars[i].get("year"), "\t",
                      cars[i].get("color"))
    elif 0 < num_car < 11:
        k = 0
        for i in range(len(cars)):
            if cars[i].get("id") == num_car:
                k = 1
                print("id\t", end="")
                if len(cars[i].get("model")) > 10:
                    print("model\t\t\t year\t color\n------------------------------------------")
                elif len(cars[i].get("model")) > 6:
                    print("model\t\t year\t color\n------------------------------------------")
                else:
                    print("model\t year\t color\n------------------------------------------")
                print(cars[i].get("id"), " ", cars[i].get("model"), "\t", cars[i].get("year"), "\t", cars[i].get("color"))
        if k == 0:
            print("Нет такого автомобиля.")
    else:
        k = 0
        print("id\tmodel\t\t\t year\t color\n------------------------------------------")
        for i in range(len(cars)):
            if cars[i].get("year") < num_car:
                k = 1
                print(cars[i].get("id"), "\t", end="")
                if len(cars[i].get("model")) > 10:
                    print(cars[i].get("model"), "\t", cars[i].get("year"), "\t",
                          cars[i].get("color"))
                elif len(cars[i].get("model")) > 6:
                    print(cars[i].get("model"), "\t\t", cars[i].get("year"), "\t",
                          cars[i].get("color"))
                else:
                    print(cars[i].get("model"), "\t\t\t", cars[i].get("year"), "\t",
                          cars[i].get("color"))
        if k == 0:
            print("Нет такого автомобиля.")


def update(num_car):
    k = 0
    for i in range(len(cars)):
        if cars[i].get("id") == num_car:
            k = 1
            print("Введите модель автомобиля: ", end="")
            cars[num_car-1]["model"] = input()
            print("Введите год выпуска автомобиля: ", end="")
            cars[num_car-1]["year"] = int(input())
            print("Введите цвет автомобиля: ", end="")
            cars[num_car-1]["color"] = input()
    if k == 0:
        print("Нет такого автомобиля.")


while True:
    print("1 – вывода информации о всех машинах\n",
          "2 – вывода информации о машине по введенному с клавиатуры номеру\n",
          "3 – вывода количества машин, моложе введённого года\n",
          "4 – обновлении всей информации о машине по введенному номеру\n",
          "5 – удалении машины по номеру\n", "Номер действия: ", end="")
    num = int(input())
    if num == 1:
        prt(0)
    elif num == 2:
        print("Введите id автомобиля: ", end="")
        prt(int(input()))
    elif num == 3:
        print("Введите год выпуска автомобиля: ", end="")
        prt(int(input()))
    elif num == 4:
        print("Введите id автомобиля: ", end="")
        update(int(input()))
    elif num == 5:
        print("Введите id автомобиля: ", end="")
        cars.pop(int(input())-1)
