import os

from pypdf import PdfReader
from conftest import RESOURSES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_reading_pdf():
    reader = PdfReader(os.path.join(RESOURSES_PATH, "docs-pytest-org-en-latest.pdf"))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    author = reader.metadata.author

    print(page)
    print(number_of_pages)
    print(text)

    assert number_of_pages == 412 and "holger krekel" in author
