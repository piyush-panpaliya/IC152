class queue:
  def __init__(self):
    self.queue_list = []
    self.element = None

  def isEmpty(self):
    return len(self.stack_list) == 0

  def push(self, element):
    self.queue_list += [element]

  def pop(self):
    if (self.isEmpty()):
      return None
    self.element = self.queue_list[0]
    self.queue_list = self.queue_list[1:]
    return self.element

  def peek(self):
    if (self.isEmpty()):
      return None
    self.element = self.queue_list[0]
    return self.element


queue_list = [1, 2, 3, 4, 5]
q = queue()
q.push(6)
print(q.pop())
print(q.peek())
print(q.queue_list)
