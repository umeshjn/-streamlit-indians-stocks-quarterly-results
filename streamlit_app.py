# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd

st.sidebar.markdown("# Indian Stocks Quarter Results")

## Reading the data
data = pd.read_excel('data.xlsx')

## Adding text on the sidebar
st.sidebar.markdown("India is one of the fastest growing economies and for the next decade or so should be the top growing economy in the world. Its a great investing opportunity for everyone to make the most out of it specially for the Indian public who have missed out greatly the last 30-40 years of Indian growth story. This application lets you see the results of some of the well known companies in the country.")

## Select the Companies 
selected_company = st.sidebar.selectbox(
	"Select the Company::",
	(list(data['Company'].unique()))
)


st.markdown("## " + selected_company + ' - Quarter Results Dec 2021')

modified = data[data['Company'] == selected_company]

modified[['Dec 2020']] = modified[['Dec 2020']].astype(int)
modified[['Dec 2021']] = modified[['Dec 2021']].astype(int)
modified[['Sep 2021']] = modified[['Sep 2021']].astype(int)


modified['YoY Numbers'] = modified['Dec 2021'] - modified['Dec 2020']
modified['QoQ Numbers'] = modified['Dec 2021'] - modified['Sep 2021']

st.markdown("**Year on Year - Numbers(in Crores)**")
col1, col2, col3 = st.columns(3)
col1.metric("Sales", str(modified.iat[0,4]), int(float(modified.iloc[0,5])))
col2.metric("Operating Profit", str(modified.iat[2,4]), int(float(modified.iloc[2,5])))
col3.metric("Net Profit", str(modified.iat[8,4]), int(float(modified.iloc[8,5])))


st.markdown("**Quarter on Quarter - Numbers(in Crores)**")
col1, col2, col3 = st.columns(3)
col1.metric("Sales", str(modified.iat[0,4]), int(float(modified.iloc[0,6])))
col2.metric("Operating Profit", str(modified.iat[2,4]), int(float(modified.iloc[2,6])))
col3.metric("Net Profit", str(modified.iat[8,4]), int(float(modified.iloc[8,6])))


st.table(modified[['Narration', 'Dec 2020', 'Sep 2021', 'Dec 2021']])

st.header("Credits")
st.write("This application uses the data from [screener.in](https://www.screener.in/)")
