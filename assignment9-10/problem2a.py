class IC152:
  def __init__(self, name, roll, marks):
    self.name = None
    self.roll = None
    self.marks = None
    if roll[:3].upper() == 'B23' and roll[3:].isdigit() and len(roll) == 6:
      self.roll = roll
    if marks.isdigit() and int(marks) >= 0 and int(marks) <= 100:
      self.marks = marks
    if name.isalpha():
      self.name = name

  def check(self):
    if self.name == None or self.roll == None or self.marks == None:
      return False
    else:
      return True

  def result(self):
    if self.check():
      if int(self.marks) >= 33:
        return 'pass'
      else:
        return 'fail'
    else:
      return 'Invalid Input'


name = input('enter name: ')
roll = input('enter roll: ')
marks = input('enter marks: ')

student = IC152(name, roll, marks)
print(student.result())
