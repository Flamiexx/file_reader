import streamlit as st
import pandas as pd
import pyreadstat
import os

DATA_DIR = "data"

files = [f for f in os.listdir(DATA_DIR) if f.endswith((".sas7bdat", ".xpt", ".xlsx", ".csv"))]


if not files:
    st.warning("У папці data немає підтримуваних файлів.")
else:
    selected_file = st.selectbox("Виберіть файл:", files)
    full_path = os.path.join(DATA_DIR, selected_file)

    try:
        if selected_file.endswith(".sas7bdat"):
            df, meta = pyreadstat.read_sas7bdat(full_path)
            st.success(f"{selected_file}")
            st.dataframe(df)
            st.caption(f"Розмір: {df.shape[0]} рядків × {df.shape[1]} колонок")

        elif selected_file.endswith(".xpt"):
            df, meta = pyreadstat.read_xport(full_path)
            st.success(f"{selected_file}")
            st.dataframe(df)
            st.caption(f"Розмір: {df.shape[0]} рядків × {df.shape[1]} колонок")

        elif selected_file.endswith(".csv"):
            df = pd.read_csv("data/SDTM_spec_Variables.csv", sep="$")
            meta = None

            st.success(f"{selected_file}")
            st.dataframe(df)
            st.caption(f"Розмір: {df.shape[0]} рядків × {df.shape[1]} колонок")

        elif selected_file.endswith(".xlsx"):
            xls = pd.ExcelFile(full_path)
            sheet_names = xls.sheet_names

            selected_sheet = st.selectbox("Виберіть лист Excel:", sheet_names)
            df = xls.parse(selected_sheet)

            st.success(f"{selected_file} | Лист: {selected_sheet}")
            st.dataframe(df)
            st.caption(f"Розмір: {df.shape[0]} рядків × {df.shape[1]} колонок")

        else:
            st.error("Непідтримуваний формат файлу.")

    except Exception as e:
        st.error(f"Помилка при відкритті файлу: {e}")
