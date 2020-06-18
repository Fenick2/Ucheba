from functools import wraps

user = {'name': 'Nick', 'access_level': 'admin'}

def make_secure(func):
    @wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permission for {user["name"]}'
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'


print(get_password('billing'))
