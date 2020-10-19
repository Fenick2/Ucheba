class Marks:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


m = Marks([3, 4, 4, 5, 6])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)
