# Built in array / list in python
# array = []

# Implement your own array!
# With methods:
# get() ==> access the data within delete with the use of a certain index
# push() ==> add or append data in the list
# pop() ==> get/extract the last item in the list and remove it from the list
# delete() ==> delete a specific data within the array

class MyArray:
	def __init__(self):
		self.length = 0 # Initial Length of array
		self.data = {}

	def __str__(self):
		return f'Length = {self.length} | Data = {self.data}'

	def push(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def get(self, index):
		return self.data[index]

	def pop(self):
		lastItem = self.data[self.length - 1]
		del(self.data[self.length - 1])
		self.length -= 1
		return lastItem

	def delete(self, index):
		for i in range(index, self.length - 1):
			self.data[i] = self.data[i+1]
		del(self.data[self.length-1])
		self.length -= 1

# Test
newArray = MyArray()
print(newArray)

newArray.push('hi')
newArray.push('you')
newArray.push('!')
newArray.push('are')
newArray.push('nice')
print(newArray)

'''
a = newArray.pop()
print(a)
print(newArray)
'''

newArray.delete(0)
print(newArray)

newArray.delete(1)
print(newArray)

b = newArray.pop()
print(b)
print(newArray)
