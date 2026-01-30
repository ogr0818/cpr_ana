import pandas as pd
import numpy as np
import streamlit as st
from plotly import express as px
import re
from pathlib import Path
from datetime import datetime, timedelta


with open(r'./statics/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["耗量輸入頁面", "📈 急救盤用藥分析"])
with tab1:
    department = st.radio("護理站/部外/ER", ['護理站', '部外單位', 'ER'], index=0, horizontal=True)
    stations = ['10', '103', '11', '12', '15', '日間', '25/26', '新生兒加護中心', '31/32', '41', '42', '51', '52', '53', '61', '62', '63', '71', '73', '81', '82', '83', '91', '92', '93', 'CCU', 'ICU-G', 'ICU-M', 'ICU-S']
    dep = ['健康管理中心', '內視鏡(胃鏡)室', '影像醫學部', '復健部', '心導管室', '心臟超音波室', '心臟重建科', '心電圖室(EKG室)', '手術室', '放射治療科', '核子醫學科', '高壓氧中心', '洗腎室']
    if department == 'ER':
         unit = '急診'
         st.markdown(f'<p style="font-size:28px";>{unit}</p>', unsafe_allow_html=True)
    elif department == '護理站':
        unit = st.selectbox('單位', stations, index=25)
    else:
        unit = st.selectbox('單位', dep, index=4)
    # st.write(f'護理站: {unit}')
    today = datetime.now()
    diff = timedelta(days=14)
    min = today - diff
    max = today + diff
    date = st.date_input('使用日期: ', 'today', min_value=min, max_value=max, format='YYYY/MM/DD')
    # st.write(f'使用日期: {date}')
    order = st.radio('急救盤:red[處方]', ['有', '無'], index=0, horizontal=True)
    change = st.radio('換盤與否', ['是', '否'], index=0, horizontal=True)
    plate = st.radio('大盤或小盤', ['大盤', '小盤'], index=0, horizontal=True)
    num = st.text_input('新盤編號:', placeholder='共 6 碼', max_chars=6)
    st.divider()
    st.subheader("急救盤耗用量：")
    vol_Adrenalin = st.number_input('Adrenalin: &nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Adenocor = st.number_input('Adenocor: &nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Agglutex = st.number_input('Agglutex: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Atropine = st.number_input('Atropine: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Cordarone = st.number_input('Cordarone: &nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Diphenhydramine = st.number_input('Diphenhydramine: ', min_value=0, max_value=30, value=0)
    vol_Dopamin = st.number_input('Dopamin: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Gendobu = st.number_input('Gendobu: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Lanoxin = st.number_input('Lanoxin: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_MgSO4 = st.number_input('MgSO4: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Norepinephrine = st.number_input('Norepinephrine: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Rolikan = st.number_input('Rolikan: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Isoproternol = st.number_input('Isoproternol: ;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Solucortef = st.number_input('Solu-cortef: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_USodin = st.number_input('U-Sodin: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_VitaCal = st.number_input('VitaCal: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;', min_value=0, max_value=30, value=0)
    vol_Vitagen50 = st.number_input('Vitagen(50%): &nbsp;', min_value=0, max_value=30, value=0)
    vol_Vitagen20 = st.number_input('Vitagen(20%): &nbsp;', min_value=0, max_value=30, value=0)

    cols =['Adrenalin', 'Adenocor', 'Agglutex', 'Atropine', 'Cordarone', 'Diphenhydramine', 'Dopamin', 'Gendobu', 'Lanoxin', 'MgSO4',
            'Norepinephrine', 'Rolikan', 'Isoproternol', 'Solu-cortef', 'U-Sodin', 'VitaCal', 'Vitagen(50%)', 'Vitagen(20%)']
    
    values = [vol_Adrenalin, vol_Adenocor, vol_Agglutex, vol_Atropine, vol_Cordarone, vol_Diphenhydramine, vol_Dopamin,
              vol_Gendobu, vol_Lanoxin, vol_MgSO4, vol_Norepinephrine, vol_Rolikan, vol_Isoproternol, vol_Solucortef,
              vol_USodin, vol_VitaCal, vol_Vitagen50, vol_Vitagen20]
    st.divider()
    reshape = list(zip(cols,values))
    record = pd.DataFrame(reshape, columns=['藥名', '耗用量'])
    st.write(record)

with tab2:
    st.title(":blue[急救盤用藥分析]")
    file_path = "./EER.xlsx"    # Path(uploaded_file).name
    
    uploaded_file = st.file_uploader("需要時上傳檔案：", type="xlsx")
    if uploaded_file is None:
        data = pd.read_excel(file_path)
        st.markdown(f'<div style="text-align: center;">\
                    <h5 style="color:red";>目前檔案為內存樣本</h5>\
                    </div>',
                    unsafe_allow_html=True)
    else:
        desktop_path = Path.home() / "Desktop"
        uploaded_desktop = st.file_uploader("📟檔案讀取：", type="xlsx")
        if uploaded_desktop is not None:
            st.write(f"檔案大小為{uploaded_desktop.size}")
    #     # st.write(f"{pd.read_excel(uploaded_file).shape[0]}")