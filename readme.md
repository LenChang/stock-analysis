## Stock Analysis Script (`main.py`)

This repository includes a script for analyzing the historical closing prices of Micron Technology (MU) stock using Python. The script performs the following steps:

1. **Data Download**: Fetches the last 5 years of daily closing price data for MU using the `yfinance` library.
2. **Data Cleaning**: Removes any missing or zero values from the closing price data to ensure accurate analysis.
3. **Statistical Analysis**:
   - Calculates the mean and standard deviation of the closing prices.
   - Computes the percentage of data points within one, two, and three standard deviations from the mean.
   - Performs the Anderson-Darling test to assess the normality of the data.
4. **Visualization**:
   - Plots a histogram of the closing prices.
   - Overlays a normal distribution curve and a fitted normal curve on the histogram.
   - Displays a Q-Q plot to visually assess normality.

These analyses help to understand the distribution and statistical properties of the stock's closing prices over the selected period.
