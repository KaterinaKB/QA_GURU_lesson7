import os.path
import xlrd
from conftest import RESOURSES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_reading_xls():
    book = xlrd.open_workbook(os.path.join(RESOURSES_PATH, "file_example_XLS_10.xls"))
    print(f"Количество листов {book.nsheets}")
    print(f"Имена листов {book.sheet_names()}")
    sheet = book.sheet_by_index(0)
    print(f"Количество столбцов {sheet.ncols}")
    print(f"Количество строк {sheet.nrows}")
    print(f"Пересечение строки 0 и столбца 1 = {sheet.cell_value(rowx=0, colx=1)}")
    # печать всех строк по очереди
    for rx in range(sheet.nrows):
        print(sheet.row(rx))

    rows_num = sheet.nrows
    columns_num = sheet.ncols
    headers = []
    for i in range(1, 8):
        headers.append(sheet.cell_value(rowx=0, colx=i))
        i += 1

    assert (
        rows_num == 10
        and columns_num == 8
        and headers
        == ["First Name", "Last Name", "Gender", "Country", "Age", "Date", "Id"]
    )
