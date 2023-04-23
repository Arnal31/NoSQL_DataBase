import pandas as pd
import os

from dataConvert import convert



def addData():
    # List of tables
    print("Список таблиц:\n")
    for root, dirs, files in os.walk("./DataBase"):
        if root == "./DataBase":
            for filename in files:
                print(filename[0:-4])

    # Asking for table name

    tableName = input("Выберите таблицу:")

    # Checking whether this file exists or not
    if not os.path.isfile(f'DataBase/{tableName}.csv'):
        print("Такой таблицы не существует")
        return 0

    file = f'DataBase/{tableName}.csv'
    con_file = f'DataBase/constraints/{tableName}c.csv'

    # Read csv file
    read_confile = pd.read_csv(con_file)
    reader = pd.read_csv(file)
    column_names = reader.columns.tolist()

    # Checking is there Primary key in table
    if "ID" in column_names:
        last_id = reader["ID"].max()

    # Variable for containing data
    data = {}
    print(type(last_id))
    # Adding values to table
    for i in column_names:
        # if there is no data, primary key will start with 0
        if i == "ID":
            if pd.isna(last_id):
                data[i] = 0
                continue
            data[i] = last_id + 1
            continue
        while True:
            # Getting constraints values
            not_null = read_confile[i][0]
            unique = read_confile[i][1]

            value = input(f'Введите значение для столбца "{i}": ')
            if not_null and not value:
                print("Данные не могут быть пустотой\n")
                continue
            if unique:
                if value in reader[i].values:
                    print("Это значение должно быть уникальным\n")
                    continue
            try:
                data[i] = convert(reader, i, value)
            except ValueError:
                print("Введите данные корректно\n")
            else:
                break

    df = pd.DataFrame(data, index=[0])
    reader = reader._append(df, ignore_index=True)

    print(df.to_string(index=False))
    reader.to_csv(file, index=False)
