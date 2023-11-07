import sys
import time


def read(file):
  targer = None
  if file.count('.txt') != 1:
    file = f'{file}.txt'
  with open(file, 'r') as f:
    lines = f.readlines()
    target = lines[0].strip()
    listToCheck = lines[1].strip().split()
    listToCheck = [int(i) for i in listToCheck]
  return int(target), listToCheck


def checkFor(target, listToCheck):
  for i in range(len(listToCheck)):
    if listToCheck[i] == target:
      return i
  return -1


def checkBS(target, listToCheck, index):
  i = len(listToCheck) // 2
  print(listToCheck, index, i)
  if listToCheck[i] == target:
    return index + i
  if len(listToCheck) == 1:
    return -1
  if target > listToCheck[i]:
    return checkBS(target, listToCheck[i + 1:], index + i + 1)
  return checkBS(target, listToCheck[:i], index)


def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 problem2a.py <file name>")
    sys.exit(1)
  target, listToCheck = read(sys.argv[1:][0])

  startFor = time.process_time()
  checkFor(target, listToCheck)
  endFor = time.process_time()
  print('for loop time', endFor - startFor)

  startBS = time.process_time()
  checkBS(target, listToCheck, 0)
  endBS = time.process_time()
  print('binary search time', endBS - startBS)


main()
