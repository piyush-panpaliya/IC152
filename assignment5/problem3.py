def prefRevCapStr(str):
  if len(str) == 0:
      return ''
  else:
    return prefRevCapStr(str[1:])+str[0].upper()

print(prefRevCapStr("Holi-to-come"),end='')
print(' -> '+"Holi-to-come")


def scatSubStr(w,s):
  if len(w) == 0:
    return True
  if w[0] in s:
    return scatSubStr(w[1:],s.replace(w[0],'',1))
  else:
    return False

print(scatSubStr("abb","cadbebb"))