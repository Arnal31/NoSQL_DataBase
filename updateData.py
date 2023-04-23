import pandas as pd
import os

from displayData import display_data
from dataConvert import convert


def update_data():
    file = display_data()
    con_file = f'DataBase/constraints/{file[1]}c.csv'

    # Read Excel
    read_confile = pd.read_csv(con_file)
    reader = pd.read_csv(file[0])

    choice = input("Выберите номер ID: ")
    update_dict = {"ID" : int(choice)}
    column_names = reader.columns.tolist()

    for i in column_names:
        if i == "ID":
            continue
        while True:
            not_null = read_confile[i][0]
            unique = read_confile[i][1]
            value = input(f'Введите значение для столбца "{i}": ')
            if not_null and not value:
                print("Данные не могут быть пустотой\n")
                continue
            if unique:
                if value in reader[i].values:
                    print("Этот файл дубликат\n")
                    continue
            try:
                update_dict[i] = convert(reader, i, value)
            except ValueError:
                print("Введите данные корректно\n")
            else:
                break

    reader.loc[reader['ID'] == int(choice), update_dict.keys()] = update_dict.values()

    # Write updated data back to file
    print(reader.to_string(index=False))
    reader.to_csv(file[0], index=False)
    print("Данные успешно обновлены")







