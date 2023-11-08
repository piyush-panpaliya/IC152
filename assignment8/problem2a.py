import sys


def read(file):
  target = None
  if file.count('.txt') != 1:
    file = f'{file}.txt'
  with open(file, 'r') as f:
    lines = f.readlines()
    target = lines[0].strip()
    listToCheck = lines[1].strip().split()
    listToCheck = [int(i) for i in listToCheck]
  return int(target), listToCheck


def check(target, listToCheck, index):
  i = len(listToCheck) // 2
  if listToCheck[i] == target:
    return index + i
  if len(listToCheck) == 1:
    return -1
  if target > listToCheck[i]:
    return check(target, listToCheck[i + 1:], index + i + 1)
  return check(target, listToCheck[:i], index)


def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 problem2a.py <file name>")
    sys.exit(1)
  target, listToCheck = read(sys.argv[1:][0])
  print(check(target, listToCheck, 0))


main()
