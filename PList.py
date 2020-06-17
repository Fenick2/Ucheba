class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x: int):
        self.x = x
        if x <= 0:
            raise NonPositiveError()
        super(PositiveList, self).append(x)



x = PositiveList([1,2,3])
x.append(5)
print(x)


