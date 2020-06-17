#print(list(map(abs,list(map(int, input().split())))))

people = {'Bob Smith': 16, 'Alice Taylor': 19, 'Rolf Wilson': 21, 'Anna Miller': 17}
adult_names = []

# for person in people:
#     if people[person] >= 18:
#         name = person.split()[0]
#         adult_names.append(name)

# print(adult_names)

print([person.split()[0] for person in people if people[person] >= 18])
print([person.split()[0] for person in list(filter(lambda x: people.get(x) >= 18, people))])
print(list(map(lambda person: person.split()[0], filter(lambda x: people.get(x) >= 18, people))))
