import sys
import numpy as np


def writeMatrix(m, file):
  with open(file, 'w') as f:
    r = len(m)
    c = len(m[0])
    lines = ['' for y in range(r + 1)]
    lines[0] = f'{r} {c} \n'
    for i in range(r):
      for j in range(c):
        lines[i + 1] += str(m[i][j]) + ' '
      lines[i + 1] += '\n'
    f.writelines(lines)


def addOp(m1, m2):
  m3 = []
  for i in range(len(m1)):
    m3.append([])
    for j in range(len(m1[0])):
      m3[i].append(m1[i][j] + m2[i][j])
  return m3


def multOP(m1, m2):
  m3 = []
  for i in range(len(m1)):
    m3.append([])
    for j in range(len(m2[0])):
      m3[i].append(0)
      for k in range(len(m2[0])):
        m3[i][j] += m1[i][k] * m2[k][j]
  return m3


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
  file1 = args[0]
  file2 = args[1]

  m1 = makeMatrix(file1)
  m2 = makeMatrix(file2)

  # m1 = np.array(m1)
  # m2 = np.array(m2)

  writeMatrix(addOp(m1, m2), 'addop.txt')
  writeMatrix(multOP(m1, m2), 'multop.txt')


main()
