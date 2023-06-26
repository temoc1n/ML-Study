import pandas as pd


csv = pd.read_csv('/Users/Duarte/Desktop/ML/Machine Learning Studies/Pandas/mini_miny_muni.csv')

print(csv['Mini'][0])
print(csv.loc[0, 'Series A'])
print(csv)