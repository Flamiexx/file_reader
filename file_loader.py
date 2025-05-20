import pandas as pd
import pyreadstat
import streamlit as st
from constants import CSV_SEPARATOR


def load_file(path: str, filename: str):
    """Загрузка файлу по типу і повертання DataFrame."""
    if filename.endswith(".sas7bdat"):
        df, _ = pyreadstat.read_sas7bdat(path)
        return df, None
    elif filename.endswith(".xpt"):
        df, _ = pyreadstat.read_xport(path)
        return df, None
    elif filename.endswith(".csv"):
        df = pd.read_csv(path, sep=CSV_SEPARATOR, engine="python")
        return df, None
    elif filename.endswith(".xlsx"):
        xls = pd.ExcelFile(path)
        sheet = st.selectbox("Оберіть лист Excel:", xls.sheet_names)
        df = xls.parse(sheet)
        return df, sheet
    else:
        st.error("Файл не підтримується.")
        return None, None
