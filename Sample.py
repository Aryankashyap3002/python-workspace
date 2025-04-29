import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt
df = pd.read_csv("/home/aryankashyap/Downloads/gapminder-FiveYearData.csv")
# print(df)
# print(df.head()) 5 rows from top
# print(df.tail())  5 rows from bottom
# print(df.shape) showing how many rows and columns
# print(df.columns) print columns
# print(df.dtypes) data type of column
# print(df.info()) info abou cols dtype
country_col = df["country"] # select country col
# print(country_col.head())
subset = df[['country', 'continent', 'year']] # select more than one cols
# print(subset)
# print(df.loc[0]) print oth colms
# print(df.loc[[0, 99, 999]]) mutiple col
# print(df.iloc[1]) get the second row
subset2 = df.loc[:, ['year', 'pop']] # select only year and pop cols
subset3 = df.iloc[:, [2,4,-1]]
small_range = list(range(3))
subset4 = df.iloc[:, small_range]
data = df.loc[42, "country"] # accesing particular row an column
data = df.iloc[42, 0]
datas = df.iloc[[0,99,999], [0, 3, 5]] # accesing multiple row an column
mean = df.groupby('year')['lifeExp'].mean() # mean of lifeExp at particular year
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
# print(multi_group_var)
flat = multi_group_var.reset_index() # used to flat 
print(flat)
