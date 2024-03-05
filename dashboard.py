import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("main_data.csv")

st.title('Dashboard Bike Sharing Dataset')
total = df.cnt.sum()
st.metric("Total sewa", value=total)

st.subheader('Bar Chart jumlah penyewaan sepeda berdasarkan musim')
fig, ax = plt.subplots()
season = ('Springer','Summer', 'Fall', 'Winter')
counts = (471348, 918589, 1061129, 841613)
season_counts = df.groupby(by=df.season).cnt.sum()
season_counts.plot(kind='bar', xlabel='Musim', ylabel='Jumlah Penyewaan', 
                   title='Jumlah Penyewaan Sepeda Berdasarkan Musim', color=['#00b4d8','#00b4d8','#023e8a','#00b4d8'])
plt.xticks([0, 1, 2, 3], ['Springer','Summer', 'Fall', 'Winter'], rotation=45)
plt.show()
st.pyplot(fig)

st.subheader('Pola Data berdasarkan jenis pelanggan')
fig, ax = plt.subplots(figsize=(12, 5))
df['dteday'] = pd.to_datetime(df['dteday'])
ax.plot(df['dteday'], df['casual'], label='casual', color='red')
ax.plot(df['dteday'], df['registered'], label='registered', color='blue')
ax.set_xlabel('date',size=15)
ax.set_ylabel('Jumlah Pengunaan',size=15)
ax.legend()
st.pyplot(fig)

st.subheader('Korelasi Spearman antar variabel')
correlation_matrix = df[['temp',
        'hum',
        'windspeed',
        'cnt']].corr(method='spearman')
print(correlation_matrix)

fig, ax = plt.subplots()
sns.heatmap(data=correlation_matrix, annot=True, annot_kws={'size':16}, cmap='Blues')
plt.title("Korelasi Spearman")
st.pyplot(fig)

st.caption('Copyright (c) Muhammad Rifai 2024')