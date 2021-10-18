class linked_node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def add_node(self, data):
		if self.head == None:
			self.head = linked_node(data)
		else:
			new_node = linked_node(data)
			new_node.next = self.head
			self.head = new_node
		print ("test")

	def peek(self):
		print(self.head.value)

newList = linked_list()
newList.add_node(5)
newList.peek()
newList.add_node(7)
newList.peek()
