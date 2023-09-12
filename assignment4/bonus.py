# Write a program to find roots of a given polynomial.


def sortArr(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr
print(sortArr([1,9,2,8,3,7,4,5,6,10]))