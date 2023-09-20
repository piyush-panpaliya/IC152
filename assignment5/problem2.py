import pandas as pd
import matplotlib.pyplot as plt

def showPlot(dict):
  fd= pd.DataFrame.from_dict({'x':dict.keys(),'y':dict.values()})
  fd.plot.scatter(x='x',y='y')
  plt.show()

# fDict={0:1,1:1}
# def f(x):
#   if not (x in fDict): 
#     fDict[x] = 1.65*f(x-1)
#     return fDict[x]
#   return fDict[x]
# f(9)
# showPlot(fDict)

# gDict={0:1,1:1}
# def g(x):
#   if not (x in gDict): 
#     gDict[x] = g(x-1)+g(x-2)
#     return gDict[x]
#   return gDict[x]
# g(9)
# showPlot(gDict)

hDict={0:2,1:2}
def h(x):
  if not (x in hDict): 
    hDict[x] = 2*h(x-2)
    return hDict[x]
  return hDict[x]
# h(9)
# showPlot(hDict)

kDict={0:3,1:3}
def k(x):
  if(x<2):
    return 3
  if not (x in kDict): 
    kDict[x] =k(x-1)+k(x-3)
    return kDict[x]
  return kDict[x]
k(9)
showPlot(kDict)