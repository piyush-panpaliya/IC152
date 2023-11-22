class stack:
  # do we have to take input as well?
  def __init__(self):
    self.stack_list = []
    self.element = None

  def isEmpty(self):
    return len(self.stack_list) == 0

  def push(self, element):
    self.stack_list = self.stack_list + [element]

  def pop(self):
    if (self.isEmpty()):
      return None
    self.element = self.stack_list[-1]
    self.stack_list = self.stack_list[:-1]
    return self.element

  def peek(self):
    if (self.isEmpty()):
      return None
    self.element = self.stack_list[-1]
    return self.element


st = stack()
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
print(st.peek())
