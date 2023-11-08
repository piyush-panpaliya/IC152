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


def check(target, listToCheck):
  for i in range(len(listToCheck)):
    if listToCheck[i] == target:
      return i
  return -1


def main():
  if (len(sys.argv) != 2):
    print("Usage: python3 problem2b.py <file name>")
    sys.exit(1)
  target, listToCheck = read(sys.argv[1:][0])
  print(check(target, listToCheck))


main()
