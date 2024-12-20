import yfinance as yf
Apple=yf.Ticker('AAPL')
data=Apple.history(period='5y') # Retrieve 5 years of historical data
print(data.head())# Print the first few rows of the data
data.to_csv('apple_stock_data.csv')# Save the data to a CSV file

google=yf.Ticker('GOOG')
data=google.history(period='5y') 
print(data.head())
data.to_csv('google_stock_data.csv')

Amazon=yf.Ticker('AMZN')
data=Amazon.history(period='5y') # Retrieve 5 years of historical data
print(data.head())
data.to_csv('amazon_stock_data.csv')