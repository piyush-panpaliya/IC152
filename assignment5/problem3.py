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

# ================ extra 3 ==================
ans=0
def scatSubStr2(s,p=0):
  global ans
  if len(w) == p:
    ans+=1
    p=0
  if len(s) == 0:
    return ans
  if w[p] in s:
    return scatSubStr2(s.replace(w[p],'',1),p+1)
  else:
    return ans

w="abb"
s="abbbadb"
print(scatSubStr2(s))
