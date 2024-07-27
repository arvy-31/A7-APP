import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Function to fetch and display stock data
def display_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    
    st.write(f"### {ticker} Stock Data")
    st.line_chart(data['Close'])

    # Candle chart
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title=f'{ticker} Candlestick Chart - {period}',
                      xaxis_title='Date',
                      yaxis_title='Price')
    st.plotly_chart(fig)

    # Open, Close, High, Low, Changes
    st.write("### Stock Metrics")
    st.dataframe(data[['Open', 'Close', 'High', 'Low']])

    # Correct Changes formula
    data['Change'] = (data['Close'].diff() / data['Close'].shift(1)) * 100
    st.write("### Changes")
    st.dataframe(data[['Change']])

# Function to create line charts with adjusted Y-axis range
def create_line_chart(data, title):
    fig = go.Figure(data=[go.Scatter(x=data.index, y=data['Close'], mode='lines')])
    fig.update_layout(title=title, xaxis_title='Date', yaxis_title='Price')
    # Set Y-axis range
    min_y = data['Close'].min() * 0.95
    max_y = data['Close'].max() * 1.05
    fig.update_yaxes(range=[min_y, max_y])
    return fig

# Sidebar for user input
st.sidebar.header("Stock Tracker")
ticker = st.sidebar.text_input("Enter Stock Ticker", value='AAPL')
period = st.sidebar.selectbox("Select Period", ['1d', '1wk', '1mo', '6mo', '1y', '3y', '5y', 'max'])

# Main content
st.title("Stock Price Tracker")

if ticker:
    display_stock_data(ticker, period)

# Nifty 50, Sensex, and USD/INR changes
st.write("### Market Indices (Last 30 Days)")
indices = {'Nifty 50': '^NSEI', 'Sensex': '^BSESN', 'USD/INR': 'INR=X'}
cols = st.columns(len(indices))

for i, (name, index) in enumerate(indices.items()):
    with cols[i]:
        st.write(f"### {name}")
        index_data = yf.Ticker(index).history(period='1mo')
        if not index_data.empty:
            fig = create_line_chart(index_data, f'{name} (Last 30 Days)')
            st.plotly_chart(fig)
        else:
            st.write("Data not available")

# Run the app using: streamlit run app.py
