i=int(input('Enter the number of rows:'))
j=int(input('Enter the number of columns:'))
tdarr=[] 
for x in range(i):
  tdarr.append([])
  for y in range(j):
    tdarr[x].append(int(input('Enter the element:')))
k=int(input('Enter the element to be searched:'))
for i in range(len(tdarr)):
  for j in range(len(tdarr[i])):
    if tdarr[i][j]==k:
      print('Element found at [{},{}]'.format(i,j))

i=int(input('Enter the number of rows:'))
tdarr=[] 
for x in range(i):
  tdarr.append([])
  for y in range(i):
    tdarr[x].append(int(input('Enter the element:')))

def isSymmetric(tdarr):
  for i in range(len(tdarr)):
    for j in range(len(tdarr[i])):
      if tdarr[i][j]!=tdarr[j][i]:
        return False
  return True
isSymmetric(tdarr)

def isSkewSymmetric(tdarr):
  for i in range(len(tdarr)):
    for j in range(len(tdarr[i])):
      if tdarr[i][j]!=-tdarr[j][i]:
        return False
  return True
isSkewSymmetric(tdarr)

