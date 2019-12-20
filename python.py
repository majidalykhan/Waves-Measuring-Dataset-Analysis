import pandas as pd
import numpy as n
import seaborn as sns
import os

path = r'F:\Bahria\Study\7\DM\Project\Dataset\Coastal Data System - Waves.csv'

#Read csv
waves = pd.read_csv(path)


waves.columns = ["time", "Hs", "Hmax","Tz","Tp","direction", "temp"]
waves["time"] = pd.to_datetime(waves["time"])
waves["year"] = waves["time"].astype(str).str[0:4]
waves["year"] = waves["year"].astype(int)

waves["time1"] = waves["time"].astype(str).str[11:16]
waves["month"] = waves["time"].astype(str).str[5:7]

waves["dir"] = 10* (waves["direction"] // 10)

waves["temp1"] = (waves["temp"] // 1)

waves[waves.temp1 > 0].pivot_table('Hs', index="temp1",columns = 'year').plot(figsize=(20,10), kind="bar")

waves.info()
waves = waves[waves.Hs > 0]
waves.head()

