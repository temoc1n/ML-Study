import pandas as pd
import numpy as np

# 2 Core objects in pandas, DataFrames and Series

# DataFrame -> Is a table it containes an array of individual entries, each of which has a certain value, each entry correspondes to a row and column
# We can assign the index on the dataframe by using "index="
# Series -> Is a list that hold a sequence of data values, basically a column of a DataFrame, we can set an overall name

#Long Story Short -> A DataFrame is a bunch of Series

name = ['Mini', 'Miny', 'Muni']

SIZE = 3


data_frame = pd.DataFrame({name[0]: [np.random.randint(1, 10) for _ in range(SIZE)], name[1]: [np.random.randint(1,10) for _ in range(SIZE)], name[2]: [np.random.randint(1,10) for _ in range(SIZE)]}, index=["Series A", "Series B", "Series C"])

print("Saving to CSV...")


data_frame.to_csv("./mini_miny_muni.csv")

print("Saved!")