import os
import pandas as pd
import os
import sys
from datetime import timedelta



args = sys.argv[1:]

df = pd.read_csv(args[0]+".csv")

parquet_name = args[0]+".parquet"

df.to_parquet("data/"+parquet_name)
