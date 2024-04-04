import pandas as pd
from numpy.random import randint

index = pd.date_range("2022-02-01", "2022-02-6")
s = pd.Series(index=index, data=randint(0, 10, 6))

# Original Series
# 2022-02-01    9
# 2022-02-02    9
# 2022-02-03    8
# 2022-02-04    3
# 2022-02-05    3
# 2022-02-06    4

s.resample('2D').sum()

# Resampled Series
# 2022-02-01    18
# 2022-02-03    11
# 2022-02-05     7

#easy way to sum the rows between the interval selected
