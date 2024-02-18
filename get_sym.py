
import yfinance as yf
import matplotlib.pyplot as plt
import sys

# Check if a stock ticker symbol was provided as and command-line argument
if len(sys.argv) < 2:
    print("Usage: {sys.argv[0]} TICKER")

# Define the stock ticker symbol
ticker_symbol = sys.argv[1]

# Get the stock data
sym_data = yf.Ticker(ticker_symbol)

# Fetch historical data for NVIDIA
hist = sym_data.history(period="1mo")  # 1 year of data

# Display the data
print(hist)

# Plot the closing prices
#plt.figure(figsize=(10, 6))
#plt.plot(hist['Close'])
#plt.title('NVIDIA Stock Closing Prices - Last 1 Month')
#plt.xlabel('Date')
#plt.ylabel('Closing Price (USD)')
#plt.xticks(rotation=45)
#plt.grid(True)
#plt.show()
