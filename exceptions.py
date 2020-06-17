GREETING = 'Hello, '


class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + ' is inappropriate name')

__all__ = ['BadName', 'greet']