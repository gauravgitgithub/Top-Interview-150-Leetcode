class Node:
	def __init__(self, data):
		self.value = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None


	def append(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
			return

		last_node = self.head
		while last_node.next:
			last_node = last_node.next

		last_node.next = new_node


	def insert_at_beginning(self, data):
		new_node = Node(data)

		if self.head is None:
			new_node.next = None
			self.head = new_node
			return

		first_node = self.head
		new_node.next = first_node
		self.head = new_node


	def insert_after_node(self, target_node_data, data):
		
		current_node = self.head

		while current_node:

			if current_node.value == target_node_data:
				temp_next_node = current_node.next

				node_to_add = Node(data)
				node_to_add.next = temp_next_node
				current_node.next = node_to_add
				return
			current_node = current_node.next



	def display(self):
		current_node = self.head

		while current_node:
			print(current_node.value, end = " -> ")
			current_node = current_node.next
		print("None")


	def reverse(self):
		prev = None
		current = self.head

		while current:
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev


	def search(self, value):
		current_node = self.head

		while current_node:
			if current_node.value == value:
				return True
			current_node = current_node.next

		return False
		


if __name__ == "__main__":
	listA = LinkedList()
	listA.append(10)
	listA.append(24)
	listA.append(56)
	listA.append(99)
	listA.append(35)
	listA.insert_after_node(56, 1)
	listA.insert_after_node(99, 100)
	listA.insert_at_beginning(11)
	listA.insert_at_beginning(5)

	listA.display()

	listA.reverse()
	listA.display()


	print("Search Result for 19", listA.search(19))
	print("Search Result for 5", listA.search(5))

