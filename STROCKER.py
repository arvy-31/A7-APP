import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

# Set the page configuration
st.set_page_config(page_title="Stock Price Tracker", layout="wide")

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: white;
    }
    .stTextInput, .stSelectbox, .stButton, .stPlotlyChart, .stDataFrame, .stTable {
        color: black;
    }
    .css-1v3fvcr {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to fetch and display stock data
@st.cache
def fetch_stock_data(ticker, period):
    stock = yf.Ticker(ticker)
    return stock.history(period=period)

def display_stock_data(ticker, period):
    data = fetch_stock_data(ticker, period)
    
    st.write(f"### {ticker} Stock Data")
    
    fig_line = px.line(data, x=data.index, y='Close', title=f'{ticker} Line Chart - {period}', labels={'Close': 'Price'})
    fig_line.update_traces(line_color='green')
    st.plotly_chart(fig_line)

    # Candle chart
    fig_candle = go.Figure(data=[go.Candlestick(x=data.index,
                                                open=data['Open'],
                                                high=data['High'],
                                                low=data['Low'],
                                                close=data['Close'])])
    fig_candle.update_layout(title=f'{ticker} Candlestick Chart - {period}',
                             xaxis_title='Date',
                             yaxis_title='Price')
    st.plotly_chart(fig_candle)

    # Open, Close, High, Low, Changes
    st.write("### Stock Metrics")
    st.write(data[['Open', 'Close', 'High', 'Low']])
    data['Change'] = (data['Close'].diff() / data['Close'].shift(1)).fillna(0)
    st.write("### Changes")
    st.write(data[['Change']])

# Sidebar for user input
st.sidebar.header("Stock Tracker")
ticker = st.sidebar.text_input("Enter Stock Ticker", value='AAPL')
period = st.sidebar.selectbox("Select Period", ['1d', '1wk', '1mo', '6mo', '1y', '3y', '5y', 'max'])
show_data = st.sidebar.button("Show Data")

# Main content
st.title("Stock Price Tracker")

if show_data:
    display_stock_data(ticker, period)

# Nifty 50, Sensex, and USD/INR changes
st.write("### Market Indices")
indices = {'Nifty 50': '^NSEI', 'Sensex': '^BSESN', 'USD/INR': 'INR=X'}
cols = st.columns(len(indices))

@st.cache
def fetch_index_data(index):
    return yf.Ticker(index).history(period='1d')

for i, (name, index) in enumerate(indices.items()):
    with cols[i]:
        st.write(f"### {name}")
        index_data = fetch_index_data(index)
        fig_index = px.line(index_data, x=index_data.index, y='Close', title=f'{name} Line Chart', labels={'Close': 'Price'})
        fig_index.update_traces(line_color='green')
        st.plotly_chart(fig_index)
