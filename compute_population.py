from math import atan, pi


def compute_population(t):
    x = (2000 - t) / 45
    n = (172 / 45) * (pi / 2 - atan(x))
    return round(n, 3)


years_str_list = list(map(int, input().split()))
population_list = []
for i in years_str_list:
    population_list.append(compute_population(i))

for i in range(len(years_str_list)):
    print('%5d - %6.3f миллиард(ов)' % (years_str_list[i], population_list[i]))
