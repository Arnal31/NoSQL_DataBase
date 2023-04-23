from table import createTable
from addData import addData
from sort import sort
from displayData import display_data
from updateData import update_data
from deleteData import delete_data


def start_up():
    print("Здравствуйе,Это программа имитирует NoSQL базу данных. \n"
          "База данных не такая мощная и в нем нельзя хранить невозможно хранить огромные данные.\n"
          "Также эта база данных поддерживает толькоnumber типов данных\n")
    while True:
        message = input(
            "Меню: \n"
            "0: Выйти\n"
            "1: Создать таблицу\n"
            "2: Добавить элемент в таблицу\n"
            "3: Удалить элемент из таблицы\n"
            "4: Обновить элемент из таблицы\n"
            "5: Показать таблицу\n"
            "6: Сортировать таблицу\n"
            "Ввод: ")

        if message == "1":
            createTable()
        elif message == "2":
            addData()
        elif message == "3":
            delete_data()
        elif message == "4":
            update_data()
        elif message == "5":
            display_data()
        elif message == "6":
            sort()
        elif message == "0":
            return 0


if __name__ == '__main__':
    start_up()

