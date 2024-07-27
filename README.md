# Stock Price Tracker

## Introduction
The Stock Price Tracker is a Streamlit application that allows users to track stock prices and view various financial metrics. It also provides visualizations of market indices such as Nifty 50, Sensex, and USD/INR. The app utilizes the `yfinance` library to fetch stock data.

## Features
- **Stock Price Tracking**: Enter a stock ticker and select a period to view the stock's performance over time.
- **Visualizations**: Line charts and candlestick charts for different periods (1 day, 1 week, 1 month, 6 months, 1 year, 3 years, 5 years, and max).
- **Financial Metrics**: Displays open, close, high, and low prices along with the percentage change from the previous closing.
- **Market Indices**: Line charts for Nifty 50, Sensex, and USD/INR showing the last 30 days of data.
- **Responsive Layout**: User-friendly interface with adjustable data frames.

## How to Use the App
1. **Enter Stock Ticker**: In the sidebar, enter the stock ticker symbol (e.g., `AAPL` for Apple).
2. **Select Period**: Choose the period for which you want to view the stock data (options range from 1 day to max).
3. **View Stock Data**: The app will display a line chart and a candlestick chart for the selected stock and period.
4. **Financial Metrics**: View the open, close, high, and low prices along with the percentage change from the previous closing.
5. **Market Indices**: Scroll down to view the Nifty 50, Sensex, and USD/INR charts showing the last 30 days of data.
