import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============== a =============
csvData = pd.read_csv('data.csv',sep=',') 
csvDataNum = csvData[['State','A','B','C','D','E','F','G','H','I','J','K']].to_numpy()
x=csvDataNum[:,2]
y=csvDataNum[:,9]
xAvg=np.mean(x)
yAvg=np.mean(y)

r=np.sum((x-xAvg)*(y-yAvg))/np.power(np.sum(np.power((x-xAvg),2))*np.sum(np.power((y-yAvg),2)),0.5)
print(r)
if r>0:
  print('positive correlation')
elif r<0:
  print('negative correlation')
else:
  print('no correlation')
# ============== b =============
plt.scatter(csvDataNum[:,0],x,label='Percentage farmers taking loans')
plt.scatter(csvDataNum[:,0],y,label='Per Capita Income')
plt.legend()
plt.show()