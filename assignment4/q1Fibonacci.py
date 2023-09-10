a = input('q1 part a input (integer): ')
def fib(n):
  if n < 0:
    print("Incorrect input")
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)
print(fib(int(a)))

n=input('q1 part b input  list length (integer): ')
arr=[]
for i in range(int(n)):
  arr.append(int(input('q1 part b input (list int): ')))
def majorityElement(arr):
  n = len(arr)
  maxCount = 0
  index = -1
  hash={}
  for i in range(n):
    count = 0
    if(arr[i] in hash):
      continue
    for j in range(i,n):
      if (arr[i] == arr[j]):
        count += 1
    if (count > maxCount):
      maxCount = count
      index = i
    hash[arr[i]]=count
  if (maxCount > n // 2):
    return arr[index]
  else:
    return -1
print(majorityElement([1,1,2,2,3,3,1,1,1]))


n=input('q1 part c input  list length (integer): ')
arr=[]
for i in range(int(n)):
  arr.append(int(input('q1 part c input (list int): ')))
def firstRepeating(arr):
  min = False
  hash = {}
  for i in range(len(arr)):
    if arr[i] in hash:
      min=True
      return arr[i]
    else:
      hash[arr[i]] = 1
  return "no repeating element exists"
print(firstRepeating(arr))


n=input('q1 part d input (integer): ')
def printPattern(n):
  for i in range(1,n+1):
    for j in range(1,n-i+1):
      print(' ',end='')
    for j in range(1,i+1):
      print(j,end='')
    for j in range(i-1,0,-1):
      print(j,end='')
    print()
printPattern(int(n))


def removeDuplicate(arr):
  hash={}
  for i in range(len(arr)):
    if arr[i] in hash:
      continue
    else:
      hash[arr[i]] = 1
  return list(hash.keys())
print(removeDuplicate([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7]))



