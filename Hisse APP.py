import streamlit as st
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd



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

