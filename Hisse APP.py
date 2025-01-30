import streamlit as st
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import numpy as np




symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value = 'GOOGL')

st.sidebar.write("* BIST için şirket kodunun sonuna .IS eklemelisin. Örnek: THYAO.IS")


st.title(symbol + ' Hisse Senedi Grafiği')

start_date = st.sidebar.date_input('Başlangıç Tarihi', value = datetime(2020,1,1))

end_date = st.sidebar.date_input('Bitiş Tarihi', value = datetime.now())


df = yf.download(symbol, start=start_date, end=end_date)

st.subheader('Hisse Senedi Fiyatları')
st.line_chart(df['Close'])


ticker = yf.Ticker(symbol)
financials = ticker.financials

# İlgili verileri seçin
selected_data = financials.reindex(['Gross Profit', 'Total Revenue', 'Net Income', 'Operating Revenue', 'Operating Income', 'EBITDA', 'EBIT', 'Total Expenses', 'Basic Average Shares', 'Research And Development'])

# Pandas DataFrame'e dönüştürün
selected_df = pd.DataFrame(selected_data)

# Streamlit ile finansal verileri gösterin
st.header("Yıllık Finansal Veriler")
st.dataframe(selected_df)


# Üç aylık finansal verileri alın ve işleyin
quarterly_financials = ticker.quarterly_financials
selected_data_quarterly = quarterly_financials.reindex(
    ['Gross Profit', 'Total Revenue', 'Net Income', 'Operating Revenue', 'Operating Income', 'EBITDA', 'EBIT', 'Total Expenses', 'Basic Average Shares', 'Research And Development'])
selected_df_quarterly = pd.DataFrame(selected_data_quarterly)

# Streamlit ile üç aylık finansal verileri gösterin
st.header("Çeyreklik Finansal Veriler")
st.dataframe(selected_df_quarterly)




# Close ve Volume grafiği
fig, ax1 = plt.subplots(figsize=(12,6))

color = 'tab:red'
ax1.set_xlabel('Kapanış Fiyatı')
ax1.set_ylabel('Fiyat', color=color)
ax1.plot(df['Close'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # İkinci y ekseni oluştur

color = 'tab:blue'
ax2.set_ylabel('Hacim', color=color)
ax2.bar(df.index.to_numpy(), df['Volume'], color=color, alpha=0.3)
ax2.tick_params(axis='y', labelcolor=color)

# Format x-axis ticks with dates
ax2.set_xticks(df.index.to_numpy()[::5])  # Adjust interval as needed
ax2.set_xticklabels(pd.to_datetime(df.index[::5]).strftime('%Y-%m-%d'))
ax2.set_xlabel('Tarih')

fig.tight_layout()  # Grafiği düzenle
st.pyplot(fig)  # Grafiği Streamlit'te göster