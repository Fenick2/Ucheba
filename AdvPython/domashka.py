from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        ts = time()
        res = f(*args, **kwargs)
        te = time()
        print(f"""func: {f.__name__}({args}, {kwargs})
              took: {te-ts:2.4f} sec""")
        return res
    return wrap

