import os


def get_available_files(data_dir="data"):
    return {
        f"{fname}": os.path.join(data_dir, fname)
        for fname in sorted(os.listdir(data_dir))
        if fname.endswith((".csv", ".xlsx", ".xpt", ".sas7bdat"))
    }
