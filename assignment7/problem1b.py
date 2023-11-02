import sys
import numpy as np


def writeMatrix(m, file):
  print(m)
  with open(file, 'w') as f:
    (r, c) = m.shape
    lines = ['' for y in range(r + 1)]
    lines[0] = f'{r} {c} \n'
    for i in range(r):
      for j in range(c):
        lines[i + 1] += str(m[i, j]) + ' '
      lines[i + 1] += '\n'
    f.writelines(lines)


def makeMatrix(file):
  with open(file, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[1:]
    m = []
    for line in lines:
      m.append([int(i) for i in line.split()])
  return m


def main():
  args = sys.argv[1:]
  if (len(args) != 2):
    print('Usage: python problem1b.py <file1> <file2>')
    sys.exit(1)

  file1 = args[0]
  file2 = args[1]
  m1 = makeMatrix(file1)
  m2 = makeMatrix(file2)

  m1 = np.array(m1, np.int32)
  m2 = np.array(m2)
  print(m1, m2)
  writeMatrix(np.add(m1, m2), 'addOp.txt')
  writeMatrix(np.dot(m1, m2), 'multOp.txt')


main()
