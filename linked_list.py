class linked_node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class linked_list:
	def __init__(self):
		self.head = None

	def show_list(self):
		runner = this.head
		while (runner.head != None):
			print(runner.value)
		print("print list")

	def add_node(self, data):
		new_node = linked_node(data)
		if self.head == None:
			self.head = new_node
			print ("test")
		else:
			new_node.next = self.head
			self.head = new_node
			print('add node')

newList = linked_list()
newList.add_node(5)
newList.add_node(6)
newList.show_list()
