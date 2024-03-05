import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")


st.header("Project Analasisis Data Bike Sharing Dataset:sparkles:")

path = 'https://missionzero.sheridancollege.ca/wp-content/uploads/2019/04/DSC03493-1600x1200.jpg'
st.image(path, caption="Bicycle Rentals")

st.subheader("Rentals Bicycle")

total_peminjaman = all_df['total'].sum()
st.metric("Total rentals", value=total_peminjaman)


st.text("Beriktu adalah data tabel dari peminjaman sepeda sharing :")

all_df

