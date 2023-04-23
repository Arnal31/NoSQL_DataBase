import pandas as pd


def createTable():
    # File name and creating csv file for database
    tableName = input("Введите название таблицы: ")
    file = f'DataBase/{tableName}.csv'
    conFile = f'DataBase/constraints/{tableName}c.csv'  # contains values of constraints

    # Primary key
    primary_key_col = 'ID'

    # Variables for containing data
    data = []
    value = {}
    valueType = {}
    conValue = {}

    if bool(int(input("Добавить Primary Key: "))):
        value = {primary_key_col: []}
        valueType = {primary_key_col: "int"}

    constraints = {
        "NOT NULL": False,
        "Unique": False}
    datadict = {'constraints': constraints,
                "Name": '',
                'DataType': 'str'}

    # Creating columns
    while True:
        cpd = datadict.copy()
        a = input("Введите название колонны (оставьте пустоту если все): ")
        if not a:
            break
        s = input("Структура данных: ")
        constraints["NOT NULL"] = bool(int(input("NOT NULL: ")))
        constraints["Unique"] = bool(int(input("Unique: ")))
        cpd["constraints"] = constraints
        cpd["Name"] = a
        cpd["DataType"] = s
        data.append(cpd)

        constraints = {
            "NOT NULL": False,
            "Unique": False}

    # Sorting the data in order to add them to database
    for i in data:
        value[i["Name"]] = []
        valueType[i["Name"]] = i["DataType"]

    for j in data:
        conValue[j["Name"]] = list(j['constraints'].values())

    # Creating DataFrames
    df1 = pd.DataFrame(conValue)
    df = pd.DataFrame(value)
    df.astype(dtype=valueType)

    # Adding columns to the table
    df.to_csv(file, index=False)
    df1.to_csv(conFile, index=False)
