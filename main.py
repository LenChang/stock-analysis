# Plot a normal distribution diagram of the 'Close' column
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy.stats import norm
from scipy.stats import anderson
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf

# Define the ticker symbol for Micron
ticker_symbol = "MU"


# Calculate date range for the past 5 years
end_date = datetime.today()
start_date = end_date - relativedelta(years=5)

# Download historical data
mu_data = yf.download(
    ticker_symbol,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d"),
)


# Ensure close_prices is non-empty and non-zero
close_prices = mu_data["Close"].dropna()
if close_prices.empty:
    raise ValueError("No non-zero close prices found in the data.")
mean = close_prices.mean()
std = close_prices.std()

# Plot histogram
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(
    close_prices,
    bins=50,
    density=True,
    alpha=0.6,
    color="g",
    label="Close Price Histogram",
)

# Anderson-Darling test for normality
ad_result = anderson(close_prices[ticker_symbol], dist="norm")
print("Anderson-Darling Test Statistic:", ad_result.statistic)
for cv, sig in zip(ad_result.critical_values, ad_result.significance_level):
    print(f"Critical Value for {sig}%: {cv}")
if ad_result.statistic < ad_result.critical_values[2]:
    print("Result: The data looks normal (fail to reject H0 at 5% level)")
else:
    print("Result: The data does not look normal (reject H0 at 5% level)")


# Plot normal distribution curve
min_bin, max_bin = bins[0], bins[-1]
x = np.linspace(min_bin, max_bin, 100)
plt.plot(x, norm.pdf(x, mean, std), "r-", lw=2, label="Normal Distribution")
plt.xlabel("Close Price")
plt.ylabel("Density")
plt.legend()
plt.show()
