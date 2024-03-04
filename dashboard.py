
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

# Judul Halaman
st.set_page_config(page_title="Beijing Air Quality")

# Fetch Dataset
# data = pd.read_csv('airquality.csv')
url='https://drive.google.com/file/d/1gB_mrLUSjZFFWK-R0iAIysa8i6nJYTNH/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url)

# Judul
st.title('Beijing Air Quality Dashboard')

st.write('Silahkan pilih tanggal yang ada ingin ketahui kondisi polutannya pada sidebar dikiri')

# Sidebar 
st.sidebar.header('Input tanggal :')

selected_year = st.sidebar.selectbox('Select Year', list(data['year'].unique()))
selected_month = st.sidebar.selectbox('Select Month', list(data['month'].unique()))

st.sidebar.markdown("""
### Tentang Saya
- **Nama**: Gery Jonathan Manurung
- **E-email**: geryjonathan21@gmail.com
""")


# Filter data 
df = data[(data['year'] == selected_year) & (data['month'] == selected_month)].copy()

# Discribe Dataframe
st.subheader('Overview Data dari Input Tanggal')
st.write(df.describe())

# Point Plot Tiap Hari untuk Bulan yang ditunjuk
st.subheader('Konsentrasi Polutan Harian')

polutanHari = st.selectbox('Pilih Polutan harian', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots(figsize=(10, 6))
sns.pointplot(x='day', y=polutanHari, data=df, color='skyblue', markers='o', linestyles='-', capsize=0.2)
plt.title('Konsentrasi ' +polutanHari+ ' Harian')
plt.xlabel('Hari dalam Satu Bulan')
plt.ylabel('Konsentrasi ' +polutanHari)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)


# Point Plot Tiap Bulan untuk tahun yang ditunjuk
df1 = data[(data['year'] == selected_year)].copy()
st.subheader('Konsentrasi Polutan Bulanan')

polutanBulan = st.selectbox('Pilih Polutan bulanan', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
fig, ax = plt.subplots(figsize=(10, 6))
sns.pointplot(x='month', y=polutanBulan, data=df1, color='skyblue', markers='o', linestyles='-', capsize=0.2)
plt.title('Konsentrasi ' +polutanBulan+ ' Bulanan')
plt.xlabel('Bulan dalam Satu Tahun')
plt.ylabel('Konsentrasi ' +polutanBulan)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Point Plot stasiun yang ditunjuk
st.subheader('Rata-rata Polutan Tiap Stasiun')

stasiun = st.selectbox('Check Station', list(data['station'].unique()))
fig, ax = plt.subplots(figsize=(10, 6))
sns.pointplot(x='day', y='PM2.5', data=df, color='skyblue', markers='o', linestyles='-', capsize=0.2)
plt.title('Konsentrasi PM2.5 Harian Pada' + stasiun)
plt.xlabel('Hari dalam Satu Bulan')
plt.ylabel('Konsentrasi PM2.5')
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)
