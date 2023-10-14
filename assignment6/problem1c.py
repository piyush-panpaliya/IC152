import sys
import numpy as np

def check(x):
  if x[0]=='-' or x[0]=='+':
    x=x[1:]
  if not x.isnumeric():
    return False
  return True
def sanitize(x,y):
  x1=[]
  y1=[]
  for i in range(len(x)):
      if check(x[i]) and check(y[i]):
        x1.append(float(x[i]))
        y1.append(float(y[i]))
  print(x1,y1)
  return x1,y1


def findPoints(fname):
  x=[]
  y=[]
  with open(fname) as f:
    content = f.readlines()
    x=content[0].strip().split(' ')
    x.pop(0)
    y=content[1].strip().split(' ')
    y.pop(0)
    return sanitize(x,y)

r=[]
def calc(x,y):
  n=len(x)
  x=np.array(x)
  y=np.array(y)
  num=n*np.sum(x*y)-np.sum(x)*np.sum(y)
  den=np.sqrt(n*np.sum(x*x)-np.sum(x)*np.sum(x))*np.sqrt(n*np.sum(y*y)-np.sum(y)*np.sum(y))
  cr=num/den
  r.append(cr)  

def main():
  files = sys.argv[1:]
  if len(files) == 0:
    print('Please provide file names as command line arguments')
    sys.exit(1)
  for fname in files:
    x,y = findPoints(fname)
    calc(x,y)

main()
print(r)
with open('Output1c.txt','w') as f:
  for i in r:
    f.write(str(i)+' ')