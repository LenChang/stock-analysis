import yfinance as yf
from datetime import datetime, timedelta

# Define the ticker symbol for Micron
ticker_symbol = "MU"

# Calculate date range for the past year
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Download historical data
mu_data = yf.download(
    ticker_symbol,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d"),
)

# Display the first 5 rows
print(mu_data)
