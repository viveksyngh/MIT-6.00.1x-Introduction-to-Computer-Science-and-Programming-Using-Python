class Queue(object) :
	"""
		A Queue is data structure which hold list of integers
		Integers are repersented by a list
		Items are inseted at only one rear 
		Items are deleted from other end front

	"""
	def __init__(self) :
		self.items = []

	def insert(self, item) :
		self.items.insert(0, item)

	def remove(self) :
		if len(self.items) == 0 :
			raise ValueError()
		return self.items.pop()
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
queue.insert(7)
print(queue.remove())
print(queue.remove())
print(queue.remove())