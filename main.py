import streamlit as st
from utils import get_available_files
from file_loader import load_file
from display import show_dataframe


def main():
    st.title("Перегляд файлів в data")
    st.info("Виберіть файл для перегляду")

    files = get_available_files()
    if not files:
        st.warning("Немає підтримуваних файлів.")
        return

    selected_file = st.selectbox("Оберіть файл:", list(files.keys()))
    full_path = files[selected_file]

    df, sheet = load_file(full_path, selected_file)
    if df is not None:
        show_dataframe(df, selected_file, sheet)


if __name__ == "__main__":
    main()
