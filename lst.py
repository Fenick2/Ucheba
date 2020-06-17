class DoubleElementListIteration:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
        #if len(lst) % 2 != 0:
            #self.lst += [None]

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            try:
                return self.lst[self.i - 2], self.lst[self.i - 1]
            except IndexError:
                return self.lst[self.i -2], None
        else:
            raise StopIteration


class MyList(list):
    def __iter__(self):
        return DoubleElementListIteration(self)

for pair in MyList([1,2,3,4,5,6,7]):
    print(pair)
