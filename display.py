import streamlit as st


def show_dataframe(df, filename=None, sheet=None):
    title = f"Загружено: {filename}"
    if sheet:
        title += f" | Лист: {sheet}"
    st.success(title)
    st.dataframe(df)
    st.caption(f"Размер: {df.shape[0]} строк × {df.shape[1]} столбцов")
