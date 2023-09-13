a=input('q2 part a input (list)(comma seperated):')
a=[int(i) for i in a.split(',')]
a.sort()
print(a)
a.reverse()
print(a)


b=input('q2 part b input (list)(comma seperated):')
b=[int(i) for i in b.split(',')]
b=b*int(input('q2 part b input (integer):'))
print(b)


c=input('q2 part c input (list)(comma seperated):')
c=[int(i) for i in c.split(',')]
print('max',max(c))
print('min',min(c))


d=input('q2 part d input (list)(comma seperated):')
d=[int(i) for i in d.split(',')]
try:
  print(d.index((int(input('q2 part d input (int):')))))
except ValueError:
  print(-1)


e=input('q2 part e input (list)(comma seperated):')
e=[int(i) for i in e.split(',')]
print(sum(e))
