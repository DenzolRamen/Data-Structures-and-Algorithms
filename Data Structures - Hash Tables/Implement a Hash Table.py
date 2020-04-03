class HashTable:
	def __init__(self, size):
		self.data = [None]*size

	def __hash(self, key):
		if len(self.data) <= 1:
			return 0
		else:
			return hash(key) % (len(self.data)-1)

	def set(self, key, value):
		address = self.__hash(key)
		if self.data[address] == None:
			self.data[address] = []
		self.data[address].append([key, value])

	def get(self, key):
		address = self.__hash(key)
		if self.data[address] != None:
			for i in self.data[address]:
				if i[0] == key:
					return i[1]
	
	def keys(self):
		keysList = []
		for i in self.data:
			if i != None:
				for j in i:
					keysList.append(j[0])
		return keysList

# Testing
h = HashTable(3)
#print(h._hash('grapes'))
h.set('grapess', 100)
h.set('grapes', 10000)
h.set('apples', 54)
h.set('pineapples', 10)
h.set('bananas', 20)
print(h.data)
print(f'Length = {len(h.data)}')

answer = h.get('apples')
print(f'apples = {answer}')

answer = h.get('grapes')
print(f'grapes = {answer}')

answer = h.get('pineapples')
print(f'pineapples = {answer}')

answer = h.get('bananas')
print(f'bananas = {answer}')

answer = h.get('grapess')
print(f'bananas = {answer}')

key = h.keys()
print(key)




