"""
# Introduction

## Quantstats Library:
1. **QuantStats**:
   - `QuantStats` is a Python library that focuses on portfolio analytics, performance metrics, and risk analysis.
   - It provides easy-to-use functions for downloading stock data and visualizing key performance metrics such as cumulative returns, drawdowns, and daily returns.
   - It can also compute various statistical measures, making it a powerful tool for financial analysis.

## Code Explanation:
- This script downloads historical stock data for the SPY (S&P 500 ETF) using `quantstats` and generates a performance snapshot.
- The snapshot includes cumulative returns, drawdowns, and daily returns in a single graph.
"""

import quantstats as qs

# Download historical returns data for the SPY ETF
stock = qs.utils.download_returns('SPY')

# Generate a performance snapshot, visualizing key metrics like cumulative return and drawdown
qs.plots.snapshot(stock, title='SPY Performance', show=True)

# Additional Example:
# You can download and analyze data for other symbols like 'AAPL' or 'GOOGL'
apple_stock = qs.utils.download_returns('AAPL')
qs.plots.snapshot(apple_stock, title='Apple Performance', show=True)

# Another Example - Display a full report on performance
# The `quantstats.reports.html()` function generates a full HTML report with more detailed statistics.
qs.reports.html(stock, "SPY_report.html")

# Example of portfolio comparison
# You can compare two portfolios by providing two return series
portfolio_1 = qs.utils.download_returns('AAPL')
portfolio_2 = qs.utils.download_returns('MSFT')

qs.reports.compare(portfolio_1, portfolio_2, title='Apple vs Microsoft Performance')