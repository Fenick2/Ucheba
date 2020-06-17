def number_of_frogs(y):
    if y == 1:
        fr = 120
        return fr
    fr = (number_of_frogs(y-1) - 50) * 2
        return fr

def n_o_f2(y):
    fr = 120
    for f in range(1, y):
        fr = (fr - 50) * 2
    return fr