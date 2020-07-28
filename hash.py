class Animal:
	def __init__(self, name):
		self.name = name
	
	def __repr__(self):
		return self.name
	
	def __hash__(self):
		return hash(self.name)

	def __eq__(self, other):
		if self.name == other.name:
			return True
		else:
			return False


cat1 = Animal('cat')
cat2 = Animal('cat')
cats = set()
cats.add(cat1)
cats.add(cat2)

print(id(cat1), hash(cat1), id(cat2), hash(cat2), sep='\n')
print(id(cat1) / hash(cat1), id(cat2) / hash(cat2), sep='\n')
print(cats)
