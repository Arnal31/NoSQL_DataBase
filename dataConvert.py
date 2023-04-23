
def convert(data, column, value):
    column_dtype = data[column].dtype
    if str(column_dtype) == "int64":
        return int(value)
    if str(column_dtype) == "float64":
        return float(value)
    if str(column_dtype) == "bool":
        if value.lower() == "true" or value == "1":
            return True
        if value.lower() == "false" or value == "0":
            return False
    return value

