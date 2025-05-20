import os

DATA_DIR = "data"


def get_available_files():
    files = {}
    for f in os.listdir(DATA_DIR):
        if f.endswith((".sas7bdat", ".xpt", ".xlsx", ".csv")):
            files[f] = os.path.join(DATA_DIR, f)
    return files
