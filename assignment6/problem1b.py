import sys
import matplotlib.pyplot as plt


def check(x):
  if x[0] == '-' or x[0] == '+':
    x = x[1:]
  if not x.isnumeric():
    return False
  return True


def sanitize(x, y):
  x1 = []
  y1 = []
  for i in range(len(x)):
    if check(x[i]) and check(y[i]):
      x1.append(float(x[i]))
      y1.append(float(y[i]))
  print(x1, y1)
  return x1, y1


def findPoints(fname):
  x = []
  y = []
  with open(fname) as f:
    content = f.readlines()
    x = content[0].strip().split(' ')
    x.pop(0)
    y = content[1].strip().split(' ')
    y.pop(0)
    return sanitize(x, y)


def plot(x, y, name):
  plt.scatter(x, y)
  plt.savefig(name + '.png')
  plt.show()


def main():
  files = sys.argv[1:]
  if len(files) == 0:
    print('Please provide file names as command line arguments')
    sys.exit(1)
  for fname in files:
    x, y = findPoints(fname)
    plot(x, y, fname)


main()
