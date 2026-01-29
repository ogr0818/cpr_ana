import pandas as pd
import streamlit as st
from plotly import express as px
import re
from pathlib import Path


st.title(":blue[急救盤用藥分析]")
file_path = "./EER.xlsx"    # Path(uploaded_file).name
st.divider()
uploaded_file = st.file_uploader("需要時上傳檔案：", type="xlsx")
if uploaded_file is None:
    data = pd.read_excel(file_path)
    st.markdown(f'<div style="text-align: center;">\
                <h5 style="color:red";>目前檔案為內存樣本</h5>\
                </div>',
                unsafe_allow_html=True)
    st.write(f"{data.columns}")
else:
    st.write(f"上傳檔案為{Path.cwd}")
    # st.write(f"{pd.read_excel(uploaded_file).shape[0]}")