import matplotlib.pyplot as plt
import numpy as np

xValues, yValues = [], []
scatteredness = 0.2
m = 2
c = 3
for i in range(40):
    for j in range(40-i):
        xValues.append(i + i*np.random.normal(0,scatteredness))
        yValues.append(m*i + i*np.random.normal(0,scatteredness) + c)
xValues.append(100)
yValues.append(10000)
plt.xlabel('Random x values', fontsize = 24)
plt.ylabel('Random y values', fontsize = 24)
plt.title('Increasing gaussian noise added to x and y in y = x')

# once problem is solved, try removing outlier (100,10000) by
# uncommenting (remove ''') following lines:
xValues = xValues[:-1]
yValues = yValues[:-1]

# Estimating m
n = len(xValues)
xValues = np.array(xValues)
#write formulae of numerator and denominator of m below:-
mNum = n*np.sum(xValues*yValues) - np.sum(xValues)*np.sum(yValues)
mDen = n*np.sum(xValues*xValues) - np.sum(xValues)*np.sum(xValues)
mEst = mNum/mDen

# Estimating c
# write formulae for c below:-
cEst = (np.sum(yValues) - mEst*np.sum(xValues))/n
print(cEst)

# dropping outlier/last element (100,10000) only in the view to zoomin:-
plt.xlim(0,max(xValues[:-1]))
plt.ylim(0,max(yValues[:-1]))

plt.scatter(xValues, yValues)

# uncomment following to show estimated line fit in orange:-
plt.plot(xValues, mEst*xValues + cEst, color='orange')

plt.show()
