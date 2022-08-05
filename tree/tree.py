class Node():
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class Tree():
  def __init__(self):
    self.head = None
  def add(self, value):
    temp = self.head
    if temp == None:
      temp = Node(value)
      self.head = temp
    elif value > temp.value:
      if temp.right == None:
        temp.right = Node(value)
      else:
        print (temp.value)
        temp = temp.right
    else:
      if temp.left == None:
        temp.left = Node(value)
      else:
        temp = temp.left

t = Tree()
t.add(3)
t.add(4)
t.add(5)
print(t.head.value)
