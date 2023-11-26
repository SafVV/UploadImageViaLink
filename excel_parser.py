from openpyxl import load_workbook
import sys
from loguru import logger

@logger.catch(reraise=True)
def get_data_in_excel(path: str) -> list:
    """Функция принимает путь к файлу эксель и возвращает данные словарями"""
    res = []
    wb = load_workbook(filename=path, read_only=True)
    ws = wb.worksheets[0]
    for row in ws.rows:
        res.append(list(map(lambda x: x.value, row)))
    return res
