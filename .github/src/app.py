import streamlit as st
import pandas as pd
import numpy as np

# Sample app to display stock price and simulate random data
def main():
    st.title("Stock Price App")
    
    # Simulate some random stock data
    stock_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=100),
        'Price': np.random.rand(100) * 100
    })
    
    st.line_chart(stock_data.set_index('Date'))

if __name__ == "__main__":
    main()
