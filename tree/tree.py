class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree():
  def __init__(self):
    self.head = None
  def add(self, value):
    if self.head == None:
      self.head.value = 3

t = Tree()
#t.add(3)
print(t)
