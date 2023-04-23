import pandas as pd

from displayData import display_data
from dataConvert import convert


def delete_data():
    file = display_data()

    df = pd.read_csv(file[0])

    choice = input("Выберите колонну: ")
    print(f"Выбрана колонна - {choice}")
    choice_value = convert(df, choice, input("Выберите значение: "))
    df = df.drop(df[df[choice] == choice_value].index)

    df.to_csv(file[0], index=False)
    print(df.to_string(index=False))
