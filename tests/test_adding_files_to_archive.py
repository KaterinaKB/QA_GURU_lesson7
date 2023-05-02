import os
from zipfile import ZipFile
from conftest import RESOURSES_PATH, TMP_PATH


def test_adding_files_to_archive_checking_sizes(create_tmp_directory):
    with ZipFile(os.path.join(TMP_PATH, "archive_with_dif_files.zip"), "w") as archive:
        for root, dirs, files in os.walk(RESOURSES_PATH):
            for file in files:
                archive.write(os.path.join(RESOURSES_PATH, file), file)

        csv_size = archive.getinfo("eggs.csv").file_size
        xlsx_size = archive.getinfo("file_example_XLSX_50.xlsx").file_size
        xls_size = archive.getinfo("file_example_XLS_10.xls").file_size
        zip_size = archive.getinfo("hello.zip").file_size
        pdf_size = archive.getinfo("docs-pytest-org-en-latest.pdf").file_size

    assert (
        csv_size == 34
        and xls_size == 8704
        and xlsx_size == 7360
        and pdf_size == 1739253
        and zip_size == 128
    )
