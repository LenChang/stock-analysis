# Plot a normal distribution diagram of the 'Close' column
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy.stats import norm
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

# Plot normal distribution curve
min_bin, max_bin = bins[0], bins[-1]
x = np.linspace(min_bin, max_bin, 100)
plt.plot(x, norm.pdf(x, mean, std), "r-", lw=2, label="Normal Distribution")


# Calculate percentage of data within one standard deviation
within_1std = close_prices[
    (close_prices["MU"] >= (mean["MU"] - std["MU"]))
    & (close_prices["MU"] <= (mean["MU"] + std["MU"]))
]
percent_1std = len(within_1std) / len(close_prices) * 100

within_2std = close_prices[
    (close_prices["MU"] >= (mean["MU"] - 2 * std["MU"]))
    & (close_prices["MU"] <= (mean["MU"] + 2 * std["MU"]))
]
percent_2std = len(within_2std) / len(close_prices) * 100


print(f"{within_1std}")

print(
    f"Mean: {mean['MU']}, Standard Deviation: {std['MU']}, within_1std: {len(within_1std)}, close_prices: {len(close_prices)}"
)
print(
    f"Percentage of data within one and two standard deviation: {percent_1std}% {percent_2std}%"
)


# Mark one, two, and three standard deviatis)")
plt.xlabel("Close Price")
plt.ylabel("Density")
plt.legend()
plt.show()
