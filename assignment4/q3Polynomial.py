a=input('q3 part a input (list)(comma seperated):')
a=a.split(',')
a=[int(i) for i in a]
n=int(input('q3 part a input (int):'))
a.reverse()
print(a[n])

b=int(input('q3 part b input (int):'))
print(4*b**3 - 6*b**2 + 0*b - 1)


c1=[int(i) for i in input('q3 part c input (list)(comma seperated):').split(',')]
c1.reverse()
c2=[int(i) for i in input('q3 part c input (list)(comma seperated):').split(',')]
c2.reverse()
# c1,c2=[1, 2,0, 1, 0, 4] ,[-10, 0, 3, 2]
if len(c2)>len(c1):
  c1.extend([0]*(len(c2)-len(c1)))
elif len(c1)>len(c2):
  c2.extend([0]*(len(c1)-len(c2)))
c=[c1[i]+c2[i] for i in range(len(c1))]
c.reverse()
print(c)