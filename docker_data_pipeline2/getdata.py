import pandas as pd

file="cust.csv"
df = pd.read_csv(file, header=0)
print("first few records of dataframe ")
print(df.head())
print("list of columns:-" , df.columns)
