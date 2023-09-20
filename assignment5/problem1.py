import pandas as pd 
import matplotlib.pyplot as plt
def readData():
  csvData = pd.read_csv('data.csv',sep=',') 
  csvDataNum = csvData[['State','A','B','C','D','E','F','G','H','I','J','K']].to_numpy()
  data = csvDataNum.tolist()
  return data

def dataFind(data,i):
  return [[x[0],x[i]] for x in data]

def highest(data):
  highest = data[0][1]
  state = data[0][0]
  for i in data:
    if i[1] > highest:
      highest = i[1]
      state = i[0]
  return state

def lowest(data):
  lowest = data[0][1]
  state = data[0][0]
  for i in data:
    if i[1] < lowest:
      lowest = i[1]
      state = i[0]
  return state

def median(data):
  data.sort(key=lambda x: x[1])
  return data[len(data)//2][1]

def average(data):
  sum = 0
  for i in data:
    sum += i[1]
  return sum/len(data)

def mode(data):
  mode = {}
  for i in data:
    if i[1] in mode:
      mode[i[1]] += 1
    else:
      mode[i[1]] = 1
  return list(mode.keys())[list(mode.values()).index(max(list(mode.values())))]

dataToPrint=[['population density',6],['percentage of marginal farmers',7],['percentage of women in the overall workforce',11]]
for i in dataToPrint:
  print(i[0]+': ')
  print('\t','highest','is',highest(dataFind(readData(),i[1])))
  print('\t','lowest','is',lowest(dataFind(readData(),i[1])))
  print('\t','median','is',median(dataFind(readData(),i[1])))
  print('\t','average','is',average(dataFind(readData(),i[1])))
  print('\t','mode','is',mode(dataFind(readData(),i[1])))
  print()


# b
data = pd.read_csv('data.csv',sep=',')
data.plot.bar(x='State',y=['D','E'])
plt.show()


# c
data.sort_values(by=['D'], inplace=True)
data.plot.bar(x='State',y=['E'])
plt.show()
