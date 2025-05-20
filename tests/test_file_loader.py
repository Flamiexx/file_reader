import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import pytest
from file_loader import load_file
from constants import CSV_SEPARATOR


def test_load_sas7bdat(monkeypatch):
    # Мокаєм pyreadstat.read_sas7bdat
    class DummyDF:
        pass

    def fake_read_sas7bdat(path):
        return pd.DataFrame({"a": [1,2]}), None

    monkeypatch.setattr("pyreadstat.read_sas7bdat", fake_read_sas7bdat)
    df, sheet = load_file("dummy_path.sas7bdat", "dummy.sas7bdat")
    assert isinstance(df, pd.DataFrame)
    assert sheet is None


def test_load_xpt(monkeypatch):
    def fake_read_xport(path):
        return pd.DataFrame({"b": [3,4]}), None

    monkeypatch.setattr("pyreadstat.read_xport", fake_read_xport)
    df, sheet = load_file("dummy_path.xpt", "dummy.xpt")
    assert isinstance(df, pd.DataFrame)
    assert sheet is None


def test_load_csv(tmp_path):
    file = tmp_path / "tests.csv"
    file.write_text(f"col1{CSV_SEPARATOR}col2\n1{CSV_SEPARATOR}2\n3{CSV_SEPARATOR}4")

    df, sheet = load_file(str(file), "tests.csv")
    assert isinstance(df, pd.DataFrame)
    assert sheet is None
    assert df.shape == (2, 2)


def test_load_xlsx(monkeypatch, tmp_path):
    file = tmp_path / "tests.xlsx"
    df_orig = pd.DataFrame({"x": [1, 2, 3]})
    df_orig.to_excel(file, sheet_name="Sheet1", index=False)

    import streamlit as st
    monkeypatch.setattr(st, "selectbox", lambda *args, **kwargs: "Sheet1")

    df, sheet = load_file(str(file), "tests.xlsx")
    assert isinstance(df, pd.DataFrame)
    assert sheet == "Sheet1"
    assert df.shape == (3, 1)


def test_load_unsupported(monkeypatch):
    import streamlit as st
    monkeypatch.setattr(st, "error", lambda msg: msg)
    df, sheet = load_file("path.unknown", "file.unknown")
    assert df is None and sheet is None
