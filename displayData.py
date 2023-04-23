import pandas as pd
import os


def display_data():
    print("Список таблиц:\n")
    for root, dirs, files in os.walk("./DataBase"):
        if root == "./DataBase":
            for filename in files:
                print(filename[0:-4])

    table_name = input("Выберите таблицу:")

    if not os.path.isfile(f'DataBase/{table_name}.csv'):
        print("Такой таблицы не существует")
        return 0

    # DataBase
    file = f'DataBase/{table_name}.csv'

    df = pd.read_csv(file)
    print(df.to_string(index=False))

    return [file, table_name]
