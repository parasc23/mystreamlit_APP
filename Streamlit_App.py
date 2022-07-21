import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

path = r"Streamlit_Data.xlsx"

st.set_page_config(page_title="Correlation Chart", page_icon=":bar_chart:", layout="wide")



Plant = st.radio("Choose Plant:",('S5','S7'))

st.title(f"**Correlation Chart of {Plant}**", anchor=None)

def get_data_from_excel(sheet):
    df = pd.read_excel(path,sheet_name=sheet,parse_dates=['Date'],na_filter=True)
    df['Date'] = df['Date'].dt.date
    return df

df = get_data_from_excel(sheet = Plant)

date_set = sorted(df['Date'].unique())

st.sidebar.header("Date Filter")
Dates = st.sidebar.multiselect(
    "Select the Date:",
    options=date_set,
    default=date_set)

df_selection = df.query(
    "Date == @Dates"
)

correlation_data = df_selection.corr()
fig = px.imshow(correlation_data, color_continuous_scale='RdBu_r', origin='lower',width=1400,height=1200,text_auto=".2f")
for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 9
# fig_corr_chart = px.bar(
#     x = correlation_data,
#     y=correlation_data.index,
#     template="plotly_white",width=1200,height=800,
# labels=dict(x="Efficiency", y="Features"))

st.plotly_chart(fig)
