import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

all_df = pd.read_csv("all_data.csv")


st.header("Final Project Analisis Data Bike Sharing Dataset :sparkles:")

path = 'bicycle.jpg'
st.image(path, caption="Bicycle Rentals")

st.subheader("Rentals Bicycle")

total_peminjaman = all_df['total_bike_day'].sum() + all_df['total_bike_hr'].sum()
st.metric("Total rentals", value=total_peminjaman)

all_df

data_cuaca = all_df[['temperature_bike_day', 'humidity_bike_day', 'weathersit_bike_day', 'total_bike_day']]

# Menghitung rata-rata jumlah peminjaman sepeda berdasarkan kondisi cuaca
rata_rata_peminjaman_cuaca = data_cuaca.groupby('weathersit_bike_day')['total_bike_day'].mean()

# Plot visualisasi
plt.figure(figsize=(12, 6))
rata_rata_peminjaman_cuaca.plot(kind='bar', color='skyblue')
plt.title('Rata-rata Jumlah Peminjaman Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Peminjaman Sepeda')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()