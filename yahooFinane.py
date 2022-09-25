import yfinance as yf
import streamlit as st

st.write(""" 
# HI """)


data = yf.Ticker("AAPL")

# ticker_data = data.history(period="max")

ticker_data = data.history(period='1d' , start='2010-1-1', end='2020-1-1')



st.line_chart(ticker_data.Close)

st.line_chart(ticker_data.Volume)



