def mod_checker(x, mod=0):
    return (lambda y: y % x == mod)

mod_3 = mod_checker(3)
print(mod_3(3))
print(mod_3(4))

mod_4 = mod_checker(3, 1)
print(mod_4(4))

print(mod_4.__dict__)
