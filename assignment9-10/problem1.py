import pandas as pd
import sys


def partA():
  df = pd.read_csv("data/Cars93.csv")
  df = df.sort_values('Model')
  df = df[['Model']].reset_index(drop=True)
  df.index += 1
  df.to_csv('problem1a.csv')
  print(df)


partA()


def partB():
  df = pd.read_csv('./data/Cars93.csv')
  df = df.drop(columns=['Unnamed: 0'])
  idx = df.groupby('Type')['Price'].idxmax()
  costliest_cars = df.loc[idx]
  costliest_cars.index += 1
  costliest_cars.to_csv('problem1b.csv')


partB()


def partC(manuf):
  df = pd.read_csv('./data/Cars93.csv')
  if (manuf in df['Manufacturer'].values):
    df = df[df['Manufacturer'] == manuf]
    return df
  return 'err'


args = sys.argv[1:]
if (len(args) != 1):
  print('give valid input')
  sys.exit(1)
# only model name or everything?
print(partC(args[0]))


def partD():
  df = pd.read_csv('./data/Cars93.csv')
  df = df.groupby('Manufacturer').size()
  df = df.reset_index(name='count')
  df[''] = df.index + 1
  df = df[['', 'Manufacturer', 'count']]
  df.to_csv('problem1d.csv', index=False)


partD()
