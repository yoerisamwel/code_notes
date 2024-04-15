# Import the quantstats library as qs for convenience.
import quantstats as qs

# Download the historical returns of the SPY ETF, which tracks the S&P 500 index.
stock = qs.utils.download_returns('SPY')

# Create a performance snapshot of the SPY ETF returns.
# This snapshot will show three plots: cumulative returns, drawdown, and daily returns.
qs.plots.snapshot(stock, title='SPY Performance', show=True)

# This script is particularly useful for financial analysts and investors looking to perform a quick
# analysis of a stock's historical performance. The plot includes a visualization of the investment
# growth over time, the periods of drawdown or losses, and the day-to-day fluctuations in returns.
