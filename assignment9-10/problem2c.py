# Create a class with a name queue, with queue_list (name
# of a list) and element as attributes. Write three methods
# under the queue class for push(), pop(), and peek()
# operations. The queue is a limited access data structure
# that follows FIFO (first in first out) rule.
# - The push() method should push its input at the
# end/top of queue_list.
# - The pop() method should remove the first/lowest
# element of queue_list, update it in the element
# attribute and return it as output.
# - The peek() method should just update the
# first/lowest element of queue_list in the element
# attribute and return it as output.
# - IMPORTANT: You are NOT allowed to use any of
# the list methods. You can use loops and indexing.
# - Test your code by giving different examples.
# - Save the code for this question in file named
# problem2c.py

class queue:
  def __init__(self, queue_list):
    self.queue_list = queue_list
    self.element = None

  def push(self, element):
    self.queue_list.append(element)

  def pop(self):
    self.element = self.queue_list[0]
    self.queue_list = self.queue_list[1:]
    return self.element

  def peek(self):
    self.element = self.queue_list[0]
    return self.element


queue_list = [1, 2, 3, 4, 5]
q = queue(queue_list)
q.push(6)
print(q.pop())
print(q.peek())
print(q.queue_list)
