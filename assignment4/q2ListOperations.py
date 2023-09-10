a=input('q2 part a input (list)(comma seperated):')
a=a.split(',')
print(a.sort())
print(a.reverse())


b=input('q2 part b input (list)(comma seperated):')
b=b.split(',')
b=b*int(input('q2 part b input (integer):'))
print(b)


c=input('q2 part c input (list)(comma seperated):')
c=c.split(',')
print('max',max(c))
print('min',min(c))


d=input('q2 part d input (list)(comma seperated):')
d=d.split(',')
try:
  print(d.index((input('q2 part d input (int):'))))
except ValueError:
  print(-1)


e=input('q2 part e input (list)(comma seperated):')
e=[int(i) for i in e.split(',')]
print(sum(e))
