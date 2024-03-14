import pandas as pd

data = "file.csv"  # 2M Rows
df = pd.read_csv(data)  # Takes 3.6 seconds

pd.concat([df for _ in range(20)])  # Takes 7.1 seconds

import modin.pandas as pd

data = "file.csv"  # 2M Rows
df = pd.read_csv(data)  # Takes 1.3 seconds, which is 2.75x faster

pd.concat([df for _ in range(20)])  # Takes 0.1 seconds, which is 70x faster