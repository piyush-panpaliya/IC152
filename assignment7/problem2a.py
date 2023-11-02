import sys
import numpy as np


def makeMatrix(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[1:]
    m = []
    for line in lines:
      m.append([int(i) for i in line.split()])
  return np.array(m)


def main():
  args = sys.argv[1:]
  if len(args) != 2:
    print('usage: filename')
    sys.exit(1)
  fA = args[0]
  fB = args[1]
  mA = makeMatrix(fA)
  mB = makeMatrix(fB)
  print(mA)
  print(mB)


main()
