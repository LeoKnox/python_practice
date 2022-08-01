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
  def remove(self, value):
    temp = self.head
    while (temp != None) and (temp.next.value != value):
      temp.next = next
    if (temp.next.value == value):
      temp.next = temp.next.next
      
      

a = List()
a.add(5)
a.add(7)
a.add(3)
a.remove(7)
a.remove(5)
a.remove(3)
a.print()
