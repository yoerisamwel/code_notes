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

input("Press Enter to close...")

# Advantages of quantstats:
# 1. Simplifies performance and risk analysis of financial securities and portfolios.
# 2. Offers a wide range of statistical measures for assessing investment performance.
# 3. Can generate comprehensive plots and reports for a clear visual understanding of performance.
# 4. Integrates seamlessly with pandas for easy manipulation of financial data.
# 5. It's open-source and can be easily extended or customized for specific needs.