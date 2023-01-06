import yfinance as yf
import streamlit as st

st.write("""
# Stock Price Chart
Shown are the stock **closing price** and ***volume*** of SBI 
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'SBIN.NS'
#get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
tickerDf = yf.download(tickerSymbol, start='2010-1-1', end='2022-12-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Traded Volume
""")
st.line_chart(tickerDf.Volume)