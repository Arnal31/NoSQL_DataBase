import pandas as pd

from displayData import display_data
def sort():
    file = display_data()
    df = pd.read_csv(file[0])

    column = input("Выберите колонну: ")
    ascending = input("0: По убыванию/алфавиту (наоборот)\n"
                      "1: По нарастанию/алфавиту\n"
                      "Ввод: ")
    df = df.sort_values(by=column, ascending=bool(int(ascending)))
    print(df.to_string(index=False))
    df.to_csv(file[0], index=False)
