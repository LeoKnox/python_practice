class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class List():
  def __init__(self):
    self.head = None

a = Node(3)
print(a.value, a.next)
