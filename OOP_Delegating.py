class Person:

    def breathe(self):
        print('Man breathing')


class Doctor(Person):

    def breathe(self):
        super().breathe()
        print('Doctor breathing')


p = Person()
d = Doctor()
