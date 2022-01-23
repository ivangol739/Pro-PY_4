#Итератор
class FlatIterator:

	def __init__(self, list):
		self.list = [a for b in list for a in b]

	def __iter__(self):
		self.cursor = -1
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.list):
			raise StopIteration
		return self.list[self.cursor]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None]
]

for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

#Генератор
def flat_generator(a: list):
	yield [x for sublist in a for x in sublist]

for item in flat_generator(nested_list):
	print(item)
