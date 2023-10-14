import csv

def sanitize(word):
  word = word.lower()
  word = word.replace("'", '')
  word=word.replace('<br />','')
  for i in '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~':
    word = word.replace(i, '')
  return word
  
dict = {}
with open('problem2Input', 'r', encoding='utf-8') as f:
  lines = f.readlines()
  for line in lines:
    if line == '' or line == '\n':
      continue
    words = line.split()
    for word in words:
      word = sanitize(word)
      if word in dict:
        dict[word] += 1
      else:
        dict[word] = 1

with open('r.json', 'w', encoding='utf-8') as f:
  f.write(str(dict))
with open('problem2Output.csv', 'w', encoding='utf-8') as csvop:
  writerObj = csv.DictWriter(csvop, fieldnames=['word', 'frequency'])
  writerObj.writeheader()
  finalDict = [{'word': key, 'frequency': value}
               for key, value in dict.items()]
  writerObj.writerows(finalDict)
