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


def calc(detA, dets, infinite, mA, mB):
  lines = ['3 1\n']
  if (not infinite):
    for det in dets:
      lines.append(str(float(det / detA)) + '\n')
  else:
    z = mA[0, 0] + mA[0, 1] - mB[0]
    lines.append('1\n')
    lines.append('1\n')
    lines.append(str(z[0]))
  with open('problem2bOp.txt', 'w') as f:
    f.writelines(lines)


def main():
  args = sys.argv[1:]
  if len(args) != 2:
    print('usage: filename')
    sys.exit(1)
  fA = args[0]
  fB = args[1]
  mA = makeMatrix(fA)
  mB = makeMatrix(fB)
  detA = np.linalg.det(mA)
  if (detA != 0):
    return calc(detA, dets, False, mA, mB)
  dets = []
  for i in range(3):
    mAX = mA.copy()
    mAX[:, i] = mB[:, 0]
    dets.append(np.linalg.det(mAX))
  if (dets[0] == 0 and dets[1] == 0 and dets[2] == 0):
    return calc(detA, dets, True, mA, mB)
  else:
    return


main()
