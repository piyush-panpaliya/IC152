import pandas as pd
df = pd.read_csv("data/Cars93.csv")
print(df)


def sortPrint(df):
  df = df.sort_values('Model')
  # df = df.reset_index(drop=True)
  # select some column and add index+1 as another column
  df = df[['Model']].reset_index(drop=True)
  df.index += 1
  df.to_csv('problem1a.csv')
  print(df)


sortPrint(df)

# Print all details of the costliest car of each of the ‘Types’.
# Hints (print each, then choose the appropriate ones):
# use price to find max
idx = df.groupby('Type')['Price'].idxmax()
costliest_cars = df.loc[idx]
costliest_cars.to_csv('problem1b.csv')
# df.groupby('Type').max().to_csv('problem1b.csv')
