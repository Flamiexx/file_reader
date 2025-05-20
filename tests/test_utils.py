import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import get_available_files

import tempfile


def test_get_available_files(tmp_path):
    # Створюємо файли різних форматів
    supported_files = ["file1.sas7bdat", "file2.xpt", "file3.xlsx", "file4.csv"]
    unsupported_files = ["file5.txt", "file6.doc"]

    for fname in supported_files + unsupported_files:
        (tmp_path / fname).write_text("data")

    # Патчимо DATA_DIR в utils
    import utils
    utils.DATA_DIR = str(tmp_path)

    files = get_available_files()
    # В returned dict повинні бути тільки підтримуваними
    assert set(files.keys()) == set(supported_files)
