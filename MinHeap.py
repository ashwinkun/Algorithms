class MinHeap():
	def __init__(self,size):
		self.size = size
		self.data =[]
	def printHeap(self):
		print(self.data)

	def add(self,x):
		if len(self.data) == self.size:
			return False
		self.data.append(x)
		self.bubbleup()

	def bubbleup(self):
		i = len(self.data)-1
		while i>0:
			p = (i-1)//2
			if self.data[i] < self.data[p]:
				self.data[i],self.data[p] = self.data[p],self.data[i]
				i = p
			else:
				break

	def extract(self):
		if len(self.data)==0:
			return False
		retValue = self.data[0]
		self.data[0] = self.data[len(self.data)-1]
		self.data.pop()
		self.bubbledown()

		return retValue
	def bubbledown(self):
		i = 0
		n = len(self.data)
		while (2*i)+1 <n:
			j = (2*i)+1
			if (2*i)+2<n and self.data[(2*i)+1] > self.data[(2*i)+2]:
				j = (2*i)+2

			if self.data[i]> self.data[j]:
				self.data[i],self.data[j] = self.data[j],self.data[i]
				i = j
			else:
				break


heap  = MinHeap(6)
heap.add(5)
heap.add(4)
heap.add(8)
heap.add(9)
heap.add(2)
heap.add(1)
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
print(heap.extract())
heap.printHeap()