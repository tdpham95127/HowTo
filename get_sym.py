
import yfinance as yf
import matplotlib.pyplot as plt
import sys

def get_current_stock_price(stock):
    # Fetch data 
    #stock      = yf.Ticker(ticker_symbol)
    today_data = stock.history(period='1d')
    current_price = today_data['Close'][0]
    return current_price

# Check if a stock ticker symbol was provided as and command-line argument
if len(sys.argv) < 2:
    sys.exit("Usage: {sys.argv[0]} TICKER")

# Define the stock ticker symbol
ticker_symbol = sys.argv[1]



# Get the stock data
stock = yf.Ticker(ticker_symbol)

current_price = get_current_stock_price(stock)

# Fetch historical data for NVIDIA
hist = stock.history(period="1mo")  # 1 year of data

# Display the data
print(hist)

#options
options = stock.options
# Display options
for exp_date in options: 
    print(exp_date)
    option_chain = stock.option_chain(exp_date)
    #calls = option_chain.calls
    #print(calls)
    puts  = option_chain.puts
    #print(puts)


# Plot the closing prices
if 0:
   plt.figure(figsize=(10, 6))
   plt.plot(hist['Close'])
   plt.title('NVIDIA Stock Closing Prices - Last 1 Month')
   plt.xlabel('Date')
   plt.ylabel('Closing Price (USD)')
   plt.xticks(rotation=45)
   plt.grid(True)
   plt.show()

print(f"Current stock price of {ticker_symbol}: ${current_price:.2f}")
