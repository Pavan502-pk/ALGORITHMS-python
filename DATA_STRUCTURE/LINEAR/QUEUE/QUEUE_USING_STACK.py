class Queue:
	def __init__(self):
		self.s = []
		
	def enQueue(self, data):
		self.s.append(data)
		
	def deQueue(self):

		if len(self.s) <= 0:
			print('Queue is empty')
			return
		
		x = self.s[len(self.s) - 1]
		self.s.pop()
		
		if len(self.s) <= 0:
			return x
			
		item = self.deQueue()
		
		self.s.append(x)
		

		return item
if __name__=="__main__":
        q=Queue()
        for i in range(1,5):
                q.enQueue(i)
        for i in range(1,5):
                print(q.deQueue())
