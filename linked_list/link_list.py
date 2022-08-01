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
  def print(self):
    temp = self.head
    while (temp.next != None):
      print(temp.value)
      temp = temp.next
    print(temp.value)

a = List()
a.add(5)
a.add(7)
a.add(3)
a.print()
