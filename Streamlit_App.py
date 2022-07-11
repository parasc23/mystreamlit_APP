import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

path = r"C:\Users\paras.chauhan\OneDrive - Mars Inc\Desktop\Agrocel\Stripping Plant\New_Model(RPM)\Streamlit_Data.xlsx"

st.set_page_config(page_title="Correlation Chart", page_icon=":bar_chart:", layout="wide")


Plant = st.radio("PLANT",('S5','S7'))
@st.cache
def get_data_from_excel(sheet):
    df = pd.read_excel(path,sheet_name=sheet,parse_dates=['Date'],na_filter=True)
    return df

df = get_data_from_excel(sheet = Plant)

st.sidebar.header("Date Filter")
Dates = st.sidebar.multiselect(
    "Select the Date:",
    options=sorted(df["Date"].unique()),
    default=sorted(df["Date"].unique())
)

df_selection = df.query(
    "Date == @Dates"
)

correlation_data = df_selection.corr()['Efficiency'][:-1]
fig_corr_chart = px.bar(
    x = correlation_data,
    y=correlation_data.index,
    title="<b>Correlation Between Efficency and features of {}".format(Plant),
    template="plotly_white",width=1200,height=800)

st.plotly_chart(fig_corr_chart)
st.dataframe(df_selection)
