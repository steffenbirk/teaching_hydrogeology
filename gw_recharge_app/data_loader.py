import pandas as pd
import streamlit as st
from pathlib import Path

@st.cache_data
def load_data(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path)

def get_csv_path(filename: str = "data.csv") -> str:
    # Path relative to this file (works well in multipage + deployments)
    base = Path(__file__).resolve().parent
    return str(base / filename)