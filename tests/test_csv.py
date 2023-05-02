import csv
import os
from conftest import RESOURSES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_writing_csv():
    with open(os.path.join(RESOURSES_PATH, "eggs.csv"), "w") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(["Anna", "Pavel", "Peter"])
        csvwriter.writerow(["Alex", "Serj", "Yana"])

    with open(os.path.join(RESOURSES_PATH, "eggs.csv")) as csvfile:
        csvreader = csv.reader(csvfile)
        list_of_rows = []
        for row in csvreader:
            print(row)
            list_of_rows.append(row)
        assert (
            csvreader.line_num == 2
            and list_of_rows[0] == ["Anna", "Pavel", "Peter"]
            and list_of_rows[1] == ["Alex", "Serj", "Yana"]
        )
