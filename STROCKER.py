import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

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
    st.write(data[['Open', 'Close', 'High', 'Low']])
    data['Change'] = data['Close'].diff()
    st.write("### Changes")
    st.write(data['Change'])

# Sidebar for user input
st.sidebar.header("Stock Tracker")
ticker = st.sidebar.text_input("Enter Stock Ticker", value='AAPL')
period = st.sidebar.selectbox("Select Period", ['1d', '1wk', '1mo', '6mo', '1y', '3y', '5y', 'max'])

# Main content
st.title("Stock Price Tracker")
display_stock_data(ticker, period)

# Nifty 50, Sensex, and USD/INR changes
st.write("### Market Indices")
indices = {'Nifty 50': '^NSEI', 'Sensex': '^BSESN', 'USD/INR': 'INR=X'}
cols = st.columns(len(indices))

for i, (name, index) in enumerate(indices.items()):
    with cols[i]:
        st.write(f"### {name}")
        index_data = yf.Ticker(index).history(period='1d')
        st.line_chart(index_data['Close'])

# Run the app using: streamlit run app.py

