class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'Top secret'

    @property
    def secret(self):
        s = input('Ведите пароль: ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Access denied')

    @property
    def password(self):
        print('get pass')
        return self.__password

    @staticmethod
    def is_include_number(password):
        digits = '0123456789'
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def bad_pass(password):
        with open('pass.txt') as p:
            sl = p.readlines()
            for line in sl:
                if line in password:
                    return False
            return

    @password.setter
    def password(self, value):
        print('set pass')
        if not isinstance(value, str):
            raise TypeError('Пароль дложен быть строкой')
        if len(value) < 4:
            raise ValueError('Длина пароля - не менее 4 символов')
        if len(value) > 12:
            raise ValueError('Длина пароля - не более 12 символов')
        if not User.is_include_number(value):
            raise ValueError('Пароль должен содержать цифру')
        if not User.bad_pass(value):
            raise ValueError('Пароль слишком простой')
        self.__password = value
