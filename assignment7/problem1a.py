import sys
import random


def isValidInp(a):
  return a.isnumeric() and int(a) > 0


def makeMatrix(r, c, file):
  with open(file, 'w') as f:
    lines = ['' for y in range(r + 1)]
    lines[0] = f'{r} {c} \n'
    for i in range(r):
      for j in range(c):
        lines[i + 1] += str(random.randint(0, 9)) + ' '
      lines[i + 1] += '\n'
    f.writelines(lines)


def main():
  args = sys.argv[1:]
  r1 = args[0]
  c1 = args[1]
  r2 = args[2]
  c2 = args[3]

  if not (isValidInp(r1) and isValidInp(c1) and isValidInp(r2) and isValidInp(c2)):
    print("Invalid input")
    return
  makeMatrix(int(r1), int(c1), 'MatA.txt')
  makeMatrix(int(r2), int(c2), 'MatB.txt')


main()
