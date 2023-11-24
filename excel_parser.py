from openpyxl import load_workbook
import sys


def get_data_in_excel(path: str) -> list:
    """Функция принимает путь к файлу эксель и возвращает данные словарями"""
    res = []
    wb = load_workbook(filename=path, read_only=True)
    ws = wb.worksheets[0]
    for row in ws.rows:
        res.append(list(map(lambda x: x.value, row)))
    print(sys.getsizeof(res))
    return res
