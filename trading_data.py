import streamlit as st
import yfinance as finance


def get_ticker(name):
    company = finance.Ticker(name)
    return company


st.title("Build and Deploy Stock Market App Using Streamlit")
st.header("A Basic Data Science Web Application")
st.sidebar.header("Developed by: \n Ritik Jain")

company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")

# fetches the data: Open, Close, High, Low and Volume
# choose the dates
From = input("enter the start date:")
To = input("enter the end date:")

google = finance.download("GOOGL", start=From, end=To)
microsoft = finance.download("MSFT", start=From, end=To)

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# choose period
peri = input("Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max \n Enter Period :")
data1 = company1.history(period=peri)
data2 = company2.history(period=peri)

# markdown syntax
st.write("""
### Google
""")

# detailed summary on Google
st.write(company1.info['longBusinessSummary'])
st.write(google)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)
