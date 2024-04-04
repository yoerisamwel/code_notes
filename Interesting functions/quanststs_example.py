import matplotlib.pyplot as plt
import quantstats as qs
import time
time.sleep(10)  # This pauses the script for 10 seconds

# Ensure the correct backend is set
plt.switch_backend('TkAgg')

stock = qs.utils.download_returns('SPY')
qs.plots.snapshot(stock, title='SPY Performance', show=True)

# Keep the window open until it is manually closed
plt.show(block=True)

# Advantages of quantstats:
# 1. Simplifies performance and risk analysis of financial securities and portfolios.
# 2. Offers a wide range of statistical measures for assessing investment performance.
# 3. Can generate comprehensive plots and reports for a clear visual understanding of performance.
# 4. Integrates seamlessly with pandas for easy manipulation of financial data.
# 5. It's open-source and can be easily extended or customized for specific needs.

#Benchmarking and Comparing with S&P 500
# Download historical returns for a stock and S&P 500 as the benchmark
stock = qs.utils.download_returns('AAPL')
benchmark = qs.utils.download_returns('SPY')

# Extend the plotting capabilities to the entire script
qs.extend_pandas()

# Benchmarking against S&P 500
qs.reports.full(stock, benchmark)

'''
This code benchmarks Apple's stock against the S&P 500, generating a comprehensive report that includes 
various performance metrics, such as Sharpe ratio, Win/Loss ratio, and Maximum Drawdown.
'''

#Monthly Returns Heatmap
stock = qs.utils.download_returns('AAPL')
qs.plots.monthly_heatmap(stock)
'''
This code creates a heatmap of the monthly returns for Apple's stock, offering a visually 
intuitive representation of performance across different months and years.
'''

#Rolling Sharpe Ratio
stock = qs.utils.download_returns('AAPL')
qs.plots.rolling_sharpe(stock)

'''
This code plots the rolling Sharpe ratio of Apple's stock over time, 
providing insights into the risk-adjusted return stability
'''

#Drawdown Underwater Plot
stock = qs.utils.download_returns('AAPL')
qs.plots.drawdown_underwater(stock)

'''
This example generates an "underwater" plot, visualizing the drawdown periods of 
Apple's stock over time. It helps in understanding the magnitude and duration of downward movements.
'''

#Comparing Two Securities

# Download historical returns for two stocks
stock1 = qs.utils.download_returns('AAPL')
stock2 = qs.utils.download_returns('MSFT')

# Plotting the cumulative returns to compare their performance
qs.plots.compare([stock1, stock2], title="AAPL vs MSFT Cumulative Returns")

'''
This example compares the cumulative returns of Apple and Microsoft, illustrating 
which stock outperformed over the same time period.
'''

input("Press Enter to close...")
