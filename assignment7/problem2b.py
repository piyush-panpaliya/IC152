import sys


def main():
  args = sys.argv[1:]
  if not args:
    print('usage: filename')
    sys.exit(1)
  fA = args[0]
  fB = args[1]
  with open(rA) as f:
    lines = f.readlines()
    a = []
    b = []
    for line in lines:
      line = line.strip().split()
      a.append(line[0:3])
      b.append(line[3])
    for i in range(len(a)):
      for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
      b[i] = int(b[i])
    if len(a) == len(a[0]):
      print("Unique solution")
    elif len(a) < len(a[0]):
      print("Infinite solutions")
    else:
      print("No solution")
