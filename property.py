class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get bal')
        return self.__balance

    def set_balance(self, value):
        print('set balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Должно быть число')
        self.__balance = value

    def delete_balance(self):
        print('del balance')
        del self.__balance

    # balance = property(fget=get_balance,
    #                    fset=set_balance,
    #                    fdel=delete_balance)

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)



