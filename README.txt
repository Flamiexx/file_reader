File Reader
Привіт! Це простий проєкт на Python + Streamlit для зручного перегляду таблиць у різних форматах — SAS, XPT, Excel і CSV.


Що вміє проєкт


- Автоматично знаходить підтримувані файли в папці data.

- Підтримує формати: .sas7bdat, .xpt, .xlsx, .csv.

- Для Excel дає можливість обирати лист.


Як запустити
Клонуй репозиторій:
git clone https://github.com/Flamiexx/file_reader.git
cd file_reader


Створи віртуальне оточення і встанови залежності:
python -m venv venv
source venv/bin/activate  # для Windows: venv\Scripts\activate
pip install -r requirements.txt


Запусти застосунок:
streamlit run main.py
Відкрий у браузері http://localhost:8501 і обери файл із папки data.

Тести
У проєкті є тести на основні функції завантаження файлів, щоб бути впевненим, що все працює.

Запустити тести можна так:
pytest tests