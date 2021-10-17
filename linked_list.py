class linked_node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def add_node(self, data):
		new_node = linked_node(data)
		self.head = new_node
		print ("test")

newList = linked_list()
newList.add_node(5)
