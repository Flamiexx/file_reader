import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from display import show_dataframe
import pandas as pd


def test_show_dataframe(monkeypatch):
    called = {}

    def fake_success(msg):
        called["success"] = msg

    def fake_dataframe(df):
        called["df"] = df

    def fake_caption(msg):
        called["caption"] = msg

    monkeypatch.setattr(st, "success", fake_success)
    monkeypatch.setattr(st, "dataframe", fake_dataframe)
    monkeypatch.setattr(st, "caption", fake_caption)

    df = pd.DataFrame({"a": [1, 2, 3]})
    show_dataframe(df, "testfile.xlsx", "Sheet1")

    assert "testfile.xlsx" in called["success"]
    assert "Sheet1" in called["success"]
    assert (called["df"] == df).all().all()
    assert "3 строк" in called["caption"] or "3 рядків" in called["caption"]
