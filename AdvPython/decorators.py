user = {'name': 'Nick', 'access_level': 'guest'}

# def get_password():
#     if user['access_level'] == 'admin':
#         return '1234'

def make_secure(func):
    def secure_function():
        if user['access_level'] == 'admin':
            return func()
        else:
            return f'No admin permissions for {user["name"]}'

    return secure_function

@make_secure
def get_password():
    return '1234'


print(get_password.__name__)
print(get_password())
