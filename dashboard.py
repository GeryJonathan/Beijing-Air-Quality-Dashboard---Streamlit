
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
# data = pd.read_csv(url)

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

tab1, tab2, tab3, tab4 = st.tabs(["Konsentrasi Polutan", "Perbandingan Polutan", "Perbandingan Stasiun", "Korelasi Polutan"])

with tab1:
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

 

with tab2:
    st.subheader('Perbadandingan Polutan')

    pol1 = st.selectbox('Polutan 1', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
    pol2 = st.selectbox('Polutan 2', ['PM10', 'PM2.5', 'SO2', 'NO2', 'CO'])
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=df['day'], y=df[pol1], label=pol1, color='blue')
    sns.lineplot(x=df['day'], y=df[pol2], label=pol2, color='orange')

    plt.title('Rata-rata konsentrasi '+ pol1+' dan '+pol2+' dalam satu bulan')
    plt.xlabel('Tanggal')
    plt.ylabel('Konsentrasi')
    plt.legend()
    st.pyplot(plt.gcf())
    
with tab3:
    st.subheader('Perbadandingan Stasiun')
    
    pollutant_means = df.groupby(["station"]).agg({
    "PM2.5": "mean",
    "PM10": "mean",
    }).reset_index()

    pollutant_means_melted = pollutant_means.melt(id_vars="station", var_name="Pollutant", value_name="Mean Concentration")

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="station", y="Mean Concentration", hue="Pollutant", data=pollutant_means_melted, palette="viridis")
    plt.title('Rata-rata Polutan pada tiap Stasiun')
    plt.xlabel('Stasiun')
    plt.ylabel('Rata-rata Konsentrasi')
    st.pyplot(plt.gcf())
    
    st.subheader('Stasiun Tertinggi dan Terendah Polutan')

    # Identify the highest and lowest values for PM2.5 and PM10
    pollutant_means = df.groupby(["station"]).agg({
    "PM2.5": "mean",
    "PM10": "mean",
    }).reset_index()

    pollutant_means_melted = pollutant_means.melt(id_vars="station", var_name="Pollutant", value_name="Mean Concentration")

    max_pm25_station = pollutant_means.loc[pollutant_means['PM2.5'].idxmax(), 'station']
    min_pm25_station = pollutant_means.loc[pollutant_means['PM2.5'].idxmin(), 'station']
    max_pm10_station = pollutant_means.loc[pollutant_means['PM10'].idxmax(), 'station']
    min_pm10_station = pollutant_means.loc[pollutant_means['PM10'].idxmin(), 'station']

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="station", y="Mean Concentration", hue="Pollutant", data=pollutant_means_melted, palette="viridis", saturation=0.1)

    # Highlight the highest and lowest values for PM2.5 and PM10
    for bar in ax.patches:
        if bar.get_height() == pollutant_means_melted.loc[(pollutant_means_melted['Pollutant'] == 'PM2.5') & (pollutant_means_melted['station'] == max_pm25_station), 'Mean Concentration'].values[0]:
            bar.set_color('red')  # Highlight highest PM2.5
        elif bar.get_height() == pollutant_means_melted.loc[(pollutant_means_melted['Pollutant'] == 'PM2.5') & (pollutant_means_melted['station'] == min_pm25_station), 'Mean Concentration'].values[0]:
            bar.set_color('lightgreen')  # Highlight lowest PM2.5
        elif bar.get_height() == pollutant_means_melted.loc[(pollutant_means_melted['Pollutant'] == 'PM10') & (pollutant_means_melted['station'] == max_pm10_station), 'Mean Concentration'].values[0]:
            bar.set_color('darkred')  # Highlight highest PM10
        elif bar.get_height() == pollutant_means_melted.loc[(pollutant_means_melted['Pollutant'] == 'PM10') & (pollutant_means_melted['station'] == min_pm10_station), 'Mean Concentration'].values[0]:
            bar.set_color('green')  # Highlight lowest PM10

    legend_labels = [
        f'Highest PM2.5: {max_pm25_station}',
        f'Lowest PM2.5: {min_pm25_station}',
        f'Highest PM10: {max_pm10_station}',
        f'Lowest PM10: {min_pm10_station}',
    ]

    legend_colors = ['red', 'lightgreen', 'darkred', 'green']
    legend_patches = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in legend_colors]

    plt.legend(legend_patches, legend_labels, loc='upper right')
    plt.title('Rata-rata Polutan pada tiap Stasiun')
    plt.xlabel('Stasiun')
    plt.ylabel('Rata-rata Konsentrasi')
    st.pyplot(plt.gcf())

    
    # Point Plot stasiun yang ditunjuk
    st.subheader('Rata-rata Polutan Tiap Stasiun')

    polut = st.selectbox('Pilih Polutan', ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO'])
    stasiun = st.selectbox('Pilih Stasiun', list(data['station'].unique()))
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.pointplot(x='day', y=polut, data=df, color='skyblue', markers='o', linestyles='-', capsize=0.2)
    plt.title('Konsentrasi '+polut+' Harian Pada ' + stasiun)
    plt.xlabel('Hari dalam Satu Bulan')
    plt.ylabel('Konsentrasi '+polut)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig)
    
with tab4: 
    st.subheader('Heatmap Korelasi Polutan')

    numeric_df = df.select_dtypes(exclude=['object']).drop(['day', 'month', 'year', 'hour'], axis=1)

    cmap = sns.color_palette("viridis", as_cmap=True)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap=cmap, fmt=".2f", linewidths=0.5, ax=ax, square=True, cbar_kws={"shrink": 0.8})
    plt.title('Heatmap of Correlation between Numeric Variables')

    plt.tight_layout()
    st.pyplot(fig)