class stack:
  # do we have to take input as well?
  def __init__(self):
    self.stack_list = []
    self.element = None

  def push(self, element):
    self.stack_list = self.stack_list + [element]

  def pop(self):
    self.element = self.stack_list[-1]
    self.stack_list = self.stack_list[:-1]
    return self.element

  def peek(self):
    self.element = self.stack_list[-1]
    return self.element


def main(test):
  mapper = {')': '(', ']': '[', '}': '{'}
  st = stack()
  for i in test:
    if i == '(' or i == '[' or i == '{':
      st.push(i)
    elif i == ')' or i == ']' or i == '}':
      if st.peek() == mapper[i]:
        st.pop()
      else:
        return 0
  if (len(st.stack_list) == 0):
    return 1
  else:
    return 0


print(main(input('give the algebric expression: ')))
