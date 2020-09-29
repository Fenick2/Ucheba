class Example:
    def hello():  # вызывается только от класса
        print('hello')

    def instance_hello(self):  # вызывается только от экземпляра
        print(f'instance_hello {self}')

    @staticmethod
    def static_hello():  # Profit!
        print('static hello')

    @classmethod
    def class_hello(cls):  # вызывает метод класса у экземпляра
        print(f'class_hello {cls}')
