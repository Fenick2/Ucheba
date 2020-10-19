class Vector:

    def __init__(self, *args):
        self.args = list(args)

    def __repr__(self):
        return str(self.args)

    def __getitem__(self, item):  # Возвращает индекс с 1-цы
        if 1 <= item <= len(self.args):
            return self.args[item-1]
        else:
            raise IndexError('Индекс за границами')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.args):
            self.args[key-1] = value
        elif key > len(self.args):
            diff = key - len(self.args)
            self.args.extend([0] * diff)
            self.args[key-1] = value
        else:
            raise IndexError('Индекс за границами')

    def __delitem__(self, key):
        if 0 <= key < len(self.args):
            del self.args[key]
        else:
            raise IndexError('Индекс за границами')
