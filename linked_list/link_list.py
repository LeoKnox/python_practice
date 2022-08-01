class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class List():
  def __init__(self):
    self.head = None
  def add(self, value):
    temp = Node(value)
    temp.next = self.head
    self.head = temp

a = List()
a.add(5)
print(a.head.value, a.head.next)
